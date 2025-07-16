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
import seaborn as sns
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from imblearn.over_sampling import SMOTE
from imblearn.under_sampling import NearMiss
from imblearn.pipeline import Pipeline as ImbPipeline
from sklearn.model_selection import (
    train_test_split,
    KFold,
    cross_validate,
    cross_val_score,
    StratifiedKFold,
    LeaveOneOut
)
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


# Case aula 3
# Enunciado do desafio
'''
1 - No processo de validação cruzada, são gerados diferentes modelos para cada divisão realizada nos dados e consequentemente diferentes valores de métricas de avaliação. Para encontrar um resultado médio das métricas, pode ser construído um intervalo de confiança a partir da média e desvio padrão das métricas. Crie uma função para calcular o intervalo de confiança dos resultados de uma validação cruzada com 2 desvios padrão. A função precisa de 2 parâmetros: um para receber uma lista com os resultados das métricas da validação cruzada e outro para receber o nome do algoritmo. Para gerar o intervalo de confiança, extraia a média dos resultados da lista e o desvio padrão. O intervalo de confiança deve ser apresentado em um print com o valor mínimo sendo a média subtraída de 2 desvios padrão e o valor máximo sendo a média somada de 2 desvios padrão. Exemplo de retorno da função:

# Intervalo de confiança ("nome do modelo"): ["valor mínimo do intervalo", "valor máximo do intervalo"]

2 - KFold é a estratégia mais simples de validação cruzada, que permite a divisão aleatória dos dados em k partes, sendo utilizada uma parte para validação e o restante para treinamento do modelo. O processo de criação de modelos é feito novamente até que todas as partes sejam utilizadas como validação. Sabendo disso, avalie o desempenho dos modelos com um intervalo de confiança utilizando a validação cruzada com o método KFold, usando 10 partes, com uso do parâmetro n_splits e embaralhando os dados antes da separação com o parâmetro shuffle. Use o método cross_val_score que não retorna o tempo de execução, apenas as métricas.

3 - No processo de divisão de dados com o KFold aleatório, pode ser que a proporção de cada categoria da variável alvo não seja mantida em cada uma das partes dos dados. Para manter essa proporção em cada uma das partes, podemos utilizar o KFold estratificado, deixando o processo de validação de dados bem mais consistente. Avalie o desempenho dos modelos com um intervalo de confiança utilizando a validação cruzada (cross_val_score) com o método StratifiedKFold, com uso do parâmetro n_splits e embaralhando os dados antes da separação com o parâmetro shuffle e avaliando a métrica F1-Score usando o parâmetro scoring.

4 - Em conjuntos de dados com poucos registros (poucas linhas), as estratégias de separação dos dados para validação podem fazer com que reste pouca informação nos dados de treinamento, fazendo com que o modelo não compreenda bem o padrão dos dados. O LeaveOneOut é uma estratégia para contornar esse problema, utilizando apenas um registro como dado de validação. Avalie o desempenho dos modelos utilizando a validação cruzada (cross_val_score) com o método LeaveOneOut.
'''

# 1. Confidence Interval Function
def interval_conf(results, model_name):
    average = results.mean()
    std_dev = results.std()
    confidence_interval = [average - 2 * std_dev, min(average + 2 * std_dev, 1)]

    print(f'=> Confidence Interval ({model_name}):\n[{confidence_interval[0]:.2%}, {confidence_interval[1]:.2%}]')

# 2. K-Fold Cross-Validation
def k_fold_cross_validation(model, x, y, n_splits=10):
    kf = KFold(n_splits=n_splits, shuffle=True, random_state=5)
    cv_results = cross_val_score(model, x, y, cv=kf)
    print(f'=> K-Fold Cross-Validation Results for {model.__class__.__name__}:')
    print(f'{cv_results}\n')
    interval_conf(cv_results, model.__class__.__name__)

# 3. Stratified K-Fold Cross-Validation
def stratified_k_fold_cross_validation(model, x, y, n_splits=10):
    skf = StratifiedKFold(n_splits=n_splits, shuffle=True, random_state=5)
    cv_results = cross_val_score(model, x, y, cv=skf, scoring='f1')
    print(f'=> Stratified K-Fold Cross-Validation Results for {model.__class__.__name__}:')
    print(f'{cv_results}\n')
    interval_conf(cv_results, model.__class__.__name__)

# 4. Leave-One-Out Cross-Validation
def leave_one_out_cross_validation(model, x, y):
    loo = LeaveOneOut()
    cv_results = cross_val_score(model, x, y, cv=loo)
    print(f'=> Leave-One-Out Cross-Validation Results for {model.__class__.__name__}:')
    print(f'{cv_results}\n')
    print(f'=> Average Accuracy: {cv_results.mean():.2%}')

k_fold_cross_validation(DecisionTreeClassifier(max_depth=10), x, y)
stratified_k_fold_cross_validation(DecisionTreeClassifier(max_depth=10), x, y)
leave_one_out_cross_validation(DecisionTreeClassifier(max_depth=10), x, y)


# Case Aula 4
# Enunciado do desafio
'''
1 - O desbalanceamento dos dados da variável alvo pode fazer com que o modelo fique tendencioso a acertar os padrões de apenas da categoria que tem maior quantidade, tornando necessário em alguns casos um tratamento específico de balanceamento de dados. A etapa inicial é identificar se existe ou não o desbalanceamento de dados na variável alvo. Por conta disso, verifique a proporção de dados da variável alvo do conjunto de dados de diabetes. Essa análise pode ser feita a partir da porcentagem de dados, usando o método value_counts(normalize=True) ou com a utilização de um gráfico de contagem, usando o gráfico countplot da biblioteca seaborn para entender se há um desbalanceamento de dados.

2 - Ao realizar o balanceamento de dados em uma validação cruzada, é necessário utilizar um pipeline, para que os dados de validação não sejam balanceados, se mantendo no padrão dos dados do mundo real. Utilize um pipeline contendo ajuste do modelo e o balanceamento dos dados usando o oversampling com SMOTE, obtendo a média do F1-Score de uma validação cruzada com StratifiedKFold.

3 - Além do oversampling, é possível utilizar a estratégia de undersampling para fazer o balanceamento dos dados. Apesar de serem estratégias distintas, ambas necessitam de um pipeline por se tratar de balanceamento de dados em uma validação cruzada. Utilize um pipeline contendo ajuste do modelo e o balanceamento dos dados usando o undersampling com NearMiss na sua versão 3, obtendo a média do F1-Score de uma validação cruzada com StratifiedKFold.

4 - Após realizar diversas análises e aprimorar o desempenho dos modelos, chega a etapa final, que consiste em selecionar o modelo com melhor desempenho e fazer a avaliação final em um conjunto de dados de teste, que não foi visto durante o processo de treinamento e validação. Escolha o modelo que obteve o melhor desempenho ao comparar as estratégias de oversampling e undersampling e treine um modelo usando todos os dados com a melhor estratégia. Realize a avaliação do modelo usando os dados de teste que foram separados no início dos desafios, obtendo o relatório de métricas e matriz de confusão.
'''

data['diabetes'].value_counts(normalize=True)
sns.countplot(data=data, x='diabetes')

def balancing(model, x, y, sampling_method, n_splits=10) -> None:
    print(f'Using {sampling_method.__class__.__name__}...\n')
    skf = StratifiedKFold(n_splits=n_splits, shuffle=True, random_state=5)
    pipeline = ImbPipeline([('smote', sampling_method), ('model', model)])
    cv_results = cross_val_score(pipeline, x, y, cv=skf, scoring='f1')
    print(f'=> Stratified K-Fold Cross-Validation Results for {model.__class__.__name__}:')
    print(f'{cv_results}')
    print(f'Length: {len(cv_results)}\n')
    interval_conf(cv_results, model.__class__.__name__)

model_tree = DecisionTreeClassifier(max_depth=10)
balancing(model_tree, x, y, SMOTE())
balancing(model_tree, x, y, NearMiss())

# SMOTE performed better
# Testing
def test_model(model, x, y, x_test, y_test, sampling_method) -> None:
    x_balanced, y_balanced = sampling_method.fit_resample(x, y) # type: ignore
    model.fit(x_balanced, y_balanced)
    y_predict = model.predict(x_test)

    print(classification_report(y_test, y_predict))
    ConfusionMatrixDisplay.from_predictions(y_test, y_predict)

test_model(model_tree, x, y, x_test, y_test, SMOTE())