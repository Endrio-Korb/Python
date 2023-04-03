# Cópia de lista

if __name__ == "__main__":
    lista_curso = ["Python", "C#", "PHP", "SQL", "Desing"]
    nova_lista_curso = lista_curso

    # Nesse caso, a linha anterior também altera o "valor" do 
    # dicionário lista_curso ambas as variáveis apontam para a mesma
    # posição de memória
    nova_lista_curso.pop(-1)
    print(nova_lista_curso)

    # Para resolver isso, podemos utilizar 2 abordagens:
    # Utilizar o métoodo copy()
    lista_curso_inverno = lista_curso.copy()
    lista_curso_inverno.append("Gollang")

    print(lista_curso_inverno)

    # Podemos gerar também um novo valor utilizando o slice
    lista_curso_primavera = lista_curso_inverno[:]
    lista_curso_primavera.append("Devops")

    print(lista_curso)
    print(nova_lista_curso)
    print(lista_curso_inverno)
    print(lista_curso_primavera)