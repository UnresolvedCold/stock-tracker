import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score

# Load your historical stock data with 'buy' column
# Assuming you have a CSV file with columns: 'Date', 'Open', 'High', 'Low', 'Close', 'Volume', 'buy'
data = pd.read_csv('data/INFY.NS.csv')

# Remove first 22 data
data = data.iloc[22:]

# Define features (X) and target (y)
X = data[['Open', 'High', 'Low', 'Close', 'Volume', 'rsi21', 'ema21', 'ema7', 'volume7', 'day1', 'day2', 'day3', 'day4', 'day5', 'day6', 'day7']]
y = data['buy']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train a Random Forest Classifier
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)

# Make predictions on the test set
y_pred = clf.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
classification_report_str = classification_report(y_test, y_pred)

print(f"Accuracy: {accuracy:.2f}")
print("Classification Report:\n", classification_report_str)
