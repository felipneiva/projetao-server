import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

import google.generativeai as genai

genai.configure(api_key="AIzaSyB52dkFpdApMbHdtMUBmOHW7EjbyzZWuqo")


model = genai.GenerativeModel('gemini-1.5-flash')
response = model.generate_content("Estou com vontade de fumar. Sugira algumas atividades que me ajudem a distrair e reduzir o desejo de fumar. Você tem que me responder 3 atividades diferentes  \
                                   e aleatórias,  Dentre a seguinte lista:  \
                                Beber um copo de água \
                                Fazer uma caminhada curta \
                                Mastigar chiclete ou comer uma bala sem açúcar \
                                Praticar respiração profunda \
                                Ler um livro ou artigo interessante \
                                Assistir a um vídeo motivacional \
                                Fazer um alongamento \
                                Escutar uma música relaxante ou animadora\
                                Praticar meditação ou mindfulness \
                                Escrever um diário ou suas razões para parar de fumar \
                                Conversar com um amigo ou familiar \
                                Fazer um quebra-cabeça ou jogo de lógica \
                                Cuidar de uma planta ou jardim \
                                Assistir a um episódio de uma série ou filme favorito \
                                Organizar ou limpar um espaço \
                                Tocar um instrumento musical ou aprender algo novo \
                                Fazer uma lista de gratidão \
                                Praticar exercícios físicos \
                                Tomar um banho relaxante \
                                Experimentar uma nova receita de comida saudável \
                                Responda apenas no seguinte formato ['atividade 1', 'atividade 2', 'atividade 3']")
print(response.text)