import datetime
from dataclasses import dataclass


def main():
    @dataclass
    class Product:
        id: str
        parent: str
        title: str
        category: str

    @dataclass
    class Review:
        id: str
        customer_id: str
        stars: int
        headline: str
        body: str
        date: datetime.datetime


if __name__ == '__main__':
    main()
