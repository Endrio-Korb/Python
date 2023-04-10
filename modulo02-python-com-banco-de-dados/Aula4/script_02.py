import sqlite3

# Dicionário com os produtos
produtos = [
    {"nome": "Pastel", "preco": 9.90},
    {"nome": "Coxinha", "preco": 5},
    {"nome": "Rolinho de Salsicha","preco": 5},
    {"nome": "Cachorro-Quente", "preco": 10},
    {"nome": "Risoles", "preco": 8}
]


# Função que exlui todas as tabelas
def excluir_tabelas(cursor):
    tabelas = ["tb_pedidos_itens", "tb_pedidos", "tb_produtos"]
    for i in tabelas:
        comando = f"DROP TABLE IF EXISTS {i};"
        cursor.execute(comando)
    print("Tabelas excluidas.")


# Função que cria a tabela de produtos
def criar_tabela_produto(cursor):

    comando = """
     CREATE TABLE IF NOT EXISTS tb_produtos(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        preco REAL NOT NULL
    )
    """
    cursor.execute(comando)
    print("Tabela tb_produtos criada com sucesso.")


# Função que cria a tabela de pedidos
def criar_tabela_pedidos(cursor):
    comando = """
    CREATE TABLE IF NOT EXISTS tb_pedidos(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        data_hora TIMESTAMP NOT NULL,
        observacoes TEXT 
    );
    """
    cursor.execute(comando)
    print("Tabela tb_pedidos criada com sucesso.")



# Função que cria a tabela de pedidos_itens
def criar_tabela_pedido_itens(cursor):
    comando = """
        CREATE TABLE IF NOT EXISTS tb_pedidos_itens(
            pedido_id INTEGER NOT NULL,
            produto_id INTEGER NOT NULL,
            quantidade INTEGER NOT NULL,
            PRIMARY KEY (pedido_id, produto_id),
            FOREIGN KEY (pedido_id) REFERENCES tb_pedidos(id),
            FOREIGN KEY (produto_id) REFERENCES tb_produtos(id)
        );
    """
    cursor.execute(comando)
    print("Tabela tb_pedidos_itens criada com sucesso.")


# Função que mostra os dados da tabela tb_pedidos
def mostrar_tb_produtos(cursor):
    comando = """
    SELECT * FROM tb_produtos;
    """
    resultado = cursor.execute(comando)
    tb_produtos = resultado.fetchall()
    return tb_produtos


# Função que insire dados em tb_produtos
def inserir_tb_produtos(cursor):

    for produto in produtos:
        nome = produto.get("nome")
        preco = produto.get("preco")
        comando = f"INSERT INTO tb_produtos(nome, preco) VALUES ('{nome}', '{preco}')"
        cursor.execute(comando)    
        print(f"O produto {nome} foi inserido com sucesso.")

if __name__ == "__main__":
    
    conexao  = sqlite3.connect("db_2.sqlite3")
    cursor = conexao.cursor()
    cursor.execute("PRAGMA foreign_key = ON;")

    #criar_tabela_produto(cursor)
    #criar_tabela_pedidos(cursor)
    #criar_tabela_pedido_itens(cursor)

    #inserir_tb_produtos(cursor)
    #conexao.commit()
    #excluir_tabelas(cursor)

    saida = """
    Sistema de Pedidos. Escolha a sua opção
    1 - Cadastrar novo pedido
    2 - Visualizar os Pedidos
    3 - Sair
    """

    while True:

        print(saida)
        
        try: 
            opcao = int(input("Opção: "))
            if opcao == 1:
                mostrar_tb_produtos(cursor)
                # Para cadastrar um novo pedido, é interessante mostrar a lista de produtos disponíveis
                # Também colocar uma validação que verifica se o ID do produto existe

                # Quando um pedido for finalizado, devemos salvar os dados em 2 tabelas:
                # tb_pedidos, tb_pedidos_itens

                # Quando o registro for inserido na tb_pedidos, vamos pegar o ID desse registro, que
                # é feito pegando o atributo lastrowid do objeto cursor 'r' gerado (r = cursor.execute(comand))

                # Após isso, vamos salvar na tabela tb_pedidos_itens esse id do pedido, e os ids dos produtos
                # escolhidos pelo usuário

                
                

            elif opcao == 2:
                # Será mostrada a lista de pedidos, contendo:
                # ID do Pedido
                # Os produtos que fazem parte desse pedido
                # O total do pedido
                pass

            elif opcao == 3:
                break

            else:
                print("A opção não foi encontrada, informe novamente.")

        except ValueError:
            print("Você deve informar uma opção válida")