import pandas as pd
import numpy as np
import itertools

from read import GetData
from parse_data import ParseDataSet
import tool


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
            for attr_ in attr:
                df_atrr.append(df[attr_].unique())

            attr_combination_total = []
            for comb_index in index_product: # iteratively access all combination
                p_each =[]
                for each_index in comb_index:
                    p_each.append(df_atrr[each_index])
                attr_combination_total.append({comb_index:p_each})

            product_toal = []
            for comb in attr_combination_total:
                len_total = len(df)
                attr_selected =[]
                index_i = list(comb.keys())
                pair_i = comb.get(index_i[0])
                product_eachs = list(itertools.product(*pair_i))
                for index in index_i[0]:
                    attr_name = 'a'+str(index+1)
                    attr_selected.append(attr_name)
                cols = attr_selected
                for product_each in product_eachs:
                    conditions = product_each
                    temp_df = df[eval(" & ".join(["(df['{0}'] == '{1}')".format(col, cond)
                                for col, cond in zip(cols, conditions)]))]
                    cls = temp_df['class'].unique()
                    if len(cls) == 1:
                        df = df[eval(" & ".join(["(df['{0}'] != '{1}')".format(col, cond)
                               for col, cond in zip(cols, conditions)]))]
                        print("For the time being, the coverage is : ", 1 - len(df)/len_total)
                        self.rules.append({tuple(cols):conditions,'class':cls[0]})
            self.number_combinations = self.number_combinations+1
        return self.rules

    def All_instances_are_classified(self):
        return self.rest_rows == 0


