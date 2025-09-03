import os,re,time,random

def limpa_tela():
    os.system('cls')

def prosseguir_ou_voltar(palavra,lugar):
    input(f"\n{"⏩" if palavra == "prosseguir" else "⏪"} Pressione Enter para {palavra} {lugar}.")
    limpa_tela()

def frase_continuar_ou_voltar(frase,palavra,lugar):
    print(f"{frase}")
    prosseguir_ou_voltar(palavra,lugar)
