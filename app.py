# import os
# import subprocess

# os.system("notepad filename.txt")
# subprocess.Popen(["notepad", "filename.txt"])

import os
import datetime

def criar_arquivo_texto(nome_arquivo, mensagem):
    with open(nome_arquivo, 'w') as arquivo:
        arquivo.write(mensagem)

def verificar_pen_drive():
    drives = [f"{d}:\\" for d in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ']
    for drive in drives:
        if os.path.exists(drive):
            return drive
        return None
    
def main():
    pen_drive = verificar_pen_drive()

    if pen_drive:
        nome_arquivo = f"{pen_drive}mensagem_alunos.txt"
        alunos = ["Aluno 1", "Aluno 2", "Aluno 3"]
        mensagem = f"Trabalho realizado por: \n"
        for aluno in alunos:
            mensagem += f"{aluno}\n"

        mensagem += f"\nData e hora: {datetime.datetime.now()}"

        criar_arquivo_texto(nome_arquivo, mensagem)
        print(f"Arquivo criado em {nome_arquivo}")
    else:
        print("Nenhum pen drive encontrado.")

if __name__ == "__main__":
    main()

