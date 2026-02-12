import pandas as pd 

def ler_panilha(caminho):
    df = pd.read_excel(caminho)
    return df 