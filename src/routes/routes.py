from src.controllers.controller import *

routes = {
    "index":"/", "index_controller":index_controller.as_view("index"),
    "cadastro_pessoa":"/cadastro/pessoa", "cadastro_pessoa_controller":cadastro_pessoa_controller.as_view("cadastro_pessoa"),
    "deletar_pessoa":"/delete/pessoa/<int:id>", "del_pessoa_controller":del_pessoa_controller.as_view("delete_pessoa"),
    "atualizar_pessoa":"/atualizar/pessoa/<int:id>", "updt_pessoa_controller":updt_pessoa_controller.as_view("atualizar_pessoa")
}