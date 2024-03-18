import sys
import psycopg2
import json

print(sys.version_info)  # Print Python version for debugging
print("--------------")

with psycopg2.connect(
    database="test", user="elorm", password="elorm", host="localhost", port="5432"
) as conn:
    with conn.cursor() as cursor:
        with open("shein_mens_fashion.json", "r") as f:
            for line in f:
                data = json.loads(line)
                cursor.execute(
                    """insert into mensfashion (url, average_rating, reviews, name, color, price, category, description) values
                                    (%s, %s, %s, %s, %s, %s, %s, %s)""",
                    (
                        data["url"],
                        data["average_rating"],
                        data["reviews_count"],
                        data["title"],
                        data["color"],
                        data["price"],
                        data["category_name"],
                        data["description"],
                    ),
                )
        # Commit the insert
        conn.commit()
