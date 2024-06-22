import streamlit as st
import qrcode
import image
qr=qrcode.QRCode(
    version=15,
    box_size=10,
    border=5,
)
st.header("QR Code Generation")

data=st.text_input('Enter your link')

qr.add_data(data)
qr.make(fit=True)
img=qr.make_image(fill="blue",back_color="white")
img.save("test1.png")
st.markdown("Here is The QR Code")
st.image("test1.png",width=300)
print(data)
