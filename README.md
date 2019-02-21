## Loom Crypto Basic User Registration API




### Design Decisions

All business logic for user is stored in `loom_crypto/models/user.py`
Server code is located in `loom_crypto/server.py`

#### How data is being stored

A user will have a name and email
where email will enforce unique criteria

User UID : the sha256 hash of email

We will store data as following
1. A key value of pair of (UID, JSON encoded user data)
2. A key value pair of (email, UID)



#### Tests
See tests in `tests.py`
To run the tests `pipenv run python tests.py`


#### Config
To change production database dir, define an enviornment variable `DATABASE_DIR`
