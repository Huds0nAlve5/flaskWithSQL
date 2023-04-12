from flask.views import MethodView
from flask import request, render_template, redirect, flash
from src.db import mysql

class index_controller(MethodView):
    def get(self):
        return render_template("public/index.html")

class cadastro_pessoa_controller(MethodView):
    def get(self):
        return render_template("public/cadastro_pessoa.html")

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
            return redirect('/listagem/pessoas')
        
class listar_pessoa_controller(MethodView):
    def get(self):
        with mysql.cursor() as cur:
            cur.execute("SELECT * FROM PESSOA")
            pessoas = cur.fetchall()
        return render_template("public/listagem_pessoa.html", pessoas=pessoas)

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
        
class cadastro_transacao_controller(MethodView):
    def get(self):
        with mysql.cursor() as cur:
            cur.execute("SELECT * FROM transacao")
            
            transacoes = cur.fetchall()
        with mysql.cursor() as cur:
            cur.execute("SELECT * FROM pessoa")
            pessoas = cur.fetchall()

        with mysql.cursor() as cur:
            cur.execute("SELECT * FROM tipo")
            tipos = cur.fetchall()

        return render_template("public/cadastro_transacao.html", transacoes=transacoes, pessoas=pessoas, tipos=tipos)

    def post(self):
        descricao = request.form['descricao']
        value = request.form['value']
        id_pessoa = request.form['id_pessoa']
        id_type = request.form['id_type']

        with mysql.cursor() as cur:
            try:
                cur.execute("INSERT INTO transacao VALUES (null, %s, %s, %s, %s)", (descricao, value, id_pessoa, id_type))
                cur.connection.commit()
                flash('Transacao cadastrada com sucesso!', 'success')
            except:
                flash('Erro ao cadastrar esta Transacao', 'error')
            return redirect('/listagem/transacoes')
        
class listar_transacao_controller(MethodView):
    def get(self):
        with mysql.cursor() as cur:
            cur.execute("SELECT * FROM transacao")
            transacoes = cur.fetchall()
        with mysql.cursor() as cur:
            cur.execute("SELECT * FROM pessoa")
            pessoas = cur.fetchall()
        with mysql.cursor() as cur:
            cur.execute("SELECT * FROM tipo")
            tipos = cur.fetchall()
        return render_template("public/listagem_transacao.html", transacoes=transacoes, pessoas=pessoas, tipos=tipos)
    
class listar_saldo_controller(MethodView):
    def get(self):
        with mysql.cursor() as cur:
            cur.execute("SELECT name, CAST(sum(value) AS DECIMAL(16,2)) FROM pessoa inner join transacao on pessoa.id = transacao.id_pessoa where transacao.id_type = 1 group by transacao.id_pessoa order by pessoa.id;")
            pessoas_receita = cur.fetchall()
        with mysql.cursor() as cur:
            cur.execute("SELECT sum(value) FROM transacao where id_type=1 GROUP by id_pessoa;")
            receitas = cur.fetchall()
        with mysql.cursor() as cur:
            cur.execute("SELECT name, CAST(sum(value) AS DECIMAL(16,2)) FROM pessoa inner join transacao on pessoa.id = transacao.id_pessoa where transacao.id_type = 2 group by transacao.id_pessoa order by pessoa.id;")
            pessoas_despesa = cur.fetchall()
        with mysql.cursor() as cur:
            cur.execute("SELECT sum(value) FROM transacao where id_type=2 GROUP by id_pessoa;")
            despesas = cur.fetchall()
        return render_template("public/listagem_saldo.html", pessoas_receita=pessoas_receita, receitas=receitas, despesas=despesas, pessoas_despesa=pessoas_despesa)