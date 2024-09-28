import os
import json
import qrcode
from PIL import Image

# Create a folder named 'qr-codes' to store QR code images if it doesn't exist
if not os.path.exists('qr-codes'):
    os.mkdir('qr-codes')

# Read data from wb-indicators.json
with open('wb-indicators.json', 'r') as json_file:
    data = json.load(json_file)

# Generate QR codes for each indicator and save them as PNG files
for entry in data:
    indicator = entry["indicator"]
    description = entry["description"].strip()
    
    qr_data = f"{indicator}: {description}"
    
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(qr_data)
    qr.make(fit=True)
    qr_img = qr.make_image(fill_color="black", back_color="white")
    
    # Sanitize the file name by replacing special characters
    file_name = f"qr-codes/{indicator.replace('.', '_')}.png"
    
    # Save the generated QR code as a PNG file
    qr_img.save(file_name)