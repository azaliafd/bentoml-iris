import bentoml
from sklearn import svm, datasets
import pandas as pd

iris = datasets.load_iris()

X, y = iris.data, iris.target
feature_names = iris.feature_names
target_names = iris.target_names

df = pd.DataFrame(X, columns=feature_names)
df["target"] = y

print("\nPreview Dataset Iris:")
print(df.head())

print("\nLabel unik dalam dataset:")
for idx, name in enumerate(target_names):
    print(f"  {idx}: {name}")

model = svm.SVC(gamma="scale")
model.fit(X, y)

model_ref = bentoml.sklearn.save_model("iris_svm_model", model)

print(f"\nModel berhasil dilatih dan disimpan ke BentoML store:")
print(f"   {model_ref}")
