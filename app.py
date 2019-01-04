from flask import Flask , render_template, jsonify
from flask_bootstrap import Bootstrap
from flaskext.mysql import MySQL

app = Flask(__name__)

Bootstrap(app)
mysql = MySQL()

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'invitadodb'
app.config['MYSQL_DATABASE_PASSWORD'] = '1nvitad0'
app.config['MYSQL_DATABASE_DB'] = 'sacdb'
app.config['MYSQL_DATABASE_HOST'] = '10.15.4.6'
mysql.init_app(app)

@app.route('/')
def reporte():
    cursor = mysql.connect().cursor()
    cursor.execute("SELECT count(folioPeticion) as cantidad, DATE(fechaPeticion) as fecha FROM peticion WHERE DATE(fechaPeticion) > '2019-01-01' GROUP BY DATE(fechaPeticion)")
    data = cursor.fetchall()

    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)

