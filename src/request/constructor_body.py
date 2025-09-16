from dataclasses import dataclass, asdict, field
from typing import List, Dict, Any, Optional
import json

@dataclass
class PetObject:
    category: Optional[Dict[str, int | str]] = None
    name: Optional[str] = None
    photoUrls: Optional[List[str]] = None
    tags: Optional[List[Dict[str, int | str]]] = None
    status: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        return {k: v for k, v in asdict(self).items() if v is not None}

    def to_json(self, indent: int = 2) -> str:
        return json.dumps(self.to_dict(), indent=indent, ensure_ascii=False)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "PetObject":
        return cls(**data)

    @classmethod
    def from_json(cls, json_str: str) -> "PetObject":
        return cls.from_dict(json.loads(json_str))