import qrcode as qr
import os

# Ensure the directory exists
output_directory = r'/home/parallels/tutorials/Python/QRCODE/'
os.makedirs(output_directory, exist_ok=True)

# URL for which to generate the QR code
url = 'https://www.youtube.com/watch?v=h8EIBWh01gs&t=49s'
qr_code = qr.make(url)

# File name for saving the QR code
file_name = 'file_name3.png'
file_path = os.path.join(output_directory, file_name)

# Save the QR code
qr_code.save(file_path)

print(f"QR code saved to {file_path}")
