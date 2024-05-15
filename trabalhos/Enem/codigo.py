import sqlite3 

# Conectar ao banco de dados (se não existir, será criado)
conn = sqlite3.connect('dados_alunos.db')
cursor = conn.cursor()

# Criar uma tabela se não existir
def criar_tabela_alunos(conexao):
    cursor = conexao.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS alunos (
            id INTEGER PRIMARY KEY,
            Linguagens REAL,
            Humanas REAL,
            Natureza REAL,
            Matemática REAL,
            Redação REAL,
            media REAL,
            status TEXT
        )
    ''')
    conexao.commit()

def salvar_alunos_banco(conexao, notas, media, status):
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO alunos (Linguagens, Humanas, Natureza, Matemática, Redação, media, status) VALUES (?, ?, ?, ?, ?, ?, ?)", (notas[0], notas[1], notas[2], notas[3], notas[4], media, status))
    conexao.commit()

def calcular_media_enem():
    notas = []
    areas_conhecimento = ["Linguagens", "Humanas", "Natureza", "Matemática", "Redação"]

    for area in areas_conhecimento:
        nota = float(input(f"Digite a nota de {area}: "))
        if nota < 0 or nota > 1000:
            print(f"Por favor, insira uma nota válida para {area}")
            return
        notas.append(nota)

    if notas[4] == 0:
        print("A nota da redação não pode ser zero. O aluno está reprovado.")
        return

    media = calcular_media(notas)
    status = "Aprovado" if media >= 450 else "Reprovado"
    mensagem = f"Sua média final no ENEM é: {media:.2f}\nStatus: {status}"

    salvar_alunos_banco(conn, notas, media, status)  # Salvando dados no banco de dados
    print(mensagem)

def calcular_media(notas):
    total = sum(notas)
    return total / len(notas)

# Chamada para criar a tabela de alunos
criar_tabela_alunos(conn)

# Chamada para calcular a média do ENEM e salvar os dados no banco de dados
calcular_media_enem()

# Fechar a conexão com o banco de dados
conn.close()
