from sistema_producao.login import criar_conta,fazer_login,sair
from sistema_producao.dados import opcoes_menu_login,opcoes_menu_principal
from sistema_producao.funcoes_essencias import frase_continuar_ou_voltar,limpa_tela
from sistema_producao.funcoes_crud import adicionar_produção,mostrar_tabela_principal,buscar_producao,editar_producao,remover_producao
from sistema_producao.manipulacao_json import inicializar_dados_ao_abrir_o_app

def exibir_opcoes(opcoes):
    for numero,opcao in enumerate(opcoes,start=1):
        print(f"{[numero]} {opcao}")

def criar_menu(opcoes,funcoes,titulo):
    while True:
        print(titulo)
        exibir_opcoes(opcoes)
        escolha = input(f"\n⭐ Selecione uma opção : ").strip();limpa_tela()
        if escolha.isdigit():
            escolha = int(escolha)
            if 1 <= escolha <= len(funcoes):
                funcoes[escolha - 1]()
                break
            else:
                frase_continuar_ou_voltar(f"❌ Escolha um número de 1 a {len(funcoes)}.","voltar","escolher uma opção");continue
        else:
            frase_continuar_ou_voltar("❌ Digite apenas números.","voltar","a escolher uma opção");continue

def menu_inicial():
    while True:
        def login_e_abrir_menu():
            pessoa = fazer_login()
            if pessoa:
                menu_principal(pessoa)
        funcoes = [login_e_abrir_menu, criar_conta, sair]
        criar_menu(opcoes_menu_login, funcoes, "\n🎬  M&G Filmes e Séries 🍿\n")
        
def menu_principal(pessoa_logada):
    while True:
        funcoes = [lambda: adicionar_produção(pessoa_logada),lambda: mostrar_tabela_principal(pessoa_logada),lambda: buscar_producao(pessoa_logada),lambda : editar_producao(pessoa_logada),lambda: remover_producao(pessoa_logada), menu_inicial]
        criar_menu(opcoes_menu_principal, funcoes, "\n🎬  Menu Principal 🎞️\n")

def main():
    inicializar_dados_ao_abrir_o_app()
    menu_inicial()

if __name__ == "__main__":
    main()    