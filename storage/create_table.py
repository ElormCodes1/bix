#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
testsqlstmts: Testing SQL statements: CREATE TABLE, INSERT, SELECT
"""
import psycopg2

import sys

print(sys.version_info)  # Print Python version for debugging
print("--------------")

with psycopg2.connect(
    database="test",
    user="elorm",
    password="elorm",
    host="localhost",
    port="5432",
) as conn:
    with conn.cursor() as cursor:
        # Create a new table
        cursor.execute("drop table if exists mensfashion")
        cursor.execute(
            """create table if not exists mensfashion(
                            id uuid,
                            url varchar(2000),
                            average_rating decimal(3,2),
                            reviews integer,
                            name varchar(200),
                            color varchar(200),
                            price decimal(5,2),
                            category varchar(200),
                            description varchar(2000),
                            primary key (id)
                        )"""
        )
