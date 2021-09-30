import sqlite3
from flask import Flask, flash, redirect, render_template, request, session, g #добавлять!!!!

app = Flask(__name__)



@app.route("/", methods=["GET", "POST"])
def index():
    con = sqlite3.connect('tracker.db')
    cur = con.cursor()
    cur.execute("SELECT task FROM tasks")
    #current_tasks = cur.fetchall()
    current_tasks = []
    for task in cur:
        current_tasks.append(task[0])
    con.close()

    #вот здесь придет запрос?? и в ответ на запрос надо добавить данные в базу???
    #тут должна происходит асинхронная фигня по клику на элемент
    

    return render_template("index.html", current_tasks=current_tasks)
    #current_tasks=" * ".join(current_tasks)

@app.route("/input", methods=["GET", "POST"]) 
def tracker():
    if request.method == "POST":
        #complete database
        con = sqlite3.connect('tracker.db')
        cur = con.cursor()
        task = request.form.get("task")
        cur.execute("INSERT INTO tasks (task) VALUES (?)", (task, ))
        con.commit()
        con.close()

        return render_template("input.html")
    else:
        return render_template("input.html")
