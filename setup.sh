#!/bin/bash
echo "Membuat virtual environment..."
python3 -m venv venv
source venv/bin/activate

echo "Menginstal dependensi..."
pip install -r requirements.txt

echo "Melatih model dan menyimpan ke BentoML store..."
python3 train.py

echo "Menjalankan pengujian prediksi..."
python3 test.py

echo "Menjalankan API BentoML di http://localhost:3000"
bentoml serve service:svc --port 3000
