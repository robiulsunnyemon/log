from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from app.db.db import Base, engine
from app.routers.user import router as user_router


# Load .env
load_dotenv()

app = FastAPI(title="Login")


#Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)



# CORS
origins = [
    "http://localhost",
    "http://localhost:8000",
    "https://khalifa.mtscorporate.com",
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



# Root
@app.get("/", tags=["Root"])
async def root():
    return {"message": "Hello Login"}

# Include Routers
app.include_router(user_router)
