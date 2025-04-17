# Secure QR Code Generator

This is a Flask-based web application that allows users to generate QR codes for secure links. It checks the safety of URLs using Google's Safe Browsing API before generating a QR code. 

## Features
- Validate URL format before processing.
- Check URL safety using Google Safe Browsing API.
- Generate QR codes only for safe URLs.
- Return the QR code as a downloadable image.

## Prerequisites
Ensure you have the following installed:
- Python 3.x
- Flask
- Requests
- QRCode
- Validators

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/your-repo-name.git
   cd your-repo-name
   ```

2. Create and activate a virtual environment:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   - Create a `.env` file or set the API key manually:
     ```sh
     export API_KEY="your-google-safe-browsing-api-key"
     ```

## Usage

1. Run the application:
   ```sh
   python app.py
   ```

2. Open the application in your browser:
   ```sh
   http://127.0.0.1:5000
   ```

3. Enter a URL, and if it's safe, a QR code will be generated.

## API Endpoints
- `GET /` - Renders the homepage.
- `POST /generate_qrcode` - Accepts a URL, checks its safety, and returns a QR code if safe.

## Security Considerations
- Uses Google Safe Browsing API to filter malicious URLs.
- Validates URLs before processing.
- Does not store any user data.

## Author
Ann Maria Jaison

## License
This project is licensed under the MIT License.

