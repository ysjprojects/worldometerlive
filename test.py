import requests
BASE = "http://worldometerlive.kekapi.com/"

response = requests.get(BASE + 'all')
print(response.json())
response = requests.get(BASE + 'fields')
print(response.json())
response = requests.get(BASE + 'categories')
print(response.json())
'''
api.add_resource(All, "/all")
api.add_resource(Fields, "/fields")
api.add_resource(DataByField, "/field/<string:field>")
api.add_resource(Categories, "/categories")
api.add_resource(DataByCategory, "/category/<string:category>")
'''