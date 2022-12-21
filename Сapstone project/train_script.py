#!/usr/bin/env python
# coding: utf-8

import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction import DictVectorizer

from sklearn.metrics import accuracy_score
from sklearn.metrics import roc_auc_score

import bentoml


df = pd.read_csv('hr_data.csv')


df.columns = df.columns.str.lower().str.replace(' ', '_')

del df['slno']
del df['candidate_ref']
del df['location']


status = df.status
status = status.replace('Joined', 1)
status = status.replace('Not Joined', 0)
df.status = status


df_full_train, df_test = train_test_split(df,
                                          test_size=0.2,
                                          random_state=2)


df_full_train = df_full_train.reset_index(drop=True)
df_test = df_test.reset_index(drop=True)

y_full_train = df_full_train.status.values
y_test = df_test.status.values


del df_test['status']
del df_full_train['status']


dv = DictVectorizer(sparse=False)
train_dict = df_full_train.to_dict(orient='records')
X_full_train = dv.fit_transform(train_dict)

test_dict = df_test.to_dict(orient='records')
X_test = dv.fit_transform(test_dict)


model = RandomForestClassifier(n_estimators=30,
                                    max_depth=7,
                                    min_samples_leaf=5,
                                    random_state=1)
model.fit(X_full_train, y_full_train)

y_pred = model.predict_proba(X_test)[:,1]


bentoml.sklearn.save_model('hr_model',
                           model,
                           signatures={
                              "predict_proba": {
                                 "batchable": True,
                                 "batch_dim": 0}
                              },
                               custom_objects={
                               'dictVectorizer': dv})
