import torch
import joblib
import pandas as pd
import numpy as np
from models import CNNIDS, LSTMIDS, TransformerIDS
from utils import preprocess_data

import os

device = torch.device('cpu')
base_dir = os.path.dirname(os.path.abspath(__file__))

print("=== 1. Checking Models and Checkpoints ===")
for m in ['CNN', 'LSTM', 'Transformer']:
    ckpt_path = os.path.join(base_dir, "saved_models", f"saved_model_{m}.pt")
    if not os.path.exists(ckpt_path):
        ckpt_path = os.path.join(base_dir, f"saved_model_{m}.pt")
    ckpt = torch.load(ckpt_path, map_location=device, weights_only=False)
    input_dim = ckpt["input_dim"]
    num_classes = ckpt["num_classes"]
    print(f"[{m}] input_dim: {input_dim}, num_classes: {num_classes}")
    
    if m == "CNN":
        model = CNNIDS(input_dim, num_classes)
    elif m == "LSTM":
        model = LSTMIDS(input_dim, 64, num_classes)
    elif m == "Transformer":
        model = TransformerIDS(input_dim, num_classes)
        
    model.load_state_dict(ckpt["model_state_dict"])
    model.eval()
    print(f"[{m}] Weights successfully loaded into architecture!")
    
    le_path = os.path.join(base_dir, "saved_models", f"label_encoder_{m}.pkl")
    if not os.path.exists(le_path):
        le_path = os.path.join(base_dir, f"label_encoder_{m}.pkl")
    le = joblib.load(le_path)
    print(f"[{m}] Label encoder classes ({len(le.classes_)}): {list(le.classes_)}")

print("\n=== 2. Testing Sample Prediction on Testing_csv.csv ===")
csv_path = os.path.join(base_dir, "data", "Testing_csv.csv")
if not os.path.exists(csv_path):
    csv_path = os.path.join(base_dir, "Testing_csv.csv")
df = pd.read_csv(csv_path)
print("Testing CSV shape:", df.shape)
print("Columns in Testing CSV:", list(df.columns[:5]), "...")

# Preprocess
df_proc = preprocess_data(df)
if "label" in df_proc.columns:
    X = df_proc.drop("label", axis=1).values.astype(np.float32)
else:
    X = df_proc.values.astype(np.float32)

print("Processed feature matrix shape:", X.shape)
tensor_x = torch.tensor(X)

with torch.no_grad():
    outputs = model(tensor_x)
    preds = torch.argmax(outputs, dim=1).numpy()

pred_labels = le.inverse_transform(preds)
print("Sample Predictions (first 5):", pred_labels[:5])
print("Summary distribution of predictions:")
print(pd.Series(pred_labels).value_counts())
print("\n=== Test Pipeline Completed Successfully! ===")
