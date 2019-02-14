# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals

__author__ = 'pankaj'

import hashlib
from .models.user import User, UserAlreadyExists
from flask import Flask, request, jsonify


app = Flask(__name__)

@app.route("/api/register", methods=["POST"])
def register_user():
	name = request.form.get("name")
	email = request.form.get("email")

	try:
		uid = User.create(name, email)
	except (ValueError, UserAlreadyExists) as err:
		return return_error_response(err)
	else:
		return jsonify({
			"success": True,
			"data": {
				"uid": uid,
			}
		})


@app.route("/api/search-by-uid/<uid>")
def search_by_uid(uid):
	try:
		user = User.get_user_by_uid(uid)
	except ValueError as err:
		return return_error_response(err)
	else:
		if not user:
			return return_error_response("No User found!")

		return jsonify({
			"success": True,
			"data": {
				"user": user,
			}
		})

@app.route("/api/search-by-email/<email>")
def search_by_email(email):
	try:
		user = User.get_user_by_email(email)
	except ValueError as err:
		return return_error_response(err)
	else:
		if not user:
			return return_error_response("No user found!")

		return jsonify({
			"success": True,
			"data": {
				"user": user,
			}
		})


def return_error_response(err_or_message):
	"""
	Will return proper API response for an error
	:param err: An instance of Exception or plain error message as string
	:return:
	"""
	message = err_or_message
	if isinstance(err_or_message, Exception):
		message = err_or_message.message

	return jsonify({
		"success": False,
		"data": {
			"message": message
		}
	})
