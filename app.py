from flask import Flask, render_template, request, jsonify, make_response
from flask_restful import Resource, Api
from flask_httpauth import HTTPBasicAuth
from flask_sqlalchemy import SQLAlchemy
import uuid, json

app = Flask(__name__)
app.config['SECRET_KEY']='Th1s1ss3cr3t'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///pallete.db' 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True 

db = SQLAlchemy(app)
# db.session.execute('CREATE TABLE IF NOT EXISTS pallete (id INTEGER PRIMARY KEY AUTOINCREMENT, roomname TEXT, key TEXT, email NOT NULL UNIQUE)')
# db.session.commit()


class Pallete(db.Model):  

    id = db.Column(db.Integer, primary_key=True)
    owner = db.Column(db.String(50))
    name = db.Column(db.String(50))
    dominant = db.Column(db.String(50))
    accent = db.Column(db.String(50))
    state = db.Column(db.Boolean)
    def __init__(self,owner, name, dominant, accent, state):
        self.owner = owner
        self.name = name
        self.dominant = dominant
        self.accent = accent
        self.state = state

class Favourite(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    owner = db.Column(db.String(50))
    fav = db.Column(db.String(80))
    def __init__(self,owner, fav):
        self.owner = owner
        self.fav = fav
        
api = Api(app, prefix="/api/v1")
auth = HTTPBasicAuth()

USER_DATA = {
    "admin": "1234",
    "user1": "1234",
}

@auth.verify_password
def verify(username, password):
    if not (username and password):
        return False
    return USER_DATA.get(username) == password

@auth.error_handler
def auth_error(status):
    return "Access Denied", status

class PrivateResource(Resource):

    @auth.login_required
    def get(self):
        return {"meaning_of_life": 42}


class HomeResource(Resource):

    def __init__(self):
        pass
    
    @auth.login_required()
    def get(self):
        print("Hello, {}!".format(auth.current_user()))
        # headers = {'Content-Type': 'text/html'}
        # return make_response(render_template('log.html'),200,headers)
        json_onject = {

            "user":auth.current_user()
            }
        r = json.dumps(json_onject)
        data = json.loads(r)
        headers = {'Content-Type': 'text/html'}
        return make_response(render_template("log.html",data = data ),200,headers)



@app.route("/pallete",methods = ["GET","POST"])
@auth.login_required
def pallete():
    if request.method == "GET":
        print("Hello, {}!".format(auth.current_user()))
        return render_template('log.html'),200

    if request.method == "POST":
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

        state = single_pallete.state
        name = single_pallete.name
        owner = single_pallete.owner
        print(owner,auth.current_user())

        json_onject = {
            "pid":pid,
            "accent":accent_array[1:],
            "dominant" : dominant_array[1:], 
            "state":state, 
            "name":name,
            "owner":owner,
            "user":auth.current_user()
            }
        r = json.dumps(json_onject)
        data = json.loads(r)
        # return render_template("edit_pallete.html",data = data )
        headers = {'Content-Type': 'text/html'}
        return make_response(render_template("edit_pallete.html",data = data ),200,headers)

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
        pallete = Pallete( owner = auth.current_user(), name=data['name'], dominant=str(data['dominant']), accent = str(data['accent']) ,state = data['state']) 
        edit_pallete.name = data['name']
        edit_pallete.dominant = str(data['dominant'])
        edit_pallete.accent = str(data['accent'])
        edit_pallete.state = data['state']
        db.session.commit()

        return jsonify({'message': 'Pallete edited'})


class BookmarkResource(Resource):

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




@app.route("/logout")
@auth.login_required
def logout():
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




# @app.route("/dashboard")
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
        # return render_template("book_mark.html",data = data )
        headers = {'Content-Type': 'text/html'}
        return make_response(render_template("book_mark.html",data = data ),200,headers)




api.add_resource(PrivateResource, '/private')
api.add_resource(HomeResource, '/home')
api.add_resource(BookmarkResource, '/bookmark/<pid>')
api.add_resource(ManagePalleteResource, '/pallete/<pid>')
api.add_resource(MyBookmarkResource, '/my_bookmark')
api.add_resource(MyPalleteResource, '/my_pallete')
api.add_resource(Dashboard, '/dashboard')


if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True, )#use_reloader=False
