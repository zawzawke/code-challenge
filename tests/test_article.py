from lib.models.article import Article
from lib.models.author import Author
from lib.models.magazine import Magazine
from lib.db.connection import get_connection

def reset_db():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM articles")
    cursor.execute("DELETE FROM authors")
    cursor.execute("DELETE FROM magazines")
    conn.commit()
    conn.close()

def test_article_methods():
    reset_db()

    # Setup: create one author and one magazine
    author = Author("Simiyu")
    author.save()
    mag = Magazine("Tech Today", "Technology")
    mag.save()

    # Create an article
    article = Article("AI and Future", author.id, mag.id)
    article.save()

    # Retrieve the article
    fetched = Article.find_by_id(article.id)
    
    #Assertions to validate the test
    assert fetched is not None
    assert fetched.title == "AI and Future"
    assert fetched.author_id == author.id
    assert fetched.magazine_id == mag.id
    
    print("Article test passed!")


if __name__ == "__main__":
    test_article_methods()
