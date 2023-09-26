from flask import Flask, jsonify, request

app = Flask(__name__)
contacts = [{
            'id' : 1,
            'Name' : "Rishabh Gupta",
            'Contact' : "123456789",
            'Done' : False
        },
            {
             'id' : 2,
             'Name' : "Rishabh Guptaa",
             'Contact' : "234567891",
             'Done' : False
        }]

@app.route("/")
def hw(): 
    return "Hello World"

@app.route("/addatask", methods = ["POST"])

def add_data():
    if not request.json :
        return jsonify({
            "Status" : "Error",
            "Message" : "Please Provide The Data"
        },400) 
    contact = {
             'id' : contacts [-1]['id']+1,
             'Name' : request.json['Name'],
             'Contact' : request.json.get('Contact', ""),
             'Done' : False
    }
    contacts.append(contact)
    return jsonify({
            "Status" : "Success",
            "Message" : "Contact Is Added"
        }) 

@app.route("/showtask")

def show_task(): 
    return jsonify({
            "data": contacts
        }) 

if(__name__ == "__main__"): 
    app.run(debug = True)