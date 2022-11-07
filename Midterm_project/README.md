[Project information](##project-information) 





## Project information

The project was made for ML Zoomcamp 2022. It involves:
- data prepartion  and EDA
- model treining and tuning
- ADDD

## Problem description

Fire incidents are one of the common insurance cases households and businesses want to be protected from. However, fire incidents occure and owners bear the loss for the damage. The aim of the project is build model which estimated dollar loss from of the fire incedent using Fire Incidents dataset provided by Toronto Fire Services.

**Dataset description**  
The dataset counts records about 11K cases of fire incedens during period from 2011 to 2018 in Toronto, Canada. Dataset contains 27 column of numerical, categorical and date time data:

- Numerical:  
persons_rescued (value range 0 - 86). 
civilian_casualties (value range 0 - 15)  
estimated_number_of_persons_displaced (value range 0 - 999)  
incident_station_area - 3 digit number represents code of the fire station   
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
  
- Date time in `%Y-%m-%dT%H:%M:%S` format:  
ext_agent_app_or_defer_time  
fire_under_control_time  
clear_time.   
tfs_alarm_time. 
tfs_arrival_time


**Theoretical usage of the model**. 
- Dollar loss estimation for insurance industry after incedent
- Dollar loss estimation for fire safety specialists before incedent with study or risk estimation purposes

## Project description
- **Data cleaning**  
Dataset was cleand before but still needed some preparation like filling the NaN values. 
  
- **EDA**  
For EDA I analyze diferent types of features and target variable separetly. Target variable have a long tail distribution and was transformed to log1. I find feature imfortanses using correlation and mutual_score. Also I add new features representing time as difference beetween timestampes.  
  
- **Training the models**. 
I trained following models using all features and the feachers with the best correlation or mutial score. Total 10 models:  
`Linear regression()`  
`DecisionTreeRegression()`  
`RandomForestRegressor()`  
`XGB`  
`Ridge()`  
Then I tuned the features of the best 4 models.







