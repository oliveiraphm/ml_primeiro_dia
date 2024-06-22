from fastapi import FastAPI
import joblib
from pydantic import BaseModel

app = FastAPI()

modelo = joblib.load("modelo_casas.pkl")

class EspecificacoesCasa(BaseModel):
    tamanho: int
    quartos: int
    n_vagas: int

@app.post("/prever/")
def prever_preco(especificacoes_casa: EspecificacoesCasa):
    
    dados_entrada = [[especificacoes_casa.tamanho, especificacoes_casa.quartos, especificacoes_casa.n_vagas]]
    preco_estimado = modelo.predict(dados_entrada)[0]
    return {
        "preco_estimado": round(preco_estimado, 2)
    }