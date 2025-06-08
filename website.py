from PIL import Image
import requests

import streamlit as st

st.set_page_config(page_title="my_website", page_icon=":tada:", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Load assets
image_1 = Image.open("jpg2png/WhatsApp Image 2025-06-08 at 18.09.16_145a0bde.png")
image_2 = Image.open("jpg2png/WhatsApp Image 2025-06-08 at 18.09.18_711f3a78.png")
image_3 = Image.open("jpg2png/WhatsApp Image 2025-06-08 at 18.09.19_5bef355a.png")
image_4 = Image.open("jpg2png/WhatsApp Image 2025-06-08 at 18.09.21_a851bcd4.png")
image_5 = Image.open("jpg2png/WhatsApp Image 2025-06-08 at 18.09.20_f673ccec.png")
image_6 = Image.open("jpg2png/WhatsApp Image 2025-06-08 at 18.09.21_3f063336.png")
image_7 = Image.open("jpg2png/WhatsApp Image 2025-06-08 at 18.09.21_1d51523d.png")

lottie_coding = load_lottieurl("https://lottie.host/aecf3d3b-3910-4aca-ac85-57a013855ece/rdqjULCC4y.json")

# Header section
with st.container():
    st.title("Welcome to My Art Portfolio")
    st.header("I am Joshi :smiley:")
    st.subheader("An artist from S.C.E.T")
    st.write("I am passionate about art and design and I am a self-taught artist. I can create pencil sketches and digital art. I love to experiment with different styles and techniques.")
    st.markdown("[See more >](https://www.instagram.com/joshful___joshi/?next=%2F&hl=en)")

# What I do
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I Do :art:")
        st.write("##")
        st.write(
            """
            - **Pencil Sketches**: I create detailed and realistic pencil sketches that capture the essence of my subjects.
            - **Digital Art**: I use digital tools to create vibrant and imaginative artworks that push the boundaries of traditional art.
            - **Artistic Exploration**: I love to experiment with different styles and techniques, constantly evolving my artistic expression.
            """
        )
    with right_column:
        if lottie_coding:
            st_lottie(lottie_coding, height=300, key="coding")
        else:
            st.error("Failed to load animation.")


# artworks section

with st.container():
    st.write("---")
    st.header("here are some of my artworks :art:")
    st.write("##")
    col1, col2, col3 ,col7= st.columns(4)
    col4 ,col5 ,col6=st.columns(3)
    

with col1:
    st.image(image_1, width=300)

with col2:
    st.image(image_2, width=300)

with col3:
    st.image(image_3, width=300)

with col4:
    st.image(image_4, width=300)

with col5:
    st.image(image_5, width=300)

with col6:
    st.image(image_6, width=300)

with col7:
    st.image(image_7, width=300)



st.markdown("[to see more art >](https://www.instagram.com/joshful___joshi/?next=%2F&hl=en)")

#contact section
with st.container():
    st.write("---")
    st.header("my contact details :phone:")
    st.write("contact:- +91 7997787866")
    st.write("gmail:- joshistylein@gmail.com")
