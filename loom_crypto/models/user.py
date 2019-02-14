# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals

__author__ = 'pankaj'

import hashlib
from .. import database
import json
from six import text_type, binary_type

import logging

logging.basicConfig(level=logging.DEBUG)
#logger = logging.getLogger()
#logger.setLevel(logging.DEBUG)
#handler = logging.StreamHandler()

class UserAlreadyExists(Exception):
	pass




class User(object):

	@classmethod
	def create(cls, name, email):
		"""
		Creating a new user in database
		A user will have a name and email
		where email will enforce unique criteria

		User UID : the sha256 hash of email

		We will store data as following
		1. A key value of pair of (UID, JSON encoded user data)
		2. A key value pair of (email, UID)


		:param name:
		:param email:
		:return: UID of user
		"""
		if not name or not email:
			raise ValueError("Invalid input provided!")

		email = cls.sanitize_email(email)

		existing_user_uid = cls.search_by_email(email)
		logging.debug("existing_user_uid: %s %s", existing_user_uid, email)

		if existing_user_uid:
			raise UserAlreadyExists("A user with this email already exists!")

		uid = cls.hash_value(email)

		data = {
			"name": name,
			"email": email,
			"uid": uid,
		}
		data_json = cls.encode_user_data(data)

		database.store(uid, data_json)
		database.store(email, uid)

		return uid

	@classmethod
	def encode_user_data(cls, user_data):
		return json.dumps(user_data)

	@classmethod
	def decode_user_data(cls, encoded_data):
		return json.loads(encoded_data)

	@classmethod
	def get_user_by_uid(cls, uid):
		":return: A dict of user data if found else None"
		if not uid:
			raise None

		encoded_user_data = database.retrieve(uid)
		if not encoded_user_data:
			return None

		user = cls.decode_user_data(encoded_user_data)

		return user

	@classmethod
	def get_user_by_email(cls, email):
		":return: A dict of user data if found else None"
		uid = cls.search_by_email(email)

		if not uid:
			return

		return cls.get_user_by_uid(uid)



	@classmethod
	def search_by_email(cls, email):
		"""
		Finds a user by email and returns uid of user if found
		:param email: Email of the user
		:return: UID of user if found else None
		"""
		email = cls.sanitize_email(email)

		return database.retrieve(email)



	@staticmethod
	def sanitize_email(email):
		if not email:
			raise ValueError("Invalid input provided!")

		return email.lower().strip()

	@staticmethod
	def hash_value(value):
		"""
		Converts a value to its sha256 hash
		:param value:
		:return: A string(unicode) hash value
		"""
		encoded_value = value
		if isinstance(encoded_value, text_type):
			encoded_value = encoded_value.encode("utf-8", "ignore")

		return hashlib.sha256(encoded_value).hexdigest()


