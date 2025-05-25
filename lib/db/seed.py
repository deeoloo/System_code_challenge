# lib/db/seed.py
from lib.models.author import Author
from lib.models.magazine import Magazine
from lib.models.article import Article
from lib.db.connection import get_connection


def initialize_database():
    conn = get_connection()
    cursor = conn.cursor()
    with open("lib/db/schema.sql", "r") as f:
        schema = f.read()
        cursor.executescript(schema)
    conn.commit()
    conn.close()

def seed_database():
    # Clear existing data
    initialize_database()
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM articles")
    cursor.execute("DELETE FROM authors")
    cursor.execute("DELETE FROM magazines")
    conn.commit()
    conn.close()

     # Create authors - now with more diverse professions
    authors = [
        Author("Alex Rivera"),      # Tech journalist
        Author("Samira Patel"),    # Science writer
        Author("James Wilson"),    # Business analyst
        Author("Taylor Chen"),     # Freelance writer
        Author("Morgan Lee")       # Investigative reporter
    ]
    for author in authors:
        author.save()

    # Create magazines - expanded categories
    magazines = [
        Magazine("Digital Frontier", "Technology"),
        Magazine("Nature Unbound", "Science"),
        Magazine("Global Markets", "Business"),
        Magazine("Creative Minds", "Arts"),
        Magazine("Health Horizons", "Medicine")
    ]
    for magazine in magazines:
        magazine.save()

    # Create articles - more varied topics
    articles = [
        # Tech articles
        Article("Blockchain Revolution", authors[0].id, magazines[0].id),
        Article("The Rise of Quantum Computing", authors[0].id, magazines[0].id),
        Article("Cybersecurity in 2024", authors[3].id, magazines[0].id),
        
        # Science articles
        Article("Mars Colonization Challenges", authors[1].id, magazines[1].id),
        Article("CRISPR Gene Editing Breakthroughs", authors[1].id, magazines[1].id),
        Article("Deep Sea Discoveries", authors[4].id, magazines[1].id),
        
        # Business articles
        Article("Emerging Markets Outlook", authors[2].id, magazines[2].id),
        Article("Sustainable Investing Trends", authors[2].id, magazines[2].id),
        Article("Remote Work Economics", authors[3].id, magazines[2].id),
        
        # Cross-category articles
        Article("Tech in Modern Art", authors[3].id, magazines[3].id),
        Article("The Science of Creativity", authors[1].id, magazines[3].id),
        Article("AI in Healthcare", authors[0].id, magazines[4].id),
        Article("Pandemic Preparedness", authors[4].id, magazines[4].id)
    ]
    for article in articles:
        article.save()

    print("Database seeded successfully!")
if __name__ == "__main__":
    seed_database()
