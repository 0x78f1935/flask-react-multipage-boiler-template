from flask import current_app
from datetime import datetime


class CustomFunctions(object):
    @staticmethod
    def datenow():
        """
        Returns
        -------
        Datetime
            UTCNOW
        """
        return datetime.utcnow()
    
    @staticmethod
    def get_debug_bool():
        """
        Returns
        -------
        Bool
            Returns the server debug value
        """
        return current_app.config["TESTING"]
