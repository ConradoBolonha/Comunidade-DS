### BIBLIOTECAS ###
import pandas as pd
import plotly.express as pl

df = pd.read_csv('D:\Comunidade-DS/train.csv')

### LIMPANDO CÉLULAS "NaN" ###
linhas_selecionadas = (df['Delivery_person_Age'] != 'NaN ') 
df = df.loc[linhas_selecionadas, :].copy()

linhas_selecionadas = (df['Road_traffic_density'] != 'NaN ') 
df = df.loc[linhas_selecionadas, :].copy()

linhas_selecionadas = (df['City'] != 'NaN ') 
df = df.loc[linhas_selecionadas, :].copy()

linhas_selecionadas = (df['Festival'] != 'NaN ') 
df = df.loc[linhas_selecionadas, :].copy()

### CONVERTENDO A COLUNA "Delivery_person_Age" PARA NÚMERO INTEIRO (int) ###
df['Delivery_person_Age'] = df['Delivery_person_Age'].astype( int )

### CONVERTENDO A COLUNA "Delivery_person_Ratings" PARA NÚMERO DECIMAL (float) ###
df['Delivery_person_Ratings'] = df['Delivery_person_Ratings'].astype( float )

### CONVERTENDO A COLUNA "Order_Date" PARA FORMATO DE DATA ###
df['Order_Date'] = pd.to_datetime( df['Order_Date'], format='%d-%m-%Y' )

### CONVERTENDO A COLUNA "multiple_deliveries" DE TEXTO PARA NÚMERO INTEIRO (int) ###
linhas_selecionadas = (df['multiple_deliveries'] != 'NaN ')
df = df.loc[linhas_selecionadas, :].copy()
df['multiple_deliveries'] = df['multiple_deliveries'].astype( int )

### REMOVENDO ESPAÇOS NAS COLUNAS ###
df.loc[:, 'ID'] = df.loc[:, 'ID'].str.strip()
df.loc[:, 'Road_traffic_density'] = df.loc[:, 'Road_traffic_density'].str.strip()
df.loc[:, 'Type_of_order'] = df.loc[:, 'Type_of_order'].str.strip()
df.loc[:, 'Type_of_vehicle'] = df.loc[:, 'Type_of_vehicle'].str.strip()
df.loc[:, 'City'] = df.loc[:, 'City'].str.strip()
df.loc[:, 'Festival'] = df.loc[:, 'Festival'].str.strip()

### LIMPANDO A COLUNA TIME TAKEN ###
df['Time_taken(min)'] = df['Time_taken(min)'].apply( lambda x: x.split( '(min) ')[1] )
df['Time_taken(min)']  = df['Time_taken(min)'].astype( int )

### SELECIONANDO AS COLUNAS ###
col = df.loc[:, ['ID', 'Order_Date']].groupby('Order_Date').count().reset_index()

### GERANDO O GRÁFICO ###
pl.bar(col, x='Order_Date', y='ID' )
