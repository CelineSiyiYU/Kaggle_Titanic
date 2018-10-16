from sklearn.ensemble import RandomForestClassifier

from data_processing import get_X_Y_train

rf = RandomForestClassifier(n_estimators=200, max_depth=4)

X_train, Y_train, X_test = get_X_Y_train()

rf.fit(X_train, Y_train)

pred = rf.predict(X_test)
import pandas as pd

sub = pd.read_csv('gender_submission.csv')
sub['Survived'] = pred

sub.to_csv('prediction.csv', index = False)