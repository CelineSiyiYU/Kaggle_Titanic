import pandas as pd

train = pd.read_csv('train.csv')
print(train.columns)

print(train['Pclass'])
print(train['Name'].unique())
print(train[train['Sex']=='male']['Survived'].mean())
print(train[train['Sex']=='female']['Survived'].mean())

print(train[train['Pclass']==1]['Survived'].mean())
print(train[train['Pclass']==2]['Survived'].mean())
print(train[train['Pclass']==3]['Survived'].mean())

import matplotlib.pyplot as plt

train['Embarked'].fillna('-1', inplace=True)
SibSp = train['Embarked'].unique()
survived_mean = [train[train['Embarked']==sp]['Survived'].mean() for sp in SibSp]

plt.figure()
plt.scatter(SibSp, survived_mean)
plt.show()
