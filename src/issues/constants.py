from enum import StrEnum, auto
from functools import lru_cache


class Status(StrEnum):
    OPENED = auto()  # "OPENED"
    ASSIGNED = auto()  # "ASSIGNED"
    CLOSED = auto()  # "CLOSED"

    @classmethod
    @lru_cache(maxsize=1)
    def choices(cls) -> list[tuple[str, str]]:
        results = []
        for element in cls:
            el = (element.value, element.value)
            results.append(el)
        return results
