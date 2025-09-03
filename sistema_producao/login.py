from sistema_producao.funcoes_essencias import limpa_tela,time
from sistema_producao.dados import campos_usuario,dados,dados_pessoa
from sistema_producao.funcoes_verificadoras import validar_dados_usuario
from sistema_producao.modelos import Pessoa

def criar_conta():
    for artigo,campo,atributo,padrao,correcao in campos_usuario:
            dados[atributo] = validar_dados_usuario(artigo,campo,atributo,padrao,correcao,False)

    pessoa = Pessoa(dados["nome"],dados["sobrenome"],dados["email"],dados["senha"])
    dados_pessoa.append(pessoa)

def fazer_login():
    email = None
    senha = None

    for artigo,campo,atributo,padrao,correcao in campos_usuario:
        if atributo == "email":
            email = validar_dados_usuario(artigo,campo,atributo,padrao,correcao,True)
        elif atributo == "senha":
            senha = validar_dados_usuario(artigo,campo,atributo,padrao,correcao,True)

    pessoa_logada = next((p for p in dados_pessoa if p.email == email), None)
    return pessoa_logada
     
def sair():
    print("Saindo do app...");time.sleep(2);limpa_tela();exit()
