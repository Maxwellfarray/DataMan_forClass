# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 12:19:14 2023

@author: trent
"""

from flask import Blueprint
from flask import flash
from flask import g
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for
from werkzeug.exceptions import abort

from flaskr.auth import login_required
from flaskr.db import get_db

math = Blueprint("blog", __name__)

@math.route("/")
