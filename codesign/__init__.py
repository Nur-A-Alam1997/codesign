from flask import Flask, render_template, request, jsonify, make_response
from flask_restful import  Api
from flask_httpauth import HTTPBasicAuth
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SECRET_KEY']='Th1s1ss3cr3t'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///pallete.db' 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True 

db = SQLAlchemy(app)
api = Api(app, prefix="/api/v1")
auth = HTTPBasicAuth()


USER_DATA = {
    "admin": "1234",
    "user1": "1234",
    "user2": "1234",
}

@auth.verify_password
def verify(username, password):
    if not (username and password):
        return False
    return USER_DATA.get(username) == password

# from codesign.resources.resource import PrivateResource,CreatePalleteResource,CreateBookmarkResource,ManagePalleteResource,MyBookmarkResource,MyPalleteResource,Dashboard, Logout

from codesign.resources.create_bookmark_resource import CreateBookmarkResource
from codesign.resources.create_pallete_resource import CreatePalleteResource
from codesign.resources.manage_pallete_resource import ManagePalleteResource
from codesign.resources.my_bookmark_resource import MyBookmarkResource
from codesign.resources.my_pallete_resource import MyPalleteResource
from codesign.resources.dashboard_resource import Dashboard
from codesign.resources.logout_resource import Logout


# api.add_resource(PrivateResource, '/private')
api.add_resource(CreatePalleteResource, '/create')
api.add_resource(CreateBookmarkResource, '/bookmark/<pid>')
api.add_resource(ManagePalleteResource, '/pallete/<pid>')
api.add_resource(MyBookmarkResource, '/my_bookmark')
api.add_resource(MyPalleteResource, '/my_pallete')
api.add_resource(Dashboard, '/dashboard')
api.add_resource(Logout, '/logout')
