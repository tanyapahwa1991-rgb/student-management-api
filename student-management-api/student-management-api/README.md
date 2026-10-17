# Student Management API

A Python backend mini-internship project for managing student records with **FastAPI**, **SQLAlchemy**, and **SQLite**. It demonstrates the four CRUD operations: Create, Read, Update, and Delete.

> Use dummy student data for demonstrations. Do not commit real student personal information or the local database file.

## Features

- Create student records.
- List all students, with optional search and course filters.
- Retrieve one student by ID.
- Update selected fields of an existing student.
- Delete a student record.
- Validate incoming data with Pydantic.
- Return clear `404` errors for missing records and `409` errors for duplicate email addresses.
- Store records persistently in a local SQLite database.
- Interactive API documentation through Swagger UI.

## Student fields

- `id`: automatically generated unique identifier
- `name`: required
- `date_of_birth`: required, formatted as `YYYY-MM-DD`
- `email`: optional; must be a valid email if provided and must be unique
- `phone`: optional
- `course`: optional
- `address`: optional
- `enrollment_date`: optional, formatted as `YYYY-MM-DD`
- `created_at`: generated timestamp

## Requirements

- Python 3.10 or newer
- pip
- Internet access for installing packages the first time

## Installation and running

### 1. Open the project folder in VS Code

Open the integrated terminal from **Terminal → New Terminal**.

### 2. Create a virtual environment

Windows:

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, use Command Prompt instead:

```bat
.venv\Scripts\activate.bat
```

macOS/Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Start the API

```bash
uvicorn main:app --reload
```

The API will normally be available at `http://127.0.0.1:8000`.

### 5. Test in Swagger UI

Open `http://127.0.0.1:8000/docs` in your browser. Expand an endpoint, click **Try it out**, enter the sample data below, and click **Execute**. Keep the terminal running while testing.

## API endpoints

| Method | Endpoint | Purpose |
|---|---|---|
| `POST` | `/students` | Create a student |
| `GET` | `/students` | List/filter students |
| `GET` | `/students/{student_id}` | Retrieve one student |
| `PUT` | `/students/{student_id}` | Update student fields |
| `DELETE` | `/students/{student_id}` | Delete a student |
| `GET` | `/health` | Health check |

### Sample create request

```json
{
  "name": "Aarav Mehta",
  "date_of_birth": "2007-05-14",
  "email": "aarav.demo@example.com",
  "phone": "9000000001",
  "course": "B.Tech AI/ML",
  "address": "Demo Address",
  "enrollment_date": "2025-08-01"
}
```

### Sample update request

Use the ID returned by the create request, then send a `PUT` request to `/students/1` (replace `1` with the actual ID). Only include fields you want to change.

```json
{
  "course": "B.Tech Computer Science",
  "phone": "9000000002"
}
```

### List and filter

- List records: `GET /students`
- Search name, email, or course: `GET /students?search=Aarav`
- Filter by course: `GET /students?course=B.Tech`
- Pagination: `GET /students?skip=0&limit=20`

### Expected response codes

- `201 Created`: student created successfully
- `200 OK`: list, retrieve, or update succeeded
- `204 No Content`: deletion succeeded
- `404 Not Found`: the requested student ID does not exist
- `409 Conflict`: duplicate email address
- `422 Unprocessable Entity`: request validation failed

## Project structure

```text
student-management-api/
├── app/
│   ├── __init__.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   └── routes/
│       ├── __init__.py
│       └── students.py
├── main.py
├── requirements.txt
├── .gitignore
└── README.md
```

The `students.db` file is created automatically when the application starts. It is intentionally excluded from Git because it is a local runtime database.

## Upload to GitHub

1. Create a new repository on GitHub named `student-management-api`.
2. Keep the repository public if your trainer requires a public link.
3. Upload the project files and folders (not the `.venv` folder or `students.db`). You can use GitHub's web upload or Git commands.
4. Confirm that `README.md`, `main.py`, `app/`, and `requirements.txt` appear in the repository.
5. Copy the repository URL and submit it using the channel/form specified by your trainer.

### Git command option

Run these commands from the project folder after creating an empty GitHub repository. Replace the URL with your own repository URL.

```bash
git init
git add .
git commit -m "Build Student Management CRUD API"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/student-management-api.git
git push -u origin main
```

## Notes

- This is a backend API; a separate frontend is not required by the core assignment.
- The optional Ollama/local AI extension is not included because the assignment says the CRUD application is sufficient.
- This project uses SQLAlchemy models and Pydantic schemas to keep database structure and request validation separate.
