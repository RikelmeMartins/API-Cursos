from flask_restful import Resource
from api import api
from ..schemas import formacao_schema
from flask import request, make_response, jsonify
from ..entidades import formacao
from ..services import formacao_service

class FormacaoList(Resource):
    def get(self):
        formacoes = formacao_service.listar_formacoes()
        fr = formacao_schema.FormacaoSchema(many=True)
        return make_response(fr.jsonify(formacoes), 200)
    
    def post(self):
        fr = formacao_schema.FormacaoSchema()
        validate = fr.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            nome = request.json.get("nome")
            descricao = request.json.get("descricao")

            nova_formacao = formacao.Formacao(nome=nome, descricao=descricao)
            resultado = formacao_service.cadastrar_formacao(nova_formacao)
            x = fr.jsonify(resultado)
            return make_response(x, 201)

class FormacaoDetail(Resource):
    def get(self, id):
        formacao = formacao_service.listar_formacao_id(id)
        if formacao is None:
            return make_response(jsonify("Formação não foi encontrado"), 404)
        fr = formacao_schema.FormacaoSchema()
        return make_response(fr.jsonify(formacao), 200)

    def put(self, id):
        formacao_bd = formacao_service.listar_formacao_id(id)
        if formacao_bd is None:
            return make_response(jsonify("Formação não foi encontrado"), 404)
        fr = formacao_schema.FormacaoSchema()
        validate = fr.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            nome = request.json.get("nome")
            descricao = request.json.get("descricao")
            nova_formacao = formacao.Formacao(nome=nome, descricao=descricao)
            formacao_service.atualiza_formacao(formacao_bd, nova_formacao)
            formacao_atualizado = formacao_service.listar_formacao_id(id)
            return make_response(fr.jsonify(formacao_atualizado), 200)

    def delete(self, id):
        formacao_bd = formacao_service.listar_formacao_id(id)
        if formacao_bd is None:
            return make_response(jsonify("Formação não foi encontrado"), 404)
        formacao_service.remove_formacao(formacao_bd)
        return make_response(jsonify('Formação excluido com sucesso!'), 204)

api.add_resource(FormacaoList, '/formacao')
api.add_resource(FormacaoDetail, '/formacao/<int:id>')