from read import GetData
from parse_data import ParseDataSet
from RULE import Classifier
from rule_interpreter import Interpreter
import numpy as np
import pandas as pd

parser = ParseDataSet()
classifier = Classifier()
interpreter = Interpreter()

reader = GetData()
# I have three data set tic-tac-toe car bscale
df = reader.read('car')


# class Classifier(object):
#     reader = GetData()
#     parser = ParseDataSet()
#     rules = [] # ruless.append({cls: rule})
#     data_info = None
#     number_combinations = 1
#
#     def classify(self,attr_size=0, df=None, dic_c=None):
#
#         while (self.number_combinations <= attr_size) and not self.All_instances_are_classified():
#             # for 1
#             #for c in np.arange(1,tool.nCr(attr_size,self.number_combinations)):
#                 #c = 'c'+ str(c)
#                 #print(dic[str(c)])
#
#             self.number_combinations = self.number_combinations+1
#
#         return self.rules
#
#     def All_instances_are_classified(self):
#
#         return False

msk = np.random.rand(len(df)) < 0.8
train = df[msk]
test = df[~msk]
print(len(train),len(test))
