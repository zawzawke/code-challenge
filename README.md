# code-challenge
## Project Overview
code-challenge is a mini content management system built in Python using SQLite to manage Authors, Articles, and Magazines. It models relationships between authors and the magazines they write for, allowing complex queries such as finding top authors, magazine contributors, and article counts.

This project demonstrates:

Object-oriented design with database-backed models

Complex SQL queries with joins and aggregates

Transaction management for batch operations

Test-driven development with automated test suites

## Features
Author, Article, and Magazine classes with CRUD and relational methods

Complex queries like top author by article count, magazines with multiple authors

Safe database transactions

Manual and automated testing with pytest

## Installation & Setup
### Prerequisites
Python 3.8+

SQLite3 installed (optional for DB inspection)

### Clone the Repository
git clone https://github.com/yourusername/code-challenge.git
cd code-challenge

### Install Dependencies
pip install -r requirements.txt

### Initialize Database
Set up the SQLite database using provided schema or migrations to create tables: authors, articles, and magazines.

## Usage
### Run Automated Tests
pytest

### Run Manual Tests
python tests/test_author.py
python tests/test_article.py
python tests/test_magazine.py

### Example Usage
from lib.models.author import Author
from lib.models.magazine import Magazine

author = Author("Paul Simiyu")
author.save()

magazine = Magazine("Tech Today", "Technology")
magazine.save()

author.add_article(magazine, "The Future of AI")

### Project Structure
code-challenge/
│
├── lib/
│   ├── models/
│   │   ├── author.py
│   │   ├── article.py
│   │   └── magazine.py
│   └── db/
│       └── connection.py
│
├── tests/
│   ├── test_author.py
│   ├── test_article.py
│   └── test_magazine.py
│
├── db/
│   └── code_challenge.db
│
├── README.md
└── requirements.txt

### Author 
Created by Paul Simiyu