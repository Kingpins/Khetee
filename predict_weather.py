import streamlit as st
import requests
from datetime import datetime , timedelta
import pandas as pd
import matplotlib.pyplot as plt
import time 

# INSERT YOUR API  KEY WHICH YOU PASTED IN YOUR secrets.toml file 
api_key =  'e3b25e266b3520c4d6c8e451c2fd1222'

url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}'
url_1 = 'https://api.openweathermap.org/data/2.5/onecall/timemachine?lat={}&lon={}&dt={}&appid={}'

# Function for LATEST WEATHER DATA
def getweather(city):
    result = requests.get(url.format(city, api_key))     
    if result:
        json = result.json()
        #st.write(json)
        country = json['sys']['country']
        temp = json['main']['temp'] - 273.15
        temp_feels = json['main']['feels_like'] - 273.15
        humid = json['main']['humidity'] - 273.15
        icon = json['weather'][0]['icon']
        lon = json['coord']['lon']
        lat = json['coord']['lat']
        des = json['weather'][0]['description']
        res = [country, round(temp,1),round(temp_feels,1),
                humid,lon,lat,icon,des]
        return res , json
    else:
        print("error in search !")

# Function for HISTORICAL DATA
def get_hist_data(lat,lon,start):
    res = requests.get(url_1.format(lat,lon,start,api_key))
    data = res.json()
    temp = []
    for hour in data["hourly"]:
        t = hour["temp"]
        temp.append(t)     
    return data , temp

# Let's write the Application

def weather_main():
    html_temp = """
    <div>
    <h1 style="color:MEDIUMSEAGREEN;text-align:left;"> Khetee - Weather Report </h1>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        city_name = st.text_input("Enter a City Name")
    with col2:  
    	if city_name:
    		res , json = getweather(city_name)
    		#st.write(res)
    		st.success('Current: ' + str(round(res[1],2)))
    		st.info('Feels Like: ' + str(round(res[2],2)))
    		st.info('Humidity: ' + str(round(res[3],2)))
    		st.subheader('Status: ' + res[7])
    		web_str = "![Alt Text]"+"(http://openweathermap.org/img/wn/"+str(res[6])+"@2x.png)"
    		st.markdown(web_str)  
    
    if city_name:        
        show_hist = st.expander(label = 'Last 5 Days History')
        with show_hist:
                start_date_string = st.date_input('Current Date')
                #start_date_string = str('2021-06-26')
                date_df = []
                max_temp_df = []
                for i in range(5):
                            date_Str = start_date_string - timedelta(i)
                            start_date = datetime.strptime(str(date_Str),"%Y-%m-%d")
                            timestamp_1 = datetime.timestamp(start_date)
                            #res , json = getweather(city_name)
                            his , temp = get_hist_data(res[5],res[4],int(timestamp_1))
                            date_df.append(date_Str)
                            max_temp_df.append(max(temp) - 273.5)

                df = pd.DataFrame()
                df['Date'] = date_df
                df['Max temp'] = max_temp_df
                st.table(df)

        st.map(pd.DataFrame({'lat' : [res[5]] , 'lon' : [res[4]]},columns = ['lat','lon']))
