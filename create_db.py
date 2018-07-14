# create a table for Entry model in db
# python create_db.py to run it
# had it in scripts folder but it wouldn't run????

import os, sys
sys.path.append(os.getcwd())
from main import db

if __name__ == '__main__':
    db.create_all()
