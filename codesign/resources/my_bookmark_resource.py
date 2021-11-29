from codesign.header import *
from codesign.models.pallete import Pallete
from codesign.models.favourite import Favourite


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
            return obj
        return jsonify({'error': "Not found"})  
