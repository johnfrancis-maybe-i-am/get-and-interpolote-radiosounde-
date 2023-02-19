from bs4 import BeautifulSoup
import requests
import pandas as pd
import os
from datetime import date,timedelta
import time
    
s = time.time()
#gaja
from_date = date(2018,11,20)
to_date = date(2018,11,21)
#madous
"""from_date = date(2022,11,20)
to_date = date(2022,12,30)"""

def fetch_data(i_time,i_day,i_month,i_year):
    region = "seasia" #midast,seasia,africa,europe,np,ant,pac,samer,nacon
    station_number = "43279" # in num for karikal = 43346 for chennai = 43279
    print(i_day)
    year = str(i_year) # in num
    month = str(i_month)  # from 1 to 12
    date = str(i_day) # from 1 to 31
    time = str(i_time) #00 or 12
    


    url =f"http://weather.uwyo.edu/cgi-bin/sounding?region={region}f&TYPE=TEXT%3ALIST&YEAR={year}&MONTH={month}&FROM={date}{time}&TO={date}{time}&STNM={station_number}"
    r = requests.get(url)
    soup = BeautifulSoup(r.content,'html.parser')
    
    if soup.pre != None:
        cont = soup.pre.text
    else:
        cont = None

       
    return cont 

def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)

def create_file(date,cont,tz):
    file = open(f"{date}-{tz}.txt","x")
    if cont != None:
        file.write(cont)
        file.close()

        with open(f"{date}-{tz}.txt", "r") as f:
            rows = f.readlines()[5:]
        with open(f"{date}-{tz}.txt","w") as f:
            f.writelines(rows[::-1])
            f.close()

        data = pd.read_fwf(f"{date}-{tz}.txt",skiprows=1)
        data.to_csv(f"{date}-{tz}.csv",index=None)
        os.remove(f"{date}-{tz}.txt")
    else:
        file.write("data not found")
        file.close()
    

r_days  = to_date - from_date
r_years = to_date.year - from_date.year
 
 #  for create folder according to years
from_year = int(from_date.year)
for i in range(1,int(r_years)+2):
    
    createFolder(f"./{from_year}")
    from_year = from_year+1

# for web scaping 
path = os.getcwd()
i = 0
while i <r_days.days+1:
    start = time.time()
    #content1 = fetch_data("00","%02d"%from_date.day,"%02d"%from_date.month,from_date.year)
    content2 = fetch_data("12","%02d"%from_date.day,"%02d"%from_date.month,from_date.year)
    end = time.time()
    fromdate = str(from_date.year)
    os.chdir(f'./{fromdate}')
    #create_file(str(from_date),content1,"00")
    create_file(str(from_date),content2,"12")
    os.chdir(path=path)
  
    i = i+1
    from_date = from_date +timedelta(days=1)
    print(end-start)
print("done")

e = time.time()
print(f"final time required : {e-s}")









