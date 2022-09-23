## Python API
___
### Sobre
API construída com python utilizando flask para uma melhor produtividade e tinydb como banco de dados em memória.
O projeto serviu para entender melhor como utilizar o pydantic e o pydantic spec para organizar as rotas e endpoints
da aplicação, além de implementar as principais funções HTTP de um CRUD (create, read, update e delete).

### Tecnologias

Como gerenciador de pacotes, utilizei o [poetry](https://python-poetry.org/), além das bibliotecas listadas abaixo:

- [Flask](https://flask.palletsprojects.com/en/2.2.x/)
- [Pydantic Spec](https://pypi.org/project/flask-pydantic-spec/)
- [TinyDB](https://tinydb.readthedocs.io/en/latest/)

### Model

Como modelo de dados, utilizei o BaseModel do Flask, organizando da seguinte maneira:

```py
class People:
    id: int
    name: str
    gender: str
    address: str
    phone: str
    
```

Para listar todas as pessoas cadastradas, criei outro model, dessa vez organizado da seguinte maneira:

```py
class PeopleList:
    people_list: list[People] # referência a classe People
    count: int # poder retornar um contador com todos da lista
```

### Rotas

**- Criando um novo registro:**

Método POST:
```cmd
http://localhost:5000/people
```
Formato JSON:
```json
{
    "name": "celio viana",
    "gender": "M",
    "address": "R. Rep. da Armênia",
    "phone": "85 9 9999-9999"
}
```

**- Listando todos os usuários:**

Método GET:
```cmd
 http://localhost:5000/people
```

**- Editando dados de uma única pessoa:**

Método PUT:

```cmd
http://localhost:5000/people/{id}
```

Formato JSON:
```json
{
    "name": "celio viana EDIT",
    "gender": "M EDIT",
    "address": "R. Rep. EDIT",
    "phone": "85 9 9999-9999 EDIT"
}
```

**- Deletando uma pessoa:**

Método DELETE:

```cmd
http://localhost:5000/people/{id}
```
___
## Considerações finais

Para fazer download do projeto, é necessário que você tenha o Python instalado na máquina, além de um gerenciador
de pacotes como pip, poetry ou conda.<br>
Dependendo do seu sistema operacional e de outras configurações, podem ocorrer alguns imprevistos durante o processo, ou seja, o que deu certo na minha máquina pode não dar certo na sua.<br>
Por essa razão, aqui estão os links para a documentação de cada ferramenta que citei acima:

- [Instalando Python](https://www.python.org/downloads/)
- [Instalando o gerenciador de pacote Pip](https://pip.pypa.io/en/stable/installation/)
- [Instalando o gerenciador de pacote Poetry](https://python-poetry.org/docs/)
- [Instalando o gerenciador de pacote Conda](https://conda.io/projects/conda/en/latest/user-guide/install/index.html)

