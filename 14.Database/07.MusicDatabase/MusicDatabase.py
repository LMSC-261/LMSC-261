import sqlite3

DATABASE = "Music.db"

db = sqlite3.connect(DATABASE) # Open a database
db.row_factory = sqlite3.Row # Get the query results from SQLite with dictionary
cursor = db.cursor() # Use the cursor to execute SQLite query commands

# Get all rows in the Album table with ArtistId 1
cursor.execute("SELECT * FROM Album WHERE ArtistId = 1") 
rows = cursor.fetchall() # Actually fetch al rows into the rows variable

# Print all rows with the ArtistId 1
for row in rows:
  print(f"AlbumID: {row['AlbumId']}, Title: {row['Title']}, ArtistId: {row['ArtistId']}.")

print()
print("Join Two Tables:")

# Get all rows in the Album and Artist tables
cursor.execute("SELECT * FROM Album, Artist WHERE Album.ArtistId = Artist.ArtistId")
rows = cursor.fetchall() # Actually fetch al rows into the rows variable

# Print all rows from the Album and Artist tables
for row in rows:
  print(f"AlbumID: {row['AlbumId']}, Title: {row['Title']}, Artist: {row['Name']}.")

print()
print("Join Two Tables with the JOIN keyword: ")

# Same as above but with the JOIN keyword
cursor.execute("SELECT * FROM Artist JOIN Album ON Artist.ArtistId = Album.ArtistId")
rows = cursor.fetchall() # Actually fetch al rows into the rows variable

# Print all rows from the Album and Artist tables
for row in rows:
  print(f"AlbumID: {row['AlbumId']}, Title: {row['Title']}, Artist: {row['Name']}.")

db.close() # Close the database