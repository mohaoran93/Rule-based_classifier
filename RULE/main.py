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

msk = np.random.rand(len(df)) < 0.8
train = df[msk]
test = df[~msk]

attr_size,dic = parser.pare(train)
Rule = classifier.classify(attr_size=attr_size,df=train,dic=dic)
print("Got the rules are: ", Rule)

interpreter.test(df=test,rules=Rule)
