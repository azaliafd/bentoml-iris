import numpy as np
import bentoml
from bentoml.io import NumpyNdarray

model_runner = bentoml.sklearn.get("iris_svm_model:latest").to_runner()

svc = bentoml.Service("bentoml_iris_service", runners=[model_runner])

@svc.api(input=NumpyNdarray(), output=NumpyNdarray())
def classify(input_array: np.ndarray) -> np.ndarray:
    """
    API endpoint untuk klasifikasi bunga Iris.
    Input: array 2D berisi fitur [sepal length, sepal width, petal length, petal width]
    Output: hasil prediksi dalam bentuk label numerik (0, 1, 2)
    """
    prediction = model_runner.predict.run(input_array)
    return prediction
