from lib.models.magazine import Magazine
from lib.models.author import Author
from lib.db.connection import get_connection

def reset_db():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM magazines")
    cursor.execute("DELETE FROM articles")
    cursor.execute("DELETE FROM authors")
    conn.commit()
    conn.close()

def test_magazine_methods():
    reset_db()

    # Setup
    mag1 = Magazine("Tech Today", "Technology")
    mag1.save()
    mag2 = Magazine("Mind Matters", "Psychology")
    mag2.save()

    author = Author("Zawzawke")
    author.save()

    # Add articles
    author.add_article(mag1, "AI in 2025")
    author.add_article(mag2, "Mindfulness")

    # Test articles()
    articles = mag1.articles()
    print("Articles in Tech Today:", articles)

    # Test contributors()
    contributors = mag1.contributors()
    print("Contributors to Tech Today:", contributors)

    # Test article_titles()
    titles = mag1.article_titles()
    print("Article titles in Tech Today:", titles)

    # Test contributing_authors()
    contrib_authors = mag1.contributing_authors()
    
    assert isinstance(contrib_authors, list)

    print("Magazine tests passed!")

if __name__ == "__main__":
    test_magazine_methods()
