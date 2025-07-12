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
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
from sklearn.ensemble import RandomForestClassifier


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


# # # Section of the course:
# 03. Validação cruzada
# # #


# # # Section of the course:
# 04. Balanceamento de dados
# # #