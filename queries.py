from seed import *

def query_experimentation():
    pass
    # import pdb; pdb.set_trace()
def grateful_dead_genres():
    return session.query(Genre.name).join(Song).join(Artist).filter(Artist.name == "Grateful Dead").all()

def all_grateful_dead_songs():
    return session.query(Song.name).join(Artist).filter(Artist.name == "Grateful Dead").all()
