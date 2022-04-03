import sqlite3

DATABASE = "ThisGo.db"

db = sqlite3.connect(DATABASE) # Open a database
db.row_factory = sqlite3.Row # Get the query results from SQLite with dictionary
cursor = db.cursor() # Use the cursor to execute SQLite query commands

cursor.execute("SELECT * FROM artists") # Get all rows in the artists table
artists = cursor.fetchall() # Actually fetch al rows into the rows variable

cursor.execute("SELECT * FROM release") # Get all rows in the release table
release = cursor.fetchall() # Actually fetch al rows into the release variable

# Print all rows
for artist in artists:
  for r in release:
    if artist['id'] == r['artist_id']:
      print(f"{artist['name']} released {r['title']}.")

db.close() # Close the database