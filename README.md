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
