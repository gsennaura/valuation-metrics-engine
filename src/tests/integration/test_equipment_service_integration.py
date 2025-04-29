import pytest
from services.equipment_service import EquipmentService
from models.exceptions import ModelNotFoundError, InvalidYearError
from models.value_response import ValueResponse

@pytest.fixture
def service():
    return EquipmentService("api-response.json")

def test_valid_model_and_year(service):
    # Should return a valid ValueResponse when both model ID and year exist
    result = service.get_equipment_value("67352", "2007")
    assert isinstance(result, ValueResponse)
    assert result.marketValue > 0
    assert result.auctionValue > 0

def test_invalid_model_id(service):
    # Should raise ModelNotFoundError when model ID is not found in the dataset
    with pytest.raises(ModelNotFoundError):
        service.get_equipment_value("99999", "2007")

def test_valid_model_missing_year_uses_default(service):
    # Should fallback to default ratios when year is not found but defaults are available
    result = service.get_equipment_value("67352", "2099")
    assert isinstance(result, ValueResponse)
    assert result.marketValue > 0
    assert result.auctionValue > 0

def test_missing_year_and_no_default(service):
    # This test assumes the JSON contains a model without default ratios defined.
    # You must add such a case to api-response.json for this to pass.
    pytest.xfail("Requires a model in api-response.json without default ratios.")
    with pytest.raises(InvalidYearError):
        service.get_equipment_value("SOME_MODEL_WITHOUT_DEFAULTS", "2010")
