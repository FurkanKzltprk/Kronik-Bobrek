# Laboratuvar Verilerinden Kronik Böbrek Hastalığı Sınıflandırması

Fırat Üniversitesi Bilgisayar Mühendisliği Tasarım Dersi projesi.
Ekip: Eren Yığmatepe (Kaptan), Furkan Kızıltoprak, Yunus Emre Suna

Rutin laboratuvar ve klinik değerlerden bir hastanın kronik böbrek hastalığı (KBH) olup olmadığını tahmin eden makine öğrenmesi modelleri.

## Veri seti
UCI Machine Learning Repository - Chronic Kidney Disease (400 kayıt, 24 özellik, ckd / notckd)
https://archive.ics.uci.edu/dataset/336/chronic+kidney+disease

## Klasör yapısı
```
data/        veri seti (ARFF)
src/         ortak Python kodları (veri okuma vb.)
notebooks/   analiz ve modelleme notebook'ları
figures/     notebook'ların ürettiği grafikler
```

## Kurulum
```bash
python -m venv .venv
source .venv/Scripts/activate      # Windows Git Bash
pip install -r requirements.txt
```

## Notebook'lar
| Dosya | İçerik |
|---|---|
| `notebooks/01_EDA.ipynb` | Keşifsel veri analizi: sınıf dağılımı, eksik değerler, sınıflara göre laboratuvar değerleri |
