from nicegui import ui

from app.services import pet_service

ui.label("Happy Paw 3 - Pet Hotel").classes("text-h4")
ui.label("Pet Management System")

pets = pet_service.get_all_pets()
ui.table(
    columns=[
        {"name": "id", "label": "ID", "field": "id"},
        {"name": "name", "label": "Name", "field": "name"},
        {"name": "type", "label": "Type", "field": "type"},
        {"name": "breed", "label": "Breed", "field": "breed"},
        {"name": "age", "label": "Age", "field": "age"},
        {"name": "owner_name", "label": "Owner", "field": "owner_name"},
    ],
    rows=pets,
    row_key="id",
).classes("w-full")

ui.run(title="Happy Paw 3", port=8080, reload=False)
