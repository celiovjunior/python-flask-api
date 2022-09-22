from itertools import count
from typing import Optional
from flask import Flask, request, jsonify
from flask_pydantic_spec import FlaskPydanticSpec, Response, Request
from pydantic import BaseModel, Field
from tinydb import TinyDB, Query

server = Flask(__name__)
spec = FlaskPydanticSpec("flask", title="Python API")
spec.register(server)
database = TinyDB('database.json')
c = count()


class People(BaseModel):
    id: Optional[int] = Field(default_factory=lambda: next(c))
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
    return jsonify(PeopleList(people_list=database.all(), count=len(database.all())).dict())


@server.post('/people')
@spec.validate(body=Request(People), resp=Response(HTTP_200=People))
def create_new_person():
    body = request.context.body.dict()
    database.insert(body)
    return body


@server.put('/people/<int:id>')
@spec.validate(body=Request(People), resp=Response(HTTP_200=People))
def edit_people(id):
    People = Query()
    body = request.context.body.dict()
    database.update(body, People.id == id)
    return jsonify(body)


@server.delete('/people/<int:id>')
@spec.validate(resp=Response('HTTP_204'))
def delete_people(id):
    database.remove(Query().id == id)
    return jsonify({})


server.run()
