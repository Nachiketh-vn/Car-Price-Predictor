import streamlit as st
import pickle
import pandas as pd

st.title('IPL Win Predictor')

teams=['Sunrisers Hyderabad',
        'Mumbai Indians',
        'Royal Challengers Bangalore',
       'Kolkata Knight Riders',
       'Punjab kings',
       'Chennai Super Kings',
       'Rajasthan Royals',
       'Delhi Capitals'
      ]

city=['Bangalore', 'Kolkata', 'Jaipur', 'Chennai', 'Delhi', 'Durban',
       'Mumbai', 'Johannesburg', 'Dharamsala', 'Port Elizabeth',
       'Cape Town', 'Kimberley', 'Hyderabad', 'Bengaluru', 'Ahmedabad',
       'Chandigarh', 'Bloemfontein', 'Sharjah', 'Pune', 'Visakhapatnam',
       'Ranchi', 'Abu Dhabi', 'Indore', 'Mohali', 'East London',
       'Cuttack', 'Nagpur', 'Raipur', 'Centurion']

pipe=pickle.load(open('pipe.pkl','rb'))

col1 ,col2 = st.columns(2)

with col1:
    batting_team=st.selectbox('Select the Batting team',sorted(teams))

with col2:
    bowling_team=st.selectbox('Select the Bowling team',sorted(teams))

city=st.selectbox('Select the city',sorted(city))

target =st.number_input('Target')

col3,col4,col5 = st.columns(3)

with col3:
    score=st.number_input('Score')

with col4:
    overs=st.number_input('Overs Completed')

with col5:
    wickets=st.number_input('Wickets out')

if st.button('Predict'):
    runs_left=target-score
    balls_left=120-(overs*6)
    wickets=10-wickets
    crr=score/overs
    rrr=(runs_left*6)/balls_left

    input_df=pd.DataFrame({'batting_team':[batting_team],'bowling_team':[bowling_team],
                           'city':[city],'runs_left':[runs_left],'balls_left':[balls_left],'wickets':       
                            [wickets],'total_runs_x':[target],'crr':[crr],'rrr':[rrr]}
                           )
    
    result=pipe.predict_proba(input_df)
    loss=result[0][0]
    win=result[0][1]
    st.text('The Winning Chance of '+batting_team+' is:'+ str(round(win*100))+'%' )
    st.text('The Winning Chance of '+bowling_team+' is:'+ str(round(loss*100))+'%' )