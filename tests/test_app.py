import unittest
from unittest.mock import patch, Mock
from app import fetch_article_content, summarize_article

class TestApp(unittest.TestCase):

    @patch('app.requests.get')
    def test_fetch_article_content_success(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.text = '<html><body><p>Test article content</p></body></html>'
        mock_get.return_value = mock_response

        result = fetch_article_content('https://example.com/test-article')
        self.assertEqual(result, 'Test article content')

    @patch('app.requests.get')
    def test_fetch_article_content_failure(self, mock_get):
        mock_get.side_effect = requests.RequestException("Failed to fetch")

        result = fetch_article_content('https://example.com/test-article')
        self.assertIsNone(result)

    @patch('app.requests.get')
    def test_fetch_article_content_invalid_url(self, mock_get):
        result = fetch_article_content('https://invalid-url.com/test-article')
        self.assertIsNone(result)

    @patch('app.requests.post')
    def test_summarize_article_success(self, mock_post):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "result": {
                "response": "Test summary"
            }
        }
        mock_post.return_value = mock_response

        result = summarize_article('Test article content', 'humorous')
        self.assertEqual(result, 'Test summary')

    @patch('app.requests.post')
    def test_summarize_article_failure(self, mock_post):
        mock_post.side_effect = requests.RequestException("Failed to summarize")

        result = summarize_article('Test article content', 'humorous')
        self.assertIsNone(result)

    @patch('app.requests.post')
    def test_summarize_article_invalid_token(self, mock_post):
        mock_post.return_value = Mock(status_code=401)

        result = summarize_article('Test article content', 'humorous')
        self.assertIsNone(result)

    @patch('app.requests.post')
    def test_summarize_article_network_issue(self, mock_post):
        mock_post.side_effect = requests.ConnectionError("Network issue")

        result = summarize_article('Test article content', 'humorous')
        self.assertIsNone(result)

    @patch('app.requests.post')
    def test_summarize_article_unexpected_response_format(self, mock_post):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"unexpected_key": "unexpected_value"}
        mock_post.return_value = mock_response

        result = summarize_article('Test article content', 'humorous')
        self.assertIsNone(result)

    @patch('app.requests.post')
    def test_summarize_article_majestic_tone(self, mock_post):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "result": {
                "response": "Majestic summary"
            }
        }
        mock_post.return_value = mock_response

        result = summarize_article('Test article content', 'majestic')
        self.assertEqual(result, 'Majestic summary')

    @patch('app.requests.post')
    def test_summarize_article_academic_tone(self, mock_post):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "result": {
                "response": "Academic summary"
            }
        }
        mock_post.return_value = mock_response

        result = summarize_article('Test article content', 'academic')
        self.assertEqual(result, 'Academic summary')

    @patch('app.requests.post')
    def test_summarize_article_inspirational_tone(self, mock_post):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "result": {
                "response": "Inspirational summary"
            }
        }
        mock_post.return_value = mock_response

        result = summarize_article('Test article content', 'inspirational')
        self.assertEqual(result, 'Inspirational summary')

    @patch('app.requests.post')
    def test_summarize_article_dramatic_tone(self, mock_post):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "result": {
                "response": "Dramatic summary"
            }
        }
        mock_post.return_value = mock_response

        result = summarize_article('Test article content', 'dramatic')
        self.assertEqual(result, 'Dramatic summary')

    @patch('app.requests.post')
    def test_summarize_article_gen_z_tone(self, mock_post):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "result": {
                "response": "Gen Z summary"
            }
        }
        mock_post.return_value = mock_response

        result = summarize_article('Test article content', 'gen z')
        self.assertEqual(result, 'Gen Z summary')

if __name__ == '__main__':
    unittest.main()
