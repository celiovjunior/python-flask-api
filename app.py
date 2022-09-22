from flask import Flask, request, jsonify
from flask_pydantic_spec import FlaskPydanticSpec, Response, Request
from pydantic import BaseModel
from tinydb import TinyDB

server = Flask(__name__)
spec = FlaskPydanticSpec("flask", title="Python API")
spec.register(server)
database = TinyDB('database.json')


class People(BaseModel):
    id: int
    name: str
    gender: str
    address: str
    phone: str


@server.get('/people')
# @spec.validate(resp=Response(HTTP_200=People))
def get_people():
    return jsonify(database.all())


@server.post('/people')
@spec.validate(body=Request(People), resp=Response(HTTP_200=People))
def create_new_person():
    body = request.context.body.dict()
    database.insert(body)
    return body


server.run()
