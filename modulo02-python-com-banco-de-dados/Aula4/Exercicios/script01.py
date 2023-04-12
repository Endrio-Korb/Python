import sqlite3

def criar_tb_pedidos(cursor):
    comando = """
    CREATE TABLE IF NOT EXISTS tb_pedidos(
        pedido_id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome_cliente TEXT NOT NULL,
        produto TEXT NOT NULL,
        quantidade INTEGER NOT NULL
    );
    """
    cursor.execute(comando)

# Inserir na tabela tb_pedidos
def inserir_tb_pedidos(cursor):
    comando = """
    INSERT INTO tb_pedidos(nome_cliente, produto, quantidade) VALUES
    ('João Silva', 'Camisa', 2),
    ('Jane Smith', 'Adesivo' , 3),
    ('Sara Correa', 'Cafeteira',1)
    """
    cursor.execute(comando)
    conexao.commit()

# Mostrar tabela tb_pedidos
def mostrar_tb_pedidos(cursor):
    comando = """
    SELECT * FROM tb_pedidos;
    """
    cursor.execute(comando)
    resultado = cursor.fetchall()
    for item in resultado:
        print(item)


if __name__ == "__main__":

    conexao = sqlite3.connect("pedidos.sqlite3")
    cursor = conexao.cursor()
    cursor.execute("PRAGMA foreign_key = ON;")

    criar_tb_pedidos(cursor)
    #inserir_tb_pedidos(cursor)
    mostrar_tb_pedidos(cursor)