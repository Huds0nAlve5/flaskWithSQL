from src.controllers.controller import *

routes = {
    "index":"/", "index_controller":index_controller.as_view("index"),
    "cadastro_pessoa":"/cadastro/pessoa", "cadastro_pessoa_controller":cadastro_pessoa_controller.as_view("cadastro_pessoa"),
    "deletar_pessoa":"/delete/pessoa/<int:id>", "del_pessoa_controller":del_pessoa_controller.as_view("delete_pessoa"),
    "atualizar_pessoa":"/atualizar/pessoa/<int:id>", "updt_pessoa_controller":updt_pessoa_controller.as_view("atualizar_pessoa"),
    "cadastro_transacao":"/cadastro/transacao", "cadastro_transacao_controller":cadastro_transacao_controller.as_view("cadastro_transacao"),
    "listar_pessoa":"/listagem/pessoas", "listar_pessoa_controller":listar_pessoa_controller.as_view("listar_pessoa"),
    "listar_transacao":"/listagem/transacoes", "listar_transacao_controller":listar_transacao_controller.as_view("listar_transacao"),
    "listar_saldo":"/listagem/saldo", "listar_saldo_controller":listar_saldo_controller.as_view("listar_saldo"),
}