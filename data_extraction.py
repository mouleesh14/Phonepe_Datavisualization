import os  # It is used to read a content from the files
import pandas as pd  # Used to create an DataFrame
import json  # To read and access the json files
from sqlalchemy import create_engine  # Used to transfer the dataframe to my MYSQL

# Extracting aggregated transaction datas from the local system and converting into a dataframe and store it in MYSQL workbech 
def agg_trans():
    path1_agg_trans="D:/Python/pulse/data/aggregated/transaction/country/india/state/"   
    states=os.listdir(path1_agg_trans)
    path_1={'State':[], 'Year':[],'Quater':[],'Transacion_type':[], 'Transacion_count':[], 'Transacion_amount':[]}
    for i in states:
        state_path=path1_agg_trans+i+'/'
        state_years=os.listdir(state_path)
        for j in state_years:
            year_path=state_path+j+'/'
            year_details=os.listdir(year_path)
            for k in year_details:
                data_path=year_path+k
                datas=open(data_path,'r')
                data=json.load(datas)
                for z in data['data']['transactionData']:
                    path_1['State'].append(i)
                    path_1['Year'].append(j)
                    path_1['Quater'].append(int(k.strip('.json')))
                    path_1['Transacion_type'].append(z['name'])
                    path_1['Transacion_count'].append(z['paymentInstruments'][0]['count'])
                    path_1['Transacion_amount'].append(z['paymentInstruments'][0]['amount'])
                datas.close()
    df=pd.DataFrame(data=path_1)
    host = "localhost"
    user = "root"
    password = "Moulee009"
    database = "phonepe"
    engine = create_engine(f"mysql+mysqlconnector://{user}:{password}@{host}/{database}")
    df.to_sql(name='Agg_Trans', con=engine, if_exists='replace', index=False)
    
# Extracting aggregated user datas from the local system and converting into a dataframe and store it in MYSQL workbech
def agg_user():
    path2_agg_user="D:/Python/pulse/data/aggregated/user/country/india/state/"
    states=os.listdir(path2_agg_user)
    path_2={'State':[], 'Year':[],'Quater':[],'Brand_name':[],'Brand_count':[],'Brand_amount':[]}
    for i in states:
        state_path=path2_agg_user+i+'/'
        state_years=os.listdir(state_path)
        for j in state_years:
            year_path=state_path+j+'/'
            year_details=os.listdir(year_path)
            for k in year_details:
                data_path=year_path+k
                datas=open(data_path,'r')
                try:
                    data=json.load(datas)
                    for z in data['data']['usersByDevice']:
                        path_2['State'].append(i)
                        path_2['Year'].append(j)
                        path_2['Quater'].append(int(k.strip('.json')))
                        path_2['Brand_name'].append(z['brand'])
                        path_2['Brand_count'].append(z['count'])
                        path_2['Brand_amount'].append(z['percentage'])
                except:
                    pass
                datas.close()
    df=pd.DataFrame(data=path_2)
    host = "localhost"
    user = "root"
    password = "Moulee009"
    database = "phonepe"
    engine = create_engine(f"mysql+mysqlconnector://{user}:{password}@{host}/{database}")
    df.to_sql(name='agg_user', con=engine, if_exists='replace', index=False)
    
# Extracting map transaction datas from the local system and converting into a dataframe and store it in MYSQL workbech
def map_trans():
    path3_map_trans="D:/Python/pulse/data/map/transaction/hover/country/india/state/"
    states=os.listdir(path3_map_trans)
    path_3={'State':[], 'Year':[],'Quater':[],'District_name':[],'Count':[],'Amount':[]}
    for i in states:
        state_path=path3_map_trans+i+'/'
        state_years=os.listdir(state_path)
        for j in state_years:
            year_path=state_path+j+'/'
            year_details=os.listdir(year_path)
            for k in year_details:
                data_path=year_path+k
                datas=open(data_path,'r')
                try:
                    data=json.load(datas)
                    for z in data['data']['hoverDataList']:
                        path_3['State'].append(i)
                        path_3['Year'].append(j)
                        path_3['Quater'].append(int(k.strip('.json')))
                        path_3['District_name'].append(z['name'])
                        path_3['Count'].append(z['metric'][0]['count'])
                        path_3['Amount'].append(z['metric'][0]['amount'])
                except:
                    pass
                datas.close()
    df=pd.DataFrame(data=path_3)
    host = "localhost"
    user = "root"
    password = "Moulee009"
    database = "phonepe"
    engine = create_engine(f"mysql+mysqlconnector://{user}:{password}@{host}/{database}")
    df.to_sql(name='Map_Trans', con=engine, if_exists='replace', index=False)
    
# Extracting map user datas from the local system and converting into a dataframe and store it in MYSQL workbech
def map_user():
    path4_map_user="D:/Python/pulse/data/map/user/hover/country/india/state/"
    states=os.listdir(path4_map_user)
    path_4={'State':[], 'Year':[],'Quater':[],'District_name':[],'Registred_user':[],"AppOpens":[]}
    for i in states:
        state_path=path4_map_user+i+'/'
        state_years=os.listdir(state_path)
        for j in state_years:
            year_path=state_path+j+'/'
            year_details=os.listdir(year_path)
            for k in year_details:
                data_path=year_path+k
                datas=open(data_path,'r')
                try:
                    data=json.load(datas)
                    for z in data['data']['hoverData']:
                        path_4['State'].append(i)
                        path_4['Year'].append(j)
                        path_4['Quater'].append(int(k.strip('.json')))
                        path_4['District_name'].append(z)
                        user=data['data']['hoverData'][z]['registeredUsers']
                        ope=data['data']['hoverData'][z]['appOpens']
                        path_4['Registred_user'].append(user)
                        path_4['AppOpens'].append(ope)
                except:
                    pass
                datas.close()
    df=pd.DataFrame(data=path_4)
    host = "localhost"
    user = "root"
    password = "Moulee009"
    database = "phonepe"
    engine = create_engine(f"mysql+mysqlconnector://{user}:{password}@{host}/{database}")
    df.to_sql(name='Map_users', con=engine, if_exists='replace', index=False)
    
# Extracting top transaction datas from the local system and converting into a dataframe and store it in MYSQL workbech
def top_trans():
    path5_top_trans="D:/Python/pulse/data/top/transaction/country/india/state/"
    states=os.listdir(path5_top_trans)
    path_5={'State':[], 'Year':[],'Quater':[],'District_name':[],'Count':[],'Amount':[]}
    for i in states:
        state_path=path5_top_trans+i+'/'
        state_years=os.listdir(state_path)
        for j in state_years:
            year_path=state_path+j+'/'
            year_details=os.listdir(year_path)
            for k in year_details:
                data_path=year_path+k
                datas=open(data_path,'r')
                try:
                    data=json.load(datas)
                    for z in data['data']['districts']:
                        path_5['State'].append(i)
                        path_5['Year'].append(j)
                        path_5['Quater'].append(int(k.strip('.json')))
                        path_5['District_name'].append(z['entityName'])
                        path_5['Count'].append(z['metric']['count'])
                        path_5['Amount'].append(z['metric']['amount'])
                except:
                    pass
                datas.close()
    df=pd.DataFrame(data=path_5)
    host = "localhost"
    user = "root"
    password = "Moulee009"
    database = "phonepe"
    engine = create_engine(f"mysql+mysqlconnector://{user}:{password}@{host}/{database}")
    df.to_sql(name='Top_Trans', con=engine, if_exists='replace', index=False)

# Extracting top user datas from the local system and converting into a dataframe and store it in MYSQL workbech
def top_user():
    path6_top_user="D:/Python/pulse/data/top/user/country/india/state/"
    states=os.listdir(path6_top_user)
    path_6={'State':[], 'Year':[],'Quater':[],'District_name':[],'Registered_Users':[]}
    for i in states:
        state_path=path6_top_user+i+'/'
        state_years=os.listdir(state_path)
        for j in state_years:
            year_path=state_path+j+'/'
            year_details=os.listdir(year_path)
            for k in year_details:
                data_path=year_path+k
                datas=open(data_path,'r')
                try:
                    data=json.load(datas)
                    for z in data['data']['districts']:
                        path_6['State'].append(i)
                        path_6['Year'].append(j)
                        path_6['Quater'].append(int(k.strip('.json')))
                        path_6['District_name'].append(z['name'])
                        path_6['Registered_Users'].append(z['registeredUsers'])
                except:
                    pass
                datas.close()
                
    df=pd.DataFrame(data=path_6)
    host = "localhost"
    user = "root"
    password = "Moulee009"
    database = "phonepe"
    engine = create_engine(f"mysql+mysqlconnector://{user}:{password}@{host}/{database}")
    df.to_sql(name='Top_User', con=engine, if_exists='replace', index=False)
    
def main():
    agg_trans()
    agg_user()
    map_trans()
    map_user()
    top_trans()
    top_user()
    
main()
