"""
This module defines the main function for the AI News Summarizer app.
"""

import os
import io
import time
import base64
from dotenv import load_dotenv
from bs4 import BeautifulSoup
import requests
import streamlit as st
from langchain_openai import ChatOpenAI

# Load API secrets
load_dotenv()
CLOUDFLARE_ACCOUNT_ID = os.environ.get("CF_ACCOUNT_ID")
CLOUDFLARE_API_TOKEN = os.environ.get("CF_API_TOKEN")
url = f'https://api.cloudflare.com/client/v4/accounts/{CLOUDFLARE_ACCOUNT_ID}/ai/run/@cf/mistral/mistral-7b-instruct-v0.1'

def fetch_article_content(news_link):
    """Fetches and returns the text content of the news article."""
    response = requests.get(news_link)
    if response.status_code != 200:
        st.error(f"Failed to fetch the article. Status code: {response.status_code}")
        return None
    soup = BeautifulSoup(response.text, 'html.parser')
    text_data = ' '.join(tag.get_text() for tag in soup.find_all('p'))
    return text_data

def summarize_article(text_data, tone):
    """Summarizes the article content using Cloudflare Workers AI."""
    headers = {
        'Authorization': f'Bearer {CLOUDFLARE_API_TOKEN}',
        'Content-Type': 'application/json'
    }
    data = {
        "messages": [
            {
                "role": "user",
                "content": f"Summarize the following content from a news article in a {tone} tone: {text_data}"
            }
        ],
        "lora": "cf-public-cnn-summarization"
    }
    try:
        response = requests.post(url, headers=headers, data=json.dumps(data))
        if response.status_code != 200:
            st.error(f"Failed to summarize the article. Status code: {response.status_code}")
            return None
        response_data = response.json()
        summary = response_data["result"]["response"]
        return summary
    except Exception as e:
        st.error(f"Error summarizing article: {e}")
        return None

def main():
    """Main function to run the Streamlit app."""
    st.markdown("""
        <style>
            .big-font {
                font-size:40px !important;
                color:green;
            }
        </style>
    """, unsafe_allow_html=True)
    st.markdown('<p class="big-font"><p>AI🤖 News🗞️ Summarizer</p>', unsafe_allow_html=True)
    st.write(":blue[This Python🐍 web🕸️ app is built👩🏻‍💻 w/ [Streamlit](https://streamlit.io/) && [Cloudflare Workers AI](https://ai.cloudflare.com/)]")

    news_link = st.text_input('Please enter a news link to summarize')
    tone = st.selectbox(
        ':green[What tone do you want the news summary to take?]',
        ('humorous🤣', 'majestic🌊', 'academic📚', '✨inspirational✨', 'dramatic🎭', 'gen z👧🏻')
    )
    st.write("You selected: ", tone)
    
    if st.button('Enter') and tone and news_link:
        if not urlparse(news_link).scheme:
            st.error("Please enter a valid URL.")
            return

        with st.spinner('Processing📈...'):
            text_data = fetch_article_content(news_link)
            if text_data:
                summary = summarize_article(text_data, tone)
                if summary:
                    html_str = f"""
                    <p style="font-family:Comic Sans; color:Pink; font-size: 18px;">{summary}</p>
                    """
                    st.markdown(html_str, unsafe_allow_html=True)

    st.write("Made w/ ❤️ in SF 🌁 || ✅ out the [👩🏻‍💻GitHub repo](https://github.com/elizabethsiegle/cf-ai-lora-news-summarizer)")

if __name__ == "__main__":
    main()
