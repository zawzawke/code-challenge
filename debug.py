from lib.db.connection import get_connection
from lib.models.author import Author
from lib.models.magazine import Magazine

def test_complex_queries():
    print("Testing complex SQL query methods...\n")

    # 1. Authors who have written for a specific magazine
    mag = Magazine.find_by_name("Tech Today")
    if mag:
        print(f"Authors who wrote for magazine '{mag.name}':")
        authors = mag.authors()
        for author in authors:
            print(f"- {author[1]}")
    else:
        print("Magazine 'Tech Today' not found.")
    print()

    # 2. Magazines with articles by at least 2 different authors
    print("Magazines with articles by 2 or more authors:")
    magazines = Magazine.magazines_with_multiple_authors(2)
    for magazine in magazines:
        print(f"- {magazine[1]} (Category: {magazine[2]})")
    print()

    # 3. Number of articles per magazine
    print("Number of articles per magazine:")
    counts = Magazine.article_counts()
    for name, count in counts:
        print(f"- {name}: {count} articles")
    print()

    # 4. Author who has written the most articles
    top_author = Author.top_author()
    if top_author:
        print(f"Author with the most articles: {top_author[1]} ({top_author[2]} articles)")
    else:
        print("No authors found.")

if __name__ == "__main__":
    test_complex_queries()
