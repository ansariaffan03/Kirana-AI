
from fastapi import FastAPI
from schemas.transactions import TransactionCreate, TransactionResponse
from routers.transactions import router as transactions_router
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from core.config import APP_NAME, APP_VERSION

app = FastAPI(
    title=APP_NAME,
    description="Backend API for the Kirana AI assistant",
    version=APP_VERSION,
)

app.include_router(transactions_router)

@app.exception_handler(Exception)
async def general_exception_handler(
    request: Request,
    exc: Exception,
):
    return JSONResponse(
        status_code=500,
        content={
            "detail": "An internal server error occurred."
        },
    )


@app.get("/")
def root():
    return {
        "message": "Kirana AI Backend is running"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "Kirana AI Backend",
    }

@app.post("/transactions", response_model=TransactionResponse)
def create_transaction(transaction: TransactionCreate):
    return TransactionResponse(
        id=1,
        item=transaction.item,
        quantity=transaction.quantity,
        amount=transaction.amount,
        payment_mode=transaction.payment_mode,
        status="success",
    )