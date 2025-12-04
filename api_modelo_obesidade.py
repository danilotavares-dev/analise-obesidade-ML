from flask import Flask, jsonify, request
from pydantic import BaseModel
from flask_pydantic import validate
import joblib
import pandas as pd

app = Flask(__name__)

class request_body(BaseModel):
    Genero_Masculino: int
    Idade: int
    Historico_Familiar_Sobrepeso: int
    Consumo_Alta_Caloria_Com_Frequencia: int
    Consumo_Vegetais_Com_Frequencia: int
    Refeicoes_Dia: int
    Consumo_Alimentos_entre_Refeicoes: int
    Fumante: int
    Consumo_Agua: int
    Monitora_Calorias_Ingeridas: int
    Nivel_Atividade_Fisica: int
    Nivel_Uso_Tela: int
    Consumo_Alcool: int
    Transporte_Automovel: int
    Transporte_Bicicleta: int
    Transporte_Motocicleta: int
    Transporte_Publico: int
    Transporte_Caminhada: int

modelo_obesidade = joblib.load('./modelo_obesidade.pkl')

@app.route('/predict', methods=['POST'])
@validate()

def predict(body: request_body):
    predict_df = pd.DataFrame(body.model_dump(), index=[0])

    bins = [10, 20, 30, 40, 50, 60, 70]
    bins_ordinal = [0, 1, 2, 3, 4, 5]
    predict_df['faixa_etaria'] = pd.cut(x = predict_df['Idade'], bins=bins, labels=bins_ordinal, include_lowest = True)

    predict_df = predict_df[[
        'Historico_Familiar_Sobrepeso',
        'Consumo_Alta_Caloria_Com_Frequencia',
        'Consumo_Alimentos_entre_Refeicoes',
        'Monitora_Calorias_Ingeridas',
        'Nivel_Atividade_Fisica',
        'Nivel_Uso_Tela',
        'Transporte_Caminhada',
        'faixa_etaria'
    ]]

    y_pred = modelo_obesidade.predict(predict_df)[0].astype(int)

    return jsonify({'Obesidade': y_pred.tolist()})

if __name__ == '__main__':
    app.run(port=5000, debug=True)
