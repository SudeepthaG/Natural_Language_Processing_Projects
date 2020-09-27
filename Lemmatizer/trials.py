e = {
    'emp1': {
        'name': 'Lisa',
        'age': '29',
        'Designation':'Programmer'
            },
         'emp2': {
             'name': 'Steve',
             'age': '25',
             'Designation':'HR'
                 },
         'emp3': {
             'name': 'Steve',
             'age': '25',
             'Designation':'HR'
                 }

             }

e['emp1'][
        'name2']= 'Lisa'
print(e)

e['emp1'][      'name2']= 'Lissa'

print(e)
#
# for x in e:
#     print(x)
#
# for x in e:
#     for y in e:
#         print("x:"+x)
#         print("y:"+y)
#         if e[x]== e[y] and x!=y:
#             print(x)
#             print(y)



a=[1,2,3,4,1,2,2]
b=[1,2,3,4,1,3,3]
d={}

#
# for i in range(len(a)):
#     if a[i] in d.keys():
#         print(d[a[i]])
#         # if b[i] in a[i]:
#         #     print("sdffdg")
#         # else:
#         d[a[i]]=d[a[i]]+[{b[i]:1},]
#     else:
#         d[a[i]]=[{b[i]:1},]
#
# print(d)
# print(d.keys())
# if 1 in d.keys():
#     print("esff")

for i in range(len(a)):
    count=0
    if a[i] in d.keys():
        print(d[a[i]])
        print("gfds")
        if b[i] in d[a[i]]:
            print("nest")
            count=d[a[i]][b[i]]+1
            d[a[i]][b[i]] = count
        else:
            print(d)
            d[a[i]][b[i]]=1
            print(d)
    else:
        print(a[i])
        print(b[i])
        d[a[i]]={b[i]:1}

print(d)
print(d.keys())
if 1 in d.keys():
    print("esff")


# print(len(d[2].keys())

e2={'emp': {'name': 'Lisas', 'age': '29', 'Designation': 'Programmer', 'name2': 'Lissa'}, 'emp2': {'name': 'Steve', 'age': '25', 'Designation': 'HR'}, 'emp3': {'name': 'Steve', 'age': '25', 'Designation': 'HR'}}

if e==e2:
    print("yes")

e3={'ef':1}

print(e3.keys())

for x in e3.keys():
    print(x)


