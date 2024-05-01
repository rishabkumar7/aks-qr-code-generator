from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import qrcode
import os
from io import BytesIO
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
from starlette.responses import StreamingResponse
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

origins = [
    "http://localhost:3000",
    "http://4.246.235.9:3000"  # Allow frontend to connect from this origin
    # add more origins if needed
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return ("This is a QR Code API, send a POST to /generate-qr to generate QR code with URL as parameter.")

@app.post("/generate-qr")
async def generate_qr(url: str):
    if not url:
        raise HTTPException(status_code=400, detail="URL is required")

    # Generate QR code
    img = qrcode.make(url)
    img_byte_arr = BytesIO()
    img.save(img_byte_arr, format='PNG')
    img_byte_arr.seek(0)

    # Generate a unique filename
    filename = url.split("://")[1].replace("/", "_") + '.png'

    # Azure storage details
    connection_string = os.getenv('AZURE_STORAGE_CONNECTION_STRING')
    container_name = os.getenv('AZURE_STORAGE_CONTAINER_NAME')
    blob_name = filename  # You may want to use a unique name for each QR code

    # Create a blob client using the local file name as the name for the blob
    blob_service_client = BlobServiceClient.from_connection_string(connection_string)
    blob_client = blob_service_client.get_blob_client(container_name, blob_name)

    # Upload the created file
    blob_client.upload_blob(img_byte_arr.getvalue(), overwrite=True)

    # Get the blob url
    blob_url = blob_client.url

    return {"qr_code_url": blob_url}
