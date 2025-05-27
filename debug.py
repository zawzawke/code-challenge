from lib.models.author import Author
from lib.models.magazine import Magazine
from lib.models.article import Article
from lib.db.connection import get_connection

# Optional: Clear data before testing (for repeat runs)
def reset_db():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM articles")
    cursor.execute("DELETE FROM authors")
    cursor.execute("DELETE FROM magazines")
    conn.commit()
    print("Database reset.")

def main():
    reset_db()

    # Create and save authors
    author1 = Author("Zawzawke")
    author1.save()

    author2 = Author("Simiyu")
    author2.save()

    # Create and save magazines
    mag1 = Magazine("Tech Today", "Technology")
    mag1.save()

    mag2 = Magazine("Mind Matters", "Psychology")
    mag2.save()

    # Create and save articles
    art1 = Article("AI in 2025", author1.id, mag1.id)
    art1.save()

    art2 = Article("Robotics & You", author1.id, mag1.id)
    art2.save()

    art3 = Article("Brain Science", author2.id, mag2.id)
    art3.save()

    art4 = Article("AI Ethics", author2.id, mag1.id)
    art4.save()

    # Fetching and displaying data
    print("\nAll Articles by Zawzawke:")
    for article in author1.articles():
        print(f"- {article.title}")

    print("\nMagazines Simiyu has written for:")
    for mag in author2.magazines():
        print(f"- {mag.name}")

    print("\nAuthors who wrote for Tech Today:")
    for author in mag1.authors():
        print(f"- {author.name}")

    print("\nMagazines with articles by 2+ authors:")
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
    SELECT m.name FROM magazines m
    JOIN articles a ON m.id = a.magazine_id
    GROUP BY m.id
    HAVING COUNT(DISTINCT a.author_id) >= 2
    """)
    for row in cursor.fetchall():
        print(f"- {row[0]}")

    print("\nNumber of articles per magazine:")
    cursor.execute("""
    SELECT m.name, COUNT(a.id) as count
    FROM magazines m
    LEFT JOIN articles a ON m.id = a.magazine_id
    GROUP BY m.id
    """)
    for name, count in cursor.fetchall():
        print(f"- {name}: {count} articles")

    print("\nAuthor with the most articles:")
    cursor.execute("""
    SELECT a.name, COUNT(ar.id) as article_count
    FROM authors a
    JOIN articles ar ON a.id = ar.author_id
    GROUP BY a.id
    ORDER BY article_count DESC
    LIMIT 1
    """)
    row = cursor.fetchone()
    print(f"- {row[0]} ({row[1]} articles)")

if __name__ == "__main__":
    main()
