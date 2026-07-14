from tkinter import *
import requests
import json

#Varia for test
o = 0


#Function--
#Get from API
def valores_bolsa():
    try:
        url = "https://brapi.dev/api/v2/stocks/quote?symbols=PETR4,VALE3,ITUB4"
        response = requests.get(url)
        bolsa = response.json()
        dados_pet4 = bolsa['results'][0]['data'] 

        vale3 = bolsa['results'][1]['data']['regularMarketPrice']
        itub4 = bolsa['results'][2]['data']['regularMarketPrice'] 
  
        pet4 = [
            dados_pet4["regularMarketPrice"],
            dados_pet4["regularMarketDayHigh"],
            dados_pet4["regularMarketDayLow"],
            dados_pet4["currency"]
        ]

        with open("dados_api.text",mode="w",errors="replace",encoding="utf-8") as arquivo:
            json_bolsa = json.dump(dados_pet4,arquivo,indent=2,ensure_ascii=False)
            arquivo.write("\n JSON OF STOCK MARKET \n ")
    
    except ConnectionError:
        print("Lost internet")

    except ValueError as error:
        print(f'Missing value {error}')
    print('api')

#Refresh API
def atualizar_api():
    print("Refresh")
    o = 3
    text1.config(text=f"sela {o}")
    valores_bolsa()


#Tkinter and cod
#Tkinter Core --
janela = Tk()
janela.title("Bolsa de valores")
janela.geometry("1000x300")

#Tkinter body
bt = Button(janela,text="Atualizar",command=atualizar_api,bg="purple",cursor='hand2')
bt.grid()

text1 = Label(janela,text=f"seila {o}")
text1.grid()


#Tkinter end
janela.mainloop()