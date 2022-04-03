# SQLite Basic Operation

## Create Database
- To create a new database, type in the following command in CLI:

		sqlite3 contact.db

- Here, `contact.db ` will be the name of the database.
- `.db` extension is optional, but makes it clear for us that this is a sqlite database
- The `contact.db ` file will be created in the same directory where the command is executed. This happens when we create a new table.
- Executing the above command will also provide us with SQLite command prompt that starts with `sqlite>`.

## Create Table
- Once we are in the sqlite command prompt, we can create a table in that database with a following command:

		CREATE TABLE 'contact' ('id' integer, 'name' varchar(255), 'email' varchar(255), 'text' TEXT);

- Here, the name of our new table is `contact`.
- We also created three fields/columns in the `contact` table, `id`, `name`, `email`, `text`.
- By convention, we use 255 for our `varchar` fields, since that used to be the maximum for many older databases, and are probably enough for all realistic possibilities, without being too excessive. 

## Query the Database Schema
- To see a list of the tables in the database, type:

		.tables

- To see the complete schema for the database, type:

		.schema
		
- To add a row to the table, type:

		INSERT INTO contact (id, name, email, text) VALUES(1, 'Mary', 'mary@berklee.edu', 'Hello');

## Add Data to a Table
- You may not need to specify the column names `(id, name, email, text)` in the SQLite query if you are adding values for all the columns of the table. However, make sure the order of the values is in the same order as the columns in the table.
- Conventionally, the uppercased words are SQL keywords, while the rest are words specific to our data. 

## Fetch Data from a Table
- To see the content of the table, type:

		SELECT * FROM contact;

- Filter out unwanted data with:

		SELECT * FROM contact WHERE name = 'Mary';

- We can also specify just the fields we want to get back:

		SELECT name FROM contact WHERE email = 'mary@berklee.edu';
		
## Update and Delete Data from a Table
- Change the contents of rows with:

		UPDATE contact SET name = 'John' WHERE id = 1;

- Delete rows with:

		DELETE FROM contact WHERE id = 1;

## Exit from SQLite
- In the command prompt, type in:

		.exit