from codesign.header import *
from codesign.models.favourite import Favourite


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
            db.session.commit()        
            return jsonify({'message': f'successfully removed {pid}'})

        except:
            fav = book_mark.fav
            fav = fav + f",{pid}"
            book_mark.fav = fav
            print("Something went wrong")
            db.session.commit()        
        return jsonify({'message': f'successfully added {pid}'})
