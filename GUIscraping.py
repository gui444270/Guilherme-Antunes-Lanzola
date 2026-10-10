import requests as r
from bs4 import BeautifulSoup

print("Aula de Scraping/Crsawlig")

try:
    resultado = r.get("https://uol.com./start/esport")
except:
    print("Erro: pagina indisponivel")
else:
    resposta = resultado.text
    soup = BeautifulSoup(resposta, 'html.parser')

    print(soup.title.string)

    lista = ["Pokemon","Neymar"]

    for paragrafo in soup.find_all('body'):
        for palavra in lista:
            for paragrafo_str in paragrafo.stripped_strings:
                if palavra.upper() in str(paragrafo_str).upper():
                    print(f"NOTICIA: {paragrafo_str}")