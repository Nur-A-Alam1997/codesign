from flask_restful import Resource
from flask import render_template, request, jsonify, make_response
from codesign import auth
import  json
from codesign.models.models import Pallete, Favourite, Dominant, Accent
# from codesign.header import *
# from codesign.models.pallete import Pallete
# from codesign.models.favourite import Favourite
# from codesign.models.dominant import Dominant
# from codesign.models.accent import Accent


class PrivateResource(Resource):

    @auth.login_required
    def get(self):
        return {"meaning_of_life": 42}


class CreatePalleteResource(Resource):

    def __init__(self):
        pass
    
    @auth.login_required()
    def get(self):
        dominant = Dominant.query.all()
        accent = Accent.query.all()
        
        dom_list= []
        for dom in dominant:
            colors = {}
            colors ['id'] = dom.id
            colors ['color'] = dom.color
            dom_list.append(colors)
        
        accent_list = []
        for acc in accent:
            colors = {}
            colors ['id'] = acc.id
            colors ['color'] = acc.color
            accent_list.append(colors)
        
        obj = {
            "dominant":dom_list,
            "accent":accent_list,
            "user":auth.current_user()
        }

        r = json.dumps(obj)
        data = json.loads(r)

        headers = {'Content-Type': 'text/html'}
        return make_response(render_template('public_view.html',data = data ),200,headers)

    @auth.login_required()
    def post(self):
        data = request.json
        pallete = Pallete( owner = auth.current_user(), name=data['name'], dominant=str(data['dominant']), accent = str(data['accent']) ,state = data['state']) 
        db.session.add(pallete)
        db.session.commit()   
        print(str(data['accent']))
        return {'success':True}, 200, {'ContentType':'application/json'} 




class ManagePalleteResource(Resource):

    def __init__(self):
        pass

    @auth.login_required
    def get(self,pid):
        
        single_pallete = Pallete.query.get(pid)
        if not single_pallete:
            return jsonify({'message': 'not found'})   
        dominant = Dominant.query.all()
        accent = Accent.query.all()
        
        dom_list= []
        for dom in dominant:
            colors = {}
            colors ['id'] = dom.id
            colors ['color'] = dom.color
            dom_list.append(colors)
        
        accent_list = []
        for acc in accent:
            colors = {}
            colors ['id'] = acc.id
            colors ['color'] = acc.color
            accent_list.append(colors)
    
        dominant = single_pallete.dominant.strip('[]').replace('\'', '').replace(' ', '').split(',')
        dominant_int = list(map(int, dominant))
        dominant_array = [0]*8
        for idx in dominant_int:
            dominant_array[idx] = 1
        print(dominant_array)
        
        accent = single_pallete.accent.strip('[]').replace('\'', '').replace(' ', '').split(',')
        accent_int = list(map(int, accent))
        accent_array = [0]*8
        for idx in accent_int:
            accent_array[idx] = 1
        print(accent_array)

        bookmark = Favourite.query.filter_by(owner = auth.current_user()).first()
        if bookmark:
            favourite = set(bookmark.fav.split(','))

            if pid in favourite:
                bookmark = True
                print(bookmark)
            else:
                bookmark = False

        state = single_pallete.state
        name = single_pallete.name
        owner = single_pallete.owner

        json_onject = {
            "pid":pid,
            "dominant":dom_list,
            "accent":accent_list,
            "accent_array":accent_array,
            "dominant_array" : dominant_array, 
            "state":state, 
            "name":name,
            "owner":owner,
            "user":auth.current_user(),
            "bookmark":bookmark
            }
        r = json.dumps(json_onject)
        data = json.loads(r)

        headers = {'Content-Type': 'text/html'}
        return make_response(render_template("test_edit.html",data = data ),200,headers)

    @auth.login_required()
    def delete(self,pid):
        bookmark = Pallete.query.filter_by(id = pid,owner= auth.current_user()).first()   
        if not bookmark:   
            return jsonify({'message': 'you are not authorized to...'})   
        db.session.delete(bookmark)  
        db.session.commit()   

        return jsonify({'message': 'Pallete deleted'})

    @auth.login_required()
    def put(self,pid):
        print("i gorhit")
        edit_pallete = Pallete.query.filter_by(id = pid,owner= auth.current_user()).first()   
        if not edit_pallete:   
            return jsonify({'message': 'you are not authorized to...'})
        print(edit_pallete.name)

        data = request.json

        edit_pallete.name = data['name']
        edit_pallete.dominant = str(data['dominant'])
        edit_pallete.accent = str(data['accent'])
        edit_pallete.state = data['state']
        db.session.commit()

        return jsonify({'message': 'Pallete edited'})


class CreateBookmarkResource(Resource):

    def __init__(self):
        pass

    @auth.login_required
    def put(self,pid):
        bookmark = Favourite.query.filter_by(owner = auth.current_user()).first()
        if not bookmark:
            book_mark = Favourite( owner = auth.current_user(), fav = str(pid)) 
            db.session.add(book_mark)
            db.session.commit()

            return jsonify({'message': 'succesful changes'})
        book_mark = Favourite.query.filter_by( owner = auth.current_user()).first()
        favour = book_mark.fav.strip('[]').replace('\'', '').replace(' ', '').split(',')
        print(favour,type(favour))
        try:
            favour.remove(pid)
            book_mark.fav = str(",".join(favour))
        except:
            fav = book_mark.fav
            fav = fav + f",{pid}"
            book_mark.fav = fav
            print("Something went wrong")
        finally:
            db.session.commit()        
        return jsonify({'message': f'successful changes'})

class MyBookmarkResource(Resource):

    def __init__(self):
        pass


    @auth.login_required
    def get(self):
        bookmark = Favourite.query.filter_by(owner = auth.current_user()).first()
        if bookmark:
            list_id = bookmark.fav.split(',')
            print(list_id)
            favourite_pallete = db.session.query(Pallete).filter(Pallete.id.in_(list_id)).all()
            result = []
            for pallete in favourite_pallete:
                pallete_data = {}
                pallete_data['id'] = pallete.id 
                pallete_data['owner'] = pallete.owner
                pallete_data['name'] = pallete.name 
                result.append(pallete_data)

            json_onject = {"pallete":result}
            r = json.dumps(json_onject)
            obj = json.loads(r)

            headers = {'Content-Type': 'text/html'}
            return make_response(render_template("book_mark.html",data = obj ),200,headers)
        return jsonify({'error': "Not found"})  


# session.query(Pallete).filter(Pallete.id.in_((123,456))).all()

# @app.route("/logout")
class Logout(Resource):
    def __init__(self):
        pass
    @auth.login_required
    def get(self):
        return ('logout', 401, {'WWW-Authenticate': 'Basic realm="Login required"'})


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

class MyPalleteResource(Resource):

    def __init__(self):
        pass

    @auth.login_required
    def get(self):

        my_pallete = Pallete.query.filter_by( owner = auth.current_user()).all()
        print(my_pallete)
        print("Hello, {}!".format(auth.current_user()))
        if not my_pallete:
            return jsonify({"message":"not found"})
        result = []

        for pallete in my_pallete:   
            pallete_data = {}   
            pallete_data['id'] = pallete.id 
            pallete_data['owner'] = pallete.owner 
            pallete_data['name'] = pallete.name 
            pallete_data['dominant'] = pallete.dominant
            pallete_data['accent'] = pallete.accent
            pallete_data['state'] = pallete.state
            result.append(pallete_data)
            accent_list = pallete_data['accent'].strip('[]').replace('\'', '').replace(' ', '').split(',')
            print(type(accent_list))

        json_onject = {"pallete":result}
        r = json.dumps(json_onject)
        data = json.loads(r)
        
        headers = {'Content-Type': 'text/html'}
        return make_response(render_template("book_mark.html",data = data ),200,headers)
