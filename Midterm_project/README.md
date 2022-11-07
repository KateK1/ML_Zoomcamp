## Readme content
- [Project information](##project-information)
- [Problem description](##problem-description)
  - [Dataset description](####dataset-description)
  - [Theoretical usage of the model](####theoretical-usage-of-the-model)
- [Project description](##project-description)
  - [Exploratory data analysis](####exploratory-data-analysis)
  - [Training the models](####training-the-models)
- [Files](##files)


## Project information

The project was made for [ML Zoomcamp 2022](https://github.com/alexeygrigorev/mlbookcamp-code/tree/master/course-zoomcamp). It involves:
- data preparation and EDA
- model treining and parametrs tuning
- deploying model with BentoML

## Problem description

Fire incidents are one of the common insurance cases households and businesses want to be protected from. However, fire incidents occur and owners bear the loss for the damage. The project aims to build a model which estimated dollar loss from the fire incident using the Fire Incidents dataset provided by Toronto Fire Services.

#### Dataset description
[The original dataset.](https://www.kaggle.com/datasets/reihanenamdari/fire-incidents) The dataset counts records about 11K cases of fire incidents during the period from 2011 to 2018 in Toronto, Canada. The dataset contains 27 columns of numerical, categorical, and date-time data:

- Numerical:  
persons_rescued (value range 0 - 86). 
civilian_casualties (value range 0 - 15)  
estimated_number_of_persons_displaced (value range 0 - 999)  
incident_station_area - 3 digit number represents the code of the fire station   
latitude, longitude,  
incident_ward
  
- Categorical:  
area_of_origin - place where fire starts, contains 73 unique values  
business_impact - contains 7 unique values  
extent_of_fire - contains 12 unique values.  
fire_alarm_system_impact_on_evacuation - contains 7 unique values.  
fire_alarm_system_operation - contains 7 unique values.   
fire_alarm_system_presence  - contains 4 unique values.   
ignition_source - object first ignited, contains 82 unique values.   
material_first_ignited - contains 54 unique values.   
method_of_fire_control - contains 5 unique values.   
possible_cause - contains 24 unique values.   
property_use - contains 217 unique values.   
smoke_alarm_at_fire_origin_alarm_failure - contains 11 unique values.   
smoke_alarm_type - contains 11 unique values.   
status_of_fire_on_arrival - contains 8 unique values.   
  
- Date-time in `%Y-%m-%dT%H:%M:%S` format:  
ext_agent_app_or_defer_time  
fire_under_control_time  
clear_time.   
tfs_alarm_time. 
tfs_arrival_time


#### Theoretical usage of the model. 
- Dollar loss estimation for the insurance industry after the incident
- Dollar loss estimation for fire safety specialists before the incident with study or risk estimation purposes

## Project description
- #### Data cleaning  
Dataset is already clean but still needed some preparation like filling in the NaN values. 
  
- #### Exploratory data analysis  
For EDA I analyze different types of features and target variables separately. The target variable has a long tail distribution and was transformed to log1. I find feature importance using correlation and mutual_score. Also, I add new features representing time as a difference between timestamps.  
  
- #### Training the models. 
I trained following models using all features and the features with the best correlation or mutial score. Total 10 models:  
`Linear regression()`  
`DecisionTreeRegression()`  
`RandomForestRegressor()`  
`XGB`  
`Ridge()`  
Then I tuned the features of the best 4 models.
  
## Files  







