
from fastapi import APIRouter

from schemas.transactions import TransactionCreate, TransactionResponse

router = APIRouter(
    prefix="/transactions",
    tags=["Transactions"],
)


@router.post("", response_model=TransactionResponse)
def create_transaction(transaction: TransactionCreate):
    return TransactionResponse(
        id=1,
        item=transaction.item,
        quantity=transaction.quantity,
        amount=transaction.amount,
        payment_mode=transaction.payment_mode,
        status="success",
    )
