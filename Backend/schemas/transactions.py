
from typing import Literal

from pydantic import BaseModel, Field


class TransactionCreate(BaseModel):
    item: str = Field(min_length=1, max_length=100)
    quantity: float = Field(gt=0)
    amount: float = Field(ge=0)
    payment_mode: Literal["cash", "upi", "card", "credit"]


class TransactionResponse(TransactionCreate):
    id: int
    status: str = "success"
