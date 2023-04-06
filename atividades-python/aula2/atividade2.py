print("Serão entrevistadas 4 pessoas.")

dicionário = {
}

for i in range(1):
    for j in range(1):
        nomePrimeiro = input("Digite o seu nome:")
        dicionário["Nome 1"] = nomePrimeiro;
        perguntaPrimeiro = input("Você já teve dengue?")
        dicionário["Já teve dengue - paciente 1"] = perguntaPrimeiro;
for i in range(1):
    for j in range(1):
        nomeSegundo = input("Digite o seu nome:")
        dicionário["Nome 2"] = nomeSegundo;
        perguntaSegundo = input("Você já teve dengue?")
        dicionário["Já teve dengue - paciente 2"] = perguntaSegundo;
for i in range(1):
    for j in range(1):
        nomeTerceiro = input("Digite o seu nome:")
        dicionário["Nome 3"] = nomeTerceiro;
        perguntaTerceiro = input("Você já teve dengue?")
        dicionário["Já teve dengue - paciente 3"] = perguntaTerceiro;
for i in range(1):
    for j in range(1):
        nomeQuarto = input("Digite o seu nome:")
        dicionário["Nome 4"] = nomeQuarto;
        perguntaQuarto = input("Você já teve dengue?")
        dicionário["Já teve dengue - paciente 4"] = perguntaQuarto;
print(dicionário)