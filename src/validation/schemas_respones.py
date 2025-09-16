from dataclasses import dataclass
from typing import List, Dict


@dataclass
class FullPetObject:
    id: int
    category: Dict[str, int | str]
    name: str
    photoUrls: List[str]
    tags: List[Dict[str, int | str]]
    status: str