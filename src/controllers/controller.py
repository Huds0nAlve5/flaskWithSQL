from flask.views import MethodView
from flask import request, render_template, redirect, flash
from src.db import mysql

class index_controller(MethodView):
    def get(self):
        return render_template("public/index.html")

class cadastro_pessoa_controller(MethodView):
    def get(self):
        with mysql.cursor() as cur:
            cur.execute("SELECT * FROM PESSOA")
            pessoas = cur.fetchall()
        return render_template("public/cadastro_pessoa.html", pessoas=pessoas)

    def post(self):
        name = request.form['name']
        age = request.form['age']

        with mysql.cursor() as cur:
            try:
                cur.execute("INSERT INTO pessoa VALUES (null, %s, %s)", (name, age))
                cur.connection.commit()
                flash('Pessoa cadastrada com sucesso!', 'success')
            except:
                flash('Erro ao cadastrar esta pessoa', 'error')
            return redirect('/')

class del_pessoa_controller(MethodView):
    def post(self, id):
        with mysql.cursor() as cur:
            cur.execute("DELETE FROM PESSOA WHERE ID = %s", (id))
            cur.connection.commit()
            return redirect("/")
        
class updt_pessoa_controller(MethodView):
    def get(self, id):
        with mysql.cursor() as cur:
            cur.execute("SELECT * FROM PESSOA WHERE ID = %s", (id))
            pessoa = cur.fetchone()
            return render_template("public/update.html", pessoa=pessoa)

    def post(self, id):
        name = request.form['name']
        age = request.form['age']

        with mysql.cursor() as cur:
            cur.execute("UPDATE PESSOA SET name = %s, age = %s WHERE id = %s", (name, age, id))
            cur.connection.commit()
            return redirect('/')