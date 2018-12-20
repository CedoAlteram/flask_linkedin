#!flask/bin/python
from flask import Flask, jsonify
from flask import abort

app = Flask(__name__)

#TODO
# write method for making the python request to the LinkedIn API and returns JSON.
# Build out memory structure add them as 'tasks'
# integrate python3-linkedin to build authorization tokens

tasks = [

]


@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    # simple test to see if functionality of API is returning values.
    #TODO
    # replace with simple for loop pulling all image urls
    # insert method here, initiate upon calling task
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    return jsonify({'task': task[0]})


if __name__ == '__main__':
    app.run(debug=True)
