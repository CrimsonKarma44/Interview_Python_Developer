from flask import Flask, render_template, url_for
from flask_mysqldb import MySQL
import hashlib

app = Flask(__name__)

app.secret_key = hashlib.sha1('password'.encode('utf-8')).hexdigest().upper()

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'pass'
app.config['MYSQL_DB'] = 'bincomphptest'

mysql = MySQL(app)


@app.route('/polling-result')
def polling_result():
    cur = mysql.connection.cursor() 
    cur.execute("SELECT polling_unit.polling_unit_name, party_abbreviation, party_score FROM announced_pu_results INNER JOIN polling_unit ON announced_pu_results.polling_unit_uniqueid=polling_unit.uniqueid;")
    fetch = cur.fetchall()
    cur.close()
    de = {}
    for i in fetch:
        if i[0] not in de.keys():
            de[i[0]] = [f'{i[1]}: {i[2]}']
        else:
            de[i[0]] += [f'{i[1]}: {i[2]}']

    return render_template('polling_result.html', data=de)

@app.route('/summed-lga-result')
def lga_result():
    cur = mysql.connection.cursor() 
    cur.execute('SELECT lga_name FROM lga;')
    lga_names = cur.fetchall()

    cur.execute('SELECT DISTINCT party_abbreviation FROM announced_pu_results;')
    party_names = cur.fetchall()
    for i in party_names:
        pass

    cur.close()
    return render_template('lga_result.html',data2=party_names, data1=lga_names)

# I saw the email late hence my inability to finish


# @app.route('/')
# def polling_result():
#     pass


if __name__ == '__main__':
    app.run(debug=True)
