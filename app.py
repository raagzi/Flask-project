from flask import Flask, render_template
import cx_Oracle
import os

HOST = '0.0.0.0'
PORT = 5000
app = Flask(__name__)
DB_IP = os.getenv('DB_IP')
SID = "aTFdb"
DB_PORT = 1521
DB_USER = "dbfirst"
DB_PASSWORD = "DevOps_123#"

@app.route('/')
def test():
    dsn_tns = cx_Oracle.makedsn(DB_IP, DB_PORT, SID)
    connection = cx_Oracle.connect(DB_USER, DB_PASSWORD, dsn_tns)
    cursor = connection.cursor()
    data = ''
    for row in cursor.execute("SELECT * FROM dept"):
        print (row)
        data = data + str(row)
    cursor.close()
    connection.commit()
    connection.close()
    data = data[2:len(data)-3]
    final_result = str(data)
    return render_template('index.html', db_data=final_result)

if __name__ == '__main__':
    app.run(host=HOST,
            debug=True,
            port=PORT)
