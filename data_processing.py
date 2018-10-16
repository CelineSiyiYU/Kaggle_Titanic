import pandas as pd

LABEL = ''


def get_raw_data():
    train = pd.read_csv('train.csv')
    test = pd.read_csv('test.csv')
    return train, test


def select_features(train):
    features_to_keep = ['Pclass', 'Age', 'SibSp', 'Parch', 'Fare']
    return train[features_to_keep]


def encode_data(train):
    train


def fill_na(train):
    for col in train:
        train[col].fillna(train[col].mean(), inplace=True)


def get_X_Y_train():
    raw_data_train, raw_data_test = get_raw_data()

    Y_train = raw_data_train['Survived']
    X_train = select_features(raw_data_train)

    X_test = select_features(raw_data_test)

    fill_na(X_train)
    fill_na(X_test)

    return X_train, Y_train, X_test
