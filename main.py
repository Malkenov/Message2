from flask import Flask,request
from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://asanalimalkenov22:asanali22@cluster0.bo8uuy6.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

collection = cluster.one_database.one_collection



messages = [{
        "_id": "_id",
        "name": "A",
        "text": "Hi",
    }]

collection.insert_many(messages)

app = Flask(__name__)
@app.route("/api/messages/", methods = ["GET"])
def get():
    return messages

@app.route("/api/message/", methods = ["POST"])
def post():
    data = {
        "_id": request.json["_id"],
        "name": request.json["name"],
        "text": request.json["text"],
        }
    messages.append(data)
    return "сообщение добавлена"

if __name__ == '__main__':
    app.run()
