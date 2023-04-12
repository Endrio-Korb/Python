import sqlite3
import datetime

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
    #print("Tabela tb_produtos criada com sucesso.")


# Função que cria a tabela de pedidos
def criar_tabela_pedidos(cursor):
    comando = """
    CREATE TABLE IF NOT EXISTS tb_pedidos(
        id INTEGER NOT NULL,
        data_hora DATETIME NOT NULL,
        observacoes TEXT,
        PRIMARY KEY (id, data_hora)
    );
    """
    cursor.execute(comando)
    #print("Tabela tb_pedidos criada com sucesso.")



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
    #print("Tabela tb_pedidos_itens criada com sucesso.")


# Função que mostra os dados da tabela tb_pedidos
def mostrar_tb_produtos(cursor):
    comando = """
    SELECT * FROM tb_produtos;
    """
    cursor.execute(comando)
    resultado = cursor.fetchall()
    for item in resultado:
        print(item)


# Função que mostra a tabela tb_pedidos_itens
def mostrar_tb_pedidos_itens(cursor):
    comando = """
    SELECT * FROM tb_pedidos_itens;
    """
    cursor.execute(comando)
    resultado = cursor.fetchall()
    for item in resultado:
        print(item)


# Função que mostra todos os pedidos feitos
def mostrar_pedidos(cursor):
    #TODO Mostrar o id do pedido, todos os itens desse pedido, valor total do pedido
    comando = f"""
    SELECT * FROM tb_pedidos_itens;
    """
    cursor.execute(comando)
    resultado = cursor.fetchall()
    return print(resultado)
    

# Função que insire dados em tb_produtos
def inserir_tb_produtos(cursor):

    for produto in produtos:
        nome = produto.get("nome")
        preco = produto.get("preco")
        comando = f"INSERT INTO tb_produtos(nome, preco) VALUES ('{nome}', '{preco}')"
        cursor.execute(comando)    
        #print(f"O produto {nome} foi inserido com sucesso.")

if __name__ == "__main__":
    
    conexao  = sqlite3.connect("db_2.sqlite3")
    cursor = conexao.cursor()
    cursor.execute("PRAGMA foreign_key = ON;")

    criar_tabela_produto(cursor)
    criar_tabela_pedidos(cursor)
    criar_tabela_pedido_itens(cursor)

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
                # Para cadastrar um novo pedido, é interessante mostrar a lista de produtos disponíveis
                # Também colocar uma validação que verifica se o ID do produto existe
                mostrar_tb_produtos(cursor)
                
                comida = int(input("Qual comida deseja pedir:"))
                quantidade = int(input("Informe a quantidade desejada: "))
                comando = f"""
                SELECT * From tb_produtos WHERE id = {comida};
                """
                cursor.execute(comando)

                # Quando um pedido for finalizado, devemos salvar os dados em 2 tabelas:
                # tb_pedidos, tb_pedidos_itens
                data = datetime.date.today()
                comando = f"""
                INSERT INTO tb_pedidos (id, data_hora) VALUES ({comida}, {data});
                """
                cursor.execute(comando)
                conexao.commit()

                # Quando o registro for inserido na tb_pedidos, vamos pegar o ID desse registro, que
                # é feito pegando o atributo lastrowid do objeto cursor 'r' gerado (r = cursor.execute(comand))
                # Após isso, vamos salvar na tabela tb_pedidos_itens esse id do pedido, e os ids dos produtos
                # escolhidos pelo usuário 
                ultimoId = cursor.lastrowid
                comando = f"""
                INSERT INTO tb_pedidos_itens (pedido_id, produto_id, quantidade) VALUES
                ( {ultimoId}, {comida}, {quantidade})
                """
                cursor.execute(comando)
                conexao.commit()

            elif opcao == 2:
                # Será mostrada a lista de pedidos, contendo:
                # ID do Pedido. Os produtos que fazem parte desse pedido. O total do pedido
                mostrar_pedidos(cursor)
                
                
                

            elif opcao == 3:
                break

            else:
                print("A opção não foi encontrada, informe novamente.")

        except ValueError:
            print("Você deve informar uma opção válida")