from flask_restful import Resource
from api import api
from ..schemas import curso_schema
from flask import request, make_response, jsonify
from ..entidades import curso
from ..services import curso_service, formacao_service

class CursoList(Resource):
    def get(self):
        cursos = curso_service.listar_cursos()
        cs = curso_schema.CursoSchema(many=True)
        return make_response(cs.jsonify(cursos), 200)
    
    def post(self):
        cs = curso_schema.CursoSchema()
        validate = cs.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            nome = request.json.get("nome")
            descricao = request.json.get("descricao")
            data_publicacao = request.json.get("data_publicacao")
            formacao = request.json.get("formacao")
            formacao_curso = formacao_service.listar_formacao_id(formacao)
            if formacao_curso is None:
                return make_response(jsonify("Formação não foi encontrada!"), 404)
            novo_curso = curso.Curso(nome=nome, descricao=descricao, data_publicacao=data_publicacao, formacao=formacao_curso)
            resultado = curso_service.cadastrar_curso(novo_curso)
            x = cs.jsonify(resultado)
            return make_response(x, 201)

class CursoDetail(Resource):
    def get(self, id):
        curso = curso_service.listar_curso_id(id)
        if curso is None:
            return make_response(jsonify("Curso não foi encontrado"), 404)
        cs = curso_schema.CursoSchema()
        return make_response(cs.jsonify(curso), 200)

    def put(self, id):
        curos_bd = curso_service.listar_curso_id(id)
        if curos_bd is None:
            return make_response(jsonify("Curso não foi encontrado"), 404)
        cs = curso_schema.CursoSchema()
        validate = cs.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            nome = request.json.get("nome")
            descricao = request.json.get("descricao")
            data_publicacao = request.json.get("data_publicacao")
            formacao = request.json.get("formacao")
            formacao_curso = formacao_service.listar_formacao_id(formacao)
            if formacao_curso is None:
                return make_response(jsonify("Formação não foi encontrada!"), 404)
            novo_curso = curso.Curso(nome=nome, descricao=descricao, data_publicacao=data_publicacao, formacao=formacao_curso)
            curso_service.atualiza_curso(curos_bd, novo_curso)
            curso_atualizado = curso_service.listar_curso_id(id)
            return make_response(cs.jsonify(curso_atualizado), 200)

    def delete(self, id):
        curos_bd = curso_service.listar_curso_id(id)
        if curos_bd is None:
            return make_response(jsonify("Curso não foi encontrado"), 404)
        curso_service.remove_curso(curos_bd)
        return make_response(jsonify('Curso excluido com sucesso!'), 204)

api.add_resource(CursoList, '/cursos')
api.add_resource(CursoDetail, '/cursos/<int:id>')