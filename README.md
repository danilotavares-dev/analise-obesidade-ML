# 🩺 Projeto de Predição de Risco de Obesidade

Este projeto consiste em uma solução completa de Machine Learning para prever o risco de obesidade com base em fatores demográficos, hábitos alimentares e estilo de vida. O sistema abrange desde a análise exploratória de dados (EDA) e treinamento do modelo até o deploy de uma API REST para consumo do modelo em produção.

## 📋 Sobre o Projeto

O objetivo é classificar se um indivíduo é considerado obeso ou não com base em um questionário de hábitos. O projeto foi desenvolvido seguindo as etapas de:
1. **Análise de Dados:** Estudo de correlações e distribuição das variáveis.
2. **Feature Engineering:** Tratamento de dados categóricos e numéricos.
3. **Otimização:** Uso do **Optuna** para encontrar os melhores hiperparâmetros.
4. **Modelagem:** Treinamento de um classificador **Gaussian Naive Bayes**.
5. **Engenharia de Dados:** Criação de uma API com **Flask** e validação de dados com **Pydantic**.

## 🛠️ Tecnologias Utilizadas

* **Linguagem:** Python 3.11.9
* **Gerenciamento de Dependências:** Pipenv
* **Machine Learning:** Scikit-learn, Optuna, Joblib
* **Análise de Dados:** Pandas, Numpy, Sweetviz, Plotly, Matplotlib
* **Backend/API:** Flask, Flask-Pydantic

## 📂 Estrutura do Projeto

* `modelo_obesidade.ipynb`: Jupyter Notebook contendo a EDA, seleção de features (SelectKBest) e o treinamento do modelo.
* `api_modelo_obesidade.py`: Aplicação Flask que expõe o endpoint `/predict`.
* `modelo_obesidade.pkl`: O modelo treinado serializado.
* `dataset_obesidade.csv`: Dataset original utilizado.
* `Pipfile` & `Pipfile.lock`: Arquivos de configuração do ambiente virtual.

## 🚀 Como Executar

### Pré-requisitos
Certifique-se de ter o Python e o [Pipenv](https://pipenv.pypa.io/en/latest/) instalados.


1. **Clone o repositório:**
   ```bash
    git clone https://github.com/danilotavares-dev/analise-obesidade-ML.git
    cd analise-obesidade-ML

2. **Instale as dependências:**
    ```bash
    pipenv install

3. **Ative o ambiente virtual:**
   ```bash
   pipenv shell

4. **Execute a API:**
   ```bash
   python api_modelo_obesidade.py
O servidor iniciará em http://127.0.0.1:5000 (ou porta configurada).


## 🔌 Documentação da API

**Endpoint:** `/predict`

* **Método:** `POST`
* **Descrição:** Recebe os dados de um paciente e retorna a predição.

### Exemplo de Requisição (JSON)

```json
{
  "Genero_Masculino": 1,
  "Idade": 26,
  "Historico_Familiar_Sobrepeso": 1,
  "Consumo_Alta_Caloria_Com_Frequencia": 1,
  "Consumo_Vegetais_Com_Frequencia": 3,
  "Refeicoes_Dia": 3,
  "Consumo_Alimentos_entre_Refeicoes": 1,
  "Fumante": 0,
  "Consumo_Agua": 2,
  "Monitora_Calorias_Ingeridas": 0,
  "Nivel_Atividade_Fisica": 0,
  "Nivel_Uso_Tela": 1,
  "Consumo_Alcool": 0,
  "Transporte_Automovel": 0,
  "Transporte_Bicicleta": 0,
  "Transporte_Motocicleta": 0,
  "Transporte_Publico": 1,
  "Transporte_Caminhada": 0
}
```
