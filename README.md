# Project Overview

* Python Code Analyst** is a web application built with Streamlit that allows users to input news article URLs and receive summarized content in various tones. The application fetches the content of the news articles, processes it, and generates summaries using Cloudflare Workers AI. The main features of the project include:

- Fetching news article content from allowed domains
- Summarizing the content in different tones (e.g., humorous, majestic, academic)
- Handling errors for invalid URLs or disallowed domains
- Providing a user-friendly interface with Streamlit

---

## Installation Instructions

To install and set up the project locally, follow these steps:

1. **Clone the repository**: Clone the repository to your local machine:
   ```bash
   git clone https://github.com/canstralian/python-code-analyst.git
   cd python-code-analyst
   ```

2. **Create and activate a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

---

## Usage Examples

1. **Run the Streamlit app**:
   ```bash
   streamlit run app.py
   ```

2. **Enter a news article URL**: Use the Streamlit interface to input a news article URL from allowed domains (e.g., `example.com`, `another-example.com`).

3. **Select a tone**: Choose a tone for the summary (e.g., humorous, majestic, academic).

4. **Generate the summary**: Click the "Enter" button to fetch the article content and generate the summary.

---

## Contribution Guidelines

We welcome contributions to the project! To contribute, please follow these guidelines:

1. **Fork the repository**: Fork the repository to your GitHub account.
2. **Create a new branch**: Create a new branch for your feature or bug fix:
   ```bash
   git checkout -b feature-name
   ```
3. **Make your changes**: Make your changes to the codebase.
4. **Commit your changes**: Commit your changes with a descriptive commit message:
   ```bash
   git commit -m "Add feature description"
   ```
5. **Push to your branch**: Push your changes to your forked repository:
   ```bash
   git push origin feature-name
   ```
6. **Create a pull request**: Create a pull request to the main repository with a description of your changes.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

---

## Changelog

### v1.0.1

- Added a timeout parameter to the `requests.get` call in the `fetch_article_content` function.
- Updated the `README.md` file with project overview, installation instructions, usage examples, contribution guidelines, and license information.

### v1.0.0

- Initial release of the Python Code Analyst project.

---

## Contact Information

For any questions or inquiries, please contact the project maintainers:

- **Canstralian**: [GitHub](https://github.com/canstralian)

---

## Acknowledgments

We would like to thank the following third-party libraries and tools that were used in this project:

- [Streamlit](https://streamlit.io/)
- [Cloudflare Workers AI](https://ai.cloudflare.com/)
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/)
- [Requests](https://docs.python-requests.org/en/latest/)
- [python-dotenv](https://github.com/theskumar/python-dotenv)

---

Let me know if you'd like any adjustments!