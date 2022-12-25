from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'This is the cult of snap!'

@app.route("/webhooks", methods=['GET'])
def fbverify():
    if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
        if not request.args.get("hub.verify_token")== "qweyt2232212":
            return "Verification token missmatch", 403
        return request.args['hub.challenge'], 200
    return "Hello world", 200