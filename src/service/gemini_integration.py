from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os

load_dotenv()
key = os.getenv("GEMINI_API_KEY")

llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    google_api_key= key
)

messages = [
    ("system",
     "Vou passar para você um dataset de três colunas. Uma delas é um timestamp, a outra é a localização do usuário e a terceira é se o usuário está com vontade de fumar ou não. Preciso que você analise as colunas de localização e de timestamp para prever se o usuário está com vontade de fumar ou não",
    ),
    ("user",
        
        '''2024-01-10 23:01:00 -10.740051   82.287765             0
        2024-01-14 16:54:00 -13.406533  -33.199698             1
        2024-01-20 08:40:00 -30.692331 -138.501117             0
        2024-01-26 07:17:00  15.612444  107.609661             0
        2024-01-30 23:25:00  64.009259 -150.670515             0
        2024-01-02 06:36:00  62.802653 -138.765478             0
        2024-01-05 05:33:00  -8.059404   97.947400             1
        2024-01-22 14:51:00 -31.559359  -23.528834             0
        2024-01-06 17:35:00 -60.027054 -124.082342             0
        2024-01-18 03:39:00  -3.589850  149.260255             1
        2024-01-04 00:52:00  83.567070  -62.123495             0
        2024-01-13 09:02:00  83.264587   -7.975343             0
        2024-01-09 18:45:00  58.789910   64.742032             0
        2024-01-17 09:42:00 -15.025321  -56.872865             0
        2024-01-07 07:03:00  -6.847978 -133.785701             0
        2024-01-20 15:38:00  47.964072   82.597830             0
        2024-01-15 05:08:00 -11.200502  -40.185328             1
        2024-01-13 19:35:00 -55.349770   91.919977             0
        2024-01-30 16:30:00 -21.546100   68.687655             0
        2024-01-19 11:23:00 -73.335654  132.528573             1'''),
]
ai_msg = llm.invoke(messages)
print(ai_msg.content)