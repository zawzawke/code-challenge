from lib.models.author import Author
from lib.models.magazine import Magazine
from lib.db.connection import get_connection

def main():
    # Connect to DB
    conn = get_connection()
    
    # Test Author methods
    print("Testing Author methods...")
    author = Author.find_by_id(1)
    if author:
        print(f"Author found: {author.name}")
        print("Articles by author:")
        for article in author.articles():
            print(article)
        print("Magazines author contributed to:")
        for mag in author.magazines():
            print(mag)
        print("Topic areas author contributed to:")
        for category in author.topic_areas():
            print(category)

        # Test add_article
        magazine = Magazine.find_by_id(1)
        if magazine:
            author.add_article(magazine, "New Article Title from debug.py")
            print("Added new article for author.")

    else:
        print("Author with ID 1 not found.")

    # Test Magazine methods
    print("\nTesting Magazine methods...")
    magazine = Magazine.find_by_id(1)
    if magazine:
        print(f"Magazine found: {magazine.name}")
        print("Articles in magazine:")
        for article in magazine.articles():
            print(article)
        print("Contributors to magazine:")
        for contributor in magazine.contributors():
            print(contributor)
        print("Article titles in magazine:")
        for title in magazine.article_titles():
            print(title)
        print("Contributing authors with > 2 articles:")
        for author in magazine.contributing_authors():
            print(author)
    else:
        print("Magazine with ID 1 not found.")

if __name__ == "__main__":
    main()
