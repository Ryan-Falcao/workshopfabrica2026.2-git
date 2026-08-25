import requests

while True:
    pokemon = input("Pokemon: ")

    resposta = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon}")

    respostaJson = resposta.json()

    print(f"Nome : {respostaJson['name']}")
    print(f"Peso : {respostaJson['weight']/3.28:.2f} Kg")

    
    for tipos in range(len(respostaJson['types'])):
        print(respostaJson['types'][tipos]['type']['name'])

    print("Status do pokemon")

    for status in range(len(respostaJson['stats'])):
        print(respostaJson['stats'][status]['stat']['name'],respostaJson['stats'][status]['base_stat'])

