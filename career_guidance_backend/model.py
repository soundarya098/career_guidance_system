import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import joblib

# Load dataset
df = pd.read_csv("career_guidance_dataset.csv")

# Encode categorical features
subject_encoder = LabelEncoder()
career_encoder = LabelEncoder()

df['preferred_subject'] = subject_encoder.fit_transform(df['preferred_subject'])
df['career'] = career_encoder.fit_transform(df['career'])

# Split into features and target
X = df.drop(columns=['career'])
y = df['career']

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model training
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save model and encoders
joblib.dump(model, "career_model.pkl")
joblib.dump(subject_encoder, "subject_encoder.pkl")
joblib.dump(career_encoder, "career_encoder.pkl")

print("✅ Model trained and saved successfully as 'career_model.pkl'!")
