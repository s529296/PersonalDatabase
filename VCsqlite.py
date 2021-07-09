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