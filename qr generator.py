# import qrcode library using "pip install qrcode"
import qrcode

# add parameter for QR code image.
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=2,
    border=8
)

# Information which we want to convert in QR code.
qr.add_data(input("Enter your text which you want to convert in qr code: "))

# Generate QR code.
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white")

# save the image.
img.save("QR2.png")

print("QR code is ready.")

