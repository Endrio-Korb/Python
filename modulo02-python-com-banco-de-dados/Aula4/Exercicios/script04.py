import sqlite3


# Criar tabela tipos serviços
def criar_tb_tipos_servicos(cursor):
    comando = """
    CREATE TABLE IF NOT EXISTS tb_tipos_servicos(
        servico_id INTEGER PRIMARY KEY AUTOINCREMENT,
        valor REAL NOT NULL
    );
    """
    cursor.execute(comando)


# Criar tabela de servicos
def criar_tb_servicos(cursor):
    comando = """
    CREATE TABLE IF NOT EXISTS tb_servicos(
    id INTEGER NOT NULL,
    servico_id INTEGER NOT NULL,
    total_horas REAL NOT NULL,
    PRIMARY KEY (id, servico_id, total_horas),
    FOREIGN KEY (servico_id) REFERENCES tb_tipos_servicos(servico_id)
    );
    """
    cursor.execute(comando)


# Inserir tipos de servicos
def inserir_tipos_servicos(cursor):
    comando = """
    INSERT INTO tb_tipos_servicos (servico_id, valor) VALUES
    (0001, 10),
    (0002, 40),
    (0003, 20)
    """
    cursor.execute(comando)
    conexao.commit()


# Inserir servicos
def inserir_tb_servicos(cursor):
    comando = """
    INSERT INTO tb_servicos (id, servico_id, total_horas) VALUES
    (0001, 0001, 40),
    (0002, 0002, 12),
    (0003, 0002, 10),
    (0004, 0003, 20)
    """
    cursor.execute(comando)
    conexao.commit()


# Mostrar servicos
def mostrar_servicos(cursor):
    comando = """
    SELECT ts.servico_id as "ID Serviço", ts.total_horas as "Total de Horas",
    tts.valor as "Valor da Hora", ts.total_horas * tts.valor as "Subtotal"
    FROM tb_servicos ts
    INNER JOIN
    tb_tipos_servicos tts ON ts.servico_id = tts.servico_id;
    """
    cursor.execute(comando)
    resultado = cursor.fetchall()
    for item in resultado:
        print(item)


if __name__ == "__main__":

    conexao = sqlite3.connect("servicos.sqlite3")
    cursor = conexao.cursor()

    comando = "PRAGMA foreign_key = ON;"

    cursor.execute(comando)
    cursor.execute(comando)

    criar_tb_tipos_servicos(cursor)
    criar_tb_servicos(cursor)

    #inserir_tipos_servicos(cursor)
    #inserir_tb_servicos(cursor)

    mostrar_servicos(cursor)