from furl import furl
from .saver_agents import saver_agents

class Saver:

    def __init__(self, database_url):
        db = furl(database_url)
        if db.scheme not in saver_agents:
            raise Exception(
                f'No saver for the {db.scheme} was found. Make sure it is defined and located in the saver_agents package')
        self.saver = saver_agents[db.scheme](database_url)
    
    def save(self,data,field):
        self.saver.save(data=data, field=field)
