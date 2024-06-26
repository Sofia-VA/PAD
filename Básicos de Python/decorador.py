def do_twice(func):
    '''Tiene return en func'''
    def wrapper_do_twice():
        func()
        func()
    return wrapper_do_twice()  # devuelve valor de la función modificada

