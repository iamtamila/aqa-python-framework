import requests

def assert_status(response: requests.Response, expected: int) -> None:
    # Check the status code; on failure show method, URL, expected vs actual and the start of the body
    assert response.status_code == expected, (
        f"{response.request.method} {response.url}: "
        f"expected {expected}, got {response.status_code}. "
        f"Body: {response.text[:300]}"
    )