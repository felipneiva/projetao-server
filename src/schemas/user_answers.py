from enum import Enum

class TimeUsingVape(str, Enum):
    less_than_1_year = "Menos de 1 ano"
    one_to_five_years = "1-5 anos"
    five_to_ten_years = "5-10 anos"
    more_than_10_years = "Mais de 10 anos"

class FrequencyUsingVape(str, Enum):
    one_day_week = "1 dia da semana"
    two_to_three_days_week = "2-3 dias da semana"
    four_to_five_days_week = "4-5 dias da semana"
    more_than_five_days_week = "Mais de 5 dias da semana"

class TimesOfDayUsingVape(str, Enum):
    upon_waking = "Ao acordar"
    morning = "Durante a manhã"
    afternoon = "Durante a tarde"
    after_lunch = "Após o almoço"
    evening = "De noite"
    before_bed = "Antes de dormir"

class ReasonsUsingVape(str, Enum):
    stress = "Estresse"
    social_habit = "Hábito social"
    peer_pressure = "Pressão dos amigos"
    pleasure = "Prazer"
    anxiety = "Ansiedade"

class StrategiesToQuit(str, Enum):
    nicotine_patches_gums = "Adesivos ou chicletes de nicotina"
    prescribed_medication = "Medicamentos prescritos"
    exercise = "Praticar exercícios físicos"
    meditation_yoga = "Meditação e yoga"
    occupational_therapy_support_groups = "Terapia ocupacional e/ou grupos de apoio"
    avoid_social_smoking_situations = "Evitar situações sociais onde se fuma"
    keep_busy_with_hobbies = "Manter-se ocupado com hobbies"
    cessation_apps = "Aplicativos de cessação de hábitos"
    none = "Nenhum"

class HealthImpacts(str, Enum):
    respiratory_problems = "Problemas respiratórios"
    chronic_cough = "Tosse crônica"
    headaches = "Dores de cabeça"
    fatigue = "Fadiga"
    shortness_of_breath = "Falta de ar"
    chest_pain = "Dores no peito"

class Hobbies(str, Enum):
    reading = "Leitura"
    gym = "Academia"
    yoga = "Yoga"
    meditation = "Meditação"
    running = "Corrida"
    pilates = "Pilates"
    cooking = "Culinária"
    photography = "Fotografia"
    art = "Arte"
    music = "Música"
    guitar = "Violão"
    electric_guitar = "Guitarra"
    bass = "Baixo"
    drums = "Bateria"
    piano = "Piano"
    gardening = "Jardinagem"
    crafts = "Artesanato"
    knitting = "Tricô"
    sewing = "Costura"
    dancing = "Dança"
    movies_series = "Filmes e Séries"
    soccer = "Futebol"
    tennis = "Tênis"
    basketball = "Basquete"
    volleyball = "Vôlei"
    handball = "Handebol"
    fighting_ufc = "Luta e UFC"
    board_games = "Jogos de Tabuleiro"
    chess = "Xadrez"
    astronomy = "Astronomia"
    other = "Outro"

