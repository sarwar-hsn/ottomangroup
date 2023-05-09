#local server uses actual database from this pc. if it doesn't start add this pc's ip
#to the database

#the production server is when you upload the changes

#dev server is to test code with in local environment with local database

# from .local import *  
from .production import *
#from .development import *
