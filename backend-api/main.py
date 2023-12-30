from fastapi import FastAPI, HTTPException
import qrcode
from io import BytesIO
from starlette.responses import StreamingResponse

app = FastAPI()

@app.post("/generate-qr")
async def generate_qr(url: str):
    if not url:
        raise HTTPException(status_code=400, detail="URL is required")

    # Generate QR code
    img = qrcode.make(url)
    img_byte_arr = BytesIO()
    img.save(img_byte_arr, format='PNG')
    img_byte_arr.seek(0)

    return StreamingResponse(img_byte_arr, media_type="image/png")
