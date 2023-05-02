# main.py

import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

# List to store messages
messages = []

# Function to index the document content
def index_message(message):
    messages.append(message)

# Authenticate with the Slack API
client = WebClient("SLACK_API_KEY", timeout=10)

# ID of the channel you're interested in
channel_id = "C055UUKK6F6"

# Get the messages from the channel
try:
    has_more = True
    cursor = None
    while has_more:
        response = client.conversations_history(channel=channel_id, cursor=cursor)
        fetched_messages = response['messages']
        for message in fetched_messages:
            index_message(message)
        cursor = response.get('response_metadata', {}).get('next_cursor', None)
        has_more = bool(cursor)
except SlackApiError as e:
    print("Error retrieving messages for channel {}: {}".format(channel_id, e))

# Print the messages
for message in messages:
    print(message['text'])