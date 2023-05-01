This project is a flask api built with Python, Flask and Oracle Database to be used as a starter template.

Built With:

Python 3,Flask, Docker, Oracle Database 18c

Prerequisites:

You will need the following things properly installed on your computer:
Git, Docker

Installation:

run `git clone https://github.com/KartikShrikantHegde/python-oracle.git`

Running:

To run the project locally follow the following steps:
change into the project directory
`docker build -t python/oracledb18 .`
`docker run -p 5000:5000 python/oracledb18`

JSON API:

The JSON API has sample endpoints to start development
Must configure `app.py` to connect to your Oracle DB and update the SQL query
`http://localhost:5000/`
(returns data from Oracle DB connection)
