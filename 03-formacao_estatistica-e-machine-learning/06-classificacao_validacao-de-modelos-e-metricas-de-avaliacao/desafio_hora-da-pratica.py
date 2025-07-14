# # #
# بِسْمِ ٱللّٰهِ ٱلرَّحْمٰنِ ٱلرَّحِيمِ
# Bismillāh ir-raḥmān ir-raḥīm
# 
# In the name of God, the Most Gracious, the Most Merciful
# Em nome de Deus, o Clemente, o Misericordioso
# # #
# # #


# Case aula 1
# Enunciado do desafio
'''
1 - Para a construção de um modelo de machine learning são necessários dados. Como tarefa inicial, faça a leitura da base de dados de diabetes e realize a divisão dos dados em variáveis explicativas e variável alvo (x e y). A variável alvo é a coluna que quer classificar, contendo a informação se o paciente possui ou não a diabetes. As variáveis explicativas são todas as colunas com exceção da diabetes. A separação dos dados pode ser feita com a seleção de colunas com pandas.

2 - Uma etapa muito importante em projetos de classificação é a validação dos modelos, para identificar se está havendo a generalização do modelo para dados novos. Realize a divisão dos dados entre treino, validação e teste. Utilize 5% dos dados para teste e com o restante, deixe 25% para validação. No momento da separação, use o parâmetro stratify a partir da variável alvo para manter a proporção dos dados.

3 - A etapa de modelagem de dados consiste em utilizar um algoritmo capaz de identificar padrões nos dados e classificar os valores. A partir do modelo é possível extrair uma taxa de acerto para entender o seu desempenho. Crie 2 modelos utilizando os algoritmos DecisionTreeClassifier e RandomForestClassifer e avalie a acurácia de treino e teste, escolhendo o valor 3 para o parâmetro max_depth do algoritmo DecisionTreeClassifier e valor 2 para o max_depth do algoritmo RandomForestClassifier, para os modelos não se especializarem demais no padrão dos dados de treino.

4 - A taxa de acerto geralmente não fornece informações suficientes para entender o comportamento do modelo. A matriz de confusão é uma ferramenta mais completa, capaz de fornecer os acertos e erros do modelo para cada classe. Construa uma matriz de confusão para cada um dos modelos para avaliar o desempenho da previsão. Para construir a matriz, use o método predict para gerar as previsões dos valores e comparar com os valores reais da base de dados.
'''

# #
# Imports
import os
import sys
import re
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
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

# Import data
data = load_data(f'{data_folder}/diabetes.csv', is_pandas=True)

x = data.drop(columns=['diabetes'])
y = data['diabetes']

x, x_test, y, y_test = train_test_split(x, y, test_size=0.05, stratify=y, random_state=5)
x_train, x_val, y_train, y_val = train_test_split(x, y, test_size=0.25, stratify=y, random_state=5)

model_tree = DecisionTreeClassifier(max_depth=3)
model_tree.fit(x_train, y_train)

model_rf = RandomForestClassifier(max_depth=2)
model_rf.fit(x_train, y_train)

def evaluate_model(model, x_val, y_val):
    predicted = model.predict(x_val)
    accuracy = model.score(x_val, y_val)
    print(f'Accuracy of {model.__class__.__name__}: {accuracy:.2%}')

    cm = confusion_matrix(y_val, predicted)
    print(f'Confusion Matrix for {model.__class__.__name__}:\n{cm}')

    view = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=model.classes_)
    view.plot()

evaluate_model(model_tree, x_val, y_val)
evaluate_model(model_rf, x_val, y_val)


# Case aula 2
# Enunciado do desafio
'''
1 - Para uma avaliação completa de um modelo de classificação, podemos explorar métricas que avaliam a taxa de acerto geral e também para cada classe da variável alvo de forma individual. Extraia as métricas acurácia, recall, precisão e F1-Score dos modelos de classificação gerados no desafio da aula 1. A biblioteca Scikit-Learn possui funções para calcular cada uma das métricas, bastando fazer a importação e utilizar como parâmetros os valores reais e previstos pelo modelo.

2 - Além de métricas numéricas, gráficos podem ser explorados para avaliar o desempenho de um modelo e compreender se ele consegue diferenciar bem uma classe da outra. Obtenha a curva ROC e a métrica AUC dos modelos de classificação gerados no desafio da aula 1, comparando as curvas no mesmo gráfico. A curva ROC pode ser gerada usando o método RocCurveDisplay.from_predictions.

3 - Além da curva ROC, a curva de precisão x recall pode ser usada para avaliar o desempenho de modelos, sendo mais interessante para dados desbalanceados. Obtenha a curva precisão x recall e a métrica AP dos modelos de classificação gerados no desafio da aula 1, comparando as curvas no mesmo gráfico. A curva precisão x recall pode ser gerada usando o método PrecisionRecallDisplay.from_predictions.

4 - Um resumo das principais métricas de classificação pode ser muito útil para sumarizar as informações e gerar insights de forma rápida. Gere os relatórios de métricas dos modelos de classificação construídos no desafio da aula 1. O relatório de métricas pode ser gerado a partir da função classification_report da biblioteca Scikit-Learn.
'''

# 1. Get accuracy, recall, precision and F1-Score
def get_metrics(model, x_val, y_val) -> None:
    y_predicted = model.predict(x_val)
    
    accuracy = accuracy_score(y_val, y_predicted)
    precision = precision_score(y_val, y_predicted)
    recall = recall_score(y_val, y_predicted)
    f1 = f1_score(y_val, y_predicted)

    print(f'Accuracy: {accuracy:.2%}')
    print(f'Precision: {precision:.2%}')
    print(f'Recall: {recall:.2%}')
    print(f'F1 Score: {f1:.2%}')

# 2. ROC Curve and AUC
def get_roc_curve(model, x_val, y_val) -> None:
    y_predicted = model.predict(x_val)
    auc = roc_auc_score(y_val, y_predicted)
    print(f'AUC: {auc:.2f}')

    RocCurveDisplay.from_predictions(y_val, y_predicted, name=model.__class__.__name__)
    plt.title('ROC Curve')
    plt.show()
    plt.close()

# 3. Precision-Recall Curve and Average Precision
def get_precision_recall_curve(model, x_val, y_val) -> None:
    y_predicted = model.predict(x_val)
    ap = average_precision_score(y_val, y_predicted)
    print(f'Average Precision: {ap:.2f}')

    PrecisionRecallDisplay.from_predictions(y_val, y_predicted, name=model.__class__.__name__)
    plt.title('Precision-Recall Curve')
    plt.show()
    plt.close()

# 4. Classification Report
def get_classification_report(model, x_val, y_val) -> None:
    y_predicted = model.predict(x_val)
    report = classification_report(y_val, y_predicted)
    print(report)

# Evaluate models
models_to_evaluate = [model_tree, model_rf]
model_evaluation_functions = [
    get_metrics,
    get_roc_curve,
    get_precision_recall_curve,
    get_classification_report
]

for model in models_to_evaluate:
    print(f'\nEvaluating {model.__class__.__name__}:\n')
    for func in model_evaluation_functions:
        func(model, x_val, y_val)
        print('-' * 40)