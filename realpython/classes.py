"""Dátumosztályok."""
import datetime
from dataclasses import dataclass


@dataclass
class Product:
    """Termékosztály."""

    id: str
    parent: str
    title: str
    category: str


@dataclass
class Review:
    """Review osztály."""

    id: str
    customer_id: str
    stars: int
    headline: str
    body: str
    date: datetime.datetime
