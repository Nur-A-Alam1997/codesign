from codesign.header import *
from codesign.models.favourite import Favourite
from codesign.models.pallete import Pallete
from codesign.models.dominant import Dominant
from codesign.models.accent import Accent

class ManagePalleteResource(Resource):

    def __init__(self):
        pass

    @auth.login_required
    def get(self,pid):
        
        single_pallete = Pallete.query.get(pid)
        if not single_pallete:
            return {'message': 'not found'},404
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
        return data

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
            return jsonify({'message': 'you are not authorized to or does not exists...'})
        print(edit_pallete.name)

        data = request.json

        edit_pallete.name = data['name']
        edit_pallete.dominant = str(data['dominant'])
        edit_pallete.accent = str(data['accent'])
        edit_pallete.state = data['state']
        db.session.commit()

        return jsonify({'message': 'Pallete edited'})
