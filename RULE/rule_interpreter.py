class Interpreter(object):

    def parse(self, rules = [{('a4',): ('2',), 'class': 'unacc'}, {('a6',): ('low',), 'class': 'unacc'}, {('a1', 'a2'): ('vhigh', 'vhigh'), 'class': 'unacc'}, {('a1', 'a5'): ('high', 'big'), 'class': 'acc'}, {('a3', 'a4', 'a5'): ('2', 'more', 'small'), 'class': 'unacc'}, {('a1', 'a2', 'a3', 'a4'): ('med', 'high', '4', '4'), 'class': 'acc'}]):
        size = len(rules)
        for rule in rules:
            attributes = list(rule)[0]  # a tuple of attr name
            values = list(rule.values())[0]  # a tuple of value correspond to attributes
            theclass = list(rule.values())[1]  # the name of the class
        return attributes, values, theclass

    def test(self,df,rules):
        attributes, values, theclass = self.parse(rules=rules)
        df
