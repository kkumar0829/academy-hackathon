import os

from flask import Flask
from flask import request

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    
    def todo_view(todos):
        the_view = 'list of todos are: ' + '<br/>'
        for todo in todos:
            the_view +=(todo + '<br/>')

        the_view += '---------list ends------------'
        return the_view

    @app.route('/todos')
    def todos():
        name = request.args.get('name')
        print('---------------')
        print(name)
        print('------------')

        if name == 'kishan':
            my_todos = ['ki1','ki2']
        elif name == 'raj':
            my_todos = ['kishan','hiurfgi']
        else:
            my_todos = []

        return todo_view(my_todos)

    # a simple page that list my todos 
    return app

