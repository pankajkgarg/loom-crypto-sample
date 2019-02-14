##Loom Crypto Basic User Registration API

### Problem statement
Build a simple server http or tcp text server


1. That takes in a username and an email address, and stores it into a LevelDB database.  Then gives the user back a unique ID for the user. The key to the data should be this unique ID.

2. Create an endpoint that retrieves the user by the uniqueid 

3. Create an endpoint that retrieves the user by email

4. Create your own secondary index on LevelDB to query by email, so you don’t have to scan the entire database

###Design Decisions

All business logic for user is stored in `loom_crypto/models/user.py`
Server code is located in `loom_crypto/server.py`

#### How data is being stored

A user will have a name and email
where email will enforce unique criteria

User UID : the sha256 hash of email

We will store data as following
1. A key value of pair of (UID, JSON encoded user data)
2. A key value pair of (email, UID)



####Tests
See tests in `tests.py`

####Config
To change production database dir, define an enviornment variable `DATABASE_DIR`
