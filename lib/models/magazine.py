from lib.db.connection import get_connection
from lib.models.article import Article

class Magazine:
    def __init__(self, name, category, id=None):
        self.id = id
        self.name = name
        self.category = category

    def save(self):
        conn = get_connection()
        cursor = conn.cursor()

        if self.id:
            cursor.execute(
                "UPDATE magazines SET name = ?, category = ? WHERE id = ?",
                (self.name, self.category, self.id)
            )
        else:
            cursor.execute(
                "INSERT INTO magazines (name, category) VALUES (?, ?)",
                (self.name, self.category)
            )
            self.id = cursor.lastrowid

        conn.commit()
        conn.close()

    def articles(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM articles WHERE magazine_id = ?", (self.id,))
        articles = cursor.fetchall()
        conn.close()
        return articles

    def contributing_authors(self):
        conn = get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT authors.* FROM authors
                JOIN articles ON authors.id = articles.author_id
                WHERE articles.magazine_id = ?
                GROUP BY authors.id
                HAVING COUNT(articles.id) > 2
            """, (self.id,))
            return cursor.fetchall()
        finally:
            conn.close()

    def contributors(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT DISTINCT authors.* FROM authors
            JOIN articles ON authors.id = articles.author_id
            WHERE articles.magazine_id = ?
        """, (self.id,))
        contributors = cursor.fetchall()
        conn.close()
        return contributors

    def article_titles(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT title FROM articles
            WHERE magazine_id = ?
        """, (self.id,))
        titles = [row["title"] for row in cursor.fetchall()]
        conn.close()
        return titles

    @classmethod
    def find_by_id(cls, id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM magazines WHERE id = ?", (id,))
        row = cursor.fetchone()
        conn.close()
        return cls(**row) if row else None

    @classmethod
    def find_by_name(cls, name):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM magazines WHERE name = ?", (name,))
        row = cursor.fetchone()
        conn.close()
        return cls(**row) if row else None

    @classmethod
    def find_by_category(cls, category):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM magazines WHERE category = ?", (category,))
        row = cursor.fetchone()
        conn.close()
        return cls(**row) if row else None

    @classmethod
    def all(cls):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM magazines")
        magazines = [cls(**row) for row in cursor.fetchall()]
        conn.close()
        return magazines

    @classmethod
    def with_multiple_authors(cls):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT magazines.* FROM magazines
            JOIN articles ON magazines.id = articles.magazine_id
            GROUP BY magazines.id
            HAVING COUNT(DISTINCT articles.author_id) > 1
        """)
        rows = cursor.fetchall()
        conn.close()
        return [cls(**row) for row in rows]

    @classmethod
    def article_counts(cls):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT magazines.*, COUNT(articles.id) AS article_count FROM magazines
            LEFT JOIN articles ON magazines.id = articles.magazine_id
            GROUP BY magazines.id
        """)
        rows = cursor.fetchall()
        conn.close()
        return [dict(row) for row in rows]
