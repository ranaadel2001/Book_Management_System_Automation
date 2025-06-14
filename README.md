# Book_Management_System_Automation
# 📚 Book Management System – API Testing Project

This project is a hands-on API testing suite for a mock Book Management System. It uses Python, `requests`, and `pytest` to automate testing for the system's CRUD operations (Create, Read, Update, Delete). The test suite also includes **data-driven testing** using CSV input.

---

## 🚀 Technologies Used

- Python 3.x
- [requests](https://pypi.org/project/requests/)
- [pytest](https://docs.pytest.org/)
- CSV (for test data input)

---

## 📂 Project Structure

📁 BookAPI_Testing/
│
├── test_books.py # Main test file
├── books_data.csv # CSV file for data-driven tests
├── requirements.txt # Dependencies
└── README.md # Project documentation



---

## ✅ Test Coverage

The test suite includes:

### 🔹 Positive Test Cases
- `GET /books` – Get all books
- `GET /books/{id}` – Get a specific book
- `POST /books` – Add a new book
- `PUT /books/{id}` – Update an existing book
- `DELETE /books/{id}` – Delete a book

### 🔸 Negative Test Cases
- `GET /books/{invalid-id}` – Handle invalid book ID
- Future improvement: add more invalid payload scenarios

### 📊 Data-Driven Testing
- Automated creation of books from a CSV file using `pytest.mark.parametrize`

---

## 🧪 How to Run Tests

### 1. 📥 Install dependencies

pip install -r requirements.txt

2. ▶ Run all tests

pytest test_books.py -v

3. 📝 Generate HTML report (optional)

pip install pytest-html
pytest test_books.py --html=report.html --self-contained-html

📄 Example CSV Format

title,author,year,genre
Book 1,Author 1,2024,Tech
Book 2,Author 2,2023,Science
Book 3,Author 3,2025,Drama

