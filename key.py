# def person(name, age, **kw):
#     if 'city' in kw:
#         pass
#     if 'job' in kw:
#         pass
#     print('name:', name, 'age:', age, 'other', kw)

# def person(name, age, *, city, job):
#     print(name, age, city, job)

# def person(name, age, *args, city, job):
#     print(name, age, args, city, job)

def person(name, age, *, city='Berjing', job):
    print(name, age, city, job)