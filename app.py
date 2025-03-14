from flask import Flask, render_template, request, send_file, jsonify
import qrcode
import io
import requests
import validators
import os

# Load API Key from environment variable (secure way)
API_KEY = os.getenv("GOOGLE_API_KEY")  # Your actual API key

if not API_KEY:
    raise ValueError("Google Safe Browsing API key is missing! Set it as an environment variable.")

app = Flask(__name__)

def is_safe_url(url):
    """Check if the URL is safe using Google Safe Browsing API."""
    API_URL = f"https://safebrowsing.googleapis.com/v4/threatMatches:find?key={API_KEY}"

    # Validate URL format first
    if not validators.url(url):
        return False, "Invalid URL format."

    payload = {
        "client": {"clientId": "your-app-name", "clientVersion": "1.0"},
        "threatInfo": {
            "threatTypes": ["MALWARE", "SOCIAL_ENGINEERING", "UNWANTED_SOFTWARE", "THREAT_TYPE_UNSPECIFIED"],
            "platformTypes": ["ANY_PLATFORM"],
            "threatEntryTypes": ["URL"],
            "threatEntries": [{"url": url}]
        }
    }

    try:
        response = requests.post(API_URL, json=payload, headers={"Content-Type": "application/json"})
        response.raise_for_status()  # Raise error for HTTP failures
        result = response.json()

        # Debugging: Print API response
        print(f"Checked URL: {url}")
        print("Google Safe Browsing API Response:", result)

        # Check if the API response contains a match
        if "matches" in result and result["matches"]:
            return False, "URL is flagged as unsafe."

    except requests.exceptions.RequestException as e:
        return False, f"Error checking URL safety: {str(e)}"

    return True, "URL is safe."

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate_qrcode', methods=['POST'])
def generate_qrcode():
    secure_link = request.form.get('secure_link', '').strip()

    # Step 1: Check if URL is safe
    is_safe, message = is_safe_url(secure_link)
    if not is_safe:
        return jsonify({"error": message}), 400

    # Step 2: Generate QR Code if the link is safe
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(secure_link)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')

    # Save QR code to buffer
    buffer = io.BytesIO()
    img.save(buffer, format='PNG')
    buffer.seek(0)

    return send_file(buffer, mimetype='image/png', as_attachment=False, download_name='qrcode.png')

if __name__ == '__main__':
    app.run(debug=True)
