from django.http import HttpResponse
import time
from channels.handler import AsgiHandler
from channels import Group
'''
reply_channel
server
headers
client
query_string
path
order
'''
# Connected to websocket.connect
def ws_add(message):
    # Accept the incoming connection
    print "==========="
    print message.content['path']
    print "==========="
    message.reply_channel.send({"accept": True})
    # Add them to the chat group
    Group("topic").add(message.reply_channel)

# Connected to websocket.receive
def ws_message(message):
    Group("topic").send({
        "text": "[user] %s" % message.content['text'],
    })

# Connected to websocket.disconnect
def ws_disconnect(message):
    Group("topic").discard(message.reply_channel)
