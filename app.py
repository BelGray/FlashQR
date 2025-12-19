import streamlit as st
import qrcode
from io import BytesIO

st.set_page_config(page_title="Flash QR", page_icon="⚡", layout="centered")

st.title("Flash QR")
st.write("Стильный простой QR-код для Вашего бизнеса за секунды ⚡")

col1, col2 = st.columns([2, 1])

with col1:
    url = st.text_input("Вставьте сюда ссылку/текст", "https://github.com/BelGray")

    fill_color = st.color_picker("Цвет QR-кода", "#000000")
    back_color = st.color_picker("Цвет фона", "#FFFFFF")

    qr_border = st.slider("Пустое пространство", 1, 10)

with col2:
    st.info("💡 Совет: Выбирайте контрастные цвета, чтобы камера могла считать код.")

if st.button("Создать QR"):
    try:

        qr = qrcode.QRCode(box_size=10, border=qr_border)
        qr.add_data(url)
        qr.make(fit=True)

        img = qr.make_image(fill_color=fill_color, back_color=back_color)

        buf = BytesIO()
        img.save(buf, format="PNG")
        byte_im = buf.getvalue()

        st.image(byte_im, caption="Ваш готовый QR", width=300)

        st.download_button(
            label="Скачать PNG",
            data=byte_im,
            file_name="qr_code.png",
            mime="image/png"
        )
    except Exception as e:
        st.error(f"Ошибка: {e}")