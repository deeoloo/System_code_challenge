
# system 
#  Author, Magazine & Article Management System

This is a Python project using SQLite to manage authors, magazines, and articles. It includes basic create, read, and relationship features for each entity.

---

##  Project Overview

- **Author**: Create and find authors by ID or name. View their articles and associated magazines.
- **Magazine**: Create and find magazines by ID or name. View all authors contributing to a magazine.
- **Article**: Create articles linked to authors and magazines. Find by ID or title.

---

##  Setup Instructions

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd System_code_challenge
````

### 2. Set up a virtual environment

For **venv**:

```bash
python3 -m venv venv
source venv/bin/activate   # On Linux/macOS
venv\\Scripts\\activate    # On Windows
```

For **pipenv** (if preferred):

```bash
pip install pipenv
pipenv shell
```

### 3. Install dependencies

There are no external packages yet. If needed later:

```bash
pip install -r requirements.txt
```

---

##  Initialize and Seed the Database

Run the following to create tables and populate them with sample data:

```bash
python3 -m lib.db.seed
```

You should see:

```
Database seeded successfully!
```

---

##  View Your Data

To inspect the database:

```bash
sqlite3 articles.db
.tables
SELECT * FROM authors;
```

---

##  Run Tests

Make sure the database is seeded, then run:

```bash
pytest
```

---

##  Project Structure

```
System_code_challenge/
├── articles.db
├── lib/
│   ├── db/
│   └── models/
├── tests/
└── README.md
```
