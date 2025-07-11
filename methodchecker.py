def find_defining_class(obj, meth_name):
    for typ in type(obj).mro():
        if meth_name in vars(typ):
            return typ
    return None