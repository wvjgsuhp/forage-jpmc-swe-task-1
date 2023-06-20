from custom_types import Quote
from typing import Dict

quote: Dict[str, Quote] = {
    'normal': {
        'top_ask': {'price': 121.2, 'size': 36},
        'timestamp': '2019-02-11 22:06:30.572453',
        'top_bid': {'price': 120.48, 'size': 109},
        'id': '0.109974697771',
        'stock': 'ABC'
    },
    'bid_greater_than_ask': {
        'top_ask': {'price': 119.2, 'size': 36},
        'timestamp': '2019-02-11 22:06:30.572453',
        'top_bid': {'price': 120.48, 'size': 109},
        'id': '0.109974697771',
        'stock': 'ABC'
    }
}

price = {
    'a': 1,
    'b': 2
}
