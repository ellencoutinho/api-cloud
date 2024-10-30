from bs4 import BeautifulSoup
import requests
from datetime import datetime, timedelta, date

def get_info():
    response = requests.get('https://g1.globo.com/previsao-do-tempo/sp/sao-paulo.ghtml')
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        return {
            "data": str((datetime.utcnow() - timedelta(hours=3)).date()),
            "descricao": soup.find(class_='forecast-header__summary').text,
            "temp_maxima": soup.find(class_='forecast-today__temperature forecast-today__temperature--max').text[:-4],
            "temp_minima": soup.find(class_='forecast-today__temperature forecast-today__temperature--min').text[:-4]
        }
    else:
        print(f'Erro ao acessar a página: {response.status_code}')