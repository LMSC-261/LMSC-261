import sqlite3

DATABASE = "ThisGo.db"

db = sqlite3.connect(DATABASE) # Open a database
db.row_factory = sqlite3.Row # Get the query results from SQLite with dictionary
cursor = db.cursor() # Use the cursor to execute SQLite query commands
rows = cursor.execute("SELECT * FROM contact") # Get all rows in the table

# Print all rows
for row in rows:
  print(f"{row['name']} with {row['email']} submitted: {row['text']}")

db.close() # Close the database

