import qrcode as qr

#URL = input('Enter the URL you want to generate the QRCode:')
qr_code = qr.make(r'https://www.youtube.com/watch?v=h8EIBWh01gs&t=49s')
#file_name = input('Enter your file name for QRCode here, do not contain space')

qr_code.save(r'/home/parallels/tutorials/Python/QRCODE/file_name3.png')
