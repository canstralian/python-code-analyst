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

## Project Overview

Python Code Analyst is a web application built with Streamlit that allows users to input news article URLs and receive summarized content in various tones. The application fetches the content of the news articles, processes it, and generates summaries using Cloudflare Workers AI. The main features of the project include:

* Fetching news article content from allowed domains
* Summarizing the content in different tones (e.g., humorous, majestic, academic)
* Handling errors for invalid URLs or disallowed domains
* Providing a user-friendly interface with Streamlit

## Installation Instructions

To install and set up the project locally, follow these steps:

1. **Clone the repository**: Clone the repository to your local machine using the following command:
   ```bash
   git clone https://github.com/canstralian/python-code-analyst.git
   ```
2. **Navigate to the project directory**: Change to the project directory:
   ```bash
   cd python-code-analyst
   ```
3. **Create a virtual environment**: Create a virtual environment to isolate the project dependencies:
   ```bash
   python -m venv venv
   ```
4. **Activate the virtual environment**: Activate the virtual environment:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS and Linux:
     ```bash
     source venv/bin/activate
     ```
5. **Install dependencies**: Install the required dependencies using the following command:
   ```bash
   pip install -r requirements.txt
   ```

## Usage Examples

Here are some examples of how to use the project:

1. **Run the application**: Start the Streamlit application using the following command:
   ```bash
   streamlit run app.py
   ```
2. **Input a news article URL**: Use the Streamlit interface to input a news article URL from the allowed domains (e.g., `example.com`, `another-example.com`).
3. **Select a tone**: Choose a tone for the summary (e.g., humorous, majestic, academic) from the dropdown menu.
4. **Generate the summary**: Click the "Enter" button to fetch the article content and generate the summary.

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

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

## Changelog

### v1.0.1

* Added a timeout parameter to the `requests.get` call in the `fetch_article_content` function.
* Updated the `README.md` file with project overview, installation instructions, usage examples, contribution guidelines, and license information.

### v1.0.0

* Initial release of the Python Code Analyst project.

## Slack Notifications Configuration

To configure Slack notifications in your GitHub Actions workflow, you can use the `slackapi/slack-github-action` action. This action allows you to send messages to a specified Slack channel upon the completion of your build.

### Example Configuration

Here is an example of how to add Slack notifications to your GitHub Actions workflow:

```yaml
- name: Notify Slack on build success
  if: success()
  uses: slackapi/slack-github-action@v1.25.0
  with:
    payload: '{"text":"Build completed successfully!"}'
    channel: '#alerts'
    token: ${{ secrets.SLACK_BOT_TOKEN }}

- name: Notify Slack on build failure
  if: failure()
  uses: slackapi/slack-github-action@v1.25.0
  with:
    payload: '{"text":"Build failed!"}'
    channel: '#alerts'
    token: ${{ secrets.SLACK_BOT_TOKEN }}
```

Make sure to add the `SLACK_BOT_TOKEN` secret to your GitHub repository settings.

## Testing the Changes

To test the changes to ensure they work correctly, you can follow these steps:

* **Run the application locally**: Ensure you have all the dependencies installed by running `pip install -r requirements.txt`. Then, run the application using `streamlit run app.py` (`app.py`). 🏃‍♂️
* **Test different URLs**: Use the Streamlit interface to input various news article URLs from the allowed domains (`example.com`, `another-example.com`) and verify that the content is fetched and summarized correctly. 🌐
* **Check different tones**: Test the summarization feature with different tones (e.g., humorous, majestic, academic) to ensure the summaries are generated as expected. 🎭
* **Review error handling**: Input invalid URLs or URLs from disallowed domains to verify that the error messages are displayed correctly. 🚫
* **Run automated tests**: If there are any automated tests defined in the repository, such as those in the GitHub Actions workflows (e.g., `.github/workflows/pylint.yml`, `.github/workflows/python-app.yml`), ensure they pass successfully. ✅
* **Check logs and outputs**: Review the logs and outputs in the Streamlit interface and the console to ensure there are no unexpected errors or warnings. 📜
