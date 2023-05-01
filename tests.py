import unittest
import os
import cx_Oracle
from app import app

class AppTests(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        app.config['DB_IP'] = os.getenv('DB_IP')
        app.config['SID'] = 'aTFdb'
        app.config['DB_PORT'] = 1521
        app.config['DB_USER'] = 'dbfirst'
        app.config['DB_PASSWORD'] = 'DevOps_123#'
        self.app = app.test_client()

    def test_index(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'<h1>Department Data</h1>', response.data)

    def test_invalid_endpoint(self):
        response = self.app.get('/invalid')
        self.assertEqual(response.status_code, 404)

    def test_database_connection(self):
        with app.app_context():
            db_ip = app.config['DB_IP']
            sid = app.config['SID']
            db_port = app.config['DB_PORT']
            db_user = app.config['DB_USER']
            db_password = app.config['DB_PASSWORD']
            dsn_tns = cx_Oracle.makedsn(db_ip, db_port, sid)
            connection = cx_Oracle.connect(db_user, db_password, dsn_tns)
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM dept")
            data = cursor.fetchall()
            cursor.close()
            connection.commit()
            connection.close()
            self.assertGreater(len(data), 0)

if __name__ == '__main__':
    unittest.main()
