# agenda.py

import json
from contato import Contato

class Agenda:
    def __init__(self, arquivo='agenda.json'):
        self.arquivo = arquivo
        self.contatos = []
        self.carregar_contatos()

    def adicionar_contato(self, contato):
        self.contatos.append(contato)
        self.salvar_contatos()

    def remover_contato(self, nome):
        self.contatos = [contato for contato in self.contatos if contato.nome != nome]
        self.salvar_contatos()

    def listar_contatos(self):
        for contato in self.contatos:
            print(contato)

    def salvar_contatos(self):
        with open(self.arquivo, 'w') as f:
            json.dump([contato.__dict__ for contato in self.contatos], f)

    def carregar_contatos(self):
        try:
            with open(self.arquivo, 'r') as f:
                contatos = json.load(f)
                self.contatos = [Contato(**contato) for contato in contatos]
        except FileNotFoundError:
            self.contatos = []
