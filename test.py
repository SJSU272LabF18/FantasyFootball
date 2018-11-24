from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = '!@)59380'
app.config['MYSQL_DATABASE_DB'] = 'footballStats'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql = MySQL(app)


@app.route('/')
def users():
    cur = mysql.connection.cursor()
    
    return str(rv)

if __name__ == '__main__':
    app.run(debug=True)
