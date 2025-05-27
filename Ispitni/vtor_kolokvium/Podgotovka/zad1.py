import os
os.environ['OPENBLAS_NUM_THREADS'] = '1'
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import MinMaxScaler, StandardScaler


from dataset_script import dataset


def transform(dataset):
    new_dataset = []
    for row in dataset:
        new_first = row[0] + row[10]
        new_row = [new_first] + row[1:10] + [row[-1]]
        new_dataset.append(new_row)
    return new_dataset


def split(dataset, C, P):
    dataset_good = [row for row in dataset if row[-1] == 'good']
    dataset_bad = [row for row in dataset if row[-1] == 'bad']

    if C == 0:
        train_set = dataset_good[:int(P / 100 * len(dataset_good))] + dataset_bad[:int(P / 100 * len(dataset_bad))]
        test_set = dataset_good[int(P / 100 * len(dataset_good)):] + dataset_bad[int(P / 100 * len(dataset_bad)):]
    else:
        train_set = dataset_good[int((100 - P) / 100 * len(dataset_good)):] + dataset_bad[
                                                                              int((100 - P) / 100 * len(dataset_bad)):]
        test_set = dataset_good[:int((100 - P) / 100 * len(dataset_good))] + dataset_bad[
                                                                             :int((100 - P) / 100 * len(dataset_bad))]

    train_X = [row[:-1] for row in train_set]
    train_Y = [row[-1] for row in train_set]
    test_X = [row[:-1] for row in test_set]
    test_Y = [row[-1] for row in test_set]

    return train_X, train_Y, test_X, test_Y

def scale(train_X, test_X):
    scaler = MinMaxScaler(feature_range=(-1, 1))
    scaler.fit(train_X)

    train_X_scaled = scaler.transform(train_X)
    test_X_scaled = scaler.transform(test_X)

    return train_X_scaled, test_X_scaled

if __name__ == '__main__':
    dataset = transform(dataset)
    C = int(input())
    #P = float(input())/100
    P = int(input())
    train_X,train_Y,test_X,test_Y = split(dataset,C,P)
    train_X_scaled, test_X_scaled = scale(train_X, test_X)

    classifier = GaussianNB()
    classifier.fit(train_X, train_Y)

    classifier2 = GaussianNB()
    classifier2.fit(train_X_scaled, train_Y)

    acc1 = classifier.score(test_X, test_Y)
    acc2 = classifier2.score(test_X_scaled, test_Y)

    print(f"Tochnost so zbir na koloni: {acc1}")
    print(f"Tochnost so zbir na koloni i skaliranje: {acc2}")


