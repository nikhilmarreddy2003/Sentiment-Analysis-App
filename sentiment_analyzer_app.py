#!/usr/bin/env python
# coding: utf-8

# In[5]:


import streamlit as st
from transformers import pipeline

# ───────────────────────────────────────────────
# Load the best 3-class sentiment model (cached)
# ───────────────────────────────────────────────
@st.cache_resource
def load_sentiment_model():
    return pipeline(
        "sentiment-analysis",
        model="j-hartmann/sentiment-roberta-large-english-3-classes"
    )


# ───────────────────────────────────────────────
# Main app
# ───────────────────────────────────────────────
def main():
    st.set_page_config(page_title="Sentiment Analysis", layout="centered")

    st.title("Sentiment Analysis")
    st.markdown(
        "Type a sentence, review, comment or tweet and click Analyze."
        
    )

    text = st.text_area(
        "",
        placeholder="Examples:\n"
                    "  • This movie is amazing! Loved every second.\n"
                    "  • It's okay, nothing special, but it's not bad either.\n"
                    "  • Terrible experience, never buying again.",
        height=160,
        label_visibility="collapsed"
    )

    if st.button("Analyze", type="primary", use_container_width=False):
        if not text.strip():
            st.warning("Please enter some text first.", icon="⚠️")
            return

        with st.spinner("Analyzing sentiment..."):
            classifier = load_sentiment_model()
            result = classifier(text.strip())[0]
            label = result["label"].lower()  # positive, neutral, negative

        st.subheader("Result")

        if "positive" in label:
            st.success("Positive 😊")
        elif "negative" in label:
            st.error("Negative 😞")
        else:
            st.info("Neutral 😐")


if __name__ == "__main__":
    main()


# In[ ]:




