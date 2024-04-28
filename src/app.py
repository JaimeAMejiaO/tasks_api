from bson import ObjectId
from flask import Flask, render_template, request, jsonify, redirect, url_for
import config.mongodb as dbase
from task import Task

# Conexion a la base de datos
db = dbase.dbConnection()

# Creando la aplicación de Flask
app = Flask(__name__)

# Ruta principal
@app.route('/')
def home():
    tasks = db['tasks']
    tasks_list = tasks.find()

    return render_template('index.html', tasks=tasks_list)



# Ruta para añadir una tarea
@app.route('/add')
def view_add_task():
    # Cargando la vista para añadir una tarea
    return render_template('add.html')

@app.route('/add', methods=['POST'])
def add_task():
    # Obteniendo los datos del formulario
    title = request.form['title']
    description = request.form['description']
    done = 'done' in request.form

    # Creando una nueva tarea
    if title and description:
        task = Task(title, description, done)
        db.tasks.insert_one(task.toCollection())
        response = jsonify({
            'message': 'Tarea añadida correctamente',
            'title': title,
            'description': description,
            'done': done
        })
    
        return redirect(url_for('view_add_task'))
    else:
        return notFount()



# Ruta para eliminar tareas
@app.route('/<id>')
def delete_task(id):
    tasks = db['tasks']
    tasks.delete_one({'_id': ObjectId(id)})

    return redirect(url_for('home'))



# Ruta para actualizar tareas
@app.route('/update')
def view_update_task():
    tasks = db['tasks']
    tasks_list = tasks.find()
    # Cargando la vista para actualizar una tarea
    return render_template('update.html', tasks=tasks_list)

@app.route('/update/<id>', methods=['POST'])
def update_task(id):
    # Conexion a la base de datos
    tasks = db['tasks']

    # Obteniendo los datos del formulario
    title = request.form['title']
    description = request.form['description']
    done = 'done' in request.form

    # Creando una nueva tarea
    tasks.update_one({'_id': ObjectId(id)}, {'$set': {'title': title, 'description': description, 'done': done}})
    response = jsonify({
        'message': 'Tarea actualizada correctamente',
        'title': title,
        'description': description,
        'done': done
    })

    return redirect(url_for('view_update_task'))



# Ruta de error 404
@app.errorhandler(404)
def notFount(error=None):
    message = {
        'status': 404,
        'message': 'Not Found: ' + request.url,
    }
    response = jsonify(message)
    response.status_code = 404
    return response



# Inicializando la aplicación
if __name__ == '__main__':
    app.run(debug=True, port=5000)
