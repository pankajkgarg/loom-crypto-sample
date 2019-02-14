# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals

__author__ = 'pankaj'

import unittest
from loom_crypto.models.user import User
from loom_crypto import server


class ServerTestCase(unittest.TestCase):

	def setUp(self):
		self.user = {
			"name": "Alpha",
			"email": "test@example.com"
		}
		self.user_uid = "973dfe463ec85785f5f95af5ba3906eedb2d931c24e69824a89ea65dba4e813b"

		server.app.testing = True
		self.client = server.app.test_client()

	def tearDown(self):
		pass

	def test_register_user(self):

		response = self.client.post("/api/register", data=self.user)

		response_json = response.json
		self.assertEqual(response_json["success"], True)
		self.assertEqual(response_json["data"]["uid"], self.user_uid)

		# Testing with incomplete data
		user_copy = dict(self.user)
		user_copy.pop("email")
		response = self.client.post("/api/register", data=user_copy)
		self.assertEqual(response.json["success"], False, "User registered with incomplete data")

	def test_register_user_again(self):
		response = self.client.post("/api/register", data=self.user)

		response_json = response.json
		self.assertEqual(response_json["success"], False, "Registered user again")



	def test_search_by_uid(self):
		response = self.client.get("/api/search-by-uid/{}".format(self.user_uid))
		response_json = response.json

		self.assertEqual(response_json["success"], True)
		self.assertEqual(response_json["data"]["user"]["name"], self.user["name"])

		# Search for a non existing user
		response = self.client.get("/api/search-by-uid/{}".format(self.user_uid + "fd"))
		response_json = response.json

		self.assertEqual(response_json["success"], False)


	def test_search_by_email(self):
		response = self.client.get("/api/search-by-email/{}".format(self.user["email"]))
		response_json = response.json

		self.assertEqual(response_json["success"], True)
		self.assertEqual(response_json["data"]["user"]["name"], self.user["name"])

		# Search for a non existing user
		response = self.client.get("/api/search-by-email/{}".format(self.user["email"] + "fd"))
		response_json = response.json

		self.assertEqual(response_json["success"], False)


if __name__ == '__main__':
	unittest.main()


