from typing import Optional
from flask import Flask, request, jsonify
from flask_pydantic_spec import FlaskPydanticSpec, Response, Request
from pydantic import BaseModel
from tinydb import TinyDB, Query

server = Flask(__name__)
spec = FlaskPydanticSpec("flask", title="Python API")
spec.register(server)
database = TinyDB('database.json')


class People(BaseModel):
    id: Optional[int]
    name: str
    gender: str
    address: str
    phone: str


class PeopleList(BaseModel):
    people_list: list[People]
    count: int


@server.get('/people')
@spec.validate(resp=Response(HTTP_200=PeopleList))
# @spec.validate(resp=Response(HTTP_200=People))
def get_people():
    return jsonify(
        PeopleList(
            people_list=database.all(),
            count=len(database.all())
        ).dict()
    )


@server.post('/people')
@spec.validate(body=Request(People), resp=Response(HTTP_200=People))
def create_new_person():
    body = request.context.body.dict()
    database.insert(body)
    return body


@server.put('/people/<int:id>')
@spec.validate(
    body=Request(People), resp=Response(HTTP_200=People)
)
def edit_people(id):
    People = Query()
    body = request.context.body.dict()
    database.update(body, People.id == id)
    return jsonify(body)


server.run()
