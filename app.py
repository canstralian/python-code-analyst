import os
import json
from urllib.parse import urlparse
from dotenv import load_dotenv
from bs4 import BeautifulSoup
import requests
import streamlit as st
from typing import Optional

# Load API secrets
load_dotenv()
CLOUDFLARE_ACCOUNT_ID = os.environ.get("CF_ACCOUNT_ID")
CLOUDFLARE_API_TOKEN = os.environ.get("CF_API_TOKEN")
url = f'https://api.cloudflare.com/client/v4/accounts/{CLOUDFLARE_ACCOUNT_ID}/ai/run/@cf/mistral/mistral-7b-instruct-v0.1'

ALLOWED_DOMAINS = ["example.com", "another-example.com"]

def fetch_article_content(news_link: str) -> Optional[str]:
    """Fetches and returns the text content of the news article."""
    parsed_url = urlparse(news_link)
    if parsed_url.netloc not in ALLOWED_DOMAINS:
        st.error("The provided URL is not allowed.")
        return None
    try:
        response = requests.get(news_link, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        st.error(f"Failed to fetch the article. Error: {e}")
        return None
    soup = BeautifulSoup(response.text, 'html.parser')
    return ' '.join(tag.get_text() for tag in soup.find_all('p'))

def summarize_article(text_data: str, tone: str) -> Optional[str]:
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
        response.raise_for_status()
        response_data = response.json()
        return response_data["result"]["response"]
    except requests.RequestException as e:
        st.error(f"Failed to summarize the article. Error: {e}")
        return None
    except (json.JSONDecodeError, KeyError) as e:
        st.error(f"Error processing the summary response: {e}")
        return None

def render_header():
    """Renders the header of the Streamlit app."""
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

def render_footer():
    """Renders the footer of the Streamlit app."""
    st.write("Made w/ ❤️ in SF 🌁 || ✅ out the [👩🏻‍💻GitHub repo](https://github.com/elizabethsiegle/cf-ai-lora-news-summarizer)")

def main():
    """Main function to run the Streamlit app."""
    render_header()

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

    render_footer()

if __name__ == "__main__":
    main()