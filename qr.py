import qrcode

def generate_qr_code(link, output_file):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(link)
    qr.make(fit=True)
    qr_img = qr.make_image(fill_color="black", back_color="white")
    qr_img.save(output_file)

# Example usage
link = str(input("Link: "))
output_file = "qr_code.png"
generate_qr_code(link, output_file)