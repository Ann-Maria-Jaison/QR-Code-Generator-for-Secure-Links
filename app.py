from flask import Flask, render_template, request, send_file
import qrcode
import io

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', qrcode_url=None)

@app.route('/generate_qrcode', methods=['POST'])
def generate_qrcode():
    secure_link = request.form['secure_link']
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(secure_link)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')

    # Save QR code to a BytesIO object
    buffer = io.BytesIO()
    img.save(buffer, format='PNG')
    buffer.seek(0)

    return send_file(buffer, mimetype='image/png', as_attachment=False, download_name='qrcode.png')

if __name__ == '__main__':
    app.run(debug=True)
