import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Hannah@2021",
    database="noahhan"
)

mycursor = mydb.cursor()



create_viewed_content_table_query = """
CREATE TABLE viewed_content (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title_viewed VARCHAR(100),
    date_viewed VARCHAR(100),
    rating DECIMAL(2,1),
    notes VARCHAR(200)
)
"""
insert_viewed_record_query = """
INSERT INTO
"""
with mydb.cursor() as cursor:
  cursor.execute(create_viewed_content_table_query)
  mydb.commit()
