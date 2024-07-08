from fastapi import APIRouter, HTTPException

router = APIRouter()

@router.put(
    "/", status_code=200 , tags=["test"]
)
def test():
    return {"message": "Test route is working!"}