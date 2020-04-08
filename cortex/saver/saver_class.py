from furl import furl
from .saver_agents import saver_agents

class Saver:
    """
    A wrapper class for the saver_agents package.
    Recieves a database_url parameter, determines which saver to use based on the scheme
    """
    def __init__(self, database_url):
        db = furl(database_url)
        if db.scheme not in saver_agents:
            raise Exception(
                f'No saver for the {db.scheme} was found. Make sure it is defined and located in the saver_agents package')
        self.saver = saver_agents[db.scheme](database_url)
    
    def save(self,data,field):
        """
        Saves the data of the given snapshot and the respective field.

        :param data: Parsed data dict as received from the parser of the respective field
        :param field: The field of the parser from which the data was received
        """
        self.saver.save(data=data, field=field)
