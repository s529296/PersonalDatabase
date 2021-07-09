import mysql.connector
import sqlite3
import os
import numpy as np
from imgarray import save_array_img, load_array_img
from os import fsync
import eel

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Hannah@2021",
    database="noahhan"
)

mycursor = mydb.cursor()
title = ''
date = ''
rating = 0
notes = ""

# Query to create table for Viewed content
create_viewed_content_table_query = """
CREATE TABLE viewed_content (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title_viewed VARCHAR(100),
    date_viewed VARCHAR(100),
    rating DECIMAL(2,1),
    notes VARCHAR(200)
)
"""

eel.init('web')


@eel.expose()
def insertnewview(title, date, rating, note):
    # Dynamic query that sends to Viewed content record to mySQL
    insert_viewed_record_query = """
        INSERT INTO viewed_content (title_viewed, date_viewed, rating, notes)
        VALUES
            ("{title}", "{date}", {rating}, "{notes}")
    """.format(title=title, date=date, rating=rating, notes=note)
    # Sends the new data to the database and commits it
    with mydb.cursor() as cursor:
        mydb.cursor().execute(insert_viewed_record_query)
        mydb.commit()


eel.start('index.html')

import sqlite3
def runsql(state):
    # Connect to the database file, if it does not exist, create it automatically
    conn = sqlite3.connect('viewedcontent.db')
    c = conn.cursor()

    # Run the sql statement and get the sqlite.cousor object
    cursor = c.execute(state)

    # Read the contents of the cursor
    for i in cursor:
        print(i)

    conn.commit()
    # Close the connection
    conn.close()

    return cursor
    pass
