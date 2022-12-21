import bentoml
from bentoml.io import JSON
from bentoml.io import NumpyNdarray

from pydantic import BaseModel

class Candidate(BaseModel):
    doj_extended: str
    duration_to_accept_offer:int
    notice_period:int
    offered_band: str
    pecent_hike_expected_in_ctc:float
    percent_hike_offered_in_ctc:float
    percent_difference_ctc: float
    joining_bonus: str
    candidate_relocate_actual: str
    gender: str
    candidate_source: str
    rex_in_yrs:int
    lob: str
    age:int



model_ref = bentoml.sklearn.get("hr_model:latest")
dv = model_ref.custom_objects['dictVectorizer']

model_runner = model_ref.to_runner()

svc = bentoml.Service("candidate_status_classifier", runners=[model_runner])

input_spec = JSON(pydantic_model=Candidate)

@svc.api(input=input_spec, output=JSON())
def predict(Candidate):
    app_data = Candidate.dict()
    
    vector = dv.transform(app_data)
    prediction = model_runner.predict_proba.run(vector)[:,1]

    print(prediction)


    if prediction > 0.62:
        return {"candidate status prediction" : "WILL JOIN THE COMPANY"}
    else:
        return {"candidate status prediction" : "WON'T JOIN THE COMPANY"}
