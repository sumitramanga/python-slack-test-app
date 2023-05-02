# python-slack-test-app 🤖
This app consists of two Python files: main.py and slash_command_handler.py. The main.py file retrieves messages from a Slack channel, while the slash_command_handler.py file listens for incoming Slash commands and responds accordingly.

## Setup
To use this app, you'll need to set up a few things first.

### Slack API Setup
1. Go to the Slack API website and click "Create a Slack App".
2. Give your app a name and select a workspace to develop it in.
3. Under the "Add features and functionality" section, select "Slash Commands" and click "Create New Command".
4. Enter a command name (e.g. "/your-slash-command") and a short description.
5. In the "Request URL" field, enter the URL where your slash_command_handler.py file will be running (e.g. http://localhost:5001/your-slash-command).
6. Save your command and note the "Token" value. You'll need this in the next step.

### Environment Variables
You'll need to set two environment variables for this app to work properly:

SLACK_API_KEY: This should be set to the Bot User OAuth Access Token for your Slack app. You can find this value on the "OAuth & Permissions" page of your app's settings.
SLACK_CHANNEL_ID: This should be set to the ID of the Slack channel that you want to retrieve messages from. You can find this value by right-clicking on the channel in Slack and selecting "Copy Link". The ID will be the string of characters after the last forward slash (/).

### Dependencies
Make sure you have the required dependencies installed. You can do this by running the following command in your terminal:

```
pip install slack-sdk flask
```

## Running the App
Once you've completed the setup steps, you can run the app by running the following commands in separate terminal windows:

```
python main.py
```

and 

```
python slash_command_handler.py
```

The main.py script will start retrieving messages from the Slack channel and storing them in memory. The slash_command_handler.py script will start a Flask server that listens for incoming Slash commands.

You can now go to Slack and type /your-slash-command (or whatever you named your command) to see the app in action. The app should respond with a greeting and the text of your command.

You will also need to get ngrok running for the URL.


## Further Improvements
This app is just a starting point, and there are many ways you could improve it. Here are a few ideas:

Store the retrieved messages in a database (e.g. PostgreSQL) instead of memory.
Implement a more complex response to the Slash command (e.g. interacting with an external API).
Add error handling to the Flask server.
Implement a user interface for the app (e.g. a web page where users can view the retrieved messages).