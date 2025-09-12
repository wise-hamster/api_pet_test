from dataclasses import dataclass, asdict
from typing import List, Dict, Any
import json



@dataclass
class PetObject:
    category: Dict[str, int | str] 
    name: str
    photoUrls: List[str]
    tags:List[Dict[str, int | str]]
    status: str


    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)

    def to_json(self, indent: int = 2) -> str:
        return json.dumps(self.to_dict(), indent=indent, ensure_ascii=False)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "PetObject":
        return cls(**data)

    @classmethod
    def from_json(cls, json_str: str) -> "PetObject":
        return cls.from_dict(json.loads(json_str))