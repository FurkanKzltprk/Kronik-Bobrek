"""Kronik Böbrek Hastalığı veri setini ARFF dosyasından okuyan yardımcı fonksiyonlar."""
from pathlib import Path

import pandas as pd

# Sayısal olarak kullanılacak sütunlar (sg, al, su sıralı kategoriler olduğu için sayıya çevrilir)
NUMERIC_COLS = ["age", "bp", "sg", "al", "su", "bgr", "bu", "sc",
                "sod", "pot", "hemo", "pcv", "wbcc", "rbcc"]


def load_ckd(path):
    """ARFF dosyasını okuyup temiz bir DataFrame döndürür.

    Dosyadaki bilinen format hataları burada düzeltilir:
    - bazı satırlardaki fazladan virgüller (boş alanlar atlanır)
    - değerlerin başında/sonunda kalan boşluk ve tab karakterleri
    - '?' ile gösterilen eksik değerler -> NaN
    """
    lines = Path(path).read_text(encoding="utf-8").splitlines()

    cols = [l.split()[1].strip("'") for l in lines if l.lower().startswith("@attribute")]
    start = next(i for i, l in enumerate(lines) if l.strip().lower() == "@data") + 1

    rows = []
    for line in lines[start:]:
        if not line.strip():
            continue
        values = [v.strip() for v in line.split(",") if v.strip() != ""]
        rows.append(values)

    bad = [i for i, r in enumerate(rows) if len(r) != len(cols)]
    if bad:
        raise ValueError(f"{len(bad)} satır {len(cols)} sütuna uymuyor: {bad[:5]}")

    df = pd.DataFrame(rows, columns=cols).replace("?", pd.NA)
    for c in NUMERIC_COLS:
        df[c] = pd.to_numeric(df[c], errors="coerce")
    return df
