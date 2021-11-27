from codesign.header import *
from flask_restful import Resource
from flask import render_template, request, jsonify, make_response
from codesign import auth
import  json

class Logout(Resource):
    def __init__(self):
        pass
    @auth.login_required
    def get(self):
        return ('logout', 401, {'WWW-Authenticate': 'Basic realm="Login required"'})


