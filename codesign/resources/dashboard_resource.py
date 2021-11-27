from codesign.header import *
from flask_restful import Resource
from flask import render_template, request, jsonify, make_response
from codesign import auth
import  json

from codesign.models.pallete import Pallete


class Dashboard(Resource):

    def __init__(self):
        pass

    @auth.login_required(optional = True)
    def get(self):

        dashboard = Pallete.query.filter_by( state = True).all()
        print(dashboard)
        result = []   

        for pallete in dashboard:   
            pallete_data = {}   
            pallete_data['id'] = pallete.id 
            pallete_data['owner'] = pallete.owner
            pallete_data['name'] = pallete.name 
            pallete_data['dominant'] = pallete.dominant
            pallete_data['accent'] = pallete.accent
            pallete_data['state'] = pallete.state
            result.append(pallete_data)
            # accent_list =pallete_data['accent'].strip('[]').replace('\'', '').replace(' ', '').split(',')
            # print(type(accent_list))

        json_onject = {"pallete":result}
        r = json.dumps(json_onject)
        data = json.loads(r)
        headers = {'Content-Type': 'text/html'}
        return make_response(render_template("book_mark.html",data = data ),200,headers)

