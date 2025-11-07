import pandas as pd
from sklearn.preprocessing import LabelEncoder
import joblib

# Load your dataset (the same one you trained on)
df = pd.read_csv("C:\\Users\\user\\Downloads\\career_guidance_system\\career_guidance_backend\\career_guidance_dataset.csv")

# --- Step 1: Encode the "preferred_subject" column ---
subject_encoder = LabelEncoder()
df["preferred_subject"] = subject_encoder.fit_transform(df["preferred_subject"])

# --- Step 2: Encode the "career" target column ---
career_encoder = LabelEncoder()
df["career"] = career_encoder.fit_transform(df["career"])

# --- Step 3: Save both encoders ---
joblib.dump(subject_encoder, "subject_encoder.pkl")
joblib.dump(career_encoder, "label_encoder.pkl")

print("✅ Encoders saved successfully: subject_encoder.pkl and label_encoder.pkl")
