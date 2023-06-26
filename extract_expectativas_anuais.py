import pandas as pd
from src.expectativas import extracao_expectativas
from src.google_cloud_handler import GoogleCloudHandler

indicadores = ['IPCA', 'PIB Total', 'PIB Serviços', 'Selic', 'Câmbio']
endpoint = 'ExpectativasMercadoAnuais'

dfs = list()
for indicador in indicadores:
    data_min = '2020-01-01' \
        if indicador in ['Selic', 'Câmbio'] \
        else '2020-01-01'
    df_extracao = extracao_expectativas(indicador, data_min, endpoint)
    dfs.append(df_extracao)

df = pd.concat(dfs)
df.to_csv('processed/expectativas_anuais.csv', sep=';', decimal=",", index=False)

handler = GoogleCloudHandler('src/gtoken/projeto-sql-318413-eb7bf8727b63.json')
handler.upload_file_to_drive_folder('processed/expectativas_anuais.csv', '174hNn8vFw7WwwgKqcCFUIHbMsr13v-mz')