# model_training.py
import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV, StratifiedKFold
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import pickle

# Set random seed for reproducibility
RANDOM_STATE = 42

# Load the data
df = pd.read_csv("data/Website Phishing.csv")

# Convert column names to lowercase
df.columns = df.columns.str.lower()

# Convert target: -1 (Phishing) to 0, keep 1 (Legitimate) as 1
print("Original target distribution:")
print(df['result'].value_counts())

# Convert values
df['result'] = df['result'].replace(-1, 0)

print("\nNew target distribution:")
print(df['result'].value_counts())

# Split features and target
X = df.drop('result', axis=1)
y = df['result']

# Split into train and test sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, stratify=y, random_state=RANDOM_STATE
)

# Define Random Forest Classifier
rf_model = RandomForestClassifier(random_state=RANDOM_STATE)

# Define parameter grid
param_grid = {
    'n_estimators': [100, 200],
    'max_depth': [None, 10, 20],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4],
    'max_features': ['sqrt', 'log2'],
    'criterion': ['gini', 'entropy']
}

# Set up GridSearchCV
cv = StratifiedKFold(n_splits=5)
grid_search = GridSearchCV(
    estimator=rf_model,
    param_grid=param_grid,
    cv=cv,
    scoring='accuracy',
    n_jobs=-1,
    verbose=0
)

# Fit model
grid_search.fit(X_train, y_train)

# Get best parameters
best_params = grid_search.best_params_
print(f"\nBest parameters: {best_params}")

# Create model with best parameters
best_rf_model = RandomForestClassifier(
    random_state=RANDOM_STATE,
    **best_params
)

# Train the model
best_rf_model.fit(X_train, y_train)

# Make predictions
y_pred = best_rf_model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f"\nModel accuracy on test data: {accuracy:.4f}")

# Print classification report
print("\nClassification Report:")
target_names = ['Phishing (0)', 'Legitimate (1)']
print(classification_report(y_test, y_pred, target_names=target_names))

# Save the model to file
model_filename = 'models/RFC_best_model.pkl'
with open(model_filename, 'wb') as file:
    pickle.dump(best_rf_model, file)

print(f"\nModel saved to {model_filename}")