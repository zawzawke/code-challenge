# Code Challenge — Magazine CMS (Phase 3)
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

## Models Overview
### Author
Author(name) – Initializes a new author.

.save() – Persists the author to the database.

.articles() – Returns all articles written by the author.

.add_article(magazine, title) – Adds a new article for this author in the given magazine.

.magazines() – Returns all magazines the author has contributed to.

@classmethod find_by_name(name) – Finds an author by name.

@classmethod top_author() – Returns the author with the most articles.

### Magazine
Magazine(name, category) – Initializes a magazine.

.save() – Persists the magazine.

.articles() – Lists all articles published in the magazine.

.contributors() – Lists all unique authors who have written for this magazine.

.article_titles() – Returns all article titles published in this magazine.

.contributing_authors() – Returns authors with >2 articles in this magazine.

### Article
Article(author, magazine, title) – Initializes and saves a new article.

.save() – Saves the article record to the database.

@classmethod all() – Returns all articles.

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