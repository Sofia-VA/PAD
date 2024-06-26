def do_twice(func):
    '''Tiene return en func'''
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)  
        return func(*args, **kwargs)  # devuelve valor de la función modificada  

    return wrapper_do_twice 

