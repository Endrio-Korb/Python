import os

if __name__ == "__main__":
    
    # Utilizamos a palavra reservada with para criar um contexto dentro do nosso código
    # A vantagem de se utlizar with é que o arquvio é fechado automaticamente quando saímos do bloco.
    # Quando abrimos um arquivo no modo "w", se o arquivno não existir ele criar, caso já exista ele sobreescreve
    with open(os.path.join(os.getcwd(),"texto_02.txt"), "w") as arquivo:
        
        nome = input("Informe o seu nome: ")

        # O método write escreve um string no arquivo
        arquivo.write(f"Seja bem vindo ao curso de Python, {nome}.\n")

        # O método writelines recebe uma lista de valores e insire no arquvio
        arquivo.writelines(["Python\n", "Goolan\n", "Java\n", "PHP\n"])


    # Quando abrimos o arquivo no modo "a" (append), se o arquivno não existir ele criar
    # Caso o arquivo já exista, o cursos é enviado para o final do arquvio, com isso sendo 
    # possível adicionar mais informações no arquvio
    with open(os.path.join(os.getcwd(),"texto_02.txt"), "a") as arquivo:
        arquivo.write("Esse texto não sobreesceveu o arquivo")

    # Também podemos abrir o arquivo como leitra e escrita
    with open(os.path.join(os.getcwd(), "texo_02.txt"), "r+t") as arquivo:
        print