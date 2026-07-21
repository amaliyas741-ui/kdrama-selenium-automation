import requests

BASE_URL = "https://jsonplaceholder.typicode.com"  # API לדוגמה


def test_get_drama_api():
    """בדיקת API מסוג GET"""
    response = requests.get(f"{BASE_URL}/posts/1")
    assert response.status_code == 200, f"סטטוס לא תואם: {response.status_code}"

    data = response.json()
    assert "id" in data
    assert data["id"] == 1


def test_create_drama_api():
    """בדיקת API מסוג POST"""
    payload = {
        "title": "Vincenzo",
        "body": "Dark Comedy Drama",
        "userId": 1
    }
    response = requests.post(f"{BASE_URL}/posts", json=payload)
    assert response.status_code == 201, "נכשל ביצירת אובייקט ב-API"
    assert response.json()["title"] == "Vincenzo"