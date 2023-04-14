import sqlite3


# Criar tb_produtos
def criar_tb_produtos(cursor):
    comando = """
    CREATE TABLE IF NOT EXISTS tb_produtos(
        produto_id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NUT NULL,
        valor REAL NOT NULL
    );
    """
    cursor.execute(comando)


# Criar tb_clientes
def criar_tb_clientes(cursor):
    comando = """
    CREATE TABLE IF NOT EXISTS tb_clientes(
        cliente_id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        endereco TEXT NOT NULL,
        cidade TEXT NOT NULL
    );
    """
    cursor.execute(comando)

# Criar tb_pedidos
def criar_tb_pedidos(cursor):
    comando = """
    CREATE TABLE IF NOT EXISTS tb_pedidos (
        pedido_id INTEGER NOT NULL,
        cliente_id INTEGER NOT NULL,
        produto_id INTEGER NOT NULL,
        PRIMARY KEY (pedido_id, cliente_id, produto_id),
        FOREIGN KEY (cliente_id) REFERENCES tb_clientes(cliente_id),
        FOREIGN KEY (produto_id) REFERENCES tb_produtos(produto_id)
    );
    """
    cursor.execute(comando)


# Inserir produtos
def inserir_tb_produtos(cursor):
    comando = """
    INSERT INTO tb_produtos (produto_id, nome, valor) VALUES
    (001, 'Camiseta', 29.99),
    (002, 'Caneca', 12.99),
    (003, 'Adesivo', 1.99)
    """
    cursor.execute(comando)
    conexao.commit()


# Inserir clientes
def inserir_tb_clientes(cursor):
    comando = """
    INSERT INTO tb_clientes (cliente_id, nome, endereco, cidade) VALUES
    (001, 'João Silva', 'Rua das Florse,123', 'São Paulo'),
    (002, 'Ana Santos', 'Av. das Palmeiras, 45', 'Rio de Janeiro')
    """
    cursor.execute(comando)
    conexao.commit()


# Inserir pedidos
def inserir_tb_pedidos(cursor):
    comando = """
    INSERT INTO tb_pedidos (pedido_id, cliente_id, produto_id) VALUES
    (1001, 001, 001),
    (1001, 001, 002),
    (1002, 002, 002),
    (1002, 002, 003);
    """
    cursor.execute(comando)
    conexao.commit()


# Mostrar pedidos
def mostrar_pedidos(cursor):
    comando = """
    SELECT tp.pedido_id as "Código do Pedido",  tc.nome as "Nome do Cliente",
    tc.endereco as "Endereço Cliente", tc.cidade as "Cidade Cliente",
    tp.produto_id as "Código do Produto", tps.valor as "Preço"
    FROM tb_pedidos tp
    INNER JOIN
    tb_clientes tc ON tp.cliente_id = tc.cliente_id,
    tb_produtos tps ON tp.produto_id = tps.produto_id;
    """
    cursor.execute(comando)
    resultado = cursor.fetchall()
    for item in resultado:
        print(item)


if __name__ == "__main__":

    conexao = sqlite3.connect("loja.sqlite3")
    cursor = conexao.cursor()

    comando = """
    PRAGMA foreing_key = ON;
    """
    cursor.execute(comando)

    criar_tb_clientes(cursor)
    criar_tb_produtos(cursor)
    criar_tb_pedidos(cursor)

    #inserir_tb_clientes(cursor)
    #inserir_tb_produtos(cursor)
    #inserir_tb_pedidos(cursor)

    mostrar_pedidos(cursor)