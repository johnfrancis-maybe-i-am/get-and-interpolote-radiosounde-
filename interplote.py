import pandas as pd
import numpy as np
from scipy.interpolate import interp1d
import os 

def sorted(array):
    temp = list()
    for i in array:
        j = '%.2f' %i
        temp.append(float(j))
    return temp

def interplote(filename):
    df = pd.read_csv(filename,header=None,skiprows=1)
    interp1 = interp1d(df[1], df[0],fill_value="extrapolate")
    interp2= interp1d(df[1], df[2],fill_value="extrapolate")
    interp3 = interp1d(df[1], df[3],fill_value="extrapolate")
    interp4 = interp1d(df[1], df[4],fill_value="extrapolate")
    interp5= interp1d(df[1], df[5],fill_value="extrapolate")
    interp6 = interp1d(df[1], df[6],fill_value="extrapolate")
    interp7= interp1d(df[1], df[7],fill_value="extrapolate")
    interp8= interp1d(df[1], df[8],fill_value="extrapolate")
    interp9= interp1d(df[1], df[9],fill_value="extrapolate")
   
    interp10= interp1d(df[1], df[10],fill_value="extrapolate")


    if df[1][0] <5000:
        new_height = np.arange(0,5000,30)
    elif df[1][0]>5000 and df[1][0] <20000:
        new_height = np.arange(0,20000,30)
    else:
        new_height = np.arange(0, 30000,30)
    dic = {
        'Geo_Height':new_height,
        'Pressure':sorted(interp1(new_height)),
        'Temperature':sorted(interp2(new_height)),
        'Dewpoint_Temperature':sorted(interp3(new_height)),
        'Relative_Humidity':sorted(interp4(new_height)),
        'Mixing_Ratio':sorted(interp5(new_height)),
        'Wind_Direction':sorted(interp6(new_height)),
        'Wind_Speed':sorted(interp7(new_height)),
        'Potential_Temperature':sorted(interp8(new_height)),
        'Equivalent_Potential_Temperature':sorted(interp9(new_height)),
        'Virtual_Potential_Temperature':sorted(interp10(new_height)),

    }
    new  = pd.DataFrame(dic)
    os.chdir(path)
    os.chdir("interploted")
    new.to_csv(filename)
    os.chdir(path)
    print("go")

go_to = './2018'
path  = os.getcwd()
newpath = './interploted'
os.makedirs(newpath)

for file in os.listdir(go_to):

    print(file)
    os.chdir(go_to)
    interplote(file)
    
print('done')