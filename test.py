import bentoml
from sklearn import datasets

runner = bentoml.sklearn.get("iris_svm_model:latest").to_runner()
runner.init_local()

sample = [[5.9, 3.0, 5.1, 1.8]]

prediction = runner.predict.run(sample)

iris = datasets.load_iris()
predicted_label = iris.target_names[prediction[0]]

print("Input:", sample)
print(f"Hasil Prediksi: {predicted_label} (kelas {prediction[0]})")
