### Problem statement
Build a simple server http or tcp text server


1. That takes in a username and an email address, and stores it into a LevelDB database.  Then gives the user back a unique ID for the user. The key to the data should be this unique ID.

2. Create an endpoint that retrieves the user by the uniqueid

3. Create an endpoint that retrieves the user by email

4. Create your own secondary index on LevelDB to query by email, so you don’t have to scan the entire database

