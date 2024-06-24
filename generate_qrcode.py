# import qrcode as qr

# img = qr.make("hlw ")
# img.save("qr_video.png")

import qrcode

#box sizing
qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

#creat funtion with parameters
def generate_qr_code(data, file_name):
    
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(file_name)

if __name__ == "__main__":
    data = input("Enter the data to be encoded: ")
    file_name = input("Enter the file name (with extension) to save the QR code: ")
    generate_qr_code(data, file_name)
    print(f"QR code saved as {file_name}")
