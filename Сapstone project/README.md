## Readme content
- [Project information](##project-information)
- [Problem description](##problem-description)
  - [Dataset description](####dataset-description)
- [Project description](##project-description)
  - [Exploratory data analysis](####exploratory-data-analysis)
  - [Training the models](####training-the-models)
- [Files](##files)
- [Instructions](##instructions)


## Project information

The project was made for [ML Zoomcamp 2022](https://github.com/alexeygrigorev/mlbookcamp-code/tree/master/course-zoomcamp). It involves:
- data preparation and EDA
- model treining and parametrs tuning
- deploying model with BentoML

## Problem description
After collecting and observing data from HR department of the IT company it turned out that 20% of candidates who accept the offer didn't join the company. The goal of the project is to predict will candidate join the company after the offer acception or not. The problem is classified as a binary classification.


#### Dataset description
[The original dataset.](https://www.kaggle.com/datasets/avikumart/hrdatasetclassif?select=hr_data.csv)
The dataset contains details of about 9K cases of hiring in several IT companies. 20% of candidates who accept the offer didn't join the company.

The following features were deleted from the dataset because they aren't valuable for the model:
- SLNO - index number  
- Candidate - Unique reference number to identify candidate  
- Location - Company location for which offer was rolled out
  
**Hiring details**  
DOJ Extended - Date of joining asked by candidate or not  
Duration to accept the offer - Number of days taken by the candidate to accept the offer  
Notice period - Notice period served before candidate can join the company    
Candidate relocate actual - Candidates have to relocate or not  
Candidate Source - Source from which resume of the candidate was obtained  
Rex in Yrs - Relevant years of experience  
LOB - Line of business for which offer was rolled out  
Offered band - Band offered to candidate based on experience, performance  
  
**Salary data**  
Percent hike expected in CTC - Percentage hike expected by the candidate  
Percent hike offered in CTC - Percentage hike offered by the company  
Percent difference CTC - Difference between expected and offered hike  
Joining Bonus - Joining bonus is given or not  

**Demographic data**  
Gender - Gender of the candidate  
Age - Age of the candidate   
  
**Status** - Target varible wh whether the candidate joined or not
 
## Project description
- #### Data cleaning  
Dataset is already clean and have no missing values and duplicates.
  
- #### Exploratory data analysis  
For numerical featured I ploted histogram and boxplot to visualize distribution and outliners. For feature importance between numerical features and categorical binary target I calculated Point Biserial and plot logistic regression plot - both show no strong correlation between target and features.  
For categorical features I checked unique values and ita distribution. Every value was represented well enought and no rows were elliminated. For feature importance between categorical features and categorical binary target I calculated 'risk' of not-joining the company for every categorical feature unique value. Also I calculated Cramer's V correlation. No feature shows strong correlation
  
- #### Training the models. 
with parametrs tuning:  
`RandomForestClassifier()`  
`ExtraTreesClassifier()`  
`AdaBoostClassifier()`  
`XGB`  
`DecisionTreeClassifier()`  
without parametrs tuning:  
`Logistic Regression()`  
`RidgeClassifier()`  
  
For the each model was calculated `roc_auc_score` for y from validation set and y from training set to control overfitting, accuracy.  
The best 3 models `RandomForestClassifier`, `XGB`, `AdaBoostClassifier` were train on full train set.  
`RandomForestClassifier` was selected as the beat model with `auc_score = 0.76` (on validation), `auc_score = 0.81` (on training), and `accuracy = 0.82`  
The most importent feature for the `RandomForestClassifier` model is `notice_period`
  
  
## Files  
[The Fire Incidents dataset](https://github.com/KateK1/ML_Zoomcamp/blob/main/Midterm_project/Fire_Incidents.csv) - original dataset  
[fire_prediction_notebook.ipynb](https://github.com/KateK1/ML_Zoomcamp/blob/main/Midterm_project/fire_prediction_notebook.ipynb) - notebook contains EDA and model training   
[df_prepared](https://github.com/KateK1/ML_Zoomcamp/blob/main/Midterm_project/df_prepared) - modified dataset to train the final model  
[train_script.py](https://github.com/KateK1/ML_Zoomcamp/blob/main/Midterm_project/train_script.py)- final model training and saving it to BentoML  
[predict.py](https://github.com/KateK1/ML_Zoomcamp/blob/main/Midterm_project/predict.py)  
[bentofile.yaml](https://github.com/KateK1/ML_Zoomcamp/blob/main/Midterm_project/bentofile.yaml)  
[test_json.txt](https://github.com/KateK1/ML_Zoomcamp/blob/main/Midterm_project/test_json.txt) - use this json to test the model


## Instructions
1. Run  
  `train_script.py`  
  
2. Run  
  `bentoml build`
    
3. Run  
  `bentoml containerize fire_loss_model:latest` 
    
 4. Run the command which will be shown in the command line. For example:  
  `docker run -it --rm -p 3000:3000 fire_loss_model: *** serve --production`  
  
 5. Now you can acsess service at `http://localhost:3000/`  
Copy json from `test_json.txt` and use it to test the service. The model has a lot of features. If you want to play with it a little more check out the last part of fire_prediction_notebook.ipynb where you can find the final model's top 20 features. Change the top features to see different values of estimated dollar loss for the fire incident.
