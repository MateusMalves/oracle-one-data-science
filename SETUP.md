"""
==============================================
Oracle ONE - Data Science Course
==============================================

SETUP.md - Guia de Configuração do Projeto
Author: Mateus Alves de Mendonça
"""

# 🚀 Guia de Configuração - Oracle ONE Data Science

## 📋 Pré-requisitos

### 🐍 Python 3.8+
```bash
python --version  # Verificar versão
```

### 📦 Gerenciador de Pacotes
```bash
pip --version     # ou
conda --version
```

## ⚙️ Instalação

### 1️⃣ Clone o Repositório
```bash
git clone https://github.com/mateusmalves/oracle_one-data-science-course.git
cd oracle_one-data-science-course
```

### 2️⃣ Criar Ambiente Virtual
```bash
# Usando venv
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
.venv\Scripts\activate     # Windows

# Usando conda
conda create -n oracle_one python=3.9
conda activate oracle_one
```

### 3️⃣ Instalar Dependências
```bash
pip install pandas numpy matplotlib seaborn plotly streamlit scikit-learn imbalanced-learn yellowbrick
```

## 🎯 Como Usar

### 📚 Executar Cursos
```bash
# Navegar para um curso específico
cd 02-formacao_aprendendo-a-fazer-ETL/01-numpy_analise-numerica-eficiente-com-python/

# Executar o arquivo principal
python aula.py
```

### 🏆 Resolver Desafios
```bash
# Usar o template
cp template_desafio_hora-da-pratica.py meu_desafio.py

# Executar com interface CLI
python meu_desafio.py
```

### 🛠️ Utilitários
```python
# Carregar dados
from load_data import load_data
data = load_data('caminho/arquivo.csv', is_pandas=True)

# Criar gráficos
from plot_utils import label_plot
import matplotlib.pyplot as plt

plt.plot([1,2,3], [1,4,9])
label_plot(title="Meu Gráfico", xlabel="X", ylabel="Y²")
plt.show()
```

## 📁 Estrutura de Dados

Os datasets estão organizados em:
```
data/
├── 02-formacao_aprendendo-a-fazer-ETL/
├── 03-formacao_estatistica-e-machine-learning/
└── README.md
```

## 🔧 Troubleshooting

### ❌ Erro de Import
```python
# Adicionar ao início do arquivo
import sys
import os
sys.path.append(os.path.abspath('../../'))
```

### ❌ Erro de Path
```python
# Verificar diretório atual
import os
print(os.getcwd())
```

## 📞 Suporte

- 📧 **Issues**: [GitHub Issues](https://github.com/mateusmalves/oracle_one-data-science-course/issues)
- 💼 **LinkedIn**: [devmateusmalves](https://www.linkedin.com/in/devmateusmalves/)
- 📝 **Documentação**: Consulte cada módulo individual

---

**Última atualização**: Agosto 2025
