# code 4: 파이써닉

import pandas as pd
from sklearn.datasets import load_iris
iris = load_iris() # sample data load
 # feature_names 와 target을 레코드로 갖는 데이터프레임 생성
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
print(df)
print(df.shape)
print(df.iloc[1])

# index = df.index
# print(index)

for i in range(1, df.shape[0]):
    if df['petal length (cm)'][i] > df['petal length (cm)'][i-1]:
        print("value found=")
        print(df['petal length (cm)'][i], df['petal length (cm)'][i-1])
        print("other column index=", df['petal width (cm)'][i])
        tmp = df['petal width (cm)'][:i]
        print("tmp=", tmp.shape, tmp.min())
