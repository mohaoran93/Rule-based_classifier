import numpy as np
from Source.RULE import Classifier
from Source.read import GetData
from Source.rule_interpreter import Interpreter
from Source.parse_data import ParseDataSet

parser = ParseDataSet()
classifier = Classifier()
interpreter = Interpreter()

reader = GetData()
# I have three data set: 1. tic-tac-toe 2. car 3. kr-vs-kp
df = reader.read()

msk = np.random.rand(len(df)) < 0.8
train = df[msk]
test = df[~msk]

# get rules

attr_size,dic = parser.parse(train)
Rule = classifier.classify(attr_size=attr_size,df=train,dic=dic)
print("Got the rules are: ", Rule)

# test rules
interpreter.test(df=test,rules=Rule)
