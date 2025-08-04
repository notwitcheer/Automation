# Using JSON files.
# Structured datas.
# using dumps and loads.

import json

people = {'name' : 'Paul', 'age' : 25, 'friends' : ['Sophie', 'Marie', 'James']}

people_json = json.dumps(people)
print('JSON: ' + people_json)

f = open('json_file.txt', 'r')
data_json = f.read()
people = json.loads(data_json)

f.close()