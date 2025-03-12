# Represents the products
# name, price, url, store, in stock

from dataclasses import dataclass
from decimal import Decimal
from models.store import Store

# @ tells python, that the different fields,
# will be publicly accessible from outside the class
@dataclass
class Product:
    id: str
    name: str
    price: Decimal
    url: str
    store: Store
    in_stock: bool
    
    def __str__(self) -> str:
        status = "INSTOCK" if self.in_instock else "OUT OF STOCK"
        return f"{self.id} is {status} at {self.store.name} at price ${self.price}"
