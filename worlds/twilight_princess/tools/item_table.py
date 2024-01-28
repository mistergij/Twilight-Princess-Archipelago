"""Dictionary of items IDs to use for receiving"""
import dataclasses


@dataclasses.dataclass
class Item:
    """Class that defines a datatype for sending and receiving items"""

    name: str
    address: int


item_table = []
