Introduction:

Big companies are not the only one that can have a database. Startups, 
like Sparkify can benefit of the use of advanced databases as well as pipelines.
With the use of postgres, Sparkify now can implement their queries and make insights
that can help the startup in understanding their users' favorite music and much more
instead of only storing the data in JSON files.
ETL pipeline will help Sparkify in transferring their data to database. The use of ETL 
pipeline will help Sparkify in implementing their queries and help their startup grow
faster in their market. 

Database Design:

The schema that is used in this data base Star Schema. It includes a fact table and four dimension tables.
The fact table is songplay and the dimension tables are users, song, artist, and time.


Repository files:
1.	Create_tables.py: 
This file includes the creation of the database, dropping tables function and create table function from sql_queries.py.
2.	Sql_queries.py:
This file includes the sql queries that will create tables and the function for inserting data into tables later in the ETL pipeline.
3.	ETL.py : 
Here, the pipeline will be used for reading the data from JSON files log_data and song_data and transferring data to the proper tables as well as combining several data from different table to insert into the fact table (songplay).
4.	Etl.ipynb: 
This files with information in-detail on how it is used for reading and inserting few data into the tables.
5.	Test.ipynb: 
This file is for testing the database and implementing some queries for showing the first 5 rows of the data in database tables.
