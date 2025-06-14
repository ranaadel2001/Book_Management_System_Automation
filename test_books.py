import requests
import csv
import pytest

BASE_URL = "https://684d954465ed087139168d92.mockapi.io/books"

def test_get_all_books():
    response = requests.get(BASE_URL)
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_book_by_id():
    response = requests.get(f"{BASE_URL}/1")
    assert response.status_code == 200
    data = response.json()
    assert "title" in data

def test_create_new_book():
    payload = {
        "title": "Automation Book",
        "author": "Rana Adel",
        "year": 2025,
        "genre": "Tech"
    }
    response = requests.post(BASE_URL, json=payload)
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "Automation Book"


def test_update_book():
    book_id = "1"  
    payload = {
        "title": "Updated Title",
        "author": "Rana Adel",
        "year": 2024,
        "genre": "Automation"
    }
    response = requests.put(f"{BASE_URL}/{book_id}", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Updated Title"

def test_delete_book():
    payload = {
        "title": "Temp Book",
        "author": "To Delete",
        "year": 2025,
        "genre": "Temp"
    }
    create_response = requests.post(BASE_URL, json=payload)
    book_id = create_response.json()["id"]

    delete_response = requests.delete(f"{BASE_URL}/{book_id}")
    assert delete_response.status_code == 200

################ Negative Test Cases ########################

def test_get_invalid_book():
    response = requests.get(f"{BASE_URL}/99999")
    assert response.status_code == 404 or response.status_code == 200  


########### Reading from csv file ##################
@pytest.mark.parametrize("title,author,year,genre", [
    (row["title"], row["author"], int(row["year"]), row["genre"])
    for row in csv.DictReader(open("books_data.csv"))
])
def test_create_book_from_csv(title, author, year, genre):
    payload = {
        "title": title,
        "author": author,
        "year": year,
        "genre": genre
    }
    response = requests.post(BASE_URL, json=payload)
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == title
    assert data["author"] == author




# def test_create_book_with_missing_fields():
#     payload = {
#         "title": "", #empty title
#         "author": "Rana",
#         # year and genre not exist
#     }
#     response = requests.post(BASE_URL, json=payload)
#     assert response.status_code in [400, 422]


