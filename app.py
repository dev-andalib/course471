from flask import *
import sqlite3


class Service:
    def __init__(self, ser_type, ser_name, ser_time):
        self.type = ser_type
        self.name = ser_name
        self.time = ser_time


app = Flask( __name__)


@app.route('/')
def home():
    connect_db()
    return render_template('index.html')

@app.route('/gotoservice')
def gotoser():
    return render_template('addService.html')

@app.route('/getallservice')
def getser():
    c = sqlite3.connect('service.db').cursor()
    c.execute("SELECT * FROM SERVICE")
    data = c.fetchall()
    
    





def connect_db():
    c = sqlite3.connect("service.db").cursor()
    c.execute("CREATE TABLE IF NOT EXISTS SERVICE("
              "service_type TEXT, service_name TEXT, time DATETIME)")
    c.connection.close()

@app.route('/addService', methods=['POST'])
def addService():
    db = sqlite3.connect('service.db')
    c = db.cursor()
    ser = Service(request.form['type'],
                      request.form['name'],
                      request.form['time'])
    c.execute("INSERT INTO SERVICE VALUES(?, ?, ?)", 
              (ser.type, ser.name, ser.time))
    db.commit()
    return render_template('addService.html')









if __name__ == "__main__":
    app.run(debug=True, port = 2349)