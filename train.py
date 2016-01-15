#!/usr/bin/env python2
# -*- coding: utf-8 -*-


import numpy as np

from sklearn import metrics
from sklearn.datasets import load_files
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.linear_model import SGDClassifier
from sklearn.externals import joblib


if __name__ == '__main__':
    bvg_train = load_files('data')
    bvg_test = load_files('data')

    text_clf = Pipeline([('vect', CountVectorizer()),
                         ('tfidf', TfidfTransformer()),
                         ('clf', SGDClassifier()),])

    _ = text_clf.fit(bvg_train.data, bvg_train.target)
    predicted = text_clf.predict(bvg_test.data)

    print(np.mean(predicted == bvg_test.target))
    print(metrics.classification_report(bvg_test.target, predicted,
                                        target_names=bvg_test.target_names))
    print(metrics.confusion_matrix(bvg_test.target, predicted))

    joblib.dump(text_clf, 'model/bvg_model.pkl')
