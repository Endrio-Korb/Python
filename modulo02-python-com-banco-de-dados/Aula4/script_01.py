import sqlite3

if __name__ == "__main__":
    
    # O banco db.sqlite3 será criado no mesmo diretório onde está o arquivo.
    conexao = sqlite3.connect("db.sqlite3")

    # Criamos o comando em SQL e salvamos em uma variável.
    comando = """
    CREATE TABLE IF NOT EXISTS tb_estados(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        sigla TEXT NOT NULL
    );
    """

    # Criamos um cursor. O cursor é necessário para executar comando no banco de dados, assim como
    # receber os resultados das consultas.
    cur = conexao.cursor()

    # Executa o comando.
    cur.execute(comando)

    estados = {
        "Acre": "AC","Alagoas": "AL","Amapá": "AP","Amazonas": "AM","Bahia": "BA",
        "Ceará": "CE","Distrito Federal": "DF","Espírito Santo": "ES","Goiás": "GO",
        "Maranhão": "MA","Mato Grosso": "MT","Mato Grosso do Sul": "MS","Minas Gerais": "MG",
        "Pará": "PA","Paraíba": "PB","Paraná": "PR","Pernambuco": "PE","Piauí": "PI",
        "Rio de Janeiro": "RJ","Rio Grande do Norte": "RN","Rio Grande do Sul": "RS",
        "Rondônia": "RO","Roraima": "RR","Santa Catarina": "SC","São Paulo": "SP",
        "Sergipe": "SE","Tocantins": "TO"
    }

    # for chave, valor in estados.items():
    #     # Montamos o comando para inserção dos dados na tabela
    #     comando = f"INSERT INTO tb_estados(nome, sigla) VALUES ('{chave}', '{valor}')"
    #     # Executamos o comando
    #     cur.execute(comando)

        #print(f"Registro {valor} inserido com sucesso!")
    
    # Para inserir os dados na tabela além de executar os comando INSERT precisamos confirmar a transação
    # utilizando o métado "commit" do objeto de conexão.
    conexao.commit()

    # Listando os dados que foram cadastrados
    comando = "SELECT * FROM tb_estados"
    resultado = cur.execute(comando)
    estados = resultado.fetchall()

    # É importante notar que quando utilizamos os métodos fetch, a posição do cursor muda de acordo
    # com o método. Ou seja, se consumirmos otodos os registros do objeto cursor, teremos que executar
    # o comando consulta novamente.

    # O método fetchone traz apenas um resultado
    # O método fetchmany(size) trás a quantidade de registro indicados como parâmetros size, por exemplo
    # fetchmany(10) irá trazer os próximos 10 resultados
    # O método fetchall traz todos os resultados

    # Trazendo novamente os dados
    resultado = cur.execute(comando)

    estados = resultado.fetchall()
    text = "Lista de estados Brasileiros"
    print("Lista de estados Brasileiros".center(40))
    for estado in estados:
        saida = f"""
        Estado: {estado [1]}
        Sigla: {estado[2]}
        """
        print(saida)


    # Ultimos comando a serem executados
    #Remove a tabela tb_estados
    comando = "DROP TABLE tb_estados"
    #cur.execute(comando)
    # Fecha a conexão com o curso
    cur.close()
    # Fecha a conexão com o banco de dados
    conexao.close()