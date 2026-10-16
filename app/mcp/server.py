from fastmcp import FastMCP

from app.services import pet_service

mcp = FastMCP("Happy Paw 3")


@mcp.tool()
def get_all_pets() -> list[dict]:
    """Retrieve all pets from MariaDB."""
    return pet_service.get_all_pets()


@mcp.tool()
def get_pet(pet_id: int) -> dict | None:
    """Retrieve a pet by its ID."""
    return pet_service.get_pet(pet_id)


if __name__ == "__main__":
    mcp.run()
