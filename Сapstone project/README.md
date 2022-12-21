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
After collecting and observing data from the HR department of the IT company it turned out that 20% of candidates who accept the offer didn't join the company. The goal of the project is to predict will candidate join the company after the offer was accepted or not. The problem is a binary classification.


#### Dataset description
[The original dataset.](https://www.kaggle.com/datasets/avikumart/hrdatasetclassif?select=hr_data.csv)
The dataset contains details of about 9K cases of hiring in several IT companies. 20% of candidates who accept the offer didn't join the company.

The following features were deleted from the dataset because they aren't valuable for the model:
- SLNO - index number  
- Candidate - Unique reference number to identify the candidate  
- Location - Company location for which the offer was rolled out
  
**Hiring details**  
DOJ Extended - Date of joining asked by candidate or not  
Duration to accept the offer - Number of days taken by the candidate to accept the offer  
Notice period - Notice period served before a candidate can join the company    
Candidate relocate actual - Candidates have to relocate or not  
Candidate Source - Source from which the resume of the candidate was obtained  
Rex in Yrs - Relevant years of experience  
LOB - Line of business for which the offer was rolled out  
Offered band - Band offered to the candidate based on experience, performance  
  
**Salary data**  
Percent hike expected in CTC - Percentage hike expected by the candidate  
Percent hike offered in CTC - Percentage hike offered by the company  
Percent difference CTC - Difference between expected and offered hike  
Joining Bonus - Joining bonus is given or not  

**Demographic data**  
Gender - Gender of the candidate  
Age - Age of the candidate   
  
**Status** - Target varible whether the candidate joined or not
 
## Project description
- #### Data cleaning  
Dataset is already clean and has no missing values, mistakes, or duplicates.
  
- #### Exploratory data analysis  
For numerical features, I plotted histograms and boxplots to visualize distribution and outliners. For feature importance between numerical features and categorical target, I calculated Point Biserial and plot logistic regression plots - both show no strong correlation between target and features.  
For categorical features, I checked unique values and their distribution. Every value was represented well enough through the dataset and no rows were elliminated. For feature importance between categorical features and categorical target, I calculated the 'risk' of not-joining the company for every categorical feature unique value. Also, I calculated Cramer's V correlation. No feature shows a strong correlation.
  
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
  
For each model, I calculated `roc_auc_score` for `y` from the validation set and `y` from the training set to prevent overfitting and accuracy.  
The best 3 models `RandomForestClassifier`, `XGB`, `AdaBoostClassifier` were trained on the full train set.  
`RandomForestClassifier` was selected as the best model with `auc_score = 0.76` (on validation), `auc_score = 0.81` (on training), and `accuracy = 0.82`  
Note: All three models show good results and their auc scores were short-range
The most important feature for the `RandomForestClassifier` model is `notice_period`
  
  
## Files  
[The dataset](https://github.com/KateK1/ML_Zoomcamp/blob/main/%D0%A1apstone%20project/hr_data.csv) - original dataset  
[HR_pred_notebook.ipynb](https://github.com/KateK1/ML_Zoomcamp/blob/main/%D0%A1apstone%20project/HR_pred_notebook.ipynb) - notebook contains EDA and model training   
[train_script.py](https://github.com/KateK1/ML_Zoomcamp/blob/main/Midterm_project/train_script.py)- final model training and saving it to BentoML  
[predict.py](https://github.com/KateK1/ML_Zoomcamp/blob/main/Midterm_project/predict.py)  
[bentofile.yaml](https://github.com/KateK1/ML_Zoomcamp/blob/main/Midterm_project/bentofile.yaml)  


## Instructions
1. Run  
  `train_script.py`  
  
2. Run  
  `bentoml build`
    
3. Run  
  `bentoml containerize candidate_status_classifie:latest` 
    
 4. Run the command which will be shown in the command line. For example:  
  `docker run -it --rm -p 3000:3000 candidate_status_classifie: *** serve --production`  
  
 5. Now you can acsess service at `http://localhost:3000/`  
 To test the servis use following JSON:  
 ```
 {"doj_extended":"Yes",  
 "duration_to_accept_offer":62,  
 "notice_period":30,  
 "offered_band":"E1",  
 "pecent_hike_expected_in_ctc":127.27,  
 "percent_hike_offered_in_ctc":138.64,  
 "percent_difference_ctc":5.0,  
 "joining_bonus":"No",  
 "candidate_relocate_actual":"No",  
 "gender":"Male",  
 "candidate_source":"Direct",  
 "rex_in_yrs":3,  
 "lob":"ERS",  
 "age":29
}
```  

To see the opposite status of the candidates change `notice_period` - the most importent feature of the model
