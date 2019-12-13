from flask import Flask, request
from models import Schema
from service import ToDoService
import sqlite3 as db
app = Flask(__name__)

@app.route("/todo", methods=["GET","POST", "PUT", "DELETE"])
def create_todo():
    if request.method == 'POST':
        return ToDoService().create(request.get_json())
    elif request.method == 'GET':
        return ToDoService().select(request.get_json())
    elif request.method == 'PUT':
        return ToDoService().update(request.get_json())
    elif request.method == 'DELETE':
        return ToDoService().delete(request.get_json())

# def update_todo():
#     return ToDoService().update(request.get_json())

# def select_todo():
#     return ToDoService().select(request.get_json())

# def delete_todo():
#     return ToDoService().delete(request.get_json())

if __name__ == "__main__":
    Schema()
    app.run(debug=True)
