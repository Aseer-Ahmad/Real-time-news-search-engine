
# =======================

from io import BytesIO
import requests
import streamlit as st
from PIL import Image
from embeddings import TextEmbedder
from settings import settings
from cleaners import clean_full
from upstash_vector import Index 

v_index = Index(url=settings.UPSTASH_VECTOR_ENDPOINT, token=settings.UPSTASH_VECTOR_KEY)

st.title("Real-Time News Search")
ph = "https://t4.ftcdn.net/jpg/05/17/53/57/360_F_517535712_q7f9QC9X6TQxWi6xYZZbMmw5cnLMr279.jpg"

# Text input field at the top
question = st.text_input("What's new?:", key="question")

# Placeholder for the results below the input field
results_placeholder = st.empty()

def download_and_resize_image(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            img = Image.open(BytesIO(response.content))
            resized_img = img.resize((200, 200))
            return resized_img
        else:
            response = requests.get(ph)
            img = Image.open(BytesIO(response.content))
            resized_img = img.resize((200, 200 ))
            return resized_img
    except Exception as e:
        st.error(f"Error downloading image: {e}")


def query_index(question: str):
    embedder = TextEmbedder()
    embds = embedder(question, to_list=True)
    similars = v_index.query(
        vector=embds, top_k=4, include_metadata=True, include_vectors=False
    )

    url = []
    list_dict = []

    for sim in similars : 
        if sim.metadata["url"] not in url:
            list_dict.append({
                "score": sim.score,
                "title": sim.metadata["title"],
                "image": sim.metadata["image_url"],
                "date": sim.metadata["published_at"],
                "original": sim.metadata["url"],
            })
            url.append(sim.metadata["url"])
 
    return list_dict

def display_articles(articles):
    if articles:
        n_cols = 2
        n_rows = (len(articles) + n_cols - 1) // n_cols
        for row in range(n_rows):
            cols = st.columns(n_cols)
            for col in range(n_cols):
                index = row * n_cols + col
                if index >= len(articles):
                    break
                article = articles[index]
                image = download_and_resize_image(article["image"])
                with cols[col]:
                    if image:
                        st.image(image, use_column_width=True, clamp=True, width=200)
                    st.caption(
                        f"Score: {(100 * article['score']):.2f}% : {article['date']} "
                    )
                    st.subheader(article["title"])
                    url = article["original"]
                    button_html = f"""<a href="{url}" target="_blank">
                                        <button style="color: white; background-color: #4CAF50; border: none; padding: 10px 24px; 
                                        text-align: center; text-decoration: none; display: inline-block; font-size: 16px; 
                                        margin: 4px 2px; cursor: pointer; border-radius: 12px;">
                                            See More
                                        </button>
                                    </a>"""
                    st.markdown(button_html, unsafe_allow_html=True)
            st.divider()

def on_text_enter():
    question = st.session_state.question
    question = clean_full(question)
    if question:
        articles = query_index(question)
        with results_placeholder.container():
            display_articles(articles)

if question:
    on_text_enter()
