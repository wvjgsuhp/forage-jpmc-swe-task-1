from typing import List, TypedDict


class Bid(TypedDict):
    price: float
    size: int


class Quote(TypedDict):
    top_ask: Bid
    timestamp: str
    top_bid: Bid
    id: str
    stock: str


Quotes = List[Quote]
