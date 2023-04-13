from twilio.rest import Client
import chaves
from random import choice 

def gerador_de_mensagem(nome_produto, quantidade, valor):
    lista_mensagem = [ f"O feirante ficou maluco!!!{nome_produto} está apenas por R${valor}, e restam {quantidade} quantidades",
                       f"Promoção!!!! {nome_produto} está apenas por R${valor}. Corre, restam apenas {quantidade} unidades", 
                      f"{nome_produto} está apenas por R${valor} corre que é só hoje!!!"]

    return choice(lista_mensagem)


def mensagem_sms(texto, num_para_envio='+5511944227457'):

    client = Client(chaves.account_sid, chaves.auth_token)

    message = client.messages.create(
        body = texto,
        from_=chaves.twilio_number,
        to=num_para_envio
    )

    print(message.body)


