import sqlite3

from flask import Flask, request, render_template

app = Flask(__name__)



@app.route("/", methods = ['GET', 'POST'])
def index():
    conn = sqlite3.connect('finances.db')
    cursor = conn.cursor()

    if request.method == 'POST':
        insert_into()

    cursor.execute("SELECT * FROM finances")
    rows = cursor.fetchall()





    conn.close()
    return render_template("index.html", expenses = rows)



def create_table():
    conn = sqlite3.connect('finances.db')
    cursor = conn.cursor()

    table_creation_query =  """
                           CREATE TABLE IF NOT EXISTS finances
                           (
                               ID INTEGER PRIMARY KEY AUTOINCREMENT,
                               NAME TEXT NOT NULL,
                               AMOUNT INTEGER NOT NULL,
                               CATEGORY TEXT NOT NULL,
                               DATE TEXT NOT NULL
                           ); """



    cursor.execute(table_creation_query)

    # cursor.execute("INSERT INTO finances (NAME, AMOUNT, CATEGORY, DATE) VALUES (?,?,?,?)", ("CASEY", 500, "Rent", 2026))

    conn.commit()
    conn.close()


def insert_into():
    conn = sqlite3.connect('finances.db')
    cursor = conn.cursor()

    name = request.form['name']
    amount = request.form['amount']
    category = request.form['category']
    date = request.form['date']

    cursor.execute("INSERT INTO finances (NAME, AMOUNT, CATEGORY, DATE) VALUES (?,?,?,?)",
                   (name, amount, category, date))
    conn.commit()



if __name__ == '__main__':
    create_table()
    app.run(debug=True)
