from sklearn import metrics

def classifier_search(classifiers, X_train, y_train, X_test, y_test):
    for classifier in classidiers:
        print("-------------")
        print(str(classifier) + '\n')
        classifier.fit(X_train, y_train)
        y_pred = classifier.predict(X_test)
        print("Accuracy: ", metrics.accuracy_score(y_test, y_pred)
        print("Precision: ", metrics.precision_Score(y_test, y_pred))
        print("Recall: ", metrics.recall_score(y_test, y_pred))
        print("-------------")

def cross_validation(candidate_models, X_train, y_train):

