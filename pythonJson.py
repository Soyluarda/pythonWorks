person = {}
person['arda'] = {
    'name' : 'arda',
    'surname' : 'soylu',
    'email' : 'ardasoylu39@hotmail.com',
    'github' : 'soyluarda'
}
person['kayra'] = {
    'name' : 'kayra',
    'surname' : 'soylu',
    'email' : 'kayroskayros@hotmail.com',
    'github' : '-'
}

print (person)

import json
json_data = json.dumps(person)
json_load = json.loads(json_data)
print(json_data)
print (json_load)
print type(person)
print type(json_data)
