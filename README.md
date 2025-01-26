---
title: Python Code Analyst
emoji: 👁
colorFrom: indigo
colorTo: indigo
sdk: streamlit
sdk_version: 1.41.1
app_file: app.py
pinned: false
license: mit
---

[![Pylint](https://github.com/canstralian/python-code-analyst/actions/workflows/pylint.yml/badge.svg)](https://github.com/canstralian/python-code-analyst/actions/workflows/pylint.yml)

Check out the configuration reference at https://huggingface.co/docs/hub/spaces-config-reference

## Project Description

The AI News Summarizer is a Python web application built with Streamlit and Cloudflare Workers AI. It allows users to input a news link and receive a summarized version of the article in a selected tone.

## Installation Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/elizabethsiegle/cf-ai-lora-news-summarizer.git
   cd cf-ai-lora-news-summarizer
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   - Create a `.env` file in the root directory of the project.
   - Add the following environment variables to the `.env` file:
     ```
     CF_ACCOUNT_ID=your_cloudflare_account_id
     CF_API_TOKEN=your_cloudflare_api_token
     ```

## Usage Examples

1. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

2. Open your web browser and go to `http://localhost:8501`.

3. Enter a news link and select the desired tone for the summary.

4. Click the "Enter" button to receive the summarized article.

## Configuration

The application uses environment variables to store sensitive information such as API keys. These variables are loaded from a `.env` file using the `python-dotenv` library. Make sure to create a `.env` file in the root directory of the project and add the required environment variables.

## Contributing Guidelines

We welcome contributions to the AI News Summarizer project! To contribute, please follow these guidelines:

1. Fork the repository and create a new branch for your feature or bugfix.
2. Make your changes and ensure that the code is well-documented and follows the project's coding style.
3. Write tests for your changes and ensure that all tests pass.
4. Submit a pull request with a clear description of your changes and the problem they solve.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

## Contact Information

For any questions or inquiries, please contact the project maintainers:

- Elizabeth Siegle: [GitHub](https://github.com/elizabethsiegle)

## Acknowledgments

We would like to thank the following third-party libraries and tools that were used in this project:

- [Streamlit](https://streamlit.io/)
- [Cloudflare Workers AI](https://ai.cloudflare.com/)
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/)
- [Requests](https://docs.python-requests.org/en/latest/)
- [python-dotenv](https://github.com/theskumar/python-dotenv)
