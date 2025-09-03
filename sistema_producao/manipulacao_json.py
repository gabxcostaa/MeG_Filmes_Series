import json
from sistema_producao.dados import dados_pessoa
from sistema_producao.modelos import Pessoa,Producao

def salvar_arquivo(caminho,dados):
    with open (caminho,"w",encoding="utf-8") as arquivo:
        json.dump(dados,arquivo,ensure_ascii=False,indent=4)

def carregar_arquivo(caminho):
    try:
        with open(caminho,"r",encoding="utf-8") as arquivo:
           return json.load(arquivo)
    except FileNotFoundError:
        return {"pessoas" : []}

def inicializar_dados_ao_abrir_o_app():
    dados_json = carregar_arquivo("dados.json")
    dados_pessoa.clear() 

    for p in dados_json["pessoas"]:
        pessoa = Pessoa(p["nome"], p["sobrenome"], p["email"], p["senha"])

    for prod in p.get("producoes", []):
            producao = Producao(
                prod.get("categoria", ""),
                prod.get("plataforma", ""),
                prod.get("nome", ""),
                prod.get("genero_um", ""),
                prod.get("genero_dois", ""),
                prod.get("data", ""),
                prod.get("nota", ""),
                prod.get("id", "")
            )
            pessoa.lista_de_producoes.append(producao)
    dados_pessoa.append(pessoa)

def salvar_dados():
    dados_para_salvar = {
        "pessoas": [
            {
                "nome": p.nome,
                "sobrenome": p.sobrenome,
                "email": p.email,
                "senha": p.senha,
                "producoes": [
                    {
                        "categoria": prod.categoria,
                        "plataforma": prod.plataforma,
                        "nome": prod.nome,
                        "genero_um": prod.genero_um,
                        "genero_dois": prod.genero_dois,
                        "data": prod.data,
                        "nota": prod.nota,
                        "id": prod.id
                    } for prod in p.lista_de_producoes
                ]
            } for p in dados_pessoa
        ]
    }
    salvar_arquivo("dados.json", dados_para_salvar)
