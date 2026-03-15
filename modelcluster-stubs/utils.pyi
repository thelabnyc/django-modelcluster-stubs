from collections.abc import Sequence
from typing import Any

from django.db.models import Field, Model

REL_DELIMETER: str

class ManyToManyTraversalError(ValueError): ...
class NullRelationshipValueEncountered(Exception): ...

class TraversedRelationship:
    from_model: type[Model]
    field: Field[Any, Any]
    def __init__(self, from_model: type[Model], field: Field[Any, Any]) -> None: ...
    @property
    def field_name(self) -> str: ...
    @property
    def to_model(self) -> type[Model]: ...

def get_model_field(model: type[Model], name: str) -> Field[Any, Any]: ...
def extract_field_value(
    obj: Model,
    key: str,
    pk_only: bool = False,
    suppress_fielddoesnotexist: bool = False,
    suppress_nullrelationshipvalueencountered: bool = False,
) -> Any: ...
def sort_by_fields(items: list[Model], fields: Sequence[str]) -> None: ...
