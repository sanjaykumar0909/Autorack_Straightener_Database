import pandas as pd

def cycles(csv):
    df=pd.read_csv(csv)
    cycle=0
    for i in range(len(df['Angle(Deg) '])-1):
        if(df['Angle(Deg) '][i]-df['Angle(Deg) '][i+1]<0):
            cycle=cycle+1
    return cycle+1