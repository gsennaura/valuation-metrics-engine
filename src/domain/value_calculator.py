from models.value_response import ValueResponse

def calculate_equipment_value(cost: float, market_ratio: float, auction_ratio: float) -> ValueResponse:
    """
    Calculates the market and auction values based on the equipment cost and ratios.

    Args:
        cost (float): Original cost of the equipment.
        market_ratio (float): Ratio used to calculate market value.
        auction_ratio (float): Ratio used to calculate auction value.

    Returns:
        ValueResponse: An object containing marketValue and auctionValue.
    """
    market_value = cost * market_ratio
    auction_value = cost * auction_ratio

    return ValueResponse(
        marketValue=round(market_value, 2),
        auctionValue=round(auction_value, 2),
    )
