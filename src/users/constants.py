from enum import StrEnum
from functools import lru_cache


class Role(StrEnum):
    ADMIN = "AD"
    SENIOR = "SR"
    JUNIOR = "JR"

    @classmethod
    @lru_cache(maxsize=1)
    def choices(cls) -> list[tuple[str, str]]:
        # ['SR', 'JR']
        # [item for item in Role]
        results = []

        # for element in iter(Role)
        #   ==> 1: element = Role.ADMIN (.value == "AD") (.name == "ADMIN")
        #   ==> 2: element = Role.SENIOR (.value == "SR") (.name == "SENIOR")
        #   ==> 3: element = Role.JUNIOR (.value == "JR") (.name == "JUNIOR")

        for element in cls:
            el = (element.value, element.value)
            results.append(el)
        return results
