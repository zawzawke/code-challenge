from lib.models.author import Author
from lib.models.magazine import Magazine
from lib.models.article import Article

def test_author_creation():
    author = Author("Test Author")
    author.save()
    assert author.id is not None
    print(f"Author created with id {author.id} and name '{author.name}'")

def test_find_author():
    author = Author.find_by_name("Test Author")
    assert author is not None
    print(f"Found author by name: {author.name} (id: {author.id})")

def test_add_article():
    magazine = Magazine("Test Magazine", "Testing")
    magazine.save()

    author = Author.find_by_name("Test Author")
    author.add_article(magazine, "Test Article")
    articles = author.articles()
    
    # If articles returns rows, check article title with indexing
    assert any(article.title == "Test Article" for article in articles)
    
    print(f"Article 'Test Article' added for author {author.name}")

def test_top_author():
    top = Author.top_author()
    if top:
        print(f"Top author: {top[1]} with {top[2]} articles")
    else:
        print("No top author found.")

def run_tests():
    print("Running Author model tests...")
    test_author_creation()
    test_find_author()
    test_add_article()
    test_top_author()
    print("All tests completed.")

if __name__ == "__main__":
    run_tests()
