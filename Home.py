import pandas as pd
import numpy as np
import plotly.express as px 
import streamlit as st 
st.title('Fifa :red[Data]')
st.image('https://media.gettyimages.com/id/129728336/photo/fifa-executive-committee-meeting.jpg?s=612x612&w=gi&k=20&c=WIyupDvn6pVqZQmFhnRMRg2Y3YzXKODyGU0RZtDz4ZI=', caption='Football Fifa')
st.markdown('''* Fédération Internationale de Football Association: the international governing body of association football.''')
st.markdown ('''*  211 men's national football teams affiliated to FIFA, through their national football associations.''')
st.markdown('''* Here is the source of data! ''')
st.write("check out [Kaggle](https://www.kaggle.com/datasets/bryanb/fifa-player-stats-database)")
df = pd.read_csv(r"c:\Users\ooo\Downloads\Project 12_FIFA EDA\fifa_eda.csv")
df.dropna(inplace = True)
selection = st.selectbox('select a field ', ['ID', 'Name', 'Age', 'Nationality', 'Overall', 'Potential', 'Club',
       'Value', 'Wage', 'Preferred Foot', 'International Reputation',
       'Skill Moves', 'Position', 'Joined', 'Contract Valid Until', 'Height',
       'Weight', 'Release Clause'])
mydf = df.nlargest(10 , selection)[['Name','Club',selection]]
st.plotly_chart(px.bar(mydf, x='Name', y = selection ,title = (f'Top 10 {selection}')))
max_value = df[selection].max()
min_value = df[selection].min()
Avg_value = df[selection].mean()
c1,c2,c3 = st.columns(3)
with c1:
   cont1 =  st.container(border=3)
   cont1.metric(label = f'max {selection}', value = max_value)
with c2:
   cont2 =  st.container(border=3)
   cont2.metric(label = f'min {selection}', value = min_value)
with c3:
   cont3 =  st.container(border=3)
   cont3.metric(label = f'mean {selection}', value = round(Avg_value , 2))
   st.write('')
st.dataframe(mydf)
