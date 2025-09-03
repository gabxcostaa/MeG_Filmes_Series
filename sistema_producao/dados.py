campos_usuario = [
    ("o","nome","nome",r"^[A-Za-zÀ-ÖØ-öø-ÿ]{3,15}$","O nome deve conter no mínimo 3 e no máximo 15 letras."),
    ("o","sobrenome","sobrenome",r"^[A-Za-zÀ-ÖØ-öø-ÿ]{3,15}$","O sobrenome deve conter no mínimo 3 e no máximo 15 letras."),
    ("o","e-mail","email",r"^[a-zA-Z0-9._%+-]{3,15}@(gmail\.com|outlook\.com)$","O email deve conter no mínimo 3 e no máximo 15 letras antes do @ e deve conter @gmail.com ou @outlook.com."),
    ("a","senha","senha",r"^(?=.*[A-Z])(?=.*[!@#$%^&*()_\-+=\[\]{};:',.<>?/\\|~]).{8,}$","A senha deve conter no mínimo 8 caracteres sendo um deles uma letra maiúscula e um caractér especial.")]

opcoes_producao = {
    "Categorias": {
        "titulo": "🍿 Categorias",
        "frase": "a categoria",
        "opcoes": [
            {"id": 1, "nome": "Filme", "emoji": "🎬"},
            {"id": 2, "nome": "Série", "emoji": "📺"}
        ]
    },
    "Plataformas": {
        "titulo": "🌐 Plataformas",
        "frase": "a plataforma",
        "opcoes": [
            {"id": 1, "nome": "Netflix", "emoji": "📽️ "},
            {"id": 2, "nome": "HBO Max", "emoji": "🎞️ "},
            {"id": 3, "nome": "Prime Video", "emoji": "🎥"},
            {"id": 4, "nome": "Kinoplex", "emoji": "🎟️ "}
        ]
    },
    "Generos": {
        "titulo": "🎭 Gêneros",
        "frase": "o gênero",
        "opcoes": [
            {"id": 1, "nome": "Ação", "emoji": "💥"},
            {"id": 2, "nome": "Animação", "emoji": "🎞️ "},
            {"id": 3, "nome": "Aventura", "emoji": "🏕️ "},
            {"id": 4, "nome": "Biografia", "emoji": "🖋️ "},
            {"id": 5, "nome": "Comédia", "emoji": "😂"},
            {"id": 6, "nome": "Crime", "emoji": "☠️ "},
            {"id": 7, "nome": "Documentário", "emoji": "🎥"},
            {"id": 8, "nome": "Drama", "emoji": "🎭"},
            {"id": 9, "nome": "Fantasia", "emoji": "🧙"},
            {"id": 10, "nome": "Ficção científica", "emoji": "🚀"},
            {"id": 11, "nome": "Mistério", "emoji": "🕵️ "},
            {"id": 12, "nome": "Musical", "emoji": "🎶"},
            {"id": 13, "nome": "Romance", "emoji": "❤️ "},
            {"id": 14, "nome": "Sobrenatural", "emoji": "👻"},
            {"id": 15, "nome": "Suspense", "emoji": "😱"},
            {"id": 16, "nome": "Terror", "emoji": "🔪"}
        ]
    }
}

opcoes_menu_login =  ["👤 Fazer Login","🆕 Criar Conta","🚪 Sair"]
opcoes_menu_principal = ["🍿 Adicionar","📊 Ver Tabela","🔍 Buscar","✏️  Editar","🗑️  Remover","↩️  Voltar"]

dados_pessoa = []
dados = {}

campos_tabela_principal = {
    "ID Produção" : ("id",11),
    "Categoria" : ("categoria",9),
    "Nome":("nome",40),
    "Gênero 1": ("genero_um",17),
    "Gênero 2" : ("genero_dois",17),
    "Plataforma": ("plataforma",15),
    "Data": ("data",12),
    "Nota": ("nota",4)}

campos_de_busca = {
    "ID": {
        "atributo" : "id",
        "emoji" : "🆔",
        "id" : 1,
        "nome_da_tabela" : "Dados da Produção [Filme/Série]"
    },
    "Categoria": {
        "atributo": "categoria",
        "emoji": "🎬",
        "id" : 2,
        "nome_da_tabela" : "Tabela"  
    },
    "Plataforma": {
        "atributo": "plataforma",
        "emoji": "📺",
        "id" : 3,
        "nome_da_tabela" : "Tabela"    
    },
    "Nome": {
        "atributo": "nome",
        "emoji": "🏷️ ",
        "id" : 4,
        "nome_da_tabela" : "Dados da Produção [Filme/Série]"
    },
    "Genero": {
        "atributo": "genero",
        "emoji": "🎭",
        "id" : 5,
        "nome_da_tabela" : "Tabela"
    },
    "Data": {
        "atributo": "data",
        "emoji": "📅",
        "id" : 6,
        "nome_da_tabela" : "Tabela das Produções assistidas nessa data"
    },
    "Nota": {
        "atributo": "nota",
        "emoji": "⭐",
        "id" : 7,
        "nome_da_tabela" : "Tabela das Produções com essa nota"
    }
}
