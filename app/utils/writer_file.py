import pandas as pd


def write_csv(file_name, data_list):
    df = pd.DataFrame(data_list)
    df.to_csv("./eventos_mais_vistos_24h_RJ/" + file_name, index=False)
