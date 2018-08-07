import numpy as np
import pandas as pd

url_bracers = 'https://nierautomata.wiki.fextralife.com/Combat+Bracers'
url_small_swords = 'https://nierautomata.wiki.fextralife.com/Small+Swords'
url_large_swords = 'https://nierautomata.wiki.fextralife.com/Large+Swords'
url_spears = 'https://nierautomata.wiki.fextralife.com/Spears'

bracers = pd.read_html(url_bracers)[0]
s_swords = pd.read_html(url_small_swords)[0]
l_swords = pd.read_html(url_large_swords)[0]
spears = pd.read_html(url_spears)[0]

dataframes = [bracers, s_swords, l_swords, spears]

def save_df(dfs,xls_path):
    writer = pd.ExcelWriter(xls_path)
    for n, df in enumerate(dfs):
        df.to_excel(writer,'sheet%s' % n, index = False)
    writer.save()
    
save_df(dataframes,'Weapon_Data.xlsx')
