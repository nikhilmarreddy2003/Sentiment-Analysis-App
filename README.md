# Sentiment Analysis Application

A clean, simple, and user-friendly web application that takes any text input (sentence, review, comment, tweet, etc.) and classifies the sentiment as **Positive 😊**, **Negative 😞**, or **Neutral 😐**.

**Live Demo**  
https://sentiment-analysis-app-vaprdffyaeuaokxsoapee2.streamlit.app/

## Features
- Intuitive text input with example placeholders  
- One-click "Analyze" button  
- Clear colored visual feedback (green/red/blue)  
- Minimal design — no confidence scores or raw output shown  
- Good handling of neutral and mixed sentiment sentences  
- Fast startup with model caching

## Tools & Technologies Used
- **Python** — core programming language  
- **Streamlit** — rapid interactive web app development  
- **Hugging Face Transformers** — easy access to pre-trained NLP models  
- **Model**: j-hartmann/sentiment-roberta-large-english-3-classes (RoBERTa-large, 3-class sentiment)  
- **PyTorch** (via torch) — deep learning backend  
- **Git & GitHub** — code version control and hosting  
- **Streamlit Community Cloud** — free deployment platform

## Approach – How I Developed the Project

1. **Requirement Understanding**  
   Read the assignment carefully: needed a web app with text input, submit button, and clear Positive/Negative/Neutral result.  
   Focused on good UI and reasonable neutral detection (many models are bad at "okay", "meh", "average").

2. **Tool & Model Selection**  
   - Chose **Streamlit** because it lets me build a working web app very fast with only Python.  
   - Used **Hugging Face Transformers pipeline** to avoid writing complex model code.  
   - Tested different models:  
     - Binary models → bad for neutral  
     - Twitter-RoBERTa → okay but sometimes wrong on neutral  
     - Emotion models → too complicated  
   - Final choice: **j-hartmann/sentiment-roberta-large-english-3-classes**  
     → Directly gives positive/neutral/negative  
     → Works well on real English text  
     → Strong enough for assignment without being too heavy

3. **Implementation**  
   - Built simple UI: title, description, text area, button  
   - Cached model with `@st.cache_resource` so it loads only once  
   - Added loading spinner during analysis  
   - Mapped model labels to Streamlit styled boxes  
   - Added check for empty input

4. **Testing & Fixes**  
   - Tested many sentences locally (positive, negative, neutral, mixed, short, sarcastic)  
   - Fixed deployment problems (requirements.txt, Python version on Cloud)  
   - Made sure neutral cases like "it's okay" are classified correctly most of the time

5. **Deployment & Documentation**  
   - Uploaded code to GitHub  
   - Deployed to Streamlit Community Cloud  
   - Wrote this README with all required sections  
   - Added screenshots to show how it looks

## How to Run Locally

1. Clone the repository  
   ```bash
   git clone https://github.com/yourusername/sentiment-analysis-app.git
   cd sentiment-analysis-app
