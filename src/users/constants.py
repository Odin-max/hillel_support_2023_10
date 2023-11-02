from enum import StrEnum
from functools import lru_cache


class Role(StrEnum):
    ADMIN = "AD"
    SENIOR = "SR"
    JUNIOR = "JR"

    @classmethod
    @lru_cache(maxsize=1)
    def choices(cls) -> list[tuple[str, str]]:
        # ['SR','JR']
        results = []

        for element in cls:
            el = (element.value, element.value.capitalize())
            results.append(el)

        return results
