from typing import Literal
from mercapy import Product as MercadonaProduct


class Product(MercadonaProduct):
    def __init__(
        self,
        id: str | dict,
        warehouses: list[str],
        language: Literal["es"] | Literal["en"] = "es",
    ):
        self.warehouses = warehouses
        super().__init__(id, warehouses[0], language)

    def add_warehouse(self, warehouse: str):
        if warehouse in self.warehouses:
            return

        self.warehouses.append(warehouse)

    def __dict__(self):
        return {**self._data, "warehouses": self.warehouses, "language": self.language}
