from flask import request, Response
from bson import json_util, ObjectId

from config.mongodb import mongo

def create_task_service():
    data = request.get_json()
    if isinstance(data, list):
        results = []
        for task in data:
            title = task.get('title', None)
            description = task.get('description', None)
            if title:
                response = mongo.db.tasks.insert_one({
                    'title': title,
                    'description': description,
                    'done': False
                })
                result = {
                    'id': str(response.inserted_id),
                    'title': title,
                    'description': description,
                    'done': False
                }
                results.append(result)
            else:
                return 'Hace falta el titulo en uno de los objetos', 400
        return results
    else:
        return 'Se esperaba una lista de objetos', 400
    

def get_tasks_services():
    data = mongo.db.tasks.find()
    result = json_util.dumps(data)
    return Response(result, mimetype='application/json')

def get_task_service(id):
    data = mongo.db.tasks.find_one({'_id': ObjectId(id)})
    result = json_util.dumps(data)
    return Response(result, mimetype='application/json')

def update_task_service(id):
    data = request.get_json()
    if len(data) == 0:
        return 'No hay tareas para actualizar', 400

    response = mongo.db.tasks.update_one({'_id': ObjectId(id)}, {'$set': data})

    if response.modified_count >= 1:
        return 'Tarea actualizada', 200
    else:
        return 'Tarea no encontrada', 404
    
def delete_task_service(id):
    response = mongo.db.tasks.delete_one({'_id': ObjectId(id)})
    if response.deleted_count >= 1:
        return 'Tarea eliminada', 200
    else:
        return 'Tarea no encontrada', 404