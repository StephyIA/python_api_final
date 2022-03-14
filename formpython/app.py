from flask import Flask,render_template,request, url_for

from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'apiplante'

mysql = MySQL(app)

@app.route('/',methods = ['GET','POST'])
def register():
    if request.method == "POST":
        keys = ["NameUse","FirstName","email"]
        data = [x for x in request.form.values()]
        d= {i: j for i, j in zip(keys, data)}
        Nom_client=d["NameUse"]
        prenom_client=d["FirstName"]
        email_client=d["email"]

        print(Nom_client,prenom_client,email_client)

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO client(Nom_client,prenom_client,email_client) VALUES(%s, %s,%s)", (Nom_client,prenom_client,email_client ))
        mysql.connection.commit()
        cur.close()
        return "success"

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True ,port=7000)
