from app.repositories import pet_repository


def get_all_pets() -> list[dict]:
    return pet_repository.get_all_pets()


def get_pet(pet_id: int) -> dict | None:
    return pet_repository.get_pet_by_id(pet_id)
