import json
import logging
from pathlib import Path
from typing import Dict

from domain.value_calculator import calculate_equipment_value
from models.equipment_data import EquipmentData
from models.value_response import ValueResponse
from models.exceptions import ModelNotFoundError, InvalidYearError

logger = logging.getLogger(__name__)


class EquipmentService:
    def __init__(self, json_path: str) -> None:
        """
        Initializes the EquipmentService by loading equipment data from a JSON file.

        Args:
            json_path (str): Path to the JSON file containing equipment data.
        """
        self.data: Dict[str, EquipmentData] = self._load_data(json_path)

    def _load_data(self, path: str) -> Dict[str, EquipmentData]:
        """
        Loads and parses the equipment data from a JSON file.

        Args:
            path (str): File path to the JSON file.

        Returns:
            Dict[str, EquipmentData]: Dictionary mapping model IDs to EquipmentData instances.

        Raises:
            FileNotFoundError: If the file does not exist.
            JSONDecodeError: If the file is not a valid JSON.
            Exception: For any unexpected errors during loading.
        """
        try:
            with Path(path).open("r") as file:
                raw_data = json.load(file)
            return {
                model_id: EquipmentData(**equipment)
                for model_id, equipment in raw_data.items()
            }
        except FileNotFoundError:
            logger.error(f"File {path} not found.")
            raise
        except json.JSONDecodeError:
            logger.error(f"Error decoding JSON in file {path}.")
            raise
        except Exception as e:
            logger.error(f"Unexpected error while loading file {path}: {e}")
            raise

    def get_equipment_value(self, model_id: str, year: str) -> ValueResponse:
        """
        Calculates the market and auction values for a given model ID and year.

        If specific year ratios are not available, default ratios are used.
        If no data is found or year/defaults are missing, appropriate exceptions are raised.

        Args:
            model_id (str): Equipment model identifier.
            year (str): Year for which to calculate values.

        Returns:
            ValueResponse: Object containing market and auction values.

        Raises:
            ModelNotFoundError: If the given model ID is not found.
            InvalidYearError: If the year is missing and no default ratios are available.
        """
        equipment = self.data.get(model_id)
        if not equipment:
            logger.error(f"Model ID {model_id} not found.")
            raise ModelNotFoundError(model_id)

        cost = equipment.saleDetails.cost
        year_data = equipment.schedule.years.get(year)

        if year_data:
            return calculate_equipment_value(
                cost, year_data.marketRatio, year_data.auctionRatio
            )

        default_market_ratio = equipment.schedule.defaultMarketRatio
        default_auction_ratio = equipment.schedule.defaultAuctionRatio

        if default_market_ratio is not None and default_auction_ratio is not None:
            logger.info(f"Year {year} not found for model {model_id}. Using default ratios.")
            return calculate_equipment_value(
                cost, default_market_ratio, default_auction_ratio
            )

        logger.error(f"Year {year} not found for model ID {model_id}, and no default ratios available.")
        raise InvalidYearError(year, model_id)
