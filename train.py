import bentoml
from sklearn import svm, datasets

iris = datasets.load_iris()

X, y = iris.data, iris.target

model = svm.SVC(gamma="scale")
model.fit(X, y)

model_ref = bentoml.sklearn.save_model("iris_svm_model", model)

print(f"Model berhasil disimpan ke BentoML store: {model_ref}")
