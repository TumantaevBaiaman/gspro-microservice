from pydantic import BaseModel


class ListPurchaseRequestsDTO(BaseModel):
    limit: int = 20
    offset: int = 0


class GetPurchaseRequestDTO(BaseModel):
    request_id: str