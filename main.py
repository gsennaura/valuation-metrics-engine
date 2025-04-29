import logging
from src.services.equipment_service import EquipmentService
from src.models.exceptions import ModelNotFoundError, InvalidYearError

# Configure logging
logging.basicConfig(level=logging.INFO)

def main() -> None:
    try:
        service = EquipmentService("api-response.json")

        test_cases = [
            ("67352", "2007"),  # Valid
            ("87390", "2015"),  # Year not found, fallback to default
            ("99999", "2007"),  # Model ID not found
            ("87390", "2000"),  # Year not found, and if no default, should raise
        ]

        for model_id, year in test_cases:
            try:
                result = service.get_equipment_value(model_id, year)
                print(f"Model ID: {model_id}, Year: {year} -> {result}")
            except ModelNotFoundError as e:
                logging.warning(f"[Handled] {e}")
            except InvalidYearError as e:
                logging.warning(f"[Handled] {e}")

    except Exception as e:
        logging.error(f"[Fatal] Error while initializing the equipment service: {e}")

if __name__ == "__main__":
    main()
