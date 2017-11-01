# read the csv file
import pandas as pd

class GetData():
    def read(self, name = None):
        if name == None:
            name = input("Type in the data set file name then continue, {bscale, car, kr-vs-kp}")
        else:
            pass
        try:
            df = pd.read_csv(name+'.csv')
            print('OK','I got the file: '+name+".csv")
        except:
            print("No such file")
        return df
