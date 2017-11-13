import itertools

import numpy as np
import pandas as pd
from Source.read import GetData

from Source.parse_data import ParseDataSet


class Classifier(object):
    reader = GetData()
    parser = ParseDataSet()
    rules = [] # ruless.append({cls: rule})
    data_info = None
    number_combinations = 1
    rest_rows = 1
    all_combination = []

    def classify(self,attr_size=0, df=None, dic=None):
        while (self.number_combinations <= attr_size) and not self.All_instances_are_classified():

            index_product = list(itertools.combinations(np.arange(0,attr_size), self.number_combinations))
            attr = df.columns[df.columns != 'class'] # attr without column of class
            df_atrr = []
            len_total = len(df)
            for attr_ in attr:
                df_atrr.append(df[attr_].unique())

            attr_combination_total = []
            for comb_index in index_product: # iteratively access all combination
                p_each =[]
                for each_index in comb_index:
                    p_each.append(df_atrr[each_index])
                attr_combination_total.append({comb_index:p_each})

            for comb in attr_combination_total:
                cols =[]
                index_i = list(comb.keys())
                pair_i = comb.get(index_i[0])
                product_eachs = list(itertools.product(*pair_i))
                for index in index_i[0]:
                    attr_name = 'a'+str(index+1)
                    cols.append(attr_name)
                for conditions in product_eachs:
                    temp_df = df[eval(" & ".join(["(df['{0}'] == '{1}')".format(col, cond)
                                for col, cond in zip(cols, conditions)]))]
                    cls = temp_df['class'].unique()
                    # print(len(cls))
                    if len(cls) == 1:
                        # df = df[eval("  ".join(["(df['{0}'] != '{1}')".format(col, cond)
                        #        for col, cond in zip(cols, conditions)]))]
                        df = pd.merge(df,temp_df,how='outer',indicator=True)
                        df = df[df['_merge'] == 'left_only']
                        del df['_merge']
                        self.rest_rows = len(df)
                        print("For the time being, the number_combinations is {0} the coverage(total) is: {1}, the number of rest of rows is {2}".format(self.number_combinations,1 - len(df)/len_total,self.rest_rows))
                        self.rules.append({tuple(cols):conditions,'class':cls[0]})
            self.number_combinations = self.number_combinations+1
        return self.rules

    def All_instances_are_classified(self):
        return self.rest_rows == 0


