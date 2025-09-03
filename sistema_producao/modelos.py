class Pessoa:
    def __init__(self,nome,sobrenome,email,senha):
        self.nome = nome
        self.sobrenome = sobrenome
        self.email = email
        self.senha = senha
        self.lista_de_producoes = []
        
class Producao:
    def __init__(self,categoria,plataforma,nome,genero_um,genero_dois,data,nota,id):
        self.categoria = categoria
        self.plataforma = plataforma
        self.nome = nome
        self.genero_um = genero_um
        self.genero_dois = genero_dois
        self.data = data
        self.nota = nota
        self.id = id

class VoltarMenu(Exception):
    pass        