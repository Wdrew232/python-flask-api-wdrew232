from flask import Flask, jsonify  # Ensure jsonify is imported
from flask import request
app = Flask(__name__)

# Correct the todos list with a comma between items
todos = [
    {"label": "my first task", "done": False},
    {"label": "my second task", "done": False}
    
]

@app.route('/todos', methods=['GET'])  # Keep only the necessary route
def get_todos():
    json_text = jsonify(todos)  # Convert the todos list to JSON
    return json_text  # Return the JSON response

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    todos.append(request_body)  
    return jsonify(todos)

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print("This is the position to delete:", position)
    if 0 <= position < len(todos):  
        del todos[position]  
    return jsonify(todos)

if __name__ == "__main__":
    app.run(debug=True)  # This will run the Flask app