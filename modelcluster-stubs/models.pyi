from typing import Any, Self

from django.db import models
from django.db.models import Field, Model
from django.db.models.fields.related import ForeignObjectRel

from modelcluster.fields import ParentalManyToManyField

def get_field_value(field: Field[Any, Any], model: Model) -> Any: ...
def get_serializable_data_for_fields(model: Model) -> dict[str, Any]: ...
def model_from_serializable_data(
    model: type[Model],
    data: dict[str, Any],
    check_fks: bool = True,
    strict_fks: bool = False,
) -> Model | None: ...
def get_all_child_relations(model: type[Model] | Model) -> list[ForeignObjectRel]: ...
def get_all_child_m2m_relations(
    model: type[Model] | Model,
) -> list[ParentalManyToManyField]: ...

class ClusterableModel(models.Model):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def save(self, **kwargs: Any) -> None: ...
    def serializable_data(self) -> dict[str, Any]: ...
    def to_json(self) -> str: ...
    @classmethod
    def from_serializable_data(
        cls, data: dict[str, Any], check_fks: bool = True, strict_fks: bool = False
    ) -> Self | None: ...
    @classmethod
    def from_json(
        cls, json_data: str, check_fks: bool = True, strict_fks: bool = False
    ) -> Self | None: ...
    def copy_child_relation(
        self,
        child_relation: str | ForeignObjectRel,
        target: ClusterableModel,
        commit: bool = False,
        append: bool = False,
    ) -> dict[tuple[Any, Any], Any]: ...
    def copy_all_child_relations(
        self,
        target: ClusterableModel,
        exclude: list[str] | None = None,
        commit: bool = False,
        append: bool = False,
    ) -> dict[tuple[Any, Any], Any]: ...
    def copy_cluster(
        self, exclude_fields: list[str] | None = None
    ) -> tuple[Self, dict[tuple[Any, Any], Any]]: ...

    class Meta:
        abstract: bool
