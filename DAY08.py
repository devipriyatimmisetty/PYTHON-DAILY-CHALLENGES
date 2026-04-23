import random
import numpy as np
import pandas as pd

def gen_data(n):
    data = []
    for i in range(1, n + 1):
        sid = f"S{i}"
        m = random.randint(0, 100)
        att = random.randint(0, 100)
        a = random.randint(0, 50)

        pi = (m * 0.7 + a * 0.3) * (att / 100)

        data.append((sid, m, att, a, pi))
    return data


def classify(data):
    categories = {
        "At Risk": [],
        "Average": [],
        "Good": [],
        "Top Performer": []
    }

    for s in data:
        sid, m, att, a, pi = s

        if m < 40 or att < 50:
            categories["At Risk"].append(sid)
        elif 40 <= m <= 70:
            categories["Average"].append(sid)
        elif 71 <= m <= 90:
            categories["Good"].append(sid)
        elif m > 90 and att > 80:
            categories["Top Performer"].append(sid)

    return categories


def analyze(data):
    df = pd.DataFrame(data, columns=[
        "ID", "Marks", "Att", "Assign", "PI"
    ])

    arr = np.array(df["Marks"])

    # Manual mean
    mean = sum(arr) / len(arr)

    # NumPy calculations
    std = np.std(arr)
    mx = np.max(arr)

    # Convert correlation to normal float
    corrcoeff = float(np.corrcoef(df["Marks"], df["Att"])[0][1])

    # Normalization
    min_val = min(arr)
    max_val = max(arr)

    df["Norm"] = [
        (x - min_val) / (max_val - min_val) if max_val != min_val else 0
        for x in arr
    ]

    # Pattern detection
    cons = std < 15
    att_risk = len([x for x in df["Att"] if x < 50]) > 3
    high = len(df[df["Marks"] > 90]) >= 2

    if cons and not att_risk and high:
        status = "Stable Academic System"
    elif cons or high:
        status = "Moderate Performance"
    else:
        status = "Critical Attention Required"

    # Convert to normal Python types
    summ = (float(mean), float(std), int(mx))

    return df, summ, corrcoeff, status

n = 24110011665%10
data = gen_data(n)

df, summ, corrcoeff, status = analyze(data)

categories = classify(data)

# OUTPUT
print("\n--- Student Data ---")
print(df)
print("\n--- Categories ---")
print(categories)
print("\n--- Statistical Summary ---")
print("Mean:", round(summ[0], 2))
print("Std Dev:", round(summ[1], 2))
print("Max:", summ[2])
print("\n--- Correlation Coefficient ---")
print(round(corrcoeff, 2))
print("\n--- Final Insight ---")
print(status)
