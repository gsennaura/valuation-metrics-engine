from domain.value_calculator import calculate_equipment_value

def test_value_calculation():
    result = calculate_equipment_value(100000, 0.3, 0.2)
    assert result.marketValue == 30000.0
    assert result.auctionValue == 20000.0

def test_zero_cost():
    result = calculate_equipment_value(0, 0.5, 0.5)
    assert result.marketValue == 0.0
    assert result.auctionValue == 0.0
