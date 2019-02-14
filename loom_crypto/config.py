# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals

__author__ = 'pankaj'

import os

CONFIG = {
	"db_dir": os.environ.get("DATABASE_DIR") or "test_db"
}

