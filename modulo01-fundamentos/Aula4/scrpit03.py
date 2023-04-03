"""
Entrada e saída em arquivos txt
I/O (Input/ Output)
"""
import os


if __name__ == "__main__":
    """
    Para abrir arquivos em Python, utilizamos a função built-in open()

    A função open() normalmente recebe 2 argumentos: O arquivo a ser aberto, e o modo de abertura
    """

    # os.getcwd() Função do pacote os que retorna o caminha atual de onde o script está sendo executado
    # path.join() Função do pacote os que "junta" os caminhos do sistema de arquivos
    # Na linha abaixo montamos o caminho até o arquivo log.txt que deve estar na mesma pasta que o 
    # script está sendo executado

    # A função open() retorna um objeto do tipo file
    arquivo = open(os.path.join(os.getcwd(), "log.txt"),"r")

    # Lendo um arquivo utilizando o método read()
    # Podemos passar um valor para o argumento size, que é a quantidade de caracteres que serão lidos
    print(arquivo.read())
    print()
    print("=" * 50 )

    contuedo = arquivo.read()

    # Essa linha não ira imprimir o contuedo pois o curso do aquivo está no final, para ler novamente
    # o conteúdo precisamos apontar o cursos para o começo do arquivo
    # O método readlines() retorna uma lista contendo as linhas do arquivo
    print(arquivo.readline())

    # Mostrando a posição atual do cursos
    print(arquivo.tell())
    
    # Apontasr o cursos para o começo do arquivo
    arquivo.seek(0)
    print(arquivo.readlines())

    # Fecha o arquivo
    arquivo.close()