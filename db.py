import sqlite3
import random


def connect_to_db():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn


def initial_setup():
    conn = connect_to_db()
    conn.execute(
        """
        DROP TABLE IF EXISTS quotes;
        """
    )
    conn.execute(
        """
        CREATE TABLE quotes (
          id INTEGER PRIMARY KEY NOT NULL,
          body TEXT,
          rarity TEXT
        );
        """
    )
    conn.commit()
    print("Table created successfully")

    quotes_seed_data = [
        ("Alright, alright, alight", "common"),
        ("Do you guys get this?", "uncommon"),
        ("Are you guys getting this?", "common"),
        ("Yeah..yeah..yeah..", "common"),
        ("Should I do that? Yeah...yeah...yeah yeah. Maybe, I don't know. Should I show it to you guys? I don't know. Yeah I'll show it to you guys.", "rare"),
        ("I'm old", "rare"),
        ("Should you choose to accept it...", "common"),
        ("You're gonna make a mistake because you're a horrible person...you're not a horrible person", "uncommon"),
        ("Don't do that, by the way. That's crazy", "common"),
        ("The correct answer is...", "common"),
        ("OR you can ask ChatGPT, but not as your first tool", "common"),
        ("ChatGPT is like a friend that you can bug anythime, but it'll be wrong 10 percent of the time", "common"),
        ("I don't know what to tell you", "common"),
        ("Coolio", "rare"),
        ("Give it some pizzazz", "rare"),
    ]
    conn.executemany(
        """
        INSERT INTO quotes (body, rarity)
        VALUES (?,?)
        """,
        quotes_seed_data,
    )
    conn.commit()
    print("Seed data created successfully")

    conn.close()


if __name__ == "__main__":
    initial_setup()

def quotes_all():
    conn = connect_to_db()
    rows = conn.execute(
        """
        SELECT * FROM quotes
        """
    ).fetchall()
    return [dict(row) for row in rows]


def quotes_create(body, rarity):
    conn = connect_to_db()
    row = conn.execute(
        """
        INSERT INTO quotes (body, rarity)
        VALUES (?, ?)
        RETURNING *
        """,
        (body, rarity),
    ).fetchone()
    conn.commit()
    return dict(row)

def quotes_update_by_id(id, body, rarity):
    conn = connect_to_db()
    row = conn.execute(
        """
        UPDATE quotes SET body = ?, rarity = ?
        WHERE id = ?
        RETURNING *
        """,
        (body, rarity, id),
    ).fetchone()
    conn.commit()
    return dict(row)

def quotes_find_random():
    conn = connect_to_db()
    row = conn.execute(
        """
        SELECT * FROM quotes
        ORDER BY RANDOM()
        LIMIT 1
        """
    ).fetchone()
    return dict(row)

def quotes_destroy_by_id(id):
    conn = connect_to_db()
    row = conn.execute(
        """
        DELETE from quotes
        WHERE id = ?
        """,
        (id,),
    )
    conn.commit()
    return {"message": "Quote destroyed successfully"}