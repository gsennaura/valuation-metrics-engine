from models.value_response import ValueResponse

def calculate_equipment_value(cost: float, market_ratio: float, auction_ratio: float) -> ValueResponse:
    """
    Calcula os valores de mercado e leilão com base no custo e nas taxas.

    Args:
        cost (float): Custo original do equipamento.
        market_ratio (float): Fator de mercado para cálculo.
        auction_ratio (float): Fator de leilão para cálculo.

    Returns:
        ValueResponse: Resultado contendo marketValue e auctionValue.
    """
    market_value = cost * market_ratio
    auction_value = cost * auction_ratio

    return ValueResponse(
        marketValue=round(market_value, 2),
        auctionValue=round(auction_value, 2),
    )