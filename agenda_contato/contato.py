class Contato:
    def __init__(self, nome,telefone, email):
        self.nome = nome
        self.telefone = telefone
        self.email = email
    
    def __repr__(self):
        return f'Contato(nome={self.nome}, telefone={self.telefone}, email={self.email})'
