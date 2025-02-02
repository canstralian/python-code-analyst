import pytest
import requests
from unittest.mock import patch
from app import fetch_article_content, summarize_article

@patch('app.requests.get')
def test_fetch_article_content_success(mock_get):
    mock_response = requests.Response()
    mock_response.status_code = 200
    mock_response._content = b'<html><body><p>Test article content</p></body></html>'
    mock_get.return_value = mock_response

    result = fetch_article_content('https://example.com/test-article')
    assert result == 'Test article content'

@patch('app.requests.get')
def test_fetch_article_content_failure(mock_get):
    mock_get.side_effect = requests.RequestException("Failed to fetch")

    result = fetch_article_content('https://example.com/test-article')
    assert result is None

@patch('app.requests.get')
def test_fetch_article_content_invalid_url(mock_get):
    mock_get.return_value.status_code = 404

    result = fetch_article_content('https://invalid-url.com/test-article')
    assert result is None

@patch('app.requests.post')
def test_summarize_article_success(mock_post):
    mock_response = requests.Response()
    mock_response.status_code = 200
    mock_response._content = b'{"result": {"response": "Test summary"}}'
    mock_post.return_value = mock_response

    result = summarize_article('Test article content', 'humorous')
    assert result == 'Test summary'

@patch('app.requests.post')
def test_summarize_article_failure(mock_post):
    mock_post.side_effect = requests.RequestException("Failed to summarize")

    result = summarize_article('Test article content', 'humorous')
    assert result is None

@patch('app.requests.post')
def test_summarize_article_invalid_token(mock_post):
    mock_response = requests.Response()
    mock_response.status_code = 401
    mock_post.return_value = mock_response

    result = summarize_article('Test article content', 'humorous')
    assert result is None

@patch('app.requests.post')
def test_summarize_article_network_issue(mock_post):
    mock_post.side_effect = requests.ConnectionError("Network issue")

    result = summarize_article('Test article content', 'humorous')
    assert result is None

@patch('app.requests.post')
def test_summarize_article_unexpected_response_format(mock_post):
    mock_response = requests.Response()
    mock_response.status_code = 200
    mock_response._content = b'{"unexpected_key": "unexpected_value"}'
    mock_post.return_value = mock_response

    result = summarize_article('Test article content', 'humorous')
    assert result is None

@patch('app.requests.post')
def test_summarize_article_majestic_tone(mock_post):
    mock_response = requests.Response()
    mock_response.status_code = 200
    mock_response._content = b'{"result": {"response": "Majestic summary"}}'
    mock_post.return_value = mock_response

    result = summarize_article('Test article content', 'majestic')
    assert result == 'Majestic summary'

@patch('app.requests.post')
def test_summarize_article_academic_tone(mock_post):
    mock_response = requests.Response()
    mock_response.status_code = 200
    mock_response._content = b'{"result": {"response": "Academic summary"}}'
    mock_post.return_value = mock_response

    result = summarize_article('Test article content', 'academic')
    assert result == 'Academic summary'

@patch('app.requests.post')
def test_summarize_article_inspirational_tone(mock_post):
    mock_response = requests.Response()
    mock_response.status_code = 200
    mock_response._content = b'{"result": {"response": "Inspirational summary"}}'
    mock_post.return_value = mock_response

    result = summarize_article('Test article content', 'inspirational')
    assert result == 'Inspirational summary'

@patch('app.requests.post')
def test_summarize_article_dramatic_tone(mock_post):
    mock_response = requests.Response()
    mock_response.status_code = 200
    mock_response._content = b'{"result": {"response": "Dramatic summary"}}'
    mock_post.return_value = mock_response

    result = summarize_article('Test article content', 'dramatic')
    assert result == 'Dramatic summary'

@patch('app.requests.post')
def test_summarize_article_gen_z_tone(mock_post):
    mock_response = requests.Response()
    mock_response.status_code = 200
    mock_response._content = b'{"result": {"response": "Gen Z summary"}}'
    mock_post.return_value = mock_response

    result = summarize_article('Test article content', 'gen z')
    assert result == 'Gen Z summary'