# lib/debug.py
from lib.models.author import Author
from lib.models.magazine import Magazine
from lib.models.article import Article
from lib.db.seed import seed_database

def debug():
    # Seed the database first
    seed_database()
    
    # Example queries
    print("\nAll Authors:")
    for author in Author.get_all():
        print(f"{author.id}: {author.name}")

    print("\nAll Magazines:")
    for magazine in Magazine.get_all():
        print(f"{magazine.id}: {magazine.name} ({magazine.category})")

    print("\nAll Articles:")
    for article in Article.get_all():
        print(f"{article.id}: {article.title} by {article.author_id} in {article.magazine_id}")

    # Test relationships
    author = Author.find_by_name("John Doe")
    if author:
        print(f"\nArticles by {author.name}:")
        for article in author.articles():
            print(article['title'])

        print(f"\nMagazines {author.name} has contributed to:")
        for magazine in author.magazines():
            print(magazine['name'])

    magazine = Magazine.find_by_name("Tech Today")
    if magazine:
        print(f"\nContributors to {magazine.name}:")
        for contributor in magazine.contributors():
            print(contributor['name'])

if __name__ == '__main__':
    debug()