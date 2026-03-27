import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import pickle

data=pd.DataFrame({
    'last grade': [50,60,70,80,20,65,90],
    'study hours': [4,3,5,7,2,3,6],
    'result':[0,0,1,1,0,0,1]
})

x=data[['last grade','study hours']]
y=data[['result']]

model=LogisticRegression()
model.fit(x,y)

pickle.dump(model,open("model.pkl" , "wb"))
print("model trained and saved")