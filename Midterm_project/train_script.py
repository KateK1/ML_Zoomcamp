#!/usr/bin/env python
# coding: utf-8

import numpy as np
import pandas as pd
import xgboost as xgb

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction import DictVectorizer

import bentoml

from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score


df = pd.read_csv('df_prepared', delimiter=',')


df_full_train, df_test = train_test_split(df,
                                            test_size=0.2,
                                            random_state=2)


y_full_train = np.log1p(df_full_train.estimated_dollar_loss.values)
y_test = np.log1p(df_test.estimated_dollar_loss.values)


del df_full_train['estimated_dollar_loss']
del df_test['estimated_dollar_loss']


dv = DictVectorizer(sparse=False)
train_dict = df_full_train.to_dict(orient='records')
X_full_train = dv.fit_transform(train_dict)

test_dict = df_test.to_dict(orient='records')
X_test = dv.transform(test_dict)


features = dv.get_feature_names_out()
dtrain = xgb.DMatrix(X_full_train, label=y_full_train)
dtest = xgb.DMatrix(X_test, label=y_test)


xgb_params = {'eta': 0.1, 
              'max_depth': 4,
              'min_child_weight':5,
              'colsample_bytree':0.2,
              'objective': 'reg:squarederror',
              'eval_metric': 'rmse',
              'nthread': 8,
              
              'seed': 1,
              'verbosity': 1
}

model = xgb.train(xgb_params,
                  dtrain,
                  num_boost_round=140)


y_pred = model.predict(dtest)
rmse = mean_squared_error(y_test, y_pred, squared=False).round(2)
r2 = r2_score(y_test, y_pred).round(2)
print(rmse, r2)

bentoml.xgboost.save_model('fire_loss_model',
                           model,
                          custom_objects={
                              'dictVectorizer': dv})

