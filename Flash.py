from asyncio import tasks
from flask import Flask,jsonify,request
app=Flask(__name__)
list=[
    {
        'Contact':'9987644456',
        'Name': "Raju",
        'Done':False,
        'id':1
    },
    {
        'Contact':'9876543222',
        'Name': "Rahul",
        'Done':False,
        'id':2
    }
]
@app.route('/add-data',methods=["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "staus":"error",
            "Message":"Please provide the data!!"
        },400)
    contact={
        ##'id':tasks[-1]['id']+1,
        'Name':request.json['Name'],
        'Contact':request.json.get('Contact',""),
        'done':False
    }
    list.append(contact)
    return jsonify({
        "status":'success',
        "message": "Contact added successfully"
    },200)
@app.route('/get-data')
def get_task():
    return jsonify({
        "data":list
    })    
if __name__ == "__main__":
    app.run()
