from pydantic import BaseModel, Field
from typing import Optional

class ProductModel(BaseModel):
    item_id: Optional[int] = None
    name: str
    code: str
    description: Optional[str] = Field(
        None, title="The description of the Product", max_length=300
    )
    price: float = Field(..., gt=0,
                         description="The price must be greater than zero")
