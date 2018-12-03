#!/usr/bin/python3
from pymongo import MongoClient
from faker import Faker

try:
    con = MongoClient()
    db = con['tdc']
except Exception as e:
    print(f'Erro: {e}')


fake = Faker('pt-BR')


def random_user():
    user = {
        'nome': fake.name(),
        'email': fake.email(),
        'cpf': fake.cpf(),
        'cep': fake.postcode(),
        'senha': fake.sha256()
    }
    return user

def register_user(user):
    db.users.insert(user)
