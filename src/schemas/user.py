from pydantic import BaseModel
from typing import List, Optional, Union
from src.schemas.user_answers import TimeUsingVape, FrequencyUsingVape, TimesOfDayUsingVape, ReasonsUsingVape, StrategiesToQuit, HealthImpacts, Hobbies

class User(BaseModel):
    name: str
    email: str
    password: str
    creation_date: str = None
    time_using_vape: TimeUsingVape
    frequency_using_vape: FrequencyUsingVape
    times_of_day_using_vape: List[TimesOfDayUsingVape]
    reasons_using_vape: List[Union[ReasonsUsingVape, str]]
    tried_to_quit: bool
    biggest_challenge_imagined: Optional[str] = None
    quit_attempts: Optional[int] = None
    challenges_faced: Optional[str] = None
    strategies_to_quit: Optional[List[Union[StrategiesToQuit, str]]] = None
    failures: Optional[str] = None
    perceives_health_impact: bool
    health_impacts: Optional[List[Union[HealthImpacts, str]]] = None
    current_program_participation: bool 
    motivation_level: int
    hobbies: List[Union[Hobbies, str]]
    willing_to_receive_notifications: bool
    additional_habits_info: Optional[str] = None

    class Config:
        json_schema_extra = {
        "example": {
        "name": "John Doe",
        "email": "john@example.com",
        "password": "password123",
        "nickname": "John",
        "time_using_vape": "1-5 anos",
        "frequency_using_vape": "2-3 dias da semana",
        "times_of_day_using_vape": [
            "Ao acordar",
            "Durante a manhã"
        ],
        "reasons_using_vape": [
            "Estresse",
            "Prazer"
        ],
        "tried_to_quit": True,
        "biggest_challenge_imagined": "Ansiedade",
        "quit_attempts": 3,
        "challenges_faced": "Dificuldade em evitar amigos que fumam",
        "strategies_to_quit": [
            "Adesivos ou chicletes de nicotina",
            "Praticar exercícios físicos",
            "Outros: Uso de suplementos naturais"
        ],
        "failures": "Não consegui devido à ansiedade",
        "perceives_health_impact": True,
        "health_impacts": [
            "Problemas respiratórios",
            "Tosse crônica",
            "Outros: Perda de apetite"
        ],
        "current_program_participation": True,
        "motivation_level": 4,
        "hobbies": [
            "Leitura",
            "Academia",
            "Outros: Colecionar selos"
        ],
        "willing_to_receive_notifications": True,
        "additional_habits_info": "Gosto de ler antes de dormir"
            }
        }
