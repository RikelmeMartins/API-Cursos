from flask_restful import Resource
from api import api
from ..schemas import professor_schema
from flask import request, make_response, jsonify
from ..entidades import professor
from ..services import professor_service

class ProfessorList(Resource):
    def get(self):
        professores = professor_service.listar_professores()
        pr = professor_schema.ProfessorSchema(many=True)
        return make_response(pr.jsonify(professores), 200)
    
    def post(self):
        pr = professor_schema.ProfessorSchema()
        validate = pr.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            nome = request.json.get("nome")
            idade = request.json.get("idade")

            novo_professor = professor.Professor(nome=nome, idade=idade)
            resultado = professor_service.cadastrar_professor(novo_professor)
            x = pr.jsonify(resultado)
            return make_response(x, 201)

class ProfessorDetail(Resource):
    def get(self, id):
        professor = professor_service.listar_professor_id(id)
        if professor is None:
            return make_response(jsonify("Professor não foi encontrado"), 404)
        pr = professor_schema.ProfessorSchema()
        return make_response(pr.jsonify(professor), 200)

    def put(self, id):
        professor_bd = professor_service.listar_professor_id(id)
        if professor_bd is None:
            return make_response(jsonify("Professor não foi encontrado"), 404)
        pr = professor_schema.ProfessorSchema()
        validate = pr.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            nome = request.json.get("nome")
            idade = request.json.get("idade")
            novo_professor = professor.Professor(nome=nome, idade=idade)
            professor_service.atualiza_professor(professor_bd, novo_professor)
            professor_atualizado = professor_service.listar_professor_id(id)
            return make_response(pr.jsonify(professor_atualizado), 200)

    def delete(self, id):
        professor_bd = professor_service.listar_professor_id(id)
        if professor_bd is None:
            return make_response(jsonify("Professor não foi encontrado"), 404)
        professor_service.remove_professor(professor_bd)
        return make_response(jsonify('Professor excluido com sucesso!'), 204)

api.add_resource(ProfessorList, '/professores')
api.add_resource(ProfessorDetail, '/professores/<int:id>')