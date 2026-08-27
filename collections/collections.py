

users = {
    "user1 ": {"Nome": "Ryan","Idade":18},
    "user2" : {"Nome": "Eduardo","Idade":18},
    "user3" : {"Nome": "Lucas","Idade":18}
}
historico = {}
operações = 0


def soma(user,n1,n2):
    global operações
    res = n1+n2
    userEscolhido = "UserNãoLogado"

    for i in users:
        if(users[i]["Nome"] == user):
            userEscolhido = users[i]["Nome"]
    operações += 1
    historico[f"operação{operações}"] = {"Nome":userEscolhido, "N1":n1,"N2":n2,"Resposta":res}

    return historico

while True:
    nome = input("Nome:")
    n1 = int(input("Numero:"))
    n2 = int(input("Numero:"))
    print(soma(nome,n1,n2))
    continuar = input("Deseja continuar [s][n]")
    if(continuar == "n"):
        break


