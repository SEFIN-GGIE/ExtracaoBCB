from google_cloud_handler import GoogleCloudHandler
# df = pd.read_csv('dict/dicionario_variaveis_ibc.csv', sep=';')

# def cria_sigla(df):
#     saz = False
#     if 'sazonal' in df['nome_serie'].lower():
#         saz = True
#     if saz:
#         return df['cod_serie'] + df['Sigla'] + 'Saz'
#     else:
#         return df['cod_serie'] + df['Sigla'] 

# # transforme pares cod_serie e sigla em um dicionario
# dicio = dict(zip(df['cod_serie'], df['sigla']))

# print(dicio)

# with open('dicionario_variaveis_ibc.json', 'w') as arquivo:
#     json.dump(dicio, arquivo)

handler = GoogleCloudHandler('gtoken/projeto-sql-318413-eb7bf8727b63.json')
handler.upload_file_to_drive_folder('teste.txt', '174hNn8vFw7WwwgKqcCFUIHbMsr13v-mz')