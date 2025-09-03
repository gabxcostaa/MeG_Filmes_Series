from sistema_producao.funcoes_essencias import frase_continuar_ou_voltar,limpa_tela,re,random,time
from sistema_producao.dados import dados_pessoa,opcoes_producao,campos_de_busca,campos_tabela_principal
from sistema_producao.modelos import VoltarMenu

def validar_dados_usuario(artigo,campo,atributo,padrao,correcao,fazer_login):
    while True:
        dado = input(f"📝 {campo.capitalize()} : ").strip();limpa_tela() # Recolhe o nome,sobrenome,email,senha do usuário #

        if not dado: # Verifica se o campo está vazio #
            frase_continuar_ou_voltar(f"🚫 {artigo.capitalize()} {campo} é obrigatóri{artigo}.","voltar",f"a validar {artigo} {campo}");continue
        
        if not re.fullmatch(padrao,dado): # Verifica se está no padrão #
            frase_continuar_ou_voltar(f"❌ {correcao}","voltar",f"a validar o {campo}");continue
        
        if fazer_login == False: # Criando a conta e não fazendo o login #
            if atributo == "email":
                dado_duplicado = any((getattr(pessoa,atributo) == dado for pessoa in dados_pessoa))
                if dado_duplicado:
                    frase_continuar_ou_voltar(f"⚠️ {artigo.capitalize()} {campo} já existe.","voltar",f"a validar o {campo}");continue
            frase_continuar_ou_voltar(f"✅ {campo.capitalize()} cadastrado com sucesso","prosseguir","com o formulário") 

        if fazer_login == True: # Fazendo o Login #

            if atributo == "email":
                email_encontrado = any((getattr(pessoa,atributo) == dado for pessoa in dados_pessoa))
                if not email_encontrado:
                    frase_continuar_ou_voltar("⚠️  Esse email não está cadastrado","voltar","a tentar novamente");continue
                
            if atributo == "senha":
                senha_encontrada = next((dado for pessoa in dados_pessoa if dado == pessoa.senha), None)
                if not senha_encontrada:  
                    frase_continuar_ou_voltar("❌ A senha está incorreta","voltar","a tentar novamente");continue
                frase_continuar_ou_voltar(f"🍿 Bem vindo ao M&G Filmes e Séries 💫","prosseguir","ao Menu Principal")
        return dado.title() if atributo in ["nome","sobrenome"] else dado

def validar_dados_pre_definidos_da_producao(opcoes):
    while True:
        print(f"\n{opcoes_producao[opcoes]['titulo']}\n") # Titulo [Categoria,Plataforma,Genero] #

        frase = opcoes_producao[opcoes]["frase"]
        opcoes_disponiveis = opcoes_producao[opcoes]["opcoes"]

        for cat in opcoes_producao[opcoes]["opcoes"]: # Exibe as opções de cada [Categoria,Plataforma,Genero] #
            print(f"[{cat['id']}] {cat['emoji']} {cat['nome']}")

        numero_maximo = len(opcoes_disponiveis)    

        if opcoes == "Categorias": 
            print(f"[3] ↩️  Voltar") 

        numero_escolhido = input(f"\n⭐ Escolha {frase} : ").strip() # Recolhe a opção da [Categoria,Plataforma,Genero] #
        limpa_tela()

        if not numero_escolhido: # Verifica se o campo está vazio #
            frase_continuar_ou_voltar(f"🚫 {frase.capitalize()} é obrigatóri{frase[0]}","voltar",f"a escolher {frase}");continue

        if not (1 <= int(numero_escolhido) <= (numero_maximo + 1 if opcoes == "Categorias" else numero_maximo)): # Verifica se o número fornecido está entre 1 e o tamanho do array #
          frase_continuar_ou_voltar(f"❌ Somente números entre 1 e {(numero_maximo + 1 if opcoes == "Categorias" else numero_maximo)}","voltar",f"a escolher {frase}");continue
        
        if int(numero_escolhido) == numero_maximo + 1: # Caso o número seja 3, o programa faz com que o usuário volte ao Menu Principal #
            raise VoltarMenu

        nome_da_escolha = next((cat["nome"] for cat in opcoes_disponiveis if int(numero_escolhido) == cat["id"]),None)
        frase_continuar_ou_voltar(f"✅ Voce escolheu {frase} '{nome_da_escolha}'","prosseguir","com o formulário")
        return nome_da_escolha

def validar_dados_escritos_da_producao(frase,artigo,atributo,padrao,correcao):
    while True:
        dado = input(f"📝 {frase} : ");limpa_tela()

        if not dado : # Verifica se o campo está vazio #
            frase_continuar_ou_voltar(f"🚫 {artigo.capitalize()} {atributo} é obrigatóri{artigo}.","voltar",f"a validar {artigo} {atributo}");continue
        
        if not re.fullmatch(padrao,dado): # Verifica se está no padrão #
            frase_continuar_ou_voltar(f"❌ {correcao}","voltar",f"a validar o {atributo}");continue
        
        frase_continuar_ou_voltar(f"✅ {atributo.capitalize()} enviad{artigo} com sucesso","prosseguir","com o formulário")
        return dado 

def validar_id(categoria_producao,nome_producao):
    while True:
        id_selecionado = random.randint(1000,9999) # Aleatoriza um número entre 1000 e 9999 para ser o ID Produção #
        id_existente = any(prod.id == id_selecionado for pessoa in dados_pessoa for prod in pessoa.lista_de_producoes)
        if not id_existente:
            print(f"🆔 {categoria_producao} {nome_producao} : {id_selecionado}\n")
            return id_selecionado

def exibir_tabela(nome_tabela,dados_classe,lista_campos):

    if not dados_classe:
        frase_continuar_ou_voltar(f"❌ Nenhuma produção cadastrado ainda.","voltar"," ao Menu Anterior")
        
    if dados_classe:    

        print(f" {nome_tabela}\n") 
        total_qtd_espacos = sum(qtd_espacos for _, (_, qtd_espacos) in lista_campos.items())
        total_separadores = (len(lista_campos) - 1) * 3 + 4   
        largura_linha = total_qtd_espacos + total_separadores
        qtd_tracos = "-" * largura_linha

        print(qtd_tracos)
        linha_fixa = "| " + " | ".join(f"{titulo:^{qtd_espacos}}" for titulo, (_, qtd_espacos) in lista_campos.items()) + " |"
        print(linha_fixa)
        print(qtd_tracos)

        for instancia in dados_classe:
            linha_com_dados = "| " + " | ".join(f"{str(getattr(instancia, atributo)):^{qtd_espacos}}" for _, (atributo, qtd_espacos) in lista_campos.items()) + " |" 
            print(linha_com_dados)
            print(qtd_tracos)
  
def validar_dados_pre_definidos_de_busca(pessoa_logada):
    if not pessoa_logada.lista_de_producoes:
         frase_continuar_ou_voltar("❌ Não há produção para buscar","voltar","ao Menu Principal")
    while True:
        print("\n🔎  Opções de Busca 🔍\n")
        for opcao, dados in campos_de_busca.items():
            print(f"[{dados['id']}] {dados['emoji']} {opcao}")
        print("[8] ↩️  Voltar")

        try:
            numero_escolhido = int(input("\n⌨️  Escolha uma opção de busca : ").strip())
        except ValueError:
            frase_continuar_ou_voltar("Digite um número válido!", "voltar", "a escolher uma opção de busca")
            continue

        limpa_tela()

        if numero_escolhido == 8: # Volta ao Menu Principal #
            break

        if not (1 <= numero_escolhido <= len(campos_de_busca)):
            frase_continuar_ou_voltar(f"❌ Somente números entre 1 e {len(campos_de_busca)}", "voltar", "a escolher a opção de busca")
            continue

   
        nome_da_escolha = next((opcao for opcao, dados in campos_de_busca.items() if dados['id'] == numero_escolhido), None)
        dados_escolhidos = campos_de_busca[nome_da_escolha]

        frase_continuar_ou_voltar(f"🔍 Opção de busca : {nome_da_escolha}", "prosseguir", "com a busca")

       
        if nome_da_escolha in ["Categoria", "Plataforma", "Genero"]:
            chave_opcoes = f"{nome_da_escolha}s" 
            print(f"\n{opcoes_producao[chave_opcoes]['titulo']}\n")
            frase = opcoes_producao[chave_opcoes]["frase"]
            opcoes_disponiveis = opcoes_producao[chave_opcoes]["opcoes"]

            for cat in opcoes_disponiveis:
                print(f"[{cat['id']}] {cat['emoji']} {cat['nome']}")

            try:
                numero_opcao = int(input(f"\n⭐ Escolha {frase} : ").strip())
            except ValueError:
                frase_continuar_ou_voltar(f"Digite um número válido!", "voltar", f"a escolher {frase}")
                continue

            limpa_tela()

            if not (1 <= numero_opcao <= len(opcoes_disponiveis)):
                frase_continuar_ou_voltar(f"❌ Somente números entre 1 e {len(opcoes_disponiveis)}", "voltar", f"a escolher {frase}")
                continue

            nome_da_escolha_selecionada = next((cat["nome"] for cat in opcoes_disponiveis if cat["id"] == numero_opcao), None)
            frase_continuar_ou_voltar(f"✅ Você escolheu {frase} '{nome_da_escolha_selecionada}'", "prosseguir", "com o formulário")

            if nome_da_escolha == "Genero":
                lista_filtrada = filtrar_por_genero(pessoa_logada.lista_de_producoes, nome_da_escolha_selecionada)
                exibir_tabela("Tabela dos Generos", lista_filtrada, campos_tabela_principal)
                frase_continuar_ou_voltar(f"\n🍿 {pessoa_logada.nome}, essa é a sua lista de produções que contém '{nome_da_escolha_selecionada}' como gênero. Total: {len(lista_filtrada)}", "voltar", "a Opções de busca")
            else:
                
                atributo = dados_escolhidos['atributo']
                lista_filtrada = [prod for prod in pessoa_logada.lista_de_producoes if getattr(prod, atributo) == nome_da_escolha_selecionada]
                exibir_tabela(f"🎬 {nome_da_escolha_selecionada}", lista_filtrada, campos_tabela_principal)
                frase_continuar_ou_voltar(f"\n🍿 {pessoa_logada.nome}, essa é a sua {nome_da_escolha_selecionada} List com o total de {len(lista_filtrada)} produções!", "voltar", "a Opções de busca")

        else:
            campo_filtrado = input(f"🔎 Filtrar por {nome_da_escolha.lower()} : ").strip()
            limpa_tela()
            atributo = dados_escolhidos['atributo']

            if atributo in ["id", "nota"]:
                try:
                    campo_filtrado = int(campo_filtrado)
                except ValueError:
                    frase_continuar_ou_voltar("Digite um número válido!", "voltar", f"a escolher {nome_da_escolha.lower()}")
                    continue

            lista_filtrada = [prod for prod in pessoa_logada.lista_de_producoes if(isinstance(getattr(prod, atributo), int) and getattr(prod, atributo) == campo_filtrado)or(isinstance(getattr(prod, atributo), str) and getattr(prod, atributo).strip().lower() == str(campo_filtrado).strip().lower())]
            nome_tabela = campos_de_busca[nome_da_escolha]["nome_da_tabela"]
            exibir_tabela(nome_tabela, lista_filtrada, campos_tabela_principal)
            frase_continuar_ou_voltar(f"\n🍿 {pessoa_logada.nome},essa é o total de produções encontradas : {len(lista_filtrada)}", "voltar", "a Opções de busca")
           
def filtrar_por_genero(lista_producoes, genero_pesquisado):
        genero_pesquisado = genero_pesquisado.strip().lower()
        return [prod for prod in lista_producoes if any(str(getattr(prod, g)).strip().lower() == genero_pesquisado for g in ["genero_um", "genero_dois"])]

def validar_dados_pre_definidos_de_edicao(pessoa_logada):
    if not pessoa_logada.lista_de_producoes:
        frase_continuar_ou_voltar("❌ Não há produção para editar","voltar","ao Menu Principal")
    
    while True:
        print("\n✏️  Opções de Edição\n")
        campo_id = 1
        id_para_campo = {}
        for opcao, dados in campos_de_busca.items():
            if opcao != "ID":  
                print(f"[{campo_id}] {dados['emoji']} {opcao}")
                id_para_campo[campo_id] = opcao
                campo_id += 1
        print(f"[{campo_id}] ↩️  Voltar")
        voltar_id = campo_id

        try:
            numero_escolhido = int(input("\n⌨️  Escolha um campo para editar: ").strip())
        except ValueError:
            frase_continuar_ou_voltar("Digite um número válido!", "voltar", "a escolher um campo");continue

        limpa_tela()

        if numero_escolhido == voltar_id: # Volta ao Menu Principal #
            break

        if numero_escolhido not in id_para_campo:
            frase_continuar_ou_voltar(f"❌ Escolha um número válido entre 1 e {voltar_id}", "voltar", "a escolher um campo");continue

        nome_da_escolha = id_para_campo[numero_escolhido]
        dados_escolhidos = campos_de_busca[nome_da_escolha]
        atributo = dados_escolhidos['atributo']

        exibir_tabela("🎬 Produções", pessoa_logada.lista_de_producoes, campos_tabela_principal)

        try:
            id_producao = int(input("\n⭐ Digite o ID da produção que deseja editar: ").strip())
        except ValueError:
            frase_continuar_ou_voltar("⚠️ Digite um número válido!", "voltar", "a escolher a produção");continue
        
        limpa_tela()
        producao_selecionada = next((p for p in pessoa_logada.lista_de_producoes if p.id == id_producao), None)
        if not producao_selecionada:
            frase_continuar_ou_voltar("❌ Produção não encontrada com esse ID!", "voltar", "a Opções de edição");continue

        if nome_da_escolha in ["Categoria", "Plataforma", "Genero"]:
            chave_opcoes = f"{nome_da_escolha}s"
            print(f"\n{opcoes_producao[chave_opcoes]['titulo']}\n")
            frase = opcoes_producao[chave_opcoes]["frase"]
            opcoes_disponiveis = opcoes_producao[chave_opcoes]["opcoes"]

            for cat in opcoes_disponiveis:
                print(f"[{cat['id']}] {cat['emoji']} {cat['nome']}")

            if nome_da_escolha == "Genero":
                try:
                    numero_genero_um = int(input(f"\n⭐ Escolha o 1º {frase} para a produção : ").strip())
                    numero_genero_dois = int(input(f"\n⭐ Escolha o 2º {frase} para a produção : ").strip())
                except ValueError:
                    frase_continuar_ou_voltar("Digite números válidos!", "voltar", f"a escolher {frase}");continue
                limpa_tela()
                if not (1 <= numero_genero_um <= len(opcoes_disponiveis)) or not (1 <= numero_genero_dois <= len(opcoes_disponiveis)):
                    frase_continuar_ou_voltar(f"❌ Somente números entre 1 e {len(opcoes_disponiveis)}", "voltar", f"a escolher {frase}");continue

                novo_genero_um = next(cat["nome"] for cat in opcoes_disponiveis if cat["id"] == numero_genero_um)
                novo_genero_dois = next(cat["nome"] for cat in opcoes_disponiveis if cat["id"] == numero_genero_dois)

                producao_selecionada.genero_um = novo_genero_um
                producao_selecionada.genero_dois = novo_genero_dois

                frase_continuar_ou_voltar(f"✅ Produção atualizada! Os novos gêneros são '{novo_genero_um}' e '{novo_genero_dois}'","voltar","a Opções de edição")

            else:  # Categoria ou Plataforma
                try:
                    numero_opcao = int(input(f"\n⭐ Escolha {frase[0]} nov{frase} para a produção : ").strip())
                except ValueError:
                    frase_continuar_ou_voltar("Digite um número válido!", "voltar", f"a escolher {frase}");continue
                limpa_tela()
                if not (1 <= numero_opcao <= len(opcoes_disponiveis)):
                    frase_continuar_ou_voltar(f"❌ Somente números entre 1 e {len(opcoes_disponiveis)}", "voltar", f"a escolher {frase}");continue

                novo_valor = next(cat["nome"] for cat in opcoes_disponiveis if cat["id"] == numero_opcao)
                setattr(producao_selecionada, atributo, novo_valor)
                frase_continuar_ou_voltar(f"✅ Produção atualizada! {frase[0].capitalize()} nov{frase} é '{novo_valor}'","voltar","a Opções de edição")

        else:
            novo_valor = input(f"Digite{f' o novo {nome_da_escolha}' if nome_da_escolha == 'Nome' else f' a nova {nome_da_escolha}'} : ").strip()
            
            if atributo in ["nota"]:
                try:
                    novo_valor = int(novo_valor)
                except ValueError:
                    frase_continuar_ou_voltar("Digite um número válido para nota!", "voltar", "ao campo");continue
            limpa_tela()
            setattr(producao_selecionada, atributo, novo_valor)
            frase_continuar_ou_voltar(f"✅ Produção atualizada! {f'O novo {nome_da_escolha}' if nome_da_escolha == 'Nome' else f'A nova {nome_da_escolha}'} é '{novo_valor}'","voltar","a Opções de edição")

def validar_dados_pre_definidos_de_remover(pessoa_logada):
    if not pessoa_logada.lista_de_producoes:
        frase_continuar_ou_voltar("❌ Não há produção para remover","voltar","ao Menu Principal")

    while True:
        print("\n🗑️ Produções Disponíveis para Remover\n")
        exibir_tabela("🎬 Produções", pessoa_logada.lista_de_producoes, campos_tabela_principal)
        print("\n[0] ↩️  Voltar")

        try:
            id_producao = int(input("\n⭐ Digite o ID da produção que deseja remover : ").strip())
        except ValueError:
            frase_continuar_ou_voltar("Digite um número válido!", "voltar", "ao Menu de Remover");continue
        limpa_tela()
        if id_producao == 0:
            break

        producao_selecionada = next((p for p in pessoa_logada.lista_de_producoes if p.id == id_producao), None)
        if not producao_selecionada:
            frase_continuar_ou_voltar("❌ Produção não encontrada com esse ID!", "voltar", "ao Menu de Remover");continue

        print("\n[1] ✅ Sim")
        print("[2] ❌ Não")

        confirmacao = input(f"\n⚠️  {pessoa_logada.nome}, tem certeza que deseja remover '{producao_selecionada.nome}' : ").strip().lower();limpa_tela()

        if confirmacao == '1':
            pessoa_logada.lista_de_producoes.remove(producao_selecionada)
            frase_continuar_ou_voltar(f"✅ Produção '{producao_selecionada.nome}' removida com sucesso!", "voltar", "ao Menu de Remover");break
        if confirmacao == '2':
            frase_continuar_ou_voltar("❌ Remoção cancelada.", "voltar", "ao Menu de Remover");break
 