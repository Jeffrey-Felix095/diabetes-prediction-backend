from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import predict
import uvicorn
app = FastAPI()

# Configuración de CORS
origins = [
    "http://localhost",
    "http://localhost:8000",
    # agrega las URLs del frontend aquí
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluye el router para las rutas del modelo de ML
app.include_router(predict.router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)