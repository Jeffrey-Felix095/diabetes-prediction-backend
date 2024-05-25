import uvicorn

from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from actions import load_models
from routers import predict


@asynccontextmanager
async def init(app: FastAPI):
    # The first part of the function, before the yield, will be executed before the application starts.
    
    models = load_models()
    print(models)

    yield
    # And the part after the yield will be executed after the application has   finished.
    

app = FastAPI(lifespan=init)

# Configuración de CORS
origins = [
    "http://localhost",
    "http://localhost:8000",
    # agrega las URLs del frontend aquí,
    "http://localhost:8501",
    "https://diabetes-prediction-uninorte.streamlit.app/"
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