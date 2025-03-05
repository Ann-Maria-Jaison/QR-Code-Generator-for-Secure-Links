# Secure Link QR Code Generator

This project is a simple web application built using Flask and Python that generates QR codes for secure URLs. It showcases how QR codes can be used to securely share links, reducing the risks associated with URL tampering or phishing attacks.

## Cybersecurity Relevance

This application is designed with cybersecurity in mind. By encoding a secure URL into a QR code, users can share links without directly exposing them, which helps to prevent malicious tampering or phishing attempts.

## Features

- Input a URL and checking is that secure or not using gogle secure link API
- User-friendly interface with form submission.
- Backend implemented using Flask to handle QR code generation.
- QR code dynamically generated and displayed on the webpage.

## Technologies Used

- **Flask**: A lightweight Python web framework for the backend.
- **qrcode**: Python library for generating QR codes.
- **HTML/CSS**: For building the frontend interface.

## Installation

Follow these steps to set up and run the project locally:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/secure-link-qr-code-generator.git
2. **Navigate to the project directory:**:
   ```bash
   cd secure-link-qr-code-generator
3. **Install the required libraries:**:
   ```bash
   pip install flask qrcode[pil]
4. **Run the Flask app:**:
   ```bash
   python app.py
5. **Open your browser** and navigate to `http://127.0.0.1:5000/` to use the app.

## How It Works

1. The user inputs a secure URL in the provided form.
2. The backend (Flask) processes the input and generates a QR code for the URL.
3. The generated QR code is displayed on the webpage, ready to be scanned.





