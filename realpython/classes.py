from datetime import datetime
from dataclasses import dataclass


@dataclass
class Product:
    """
    Represents a product with an identifier, parent product, title, and category.

    Attributes:
        product_id (str): Unique identifier for the product.
        parent (str): Identifier of the parent product, if any.
        title (str): Name or title of the product.
        product_category (str): Category to which the product belongs.
        date (datetime): Date associated with the product (if any).
    """
    product_id: str
    parent: str
    title: str
    product_category: str
    date: datetime  # dátum lehet None is, ha nem áll rendelkezésre


@dataclass
class Review:
    """Represents a review left by a customer for a product."""

    id: str
    customer_id: str
    stars: int
    headline: str
    body: str
    date: datetime


@dataclass
class Strange:
    """Represents a strange object for a product"""

    helpvotes: int
    tot_votes: int
    vine: str
    veripurch: str
