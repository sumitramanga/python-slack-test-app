# slash_command_handler.py

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/jarvis', methods=['POST'])
def handle_slash_command():
    # Parse the command input from the request
    user_id = request.form.get('user_id')
    user_name = request.form.get('user_name')
    command = request.form.get('command')
    text = request.form.get('text')

    print(f"Received command from {user_name} (ID: {user_id}): {command} {text}")

    # Respond to the command
    # response_text = f"Hello, {user_name}! You entered: {command} {text}"

    # Check if the user asked for help
    if text == 'help' or text == '--help':
        help_message = "Hi there! To use the `/jarvis` command, simply type the command followed by any text you want to include. For example:\n\n/jarvis hello world\n\nThis will send a message to the channel with the text 'Hello world'."
        return jsonify({"response_type": "ephemeral", "text": help_message})

    # Check if the user asked for help
    if len(text) == 0:
        no_message = "Need help? Try `/jarvis help`"
        return jsonify({"response_type": "ephemeral", "text": no_message})

    # Do a serach of text and return it's results
    

    # Logic here to return what was typed within the command 

    return jsonify({"response_type": "in_channel", "text": response_text})

if __name__ == "__main__":
    app.run(port=5003, debug=True)
