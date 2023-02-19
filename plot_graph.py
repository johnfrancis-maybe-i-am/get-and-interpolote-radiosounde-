import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

def graphplot(filename):
    df = pd.read_csv(f'{filename}.csv')
    

    Pressure = df['Pressure'][0:120]
    Geo_Height = df['Geo_Height'][0:120]
    Temperature = df['Temperature'][0:120]
    Dewpoint_Temperature = df['Dewpoint_Temperature'][0:120]
    Relative_Humidity=df['Relative_Humidity'][0:120]
    Mixing_Ratio=df['Mixing_Ratio'][0:120]
    Wind_Direction=df['Wind_Direction'][0:120]
    Wind_Speed=df['Wind_Speed'][0:120]
    Potential_Temperature=df['Potential_Temperature'][0:120]
    Equivalent_Potential_Temperature=df['Equivalent_Potential_Temperature'][0:120]
    Virtual_Potential_Temperature=df['Virtual_Potential_Temperature'][0:120]


    fig,ax = plt.subplots(3,3,figsize=(22,20))
    fig.suptitle(f'Graphs for all parameters on {filename}')

    #plt.subplot(3,3,1)
    ax[0, 0].plot(Pressure,Geo_Height)
    ax[0, 0].set_title("Pressure VS Height")
    ax[0, 0].set_xlabel("pressure (hpa)")
    ax[0, 0].set_ylabel("height (m)")
    ax[0, 0].grid()

    #plt.subplot(3,3,2)
    ax[0, 1].plot(Temperature,Geo_Height)
    ax[0, 1].set_title("Temperature VS Height")
    ax[0, 1].set_xlabel("Temperature (C)")
    ax[0, 1].set_ylabel("height (m)")
    ax[0, 1].grid()

    #plt.subplot(3,3,3)
    ax[0, 2].plot(Dewpoint_Temperature,Geo_Height)
    ax[0, 2].set_title("Dewpoint_Temperature VS Height")
    ax[0, 2].set_xlabel("Dewpoint_Temperature (C)")
    ax[0, 2].set_ylabel("height (m)")
    ax[0, 2].grid()

    ax[1, 0].plot(Relative_Humidity,Geo_Height)
    ax[1, 0].set_title("Relative_Humidity VS Height")
    ax[1, 0].set_xlabel("Relative_Humidity (%)")
    ax[1, 0].set_ylabel("height (m)")
    ax[1, 0].grid()

    ax[1, 1].plot(Mixing_Ratio,Geo_Height)
    ax[1, 1].set_title("Mixing_Ratio VS Height")
    ax[1, 1].set_xlabel("Mixing_Ratio (g/kg)")
    ax[1, 1].set_ylabel("height (m)")
    ax[1, 1].grid()

    ax[1, 2].plot(Wind_Speed,Geo_Height)
    ax[1, 2].set_title("Wind_Speed VS Height")
    ax[1, 2].set_xlabel("Wind_Speed (knot)")
    ax[1, 2].set_ylabel("height (m)")
    ax[1, 2].grid()

    ax[2, 0].plot(Potential_Temperature,Geo_Height)
    ax[2, 0].set_title("Potential_Temperature VS Height")
    ax[2, 0].set_xlabel("Potential_Temperature (K)")
    ax[2, 0].set_ylabel("height (m)")
    ax[2, 0].grid()

    ax[2, 1].plot(Equivalent_Potential_Temperature,Geo_Height)
    ax[2, 1].set_title("Equivalent_p_Temperature VS Height")
    ax[2, 1].set_xlabel("Equivalent_Potential_Temperature (K)")
    ax[2, 1].set_ylabel("height (m)")
    ax[2,1].grid()

    ax[2, 2].plot(Virtual_Potential_Temperature,Geo_Height)
    ax[2, 2].set_title("Virtual_P_Temperature VS Height")
    ax[2, 2].set_xlabel("Virtual_Potential_Temperature (K)")
    ax[2, 2].set_ylabel("height (m)")
    ax[2, 2].grid()

    fig.tight_layout()

    plt.savefig(f"{filename}.jpg")

    plt.close()
    print(f"done-{filename}")

print(os.listdir('./interploted'))
go_to = './interploted'
path  = os.getcwd()
for file in os.listdir(go_to):

    file_name = os.fsdecode(file).split('.')[0]
    os.chdir(go_to)
    graphplot(file_name)
    os.chdir(path)

print("done")
