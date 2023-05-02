# slash_command_handler.py

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/your-slash-command', methods=['POST'])
def handle_slash_command():
    # Parse the command input from the request
    user_id = request.form.get('user_id')
    user_name = request.form.get('user_name')
    command = request.form.get('command')
    text = request.form.get('text')

    print(f"Received command from {user_name} (ID: {user_id}): {command} {text}")

    # Respond to the command
    response_text = f"Hello, {user_name}! You entered: {command} {text}"
    return jsonify({"response_type": "in_channel", "text": response_text})

if __name__ == "__main__":
    app.run(port=5001)
