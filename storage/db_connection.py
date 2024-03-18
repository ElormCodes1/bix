#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
testdbconn: Testing PostgreSQL database connection
"""
import sys
import psycopg2

print(sys.version_info)  # Print Python version for debugging
print("--------------")
conn = None

try:
    # Open database connection.
    # conn = psycopg2.connect(database='testdb', user='testuser', password='xxxx', host='localhost', port='5432')
    conn = psycopg2.connect(
        database="leads",
        user="elorm",
        password="elorm",
        host="localhost",
        port="5432",
    )
    print("Connected...")

    # Get a cursor from the connection, for traversing the records in result-set
    cursor = conn.cursor()

    # Execute a MySQL query via execute()
    cursor.execute("SELECT VERSION()")
    # cursor.execute("SELECT xxx")  # uncomment to trigger an exception

    # Fetch one (current) row into a tuple
    version = cursor.fetchone()
    print("Database version: {}".format(version))  # one-item tuple

except psycopg2.DatabaseError as e:
    print("Error code {}: {}".format(e.pgcode, e))
    sys.exit(1)  # Raise a SystemExit exception for cleanup, but honor finally-block

finally:
    print("finally...")
    if conn:
        # Always close the connection
        conn.close()
        print("Closed...")
