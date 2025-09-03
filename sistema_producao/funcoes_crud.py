from sistema_producao.funcoes_verificadoras import validar_dados_pre_definidos_da_producao, validar_dados_escritos_da_producao, validar_id, exibir_tabela,validar_dados_pre_definidos_de_busca,validar_dados_pre_definidos_de_edicao,validar_dados_pre_definidos_de_remover
from sistema_producao.dados import campos_tabela_principal
from sistema_producao.funcoes_essencias import limpa_tela, frase_continuar_ou_voltar
from sistema_producao.modelos import Producao,VoltarMenu
from sistema_producao.manipulacao_json import salvar_dados

def adicionar_produção(pessoa_logada):
    while True:
        try:
            categoria = validar_dados_pre_definidos_da_producao("Categorias"); limpa_tela()
            plataforma = validar_dados_pre_definidos_da_producao("Plataformas"); limpa_tela()
            nome = validar_dados_escritos_da_producao(f"Qual o nome{' do filme' if categoria == 'Filme' else ' da série'}", "o", "nome", r"^[A-Za-zÀ-ÿ0-9\s\-\:\'!&\.]{3,30}$", "O título deve conter entre 3 a 30 caracteres."); limpa_tela()
            genero_um = validar_dados_pre_definidos_da_producao("Generos"); limpa_tela()
            genero_dois = validar_dados_pre_definidos_da_producao("Generos"); limpa_tela()
            data = validar_dados_escritos_da_producao(f"Data que você viu {nome}", "a", "data", r"^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/[0-9]{4}$", "A data deve ser no padrão : DD/MM/AAAA"); limpa_tela()
            nota = validar_dados_escritos_da_producao(f"Qual a sua nota para {nome}", "a", "nota", r"^(10|[1-9])$", "A nota deve ser entre 1 a 10"); limpa_tela()
            id_gerado = validar_id(f"{'do filme' if categoria == 'Filme' else 'da série'}", nome)
            producao = Producao(categoria, plataforma, nome, genero_um, genero_dois, data, nota, id_gerado)
            pessoa_logada.lista_de_producoes.append(producao)
            salvar_dados()
        except VoltarMenu:
            frase_continuar_ou_voltar("↩️  Voltando ao Menu Principal","voltar","ao Menu Principal")
            break

        frase_continuar_ou_voltar("✅ Todas as informações foram enviadas com sucesso!", "voltar", "ao Menu Principal")

def mostrar_tabela_principal(pessoa_logada):
    exibir_tabela("🎬 Tabela das Produções [Filmes/Séries]\n",pessoa_logada.lista_de_producoes, campos_tabela_principal)
    frase_continuar_ou_voltar(f"\n📺 Essas são todas as suas {len(pessoa_logada.lista_de_producoes)} produções [Filmes e Séries] que você já assistiu!","voltar","ao Menu Principal")

def buscar_producao(pessoa_logada):
    validar_dados_pre_definidos_de_busca(pessoa_logada)

def editar_producao(pessoa_logada):
    validar_dados_pre_definidos_de_edicao(pessoa_logada)
    salvar_dados()

def remover_producao(pessoa_logada):
    validar_dados_pre_definidos_de_remover(pessoa_logada)
    salvar_dados()
    