# AKS QR Code Generator

This project consists of a front-end application built with [Next.js](https://nextjs.org/) and a backend API. The application runs on AKS(Azure Kubernetes Service).

## Project Structure

The project is divided into two main parts:

1. Front-end: Located in the `front-end-nextjs` directory. It's a Next.js application that provides the user interface for generating QR codes.

2. Backend API: Located in the `backend-api` directory. It's responsible for generating the QR codes.

## Getting Started

### Front-end

Navigate to the `front-end-nextjs` directory and run the following command to start the development server:

```bash
npm run install
npm run dev
```

Open `http://localhost:3000` with your browser to see the result.

### Backend API

To run the backend API, you need to have Docker installed. Go to the `backend-api` directory and run the following commands:

```bash
# Build the Docker image
$ docker build -t aks-qr-code-generator-backend .

# Run the Docker container
$ docker run -p 80:80 aks-qr-code-generator-backend
```

The backend API will be running at `http://localhost:80`.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements
