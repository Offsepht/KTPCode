import pandas as pd



element = 'H:\\PICK_TO_XLS\\C404-CANADA GOOSE US INC._Styles_39983.txt'

my_cols = [str(i) for i in range(17)]
df = pd.read_csv(element, sep='\t', names=my_cols, header=None, engine='python')
df = df.drop([0,0])
# df = df.drop([1,1])
df.to_excel('gooseInv.xlsx', 'Sheet1', header=None, index = False)
