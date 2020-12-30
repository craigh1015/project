from flask import Flask, jsonify, request, redirect
from flask.helpers import make_response

app = Flask(__name__)
list_of_tasks = {}

@app.route('/')
@app.route('/index.html')
def home():
    return redirect('static/index.html')

@app.route('/tasks', methods = ['POST', 'GET'])
def tasks():
    if request.method == 'POST':
        task = request.get_json()
        task["id"] = len(list_of_tasks)
        list_of_tasks[task["id"]] = task
        return jsonify(task)
    else:
        response = jsonify(list(list_of_tasks.values()))
        return response

@app.route('/tasks/<int:taskId>', methods = ['PUT', 'GET', 'DELETE'])
def tasksById(taskId):
    if request.method == 'PUT':
        task = request.get_json()
        list_of_tasks[taskId] = task
        return make_response("OK")
    elif request.method == 'DELETE':
        task = list_of_tasks.pop(taskId)
        return jsonify(task)
    else:
        response = jsonify(list_of_tasks[taskId])
        response.mimetype = 'application/json'
        return response
