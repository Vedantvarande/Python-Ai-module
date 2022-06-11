from flask import Flask,jsonify,request

app= Flask(__name__)

tasks = [
    {
        'id': 1,
        'Name': u'Buy groceries',
        'Contact': u'Milk, Cheese, Pizza, Fruit, Tylenol',
        'done': False
    },
    {
        'id': 2,
        'Name': u'Learn Python',
        'Contact': u'Need to find a good Python tutorial on the web',
        'done': False
    }
]

@app.route("/add-data", methods=["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status": "error",
            "message": "Please provide the data"
        }, 400)

    contact = {
        'id': tasks[-1]['id'] + 1,
        'Name': request.json['Name'],
        'Contact': request.json.get('Contact', ""),
        'done': False
    }
    tasks.append(contact)
    return jsonify({
        "status": "success",
        "message": "Task added succesfully!"
    })


@app.route("/get-data")
def get_task():
    return jsonify({
        "data": tasks
    })


if (__name__ == "__main__"):
    app.run()

