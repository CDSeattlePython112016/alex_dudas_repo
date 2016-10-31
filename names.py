users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }

for Dict, List in users.items():
    print(Dict)
    count = 1
    for person in List:
        name = person['first_name'] + ' ' + person['last_name']
        length = len(name) - 1
        print(str(count) + ' - ' + name + ' - ' + str(length))
        count += 1
