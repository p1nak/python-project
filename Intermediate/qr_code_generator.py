import qrcode as qr
from PIL import Image


qr_code = qr.QRCode(
    version=1,
    error_correction=qr.constants.ERROR_CORRECT_H, 
    box_size=10,
    border=4
)

qr_code.add_data("https://www.gtu.ac.in/result.aspx")
qr_code.make(fit=True)

img = qr_code.make_image(fill_color="red", back_color="white").convert("RGB")

logo = Image.open("logo.png")

logo_size = img.size[0] // 4
logo = logo.resize((logo_size, logo_size), Image.LANCZOS)

pos = ((img.size[0] - logo_size) // 2, (img.size[1] - logo_size) // 2)
img.paste(logo, pos, mask=logo if logo.mode == 'RGBA' else None)

img.save("GTU_Result_QR_Code_with_Logo.png")
