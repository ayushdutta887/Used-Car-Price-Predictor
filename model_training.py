print("SCRIPT STARTED")
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import pickle
import datetime

# Load dataset
df = pd.read_csv('data/car_data.csv')

# Create car age
current_year = datetime.datetime.now().year
df['car_age'] = current_year - df['year']

# Drop unused columns
df.drop(['name', 'year'], axis=1, inplace=True)

# Convert categorical to numeric
df = pd.get_dummies(df, drop_first=True)

# Split data
X = df.drop('selling_price', axis=1)
y = df['selling_price']

print(X.columns)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = RandomForestRegressor()
model.fit(X_train, y_train)

# Save model
pickle.dump(model, open('model/car_price_model.pkl', 'wb'))

print("✅ Model trained and saved successfully!")