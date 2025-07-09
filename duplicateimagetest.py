import os
import hashlib
import shelve


def walk(dirname, visit_func):
    for name in os.listdir(dirname):
        path = os.path.join(dirname, name)
        if os.path.isfile(path):
            visit_func(path)
        else:
            walk(path, visit_func)

# walk('photos', print)

def is_image(path,extensions):
    name, ext = os.path.splitext(path)
    if ext in extensions:
        return True
    else:
        return False


# print(is_image('photos copy/chipmunk.jpg',['.jpg','.png','.gif']))

import hashlib
def md5_digest(filename):
        data = open(filename, 'rb').read()
        md5_hash = hashlib.md5()
        md5_hash.update(data)
        digest = md5_hash.hexdigest()
        return(digest)

# print(md5_digest('photos copy/chipmunk.jpg'))

def add_path(path, shelf):
    contents = md5_digest(path)
    if contents not in shelf:
        shelf[contents] = [path]
    else:
        path_list = shelf[contents]
        path_list.append(path)
        shelf[contents] = path_list

dg = shelve.open('digest_map', 'n')

def process_path(path):
    if is_image(path,['.jpg','.jpeg','.gif']):
        add_path(path,dg)

dg = shelve.open('digest_map', 'n')
walk('photos copy', process_path)

for digest, paths in dg.items():
    if len(paths) > 1:
        print(paths)
