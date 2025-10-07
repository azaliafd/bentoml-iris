# BentoML Iris Classifier

Proyek ini merupakan contoh sederhana bagaimana model Machine Learning dapat **di-deploy menjadi REST API** menggunakan **[BentoML](https://github.com/bentoml/BentoML)**.  
Model yang digunakan adalah **Support Vector Machine (SVM)** untuk melakukan klasifikasi dataset **Iris** dari `scikit-learn`.

---

## Struktur Proyek

Bentoml-Iris-Classifier_ML/
├── train.py 
├── test.py
├── service.py 
├── requirements.txt
├── bentofile.yaml
├── setup.sh
└── README.md

---

## Tools & Library yang Digunakan
**Python 3.10**: Bahasa utama pengembangan proyek
**BentoML 1.0.25**: Framework untuk model serving dan deployment ML sebagai REST API
**scikit-learn**: Library untuk training dan evaluasi model (SVM + dataset Iris)
**pandas**: Untuk manipulasi dan manajemen data tabular
**uvicorn**: ASGI server bawaan BentoML untuk menjalankan API
**aiohttp / starlette**: Library internal yang digunakan BentoML untuk menangani HTTP request async
**pyenv (opsional)**: Menjaga versi Python tetap konsisten antar environment 
**curl (opsional)**: Menguji endpoint API langsung dari terminal

---

## Cara Menjalankan

### 1. Persiapan Environment
Pastikan sudah menggunakan **Python 3.10 atau 3.11**  
(disarankan memakai `pyenv` agar versi Python stabil)
```bash
pyenv install 3.10.14
pyenv local 3.10.14
```
Lalu jalankan setup otomatis:
```bash
chmod +x setup.sh
./setup.sh
```
#### Script ini akan:
Membuat virtual environment (venv/)
Menginstal semua dependency
Melatih model dan menyimpannya ke BentoML store
Menguji prediksi model
Menjalankan API server di port 3000

### 2. Latih & Tes Model Secara Manual
Jika ingin menjalankan manual tanpa script:
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt pandas

python3 train.py
python3 test.py
```

### 3. Jalankan REST API BentoML
Aktifkan environment dulu:
```bash
source venv/bin/activate
```
Lalu jalankan service:
```bash
bentoml serve service:svc
```
Secara default, API berjalan di:
```bash
http://localhost:3000/classify
```
Jika port 3000 sudah digunakan:
```bash
bentoml serve service:svc --port 3001
```
#### Contoh Request API
Gunakan curl untuk melakukan prediksi:
``` bash
curl -X POST \
  -H "Content-Type: application/json" \
  --data '[[5.9,3.0,5.1,1.8]]' \
  http://localhost:3000/classify
```
Output:
[2]

# Tentang BentoML
BentoML adalah framework open-source untuk serving dan deployment model machine learning.
Ia memudahkan proses dari model training → packaging → serving API → deployment ke cloud atau container.
