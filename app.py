from flask import Flask, render_template
from flask_restful import Api, Resource, abort
import livedata

app = Flask(__name__)
app.config ['JSON_SORT_KEYS'] = False

api = Api(app)

@app.route("/")
def index():
    return render_template('index.html')


class All(Resource):
    def get(self):
        result = livedata.get_all() 
        if not result:
            abort(404, message="no data")
        
        return {"result": result}

class Fields(Resource):
    def get(self):
        result = livedata.get_fields()
        if not result:
            abort(404, message="no fields")
        
        return {"result": result}

class DataByField(Resource):
    def get(self,field):
        if field not in livedata.DATA:
            abort(404, message="field not found")
        
        return {"result": livedata.DATA[field]}

class Categories(Resource):
    def get(self):
        result = livedata.get_categories()
        if not result:
            abort(404, message="no categories")
        
        return {"result": result}

class DataByCategory(Resource):
    def get(self, category):
        if category not in livedata.get_categories():
            abort(404, message="category does not exist")
        
        return {"result": eval(f'livedata.get_{category}')()}
        


api.add_resource(All, "/all")
api.add_resource(Fields, "/fields")
api.add_resource(DataByField, "/field/<string:field>")
api.add_resource(Categories, "/categories")
api.add_resource(DataByCategory, "/category/<string:category>")