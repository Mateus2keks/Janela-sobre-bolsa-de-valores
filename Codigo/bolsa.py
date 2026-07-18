# Importaçao das bibliotecas
import os
import sys
import json
import requests
from PIL import Image, ImageTk
import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# Variaveis
x = "XXXX"

# --- PROCURAR E USAR FOTOS ---
def caminho_arquivo(arquivos):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, arquivos)
    pasta_atual = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(pasta_atual, arquivos)


# Function--
# Get from API
def valores_bolsa():
    try:
        # Puxa os dados da API e transformar em .JSON
        url = "https://brapi.dev/api/v2/stocks/quote?symbols=PETR4,VALE3,ITUB4"
        response = requests.get(url)
        bolsa = response.json()
        
        # --- PUXA OS DADOS DA API ---
        dados_petr4 = bolsa['results'][0]['data']
        dados_vale3 = bolsa['results'][1]['data']
        dados_itub4 = bolsa['results'][2]['data']

        # Usando os dados das bolsas PETR(petrobras) VALE(vale) ITUB(itau)
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
        # Junta todas as acoes e seus valores
        todas_acoes = [petr4, itub4, vale3]

        # Muda o valor na janela para os valores atuais
        petr4_texto.configure(text=f"VALOR PETROBRAS \n Moeda {petr4[4]}\n Valor atual {petr4[0]}\n Alta do dia {petr4[1]}\n Baixa do dia {petr4[2]}\n Mudança em % {petr4[3]:.3f}")
        itub4_texto.configure(text=f"VALOR ITAU \n Moeda {itub4[4]}\n Valor atual {itub4[0]}\n Alta do dia {itub4[1]}\n Baixa do dia {itub4[2]}\n Mudança em % {itub4[3]:.3f}")
        vale3_texto.configure(text=f"VALOR VALE \n Moeda {vale3[4]}\n Valor atual {vale3[0]}\n Alta do dia {vale3[1]}\n Baixa do dia {vale3[2]}\n Mudança em % {vale3[3]:.3f}")

        # Salva os dados da cotaçao atual em um json
        with open(caminho_arquivo("dados_api.text"), mode="w", errors="replace", encoding="utf-8") as arquivo:
            json.dump(todas_acoes, arquivo, indent=2, ensure_ascii=False)

    # --- CASO CAIA A NET ---
    except requests.exceptions.ConnectionError:
        print("Lost internet")
    # --- CASO A API MUDE A URL ---
    except (ValueError, KeyError) as error:
        print(f'Missing or invalid value {error}')
        
    # Atualizar automaticamente
    janela.after(10000, valores_bolsa)
    # Reajustar a janela pra caber os itens
    janela.geometry(None)
    janela.update_idletasks()


# Tkinter 
# Tkinter Core --
janela = ctk.CTk()
janela.title("Bolsa de valores")

#Abre e usa a imagem como icone
icone_nativo = ImageTk.PhotoImage(Image.open(caminho_arquivo('pixil.png')))
janela.wm_iconphoto(True, icone_nativo)

# Abre as imagems para transforma em icones
petr4_img = Image.open(caminho_arquivo("petr4.png"))
itub4_img = Image.open(caminho_arquivo("itub4.png"))
vale3_img = Image.open(caminho_arquivo("vale3.png"))


# Tkinter body
# Coluna 0 - Botao para Atualizar e Receber os valores da API
atualizar = ctk.CTkButton(janela, text="Atualizar", command=valores_bolsa, fg_color="purple", cursor='hand2')
atualizar.grid(column=0, row=0, padx=(10, 15), pady=10)

read = ctk.CTkLabel(janela, text="Clique no botao para atualizar \n E receber novos dados da API")
read.grid(column=0, row=1, padx=(10, 15), pady=10)
# ---

# Cria uma barreira para dividir as configuraçoes e os valores
barreira = ctk.CTkFrame(janela, fg_color="purple", width=20)
barreira.place(relheight=1.0, x=195)
# ---

# Coluna 2 
# ---
fundo_petr4 = ctk.CTkFrame(janela, fg_color="green")
fundo_petr4.grid(column=2, row=0, rowspan=7, sticky="nsew", padx=5, pady=5)

# INFO das açao PETROBRAS
petr4_texto = ctk.CTkLabel(fundo_petr4, font=("Arial", 15, "bold"), text=f"VALOR PETROBRAS \n Moeda {x}\n Valor atual {x}\n Alta do dia {x}\n Baixa do dia {x}\n Mudança em % {x}", fg_color="#0A521A", text_color="white")
petr4_texto.grid(column=2, row=0, padx=(10, 10), pady=10)

# Manipular a imagem para exibir ela
foto_petr4 = ctk.CTkImage(light_image=petr4_img, dark_image=petr4_img, size=(50, 50))

# Exibir a imagem
mostrarimg_petr4 = ctk.CTkLabel(fundo_petr4, text="", image=foto_petr4)
mostrarimg_petr4.grid(column=2, row=1, pady=5)
# -----

# coluna 3 
# ---
fundo_vale3 = ctk.CTkFrame(janela, fg_color="#dade7c")
fundo_vale3.grid(column=3, row=0, rowspan=7, sticky="nsew", padx=5, pady=5)
# INFO das açoes VALE
vale3_texto = ctk.CTkLabel(fundo_vale3, font=("Arial", 15, "bold"), text=f"VALOR VALE \n Moeda {x}\n Valor atual {x}\n Alta do dia {x}\n Baixa do dia {x}\n Mudança em % {x}", fg_color="#075e4e", text_color="white")
vale3_texto.grid(column=3, row=0, padx=(10, 10), pady=10)

# Manipular a imagem para exibir ela
foto_vale3 = ctk.CTkImage(light_image=vale3_img, dark_image=vale3_img, size=(50, 50))

# Exibir a imagem
mostrarimg_vale3 = ctk.CTkLabel(fundo_vale3, text="", image=foto_vale3)
mostrarimg_vale3.grid(column=3, row=1, pady=5)
# -----

# Coluna 4 
fundo_itub4 = ctk.CTkFrame(janela, fg_color="blue")
fundo_itub4.grid(column=4, row=0, rowspan=7, sticky="nsew", padx=5, pady=5)
# ---
# INFO das açoes ITAU
itub4_texto = ctk.CTkLabel(fundo_itub4, font=("Arial", 15, "bold"), text=f"VALOR ITAU \n Moeda {x}\n Valor atual {x}\n Alta do dia {x}\n Baixa do dia {x}\n Mudança em % {x}", fg_color="#030f22", text_color="white")
itub4_texto.grid(column=4, row=0, padx=(10, 10), pady=10)

# Manipular a imagem para exibir ela
foto_itub4 = ctk.CTkImage(light_image=itub4_img, dark_image=itub4_img, size=(50, 50))

# Exibir a imagem
mostrarimg_itub4 = ctk.CTkLabel(fundo_itub4, text="", image=foto_itub4)
mostrarimg_itub4.grid(column=4, row=1, pady=5)
# -----

# Tkinter end
janela.mainloop()
