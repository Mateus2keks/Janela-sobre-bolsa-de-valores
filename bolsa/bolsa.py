#Importaçao das bibliotecas
from tkinter import * 
from tkinter import ttk
from PIL import ImageTk, Image
import requests
import json



#Function--
#Get from API
def valores_bolsa():
    try:
        #Puxa os dados da API e transformar em .JSON
        url = "https://brapi.dev/api/v2/stocks/quote?symbols=PETR4,VALE3,ITUB4"
        response = requests.get(url)
        bolsa = response.json()
        dados_petr4 = bolsa['results'][0]['data'] 
        dados_itub4 = bolsa['results'][2]['data']
        dados_vale3 = bolsa['results'][1]['data']

        #Usando os dados das bolsas PETR(petrobras) VALE(vale) ITUB(ambev)
        #Oque ele puxa? Valor atual, Valor da alta, Valor da baixa, Quantos % mudou , Tipo de moeda 
        petr4 = [
            dados_petr4["regularMarketPrice"],
            dados_petr4["regularMarketDayHigh"],
            dados_petr4["regularMarketDayLow"],
            dados_petr4["regularMarketChangePercent"],
            dados_petr4["currency"]
        ]
        itub4 = [
            dados_itub4["regularMarketPrice"],
            dados_itub4["regularMarketDayHigh"],
            dados_itub4["regularMarketDayLow"],
            dados_itub4["regularMarketChangePercent"],
            dados_itub4["currency"]
        ]
        vale3 = [
            dados_vale3["regularMarketPrice"],
            dados_vale3["regularMarketDayHigh"],
            dados_vale3["regularMarketDayLow"],
            dados_vale3["regularMarketChangePercent"],
            dados_vale3["currency"]
        ]
        #Junta todas as acoes e seus valores
        todas_acoes = [petr4,itub4,vale3]

        #Muda o valor na janela para os valores atuais
        petr4_texto.config(text=f"VALOR PETROBRAS \n Moeda {petr4[4]}\n Valor atual {petr4[0]}\n Alta do dia {petr4[1]}\n Baixa do dia {petr4[2]}\n Mudança em % {petr4[3]:.3f}")
        itub4_texto.config(text=f"VALOR AMBEV \n Moeda {itub4[4]}\n Valor atual {itub4[0]}\n Alta do dia {itub4[1]}\n Baixa do dia {itub4[2]}\n Mudança em % {itub4[3]:.3f}")
        vale3_texto.config(text=f"VALOR VALE \n Moeda {vale3[4]}\n Valor atual {vale3[0]}\n Alta do dia {vale3[1]}\n Baixa do dia {vale3[2]}\n Mudança em % {vale3[3]:.3f}")

        #Salva em os dados da cotaçao atual em um json
        with open("dados_api.text",mode="w",errors="replace",encoding="utf-8") as arquivo:
            json_bolsa = json.dump(todas_acoes,arquivo,indent=2,ensure_ascii=False)
            arquivo.write("\n JSON OF STOCK MARKET \n ")

    #Caso a API fique offline
    except ConnectionError:
        print("Lost internet")
    #Caso a API mude a url
    except ValueError as error:
        print(f'Missing value {error}')
        
    #Atualizar automaticamente
    janela.after(5000,valores_bolsa)
    #Reajustar a janela pra caber os itens
    janela.geometry("")
    print('api')
    print(petr4)
    #Testa se a Funçao(valores_bolsa) foi chamada e o fim da Funçao(valores_bolsa)


#Tkinter 
#Tkinter Core --
janela = Tk()
janela.title("Bolsa de valores")
janela.geometry("700x300")
icone = PhotoImage(file='pixil.png')
janela.iconphoto(True,icone)

#Abre as imagems para transforma em icones
petr4_img = Image.open("petr4.png")
itub4_img = Image.open("itub4.png")
vale3_img = Image.open("vale3.png")


#Tkinter body
#Coluna 0 - Botao para Atualizar e Receber os valores da API
atualizar = Button(janela,text="Atualizar",command=valores_bolsa,bg="purple",cursor='hand2')
atualizar.grid(column=0,row=0,padx=(0,15))

read = Label(janela,text="Clique no botao para atualizar \n E receber novos dados da API")
read.grid(column=0,row=1,padx=(0,15))
#---

#Cria uma barreira para dividir as configuraçoes e os valores
barreira = Frame(janela,bg="purple",width=20)
barreira.place(relheight=1.0,x=195)
#---

#Coluna 2 
# ---
#INFO das açao PETROBRAS
petr4_texto = Label(janela,text='Atualize')
petr4_texto.grid(column=2,row=0,padx=(40,20))

#Manipular a imagem para exibir ela
petr4_redimensionada = petr4_img.resize((20, 20), Image.Resampling.LANCZOS)
foto_petr4 = ImageTk.PhotoImage(petr4_redimensionada)

#Exibir a imagem
mostrarimg_petr4 = Label(janela,image=foto_petr4)
mostrarimg_petr4.grid(column=2,row=1)
#-----

#coluna 3 
# ---
#INFO das açoes VALE
vale3_texto = Label(janela,text="Atualize")
vale3_texto.grid(column=3,row=0,padx=(20,20))

#Manipular a imagem para exibir ela
vale3_redimensionada = vale3_img.resize((20, 20), Image.Resampling.LANCZOS)
foto_vale3 = ImageTk.PhotoImage(vale3_redimensionada)

#Exibir a imagem
mostrarimg_vale3 = Label(janela,image=foto_vale3)
mostrarimg_vale3.grid(column=3,row=1)
#-----

#Coluna 4 
# ---
#INFO das açoes AMBEV
itub4_texto = Label(janela,text="Atualize")
itub4_texto.grid(column=4,row=0,padx=(20,20))

#Manipular a imagem para exibir ela
itub4_redimensionada = itub4_img.resize((20, 20), Image.Resampling.LANCZOS)
foto_itub4 = ImageTk.PhotoImage(itub4_redimensionada)

#Exibir a imagem
mostrarimg_itub4 = Label(janela,image=foto_itub4)
mostrarimg_itub4.grid(column=4,row=1)
#-----

#Tkinter end
janela.mainloop()