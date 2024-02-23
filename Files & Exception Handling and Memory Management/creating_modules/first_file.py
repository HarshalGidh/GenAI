#import os and sys to merger all the directories path in a same location 
import os,sys
from os.path import dirname ,join, abspath
#join the files wat 0th index with absolute path and dir name and with '..'
sys.path.insert(0,abspath(join(dirname(__file__),'..')))

#importing file from second folder :
#from second_package import second_file

def kuch_kar():
    print("Hello Harshal ")

#second_file.kuch_bhi_kar() 