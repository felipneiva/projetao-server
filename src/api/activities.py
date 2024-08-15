from fastapi import APIRouter, HTTPException
import random

router = APIRouter()

atividades = [
    "Beber um copo de água",
    "Fazer uma caminhada curta",
    "Mastigar chiclete ou comer uma bala sem açúcar",
    "Praticar respiração profunda",
    "Ler um livro ou artigo interessante",
    "Assistir a um vídeo motivacional",
    "Fazer um alongamento",
    "Escutar uma música relaxante ou animadora",
    "Praticar meditação ou mindfulness",
    "Escrever um diário ou suas razões para parar de fumar",
    "Conversar com um amigo ou familiar",
    "Fazer um quebra-cabeça ou jogo de lógica",
    "Cuidar de uma planta ou jardim",
    "Assistir a um episódio de uma série ou filme favorito",
    "Organizar ou limpar um espaço",
    "Tocar um instrumento musical ou aprender algo novo",
    "Fazer uma lista de gratidão",
    "Praticar exercícios físicos",
    "Tomar um banho relaxante",
    "Experimentar uma nova receita de comida saudável"
]

@router.get("/", status_code=200)
def get_atividades():
    try:
        atividades_selecionadas = random.sample(atividades, 3)
        return {"atividades": atividades_selecionadas}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

