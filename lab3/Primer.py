import os

os.environ['OPENBLAS_NUM_THREADS'] = '1'

#from dataset_script import dataset  # this will import the dataset on coderunner at courses
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import OrdinalEncoder, MinMaxScaler


def split_dataset(dataset,C,P):
    good=[row for row in dataset if row[-1]=='good']
    bad=[row for row in dataset if row[-1]=='bad']
    test_set=[]
    train_set=[]
    if C==0:
        P/=100
        train_set.extend(good[:int(len(good)*P)])
        train_set.extend(bad[:int(len(bad)*P)])
        test_set.extend(good[int(len(good)*P):])
        test_set.extend(bad[int(len(bad)*P):])
    elif C==1:
        P=100-P
        P/=100
        train_set.extend(good[int(len(good) * P):])
        train_set.extend(bad[int(len(bad) * P):])
        test_set.extend(good[:int(len(good) *  P)])
        test_set.extend(bad[:int(len(bad) * P)])
    return train_set,test_set

def transform_dataset(dataset):
    new_dataset = []

    for row in dataset:
        sum_val = row[0] + row[10]
        new_row = [sum_val] + row[1:10] + [row[-1]]
        new_dataset.append(new_row)

    return new_dataset


def scale(train_X, test_X):
    scaler = MinMaxScaler()
    scaler.fit(train_X)
    scaler_train_X = scaler.transform(train_X)
    scaler_test_X = scaler.transform(test_X)
    return scaler_train_X, scaler_test_X


def main():
    global dataset
    transformed_dataset = transform_dataset(dataset)

    C = int(input())
    P = float(input())

    dataset = transformed_dataset

    train_set, test_set = split_dataset(dataset, C, P)

    train_X = [row[:-1] for row in train_set]
    train_Y = [row[-1] for row in train_set]
    test_X = [row[:-1] for row in test_set]
    test_Y = [row[-1] for row in test_set]

    classifier = GaussianNB()
    classifier.fit(train_X, train_Y)
    accuracy = classifier.score(test_X, test_Y)

    print(f'Broj na podatoci vo train se: {len(train_set)}')
    print(f'Broj na podatoci vo test se: {len(test_set)}')
    print(f"Tochnost so zbir na koloni: {accuracy}")

    scaled_train_x, scaled_test_x = scale(train_X, test_X)
    classifier2 = GaussianNB()
    classifier2.fit(scaled_train_x, train_Y)
    accuracy2 = classifier2.score(scaled_test_x, test_Y)
    print(f"Tochnost so zbir na koloni i skaliranje: {accuracy2}")

main()