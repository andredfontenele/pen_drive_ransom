import os

arquivo = "mensagem_alunos.txt"
caminho = os.path.join(os.getcwd(), arquivo)

try:
    os.startfile(caminho)
except Exception as e:
    print(f"Erro ao abrir o arquvi: {e}")