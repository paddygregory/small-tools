import os

def walk(dirname, visit_func):
    for name in os.listdir(dirname):
        path = os.path.join(dirname, name)
        if os.path.isfile(path):
            visit_func(path)
        else:
            walk(path, visit_func)

#walk('photos copy', print)

import hashlib 
import shelve

def is_image(path, extensions):
    name, ext = os.path.splitext(path)
    if ext in extensions:
        return True
    else:
        return False



def md5_digest(filename):
    data = open(filename, 'rb').read()
    md5_hash = hashlib.md5()
    md5_hash.update(data)
    digest = md5_hash.hexdigest()
    return digest

db = shelve.open('shelf', 'n')

def add_path(path, db):
    digest = md5_digest(path)
    if digest not in db:
        db[digest] = [path]
    else:
        db[digest].append(path)

def process_path(path, extensions, db):
    if is_image(path, extensions):
        add_path(path, db)

extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp']
walk('photos copy', lambda path: process_path(path, extensions, db))

for digest, paths in db.items():
    if len(paths) > 1:
        print(paths)

db.close()

