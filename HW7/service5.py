import bentoml
from bentoml.io import JSON
from bentoml.io import NumpyNdarray

model_ref = bentoml.sklearn.get("mlzoomcamp_homework:qtzdz3slg6mwwdu5")

model_runner = model_ref.to_runner()

svc = bentoml.Service("Q5_model", runners=[model_runner])


@svc.api(input=NumpyNdarray(), output=JSON())
def classify(vector):
    prediction = model_runner.predict.run(vector)
    print(prediction)
    result = prediction[0]

    return result

    
