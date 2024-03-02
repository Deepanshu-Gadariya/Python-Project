import qrcode
# from pil import image
qr=qrcode.QRCode(
    version=1,error_correction=qrcode.ERROR_CORRECT_H,box_size=10,border=4
)
qr.add_data("www.linkedin.com/in/deepanshu-pal-343190254")
qr.make(fit=True)
img = qr.make_image(fill_color="red",back_color="white")
img.save("profile.png")