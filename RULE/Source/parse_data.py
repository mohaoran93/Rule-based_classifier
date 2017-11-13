import numpy as np

class ParseDataSet(object):
# dic -> attr : [possible value]
    def parse(self,df=None):
        attr_size =len(df.columns) - 1
        rows_size = len(df)
        dic = {}
        for c in list(df):
            if c != 'class':
              values = df[c].unique()
              dic[c] = values
        for c in np.arange(1,attr_size):
            c = 'c'+ str(c)
            #print(dic[str(c)])
        return attr_size,dic,
