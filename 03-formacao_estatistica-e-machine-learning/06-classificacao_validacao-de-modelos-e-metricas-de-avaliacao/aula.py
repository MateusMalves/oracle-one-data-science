# # #
# بِسْمِ ٱللّٰهِ ٱلرَّحْمٰنِ ٱلرَّحِيمِ
# Bismillāh ir-raḥmān ir-raḥīm
# 
# In the name of God, the Most Gracious, the Most Merciful
# Em nome de Deus, o Clemente, o Misericordioso
# # #
# # #


# #
# Imports
import os
import sys
import re
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    confusion_matrix,
    ConfusionMatrixDisplay,
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    RocCurveDisplay,
    roc_auc_score,
    PrecisionRecallDisplay,
    average_precision_score,
    classification_report
)


cwd = os.getcwd()
while bool(re.search(r'\d-', cwd)):
    cwd = os.path.dirname(cwd)
load_data_path = os.path.join(cwd)
if load_data_path not in sys.path:
    sys.path.append(load_data_path)
from load_data import load_data

data_folder = cwd + '/data/03-formacao_estatistica-e-machine-learning/06-classificacao_validacao-de-modelos-e-metricas-de-avaliacao/'
outputs_folder = data_folder + 'outputs/'


# # # Section of the course:
# 01. Classificando dados
# # #
data = load_data(f'{data_folder}emp_automovel.csv', is_pandas=True)
data.head()
data.info()

# Creating an initial model
# 
x = data.drop(columns=['inadimplente'])
y = data['inadimplente']

model = DecisionTreeClassifier()
model.fit(x, y)
model.score(x, y)
print(f'Accuracy: {model.score(x, y):.2%}')

# Validating the model
# 
x, x_test, y, y_test = train_test_split(x, y, test_size=0.15, stratify=y, random_state=5)
x_train, x_val, y_train, y_val = train_test_split(x, y, stratify=y, random_state=5)

model = DecisionTreeClassifier()
model.fit(x_train, y_train)
print(f'Accuracy on training set: {model.score(x_train, y_train):.2%}')
print(f'Accuracy on validation set: {model.score(x_val, y_val):.2%}')

# Changing max depth
model = DecisionTreeClassifier(max_depth=10)
model.fit(x_train, y_train)
print(f'Accuracy on training set: {model.score(x_train, y_train):.2%}')
print(f'Accuracy on validation set: {model.score(x_val, y_val):.2%}')

# Evaluating the model
# 
# Building a confusion matrix
y_predicted = model.predict(x_val)
cm = confusion_matrix(y_val, y_predicted)
view = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=['Adimplente', 'Inadimplente'])
view.plot()

# Challenge: Using a Random Forest Classifier
# 
rf_model = RandomForestClassifier(
    n_estimators=100,       # Number of trees in the forest
    max_depth=None,         # Nodes are expanded until all leaves are pure or until all leaves contain less than min_samples_split samples
    min_samples_split=2,    # The minimum number of samples required to split an internal node
    min_samples_leaf=1,     # The minimum number of samples required to be at a leaf node
    max_features='sqrt',    # Number of features to consider at each split ('sqrt' is a good default for classification)
    random_state=5,         # Ensures reproducibility
    n_jobs=-1               # Use all available CPU cores
)
rf_model.fit(x_train, y_train)

# Evaluating the Random Forest model
print(f'Accuracy on training set (Random Forest): {rf_model.score(x_train, y_train):.2%}')
print(f'Accuracy on validation set (Random Forest): {rf_model.score(x_val, y_val):.2%}')

y_predicted_rf = rf_model.predict(x_val)

confusion_matrix_rf = confusion_matrix(y_val, y_predicted_rf)
print(confusion_matrix_rf)
view_rf = ConfusionMatrixDisplay(confusion_matrix=confusion_matrix_rf, display_labels=['Adimplente', 'Inadimplente'])
view_rf.plot()


# # # Section of the course:
# 02. Métricas de avaliação
# # #

# Measuring accuracy
# 
# Formula:
# Accuracy = (True Positives + True Negatives) / Total Samples
# 
accuracy = accuracy_score(y_val, y_predicted) # Formula: (8824 + 32) / (8824 + 32 + 82 + 820)
print(f'Accuracy: {accuracy:.2%}')

# Measuring precision and recall
# 
# Formulas:
# Precision = True Positives / (True Positives + False Positives)
# Recall = True Positives / (True Positives + False Negatives)
# 
precision = precision_score(y_val, y_predicted) # Formula: 32 / (32 + 82)
recall = recall_score(y_val, y_predicted) # Formula: 32 / (32 + 820)
print(f'Precision: {precision:.2%}')
print(f'Recall: {recall:.2%}')

# Measuring F1 Score
# 
# Formula:
# F1 Score = 2 * (Precision * Recall) / (Precision + Recall)
f1_score_value = f1_score(y_val, y_predicted) # Formula (approx.): 2 * (0.2807 * 0.0375) / (0.2807 + 0.0375)
print(f'F1 Score: {f1_score_value:.2%}')

# ROC curve: Receiver Operating Characteristic curve
# 
# ROC Curve: Plot of True Positive Rate (TPR) vs False Positive Rate (FPR)
# Formula:
# TPR (Recall) =  True Positives / (True Positives + False Negatives)
# FPR = False Positives / (False Positives + True Negatives)
RocCurveDisplay.from_predictions(y_val, y_predicted, name='Decision Tree Classifier') # AUC 0.51
auc = roc_auc_score(y_val, y_predicted) # Area Under the ROC Curve
print(f'AUC: {auc:.2f}')

# Precision-Recall curve
# 
PrecisionRecallDisplay.from_predictions(y_val, y_predicted, name='Decision Tree Classifier') # AP 0.10
ap = average_precision_score(y_val, y_predicted) # Average Precision
print(f'Average Precision: {ap:.2f}')

# Metrics Relatory
print(classification_report(y_val, y_predicted))


# # # Section of the course:
# 03. Validação cruzada
# # #


# # # Section of the course:
# 04. Balanceamento de dados
# # #