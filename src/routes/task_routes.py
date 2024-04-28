from flask import Blueprint

from services.task import create_task_service, get_tasks_services, get_task_service, update_task_service, delete_task_service

task = Blueprint('task', __name__)

@task.route('/', methods=['GET'])
def get_tasks():
    return get_tasks_services()

@task.route('/<id>', methods=['GET'])
def get_task(id):
    return get_task_service(id)

@task.route('/', methods=['POST'])
def create_task():
    return create_task_service()

@task.route('/<id>', methods=['PUT'])
def update_task(id):
    return update_task_service(id)

@task.route('/<id>', methods=['DELETE'])
def delete_task(id):
    return delete_task_service(id)