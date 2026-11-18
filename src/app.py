"""Lightweight HTTP health-check helper for CI/CD testing."""

from typing import Dict, Any
import requests


def fetch_service_status(url: str, timeout: int = 5) -> Dict[str, Any]:
    """Fetch HTTP status information for a target URL safely.

    Args:
        url: Target HTTP or HTTPS URL.
        timeout: Request timeout in seconds.

    Returns:
        Dictionary containing the URL, status code, and ok flag.
    """
    if not url.startswith(("http://", "https://")):
        raise ValueError("URL must start with http:// or https://")

    response = requests.get(url, timeout=timeout)
    return {
        "url": url,
        "status_code": response.status_code,
        "ok": response.ok,
    }


def is_healthy(status_payload: Dict[str, Any]) -> bool:
    """Return True if the status payload represents a healthy 2xx response."""
    code = status_payload.get("status_code", 0)
    return 200 <= int(code) < 300
