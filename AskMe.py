import random2

def random_answer(question):
    respostas = [
        "Sim, definitivamente.",
        "Não, de jeito nenhum.",
        "Pode ser.",
        "Não tenho certeza, tente novamente.",
        "Provavelmente não.",
        "Sim, parece uma boa ideia.",
        "Não conte com isso.",
        "Concentre-se em outra coisa.",
    ]

    # Obtemos uma resposta aleatória da lista
    resposta_aleatoria = random2.choice(respostas)

    return resposta_aleatoria

# Exemplo de uso
user_question = input("Faça-me uma pergunta: ")
resposta = random_answer(user_question)
print("Resposta:", resposta)
