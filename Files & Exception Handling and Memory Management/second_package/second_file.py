#import os and sys to merger all the directories path in a same location 
import os,sys
from os.path import dirname ,join, abspath
#join the files wat 0th index with absolute path and dir name and with '..'
sys.path.insert(0,abspath(join(dirname(__file__),'..')))

from creating_modules import first_file
def kuch_bhi_kar():
    print("This is second file")
first_file.kuch_kar()