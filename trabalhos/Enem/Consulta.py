import sqlite3

# Conectar ao banco de dados
conn = sqlite3.connect('dados_alunos.db')
cursor = conn.cursor()

# Executar uma consulta SQL para selecionar todos os registros da tabela usuarios
cursor.execute("SELECT * FROM alunos")

# Recuperar todos os resultados da consulta
resultados = cursor.fetchall()

# Exibir os resultados
for linha in resultados:
    print(linha)

# Fechar a conexão com o banco de dados
conn.close()
