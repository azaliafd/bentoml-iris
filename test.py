import bentoml

runner = bentoml.sklearn.get("iris_svm_model:latest").to_runner()
runner.init_local()

sample = [[5.9, 3.0, 5.1, 1.8]]
prediction = runner.predict.run(sample)

print(f"Hasil prediksi untuk {sample}: {prediction}")
