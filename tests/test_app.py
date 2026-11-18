"""Unit tests for src.app."""

import unittest
from unittest.mock import MagicMock, patch
from src.app import fetch_service_status, is_healthy


class TestApp(unittest.TestCase):
    """Test cases for service status helpers."""

    def test_invalid_url_raises_value_error(self) -> None:
        with self.assertRaises(ValueError):
            fetch_service_status("ftp://example.com")

    @patch("src.app.requests.get")
    def test_fetch_service_status_success(self, mock_get: MagicMock) -> None:
        mock_resp = MagicMock()
        mock_resp.status_code = 200
        mock_resp.ok = True
        mock_get.return_value = mock_resp

        result = fetch_service_status("https://example.com/health")
        self.assertEqual(result["status_code"], 200)
        self.assertTrue(result["ok"])
        mock_get.assert_called_once_with("https://example.com/health", timeout=5)

    def test_is_healthy(self) -> None:
        self.assertTrue(is_healthy({"status_code": 200}))
        self.assertTrue(is_healthy({"status_code": 204}))
        self.assertFalse(is_healthy({"status_code": 503}))
        self.assertFalse(is_healthy({}))


if __name__ == "__main__":
    unittest.main()
