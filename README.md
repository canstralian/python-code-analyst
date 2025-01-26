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
