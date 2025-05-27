import os
os.environ['OPENBLAS_NUM_THREADS'] = '1'
from sklearn.tree import DecisionTreeClassifier



from dataset_script import dataset


def splitanje(P, dataset):
    train_set = dataset[:int(P/100 * len(dataset))]
    test_set = dataset[int(P/100 * len(dataset)):]

    train_X = [row[:-1] for row in train_set]
    train_Y = [row[-1] for row in train_set]

    test_X = [row[:-1] for row in test_set]
    test_Y = [row[-1] for row in test_set]

    return train_X, train_Y, test_X, test_Y


if __name__ == '__main__':
    P = int(input())
    C = input()
    L = int(input())

    train_X, train_Y, test_X, test_Y = splitanje(P,dataset)

    classifier = DecisionTreeClassifier(criterion=C,max_leaf_nodes=L,random_state=0)
    classifier.fit(train_X, train_Y)
    acc1 =classifier.score(test_X, test_Y)

    models = []

    for cls in ['Perch', 'Roach', 'Bream']:
        model = DecisionTreeClassifier(criterion=C,max_leaf_nodes=L,random_state=0)
        model.fit(train_X, [1 if label==cls else 0 for label in train_Y])
        models.append((cls,model))

    count = 0

    for X, Y in zip(test_X, test_Y):
        all_correct = True
        for cls,model in models:
            pred = model.predict([X])[0]
            if cls == Y:
                if pred != 1:
                    all_correct = False
                    break
            else:
                if pred != 0:
                    all_correct = False
                    break
        if all_correct:
            count += 1

    acc2 = count / len(test_X)

    print(f'Tochnost so originalniot klasifikator: {acc1}')
    print(f'Tochnost so kolekcija od klasifikatori: {acc2}')
