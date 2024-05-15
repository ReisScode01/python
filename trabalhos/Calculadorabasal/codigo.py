import sqlite3

def calcular_basal(sexo, idade, peso, altura):
  if sexo == "M":
    tmb = 88.362 + (13.397 * peso) + (4.799 * altura) - (5.677 * idade)
    mensagem = f"Seu TMB é de {tmb:.2f} calorias por dia."
    return mensagem
    
  elif sexo == "F":
    tmb = 447.593 + (9.247 * peso) + (3.098 * altura) - (4.330 * idade)
    mensagem = f"Seu TMB é de {tmb:.2f} calorias por dia."
    return mensagem

  else:
    mensagem = "Sexo inválido"
    return mensagem



while True:
    try:
        sexo = input("Digite seu sexo com M para masculino e F para feminino: ")
        idade = float(input("Digite sua idade: "))
        peso = float(input("Digite seu peso em kg: "))
        altura = float(input("Digite sua altura em metros: "))

        resultado = calcular_basal(sexo, idade, peso, altura)
        if resultado is not None:
            print(resultado)

           
            break
        else:
            print(resultado)
    except ValueError:
        print("Por favor, insira um valor numérico para peso e altura.")
      
    # Conectar ao banco de dados (se não existir, será criado)
conn = sqlite3.connect('dados_usuarios.db')
cursor = conn.cursor()

# Criar uma tabela se não existir
cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios
                  (id INTEGER PRIMARY KEY AUTOINCREMENT, sexo TEXT, idade INT, peso REAL, altura REAL, resultado REAL)''')  
      
      # Inserir os dados do usuário no banco de dados
cursor.execute("INSERT INTO usuarios (sexo, idade, peso, altura, resultado) VALUES (?, ?, ?, ?, ?)", (sexo, idade, peso, altura, resultado))
conn.commit()


# Fechar a conexão com o banco de dados
conn.close()
