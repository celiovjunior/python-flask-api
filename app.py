from flask import Flask, request
from flask_pydantic_spec import FlaskPydanticSpec, Response, Request
from pydantic import BaseModel

server = Flask(__name__)
spec = FlaskPydanticSpec("flask", title="Python API")
spec.register(server)


class People(BaseModel):
    id: int
    name: str
    gender: str
    address: str
    phone: str


@server.get('/people')
# @spec.validate(resp=Response(HTTP_200=People))
def get_people():
    return 'listando todos os usuários'


@server.post('/people')
@spec.validate(body=Request(People), resp=Response(HTTP_200=People))
def create_new_person():
    body = request.context.body.dict()
    return body


server.run()
