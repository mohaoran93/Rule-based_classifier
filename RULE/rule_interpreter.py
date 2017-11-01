import pandas as pd
class Interpreter(object):

    def test(self,df, rules=[]):
        total_rows = len(df)
        right_rows = 0
        for rule in rules:
            cols = list(rule)[0]  # a tuple of attr name
            conds = list(rule.values())[0]  # a tuple of value correspond to attributes
            theclass = list(rule.values())[1]  # the name of the class

            temp_df = df[eval(" & ".join(["(df['{0}'] == '{1}')".format(col,cond) for col,cond in zip(list(cols),list(conds))]))]  #

            df = pd.merge(df,temp_df,how='outer',indicator=True)  # I delete the rows that has been tested. This denotes that the rules has to been applied by order.
            df = df[df['_merge'] == 'left_only']
            del df['_merge']

            temp_df_right = temp_df[temp_df['class'] == theclass]

            n = len(temp_df_right)
            right_rows = right_rows + n
            if len(temp_df) != 0:
                print("Applying rule {0} then got {1} rows(denote the coverage), and the precision of this rule is {2}".format(rule,len(temp_df),len(temp_df_right)/len(temp_df)))

        print("Final accuracy is {0}".format(right_rows/total_rows))
