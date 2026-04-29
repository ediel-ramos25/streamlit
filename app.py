import streamlit as st 
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt


####################
## ajustar el layout
#################### 

st.set_page_config(layout="wide")


##################
## tamaño del plot
################## 

fig, ax = plt.subplots()


#########
## titulo
######### 

st.title("Esta es mi primer app...")


##############################################
## esto es para que salga una linea horizontal
############################################## 

st.divider()

#################
## datos de covid 
################# 

df_covid = pd.read_csv("https://raw.githubusercontent.com/elioramosweb/archivo_datos/main/datos_diarios-2022-03-22_10_20_15.csv",parse_dates=['date'])

st.write(df_covid.head())
st.write(df_covid.tail())

df_covid["date"]= pd.to_datetime(df_covid["date"])

nombres = list(df_covid.columns)[1:]

columna = st.sidebar.selectbox("Columna de interés",nombres)

st.write(df_covid.columns)

#df_covid.plot(x="date",y="tests_rate",ax=ax)

test_rate_rolling = df_covid[columna].rolling(window=7,center=True).mean()

df_covid[columna] = test_rate_rolling

st.sidebar.write("Barra izquierda")

col1, col2 = st.columns(2)

df_covid.plot(x="date",y="tests_rate",ax=ax,ylabel="tasa-positividad",linewidth=3,linestyle="dotted")
df_covid.plot(x="date",y="test_rate_rolling",ax=ax)

col1.pyplot(fig)
col2.write(df_covid.head())