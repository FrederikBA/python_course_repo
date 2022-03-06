import numpy as np
import pandas as pd

data_set = pd.read_csv("API_EN.ATM.CO2E.KT_DS2_en_csv_v2_1345584.csv", skiprows=4)

new_index_data = data_set.set_index('Country Name')

emission = pd.Series(new_index_data["2014"])

emissions_sorted = emission.nlargest(10)

print(emissions_sorted)
