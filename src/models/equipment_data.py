from pydantic import BaseModel
from typing import Dict

class YearRatios(BaseModel):
    marketRatio: float
    auctionRatio: float

class SaleDetails(BaseModel):
    cost: float
    retailSaleCount: int
    auctionSaleCount: int

class Classification(BaseModel):
    category: str
    subcategory: str
    make: str
    model: str

class Schedule(BaseModel):
    years: Dict[str, YearRatios]
    defaultMarketRatio: float
    defaultAuctionRatio: float

class EquipmentData(BaseModel):
    schedule: Schedule
    saleDetails: SaleDetails
    classification: Classification