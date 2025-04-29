from pydantic import BaseModel

class ValueResponse(BaseModel):
    marketValue: float
    auctionValue: float