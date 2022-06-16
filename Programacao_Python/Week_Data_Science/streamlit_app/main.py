# importar pacotes necessários
import streamlit as st
import cv2
import numpy as np
from PIL import Image, ImageEnhance

OUTPUT_WIDTH = 500


def main():
    """Masterclass Visão Computacional"""

    st.title("Masterclass Visão Computacional")
    st.text("Carlos Melo - Sigmoidal")

    opcoes_menu = ["Filtros", "Sobre"]
    choice = st.sidebar.selectbox("Escolha uma Opção", opcoes_menu)

    our_image = Image.open("empty.jpg")

    if choice == 'Filtros':
        st.subheader("App feito em 100% em Python")

        image_file = st.file_uploader("Carregue uma foto sua e escolha um filtro no menu lateral", type=['jpg', 'png', 'jpeg'])

        if image_file is not None:
            our_image = Image.open(image_file)
            st.text("Imagem Original")
            st.sidebar.image(our_image, width=150)

        filtros = st.sidebar.radio("Filtros", ["Original", "Grayscale", "Desenho", "Sépia", "Contraste", "Blur", "Canny"])

        if filtros == 'Grayscale':
            converted_image = np.array(our_image.convert('RGB'))
            gray_image = cv2.cvtColor(converted_image, cv2.COLOR_RGB2GRAY)
            st.image(gray_image, width=OUTPUT_WIDTH)

        elif filtros == 'Desenho':
            converted_image = np.array(our_image.convert('RGB'))
            gray_image = cv2.cvtColor(converted_image, cv2.COLOR_BGR2GRAY)
            inv_gray_image = 255 - gray_image
            blurred_image = cv2.GaussianBlur(inv_gray_image, (21, 21), 0, 0)
            sketch_image = cv2.divide(gray_image, 255 - blurred_image, scale=256)
            st.image(sketch_image, width=OUTPUT_WIDTH)

        elif filtros == 'Sépia':
            converted_image = np.array(our_image.convert('RGB'))
            converted_image = cv2.cvtColor(converted_image, cv2.COLOR_RGB2BGR)
            kernel = np.array([[0.272, 0.534, 0.131],
                               [0.349, 0.686, 0.168],
                               [0.393, 0.769, 0.189]])
            output_image = cv2.filter2D(converted_image, -1, kernel)
            st.image(output_image, channels="BGR", width=OUTPUT_WIDTH)

        elif filtros == 'Contraste':
            c_amount = st.sidebar.slider("Contraste", 0.0, 2.0, 1.0)
            enhancer = ImageEnhance.Contrast(our_image)
            img_output = enhancer.enhance(c_amount)
            st.image(img_output, width=OUTPUT_WIDTH)

        elif filtros == 'Blur':
            b_amount = st.sidebar.slider("Kernel (n x n)", 3, 21, 9, 2)
            converted_image = np.array(our_image.convert('RGB'))
            blur_image = cv2.GaussianBlur(converted_image, (int(b_amount), int(b_amount)), 0)
            st.image(blur_image, width=OUTPUT_WIDTH)

        elif filtros == 'Canny':
            converted_image = np.array(our_image.convert('RGB'))
            converted_image = cv2.cvtColor(converted_image, cv2.COLOR_RGB2BGR)
            blur_image = cv2.GaussianBlur(converted_image, (11, 11), 0)
            canny = cv2.Canny(blur_image, 100, 150)
            st.image(canny, width=OUTPUT_WIDTH)

        elif filtros == 'Original':
            st.image(our_image, width=OUTPUT_WIDTH)
        else:
            st.image(our_image, width=OUTPUT_WIDTH)

    elif choice == 'Sobre':
        st.subheader("Sobre a Masterclass de Visão Computacional")
        st.markdown("Masterclass disponível em [Sigmoidal](https://sigmoidal.ai)")
        st.text("Carlos Melo")
        st.success("Instagram @carlos_melo.py")


if __name__ == '__main__':
    main()
