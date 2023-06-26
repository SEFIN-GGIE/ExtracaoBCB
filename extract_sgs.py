from bcb import sgs
import pandas as pd
import json
from src.google_cloud_handler import GoogleCloudHandler

dicio = json.load(open('src/dict/dicionario_variaveis_ibc.json', 'r'))

sazonal = [24364, 25380, 25382, 25384, 25389, 25391, 25394, 25395, 25397, 25399,
25403, 25404, 25405, 25407, 25410, 25412, 25413, 25416, 25418]

nao_sazonal = [24363, 25379, 25381, 25383, 25388, 25390, 25392, 25393, 25396, 25398,
25400, 25401, 25402, 25406, 25408, 25409, 25411, 25415, 25417]

def get_series(ids, start=None, end=None, multi=False):
    series = sgs.get(ids, start=start, end=end, multi=multi)
    return series

df = get_series(nao_sazonal + sazonal, multi=True)
df.reset_index(inplace=True)
df.rename(columns=dicio, inplace=True)
df.to_csv('processed/series_ibc.csv', index=False, sep=',')

handler = GoogleCloudHandler('src/gtoken/projeto-sql-318413-eb7bf8727b63.json')
handler.upload_file_to_drive_folder('processed/series_ibc.csv', '174hNn8vFw7WwwgKqcCFUIHbMsr13v-mz')
