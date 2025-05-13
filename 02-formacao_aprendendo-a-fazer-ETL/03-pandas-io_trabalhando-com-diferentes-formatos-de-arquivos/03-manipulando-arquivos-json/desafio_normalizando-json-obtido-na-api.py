# Enunciado do desafio:
'''
Chegou a hora de testar os conhecimentos desenvolvidos durante a aula.

O DataFrame mostrado abaixo foi gerado após a obtenção de dados da API JSONPlaceholder:
[Dataframe]

Este DataFrame possui 8 colunas: id, name (nome), username (nome de usuário), email , address (endereço), phone(telefone), website e company (empresa). Note que as colunas address e company contém informações aninhadas, ou seja, os dados dessas colunas estão organizados em subcampos. Por exemplo, na coluna address, você encontrará subcampos como street (rua), suite (complemento), city (cidade) e zipcode (CEP). Já na coluna company, os subcampos incluem name (nome da empresa), catchPhrase (slogan) e bs (área de atuação). Isso significa que, para acessar essas informações, é necessário realizar o processo de normalização.

O desafio agora é normalizar esse DataFrame, expandindo as colunas address e company em suas respectivas subcolunas para facilitar a visualização e a análise dos dados.

Se você tiver dúvidas sobre como resolver, consulte a opinião da pessoa instrutora!
'''

# Imports
import requests
import json
import pandas as pd

# Load data
data_users = requests.get('https://jsonplaceholder.typicode.com/users')
result = json.loads(data_users.text)
normalized_data = pd.json_normalize(result)
normalized_data