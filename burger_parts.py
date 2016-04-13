def burger_top():
    txt = """

               _....-----------...._
            .-'  o    o    o    o   '-.
           /  o    o    o         o    \\
          /__o___o_ _ o___ _ o_ o_ _ _o_\\   """
    return txt


def burger_bottom():
    abc = '''
          ________________________________
          \~`-`.__.`-~`._.~``~.-~.__.~`-`/
           \                            /
            `._______________________.-'    '''
    return abc


def ingredients(kind, size=31):

    space = " " * 10

    if kind == 'ketchup':
        txt = space + "=" * size
    elif kind == 'burger':
        txt = space + "8" * size
    elif kind == 'cheese':
        txt = space + "~" * size
    else:
        txt = space + "^" * size


    return txt

print 'It\'s a burger'
print burger_top()
print ingredients('greens')
print ingredients('burger')
print ingredients('ketchup')
print ingredients('cheese')
print ingredients('xyz')
print burger_bottom()