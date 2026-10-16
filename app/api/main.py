from fastapi import FastAPI, HTTPException

from app.services import pet_service

app = FastAPI(
    title="Happy Paw 3 API",
    description="Pet Management API",
    version="1.0.0",
)


@app.get("/")
def home() -> dict[str, str]:
    return {"message": "Welcome to Happy Paw 3 API"}


@app.get("/pets")
def get_all_pets() -> list[dict]:
    return pet_service.get_all_pets()


@app.get("/pets/{pet_id}")
def get_pet(pet_id: int) -> dict:
    pet = pet_service.get_pet(pet_id)
    if pet is None:
        raise HTTPException(status_code=404, detail="Pet not found")
    return pet
