from codesign.header import *
from codesign.models.pallete import Pallete
from codesign.models.dominant import Dominant
from codesign.models.accent import Accent

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