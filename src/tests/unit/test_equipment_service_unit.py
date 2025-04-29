import pytest
from services.equipment_service import EquipmentService
from models.equipment_data import EquipmentData, Schedule, SaleDetails, Classification, YearRatios
from models.exceptions import ModelNotFoundError

@pytest.fixture
def mock_service():
    mock_data = {
        "67352": EquipmentData(
            schedule=Schedule(
                years={
                    "2007": YearRatios(marketRatio=0.5, auctionRatio=0.3)
                },
                defaultMarketRatio=0.1,
                defaultAuctionRatio=0.1
            ),
            saleDetails=SaleDetails(cost=100000, retailSaleCount=10, auctionSaleCount=5),
            classification=Classification(category="Earthmoving", subcategory="Dozers", make="Caterpillar", model="D8T")
        )
    }
    service = EquipmentService.__new__(EquipmentService)  # Bypass __init__
    service.data = mock_data
    return service

def test_get_equipment_value_valid(mock_service):
    result = mock_service.get_equipment_value("67352", "2007")
    assert result.marketValue == 50000.0
    assert result.auctionValue == 30000.0

def test_get_equipment_value_invalid_id(mock_service):
    with pytest.raises(ModelNotFoundError):
        mock_service.get_equipment_value("99999", "2007")

def test_get_equipment_value_missing_year(mock_service):
    result = mock_service.get_equipment_value("67352", "2010")
    assert result.marketValue == 10000.0
    assert result.auctionValue == 10000.0
