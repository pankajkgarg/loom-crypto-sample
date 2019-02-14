# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals

__author__ = 'pankaj'

import os
from .config import CONFIG
import plyvel
from six import text_type, binary_type

parent_dir = os.path.dirname(os.path.abspath(__file__))

db_dir_path = os.path.join(parent_dir, CONFIG["db_dir"])

db = plyvel.DB(db_dir_path, create_if_missing=True)

def store(key, value):
	"""
	Store key, value pair in leveldb database
	(Encodes key, value to binary type before making db call)
	:param key:
	:param value:
	:return:
	"""
	encoded_key = convert_to_binary(key)
	encoded_value = convert_to_binary(value)

	db.put(encoded_key, encoded_value)

def retrieve(key):
	encoded_key = convert_to_binary(key)

	return db.get(encoded_key)


def convert_to_binary(value):
	"""
	Converts value to binary type (if its text type)
	:param value:
	:return:
	"""
	encoded_value = value
	if isinstance(encoded_value, text_type):
		encoded_value = encoded_value.encode("utf-8")

	return encoded_value

