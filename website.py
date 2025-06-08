import streamlit as st
from PIL import Image
import requests
from streamlit_lottie import st_lottie
import os

st.set_page_config(page_title="My Art Portfolio", page_icon=":art:", layout="wide")

def load_lottieurl(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        return r.json()
    except requests.RequestException:
        return None

def safe_open_image(path):
    try:
        img = Image.open(path)
        return img
    except Exception:
        st.warning(f"Could not load image: {path}")
        return None

# Load Lottie animation
lottie_coding = load_lottieurl("https://lottie.host/aecf3d3b-3910-4aca-ac85-57a013855ece/rdqjULCC4y.json")

# Header Section
with st.container():
    st.title("Welcome to My Art Portfolio")
    st.header("I am Joshi :smiley:")
    st.subheader("An artist from S.C.E.T")
    st.write("I am passionate about art and design and am a self-taught artist. I create pencil sketches and digital art, and I love to experiment with different styles and techniques.")
    st.markdown("[See more on Instagram >](https://www.instagram.com/joshful___joshi/?next=%2F&hl=en)")

# What I Do Section
with st.container():
    st.write("---")
    left, right = st.columns(2)
    with left:
        st.header("What I Do :art:")
        st.write("###")
        st.markdown(
            """
            - **Pencil Sketches:** Detailed and realistic sketches.
            - **Digital Art:** Vibrant and imaginative digital works.
            - **Artistic Exploration:** Always experimenting and evolving!
            """
        )
    with right:
        if lottie_coding:
            st_lottie(lottie_coding, height=300, key="coding")
        else:
            st.error("Failed to load animation.")

# Artworks Section
with st.container():
    st.write("---")
    st.header("Here are some of my artworks :art:")
    st.write("###")
    # Dynamically load all images from the directory
    image_dir = "jpg2png"
    image_files = [
        os.path.join(image_dir, fname) 
        for fname in os.listdir(image_dir) 
        if fname.lower().endswith((".png", ".jpg", ".jpeg"))
    ]
    image_files.sort()  # Optional: sort for consistent order

    cols = st.columns(3)
    for idx, img_path in enumerate(image_files):
        img = safe_open_image(img_path)
        if img:
            with cols[idx % 3]:
                st.image(img, width=300, caption=os.path.basename(img_path), use_column_width="never")

st.markdown("[See more art on Instagram >](https://www.instagram.com/joshful___joshi/?next=%2F&hl=en)")

# Contact Section with Form
with st.container():
    st.write("---")
    st.header("Contact Me :phone:")
    with st.form(key="contact_form"):
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        message = st.text_area("Message")
        submit = st.form_submit_button("Send")
        if submit:
            if name and email and message:
                st.success("Thank you for reaching out! I will get back to you soon.")
            else:
                st.error("Please complete all fields before submitting.")
    st.write("Or reach out directly:")
    st.write("Phone: +91 7997787866")
    st.write("Email: joshistylein@gmail.com")
