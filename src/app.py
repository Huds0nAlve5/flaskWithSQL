from flask import Flask
from src.routes.routes import *

app = Flask(__name__)
app.config.from_mapping(
    SECRET_KEY="development"
)

app.add_url_rule(routes["index"], view_func=routes["index_controller"])
app.add_url_rule(routes["cadastro_pessoa"], view_func=routes["cadastro_pessoa_controller"])
app.add_url_rule(routes["deletar_pessoa"], view_func=routes["del_pessoa_controller"])
app.add_url_rule(routes["atualizar_pessoa"], view_func=routes["updt_pessoa_controller"])
app.add_url_rule(routes["listar_pessoa"], view_func=routes["listar_pessoa_controller"])

app.add_url_rule(routes["cadastro_transacao"], view_func=routes["cadastro_transacao_controller"])
app.add_url_rule(routes["listar_transacao"], view_func=routes["listar_transacao_controller"])

app.add_url_rule(routes["listar_saldo"], view_func=routes["listar_saldo_controller"])