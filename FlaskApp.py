from flask import Flask , request , jsonify

app = Flask(__name__)

contacts = [
    {
        'id':1,
        'name':u'Raju',
        'phone no':u'9987644456',
        'done':False
    },
    {
        'id':2,
        'name':u'Rahul',
        'phone no':u'9876543222',
        'done':False
    }
]

@app.route('/add-data',methods = ['POST'])

def add_contact():
    if not request.json:
        return jsonify({
            'status':'error',
            'message':'please provide the data'
        },400)
    
    contact  = {
        'id':contacts[-1]['id']+1,
        'name':request.json['name'],
        'phone no':request.json.get('phone no',''),
        'done':False
    }

    contacts.append(contact)
    return jsonify({
        'status':'success',
        'message':'task added successfully'
    })

@app.route('/get-data')

def get_task():
    return jsonify({
        'data':contacts
    })

if (__name__=='__main__'):
    app.run(debug=True)