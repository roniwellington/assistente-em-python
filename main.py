from interface_chat import InterfaceChat
from assistente_commit import AssistenteCommit

def main():
    
    nome = "Assistente de Commits"
    caminho_arquivo = "Projeto_Dados\\twitch_analytics\\data_analytics.py"
    assistente_commit = AssistenteCommit(caminho_arquivo=caminho_arquivo)
    assistente_commit = InterfaceChat(assistente_commit)
    lista_mensagems = assistente_commit.conversar("Você pode gerar uma sugestão de commit para o script data_analytics que estou envidando para você")
    
    for uma_mensagem in lista_mensagems:
        print(f"\n{uma_mensagem.text.value}")
        
        
if __name__ == "__main__":
    main()