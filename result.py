import pandas as pd

get_info = input() 

fails = pd.read_excel("description.xlsx", sheet_name="LookupAREA") 
info_list = fails.values.tolist()

region_to_code = dict(zip(fails['RegionName'], fails['RegionCode']))

data_df = pd.read_csv("data.csv", encoding='ISO-8859-1')

while True:
    region_code = region_to_code.get(get_info)

    if not region_code:
        print(0)
    else:
        geo_count_sum = data_df[data_df['RegionCode'] == region_code]['geo_count'].sum()

        print(int(geo_count_sum))

    get_info = input("Enter region name (or type 'exit' to quit): ")

    if get_info.lower() == 'exit':
        break

