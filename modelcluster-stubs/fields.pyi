from collections.abc import Iterable
from typing import Any

from django.core import checks
from django.db.models import Model
from django.db.models.fields.related import (
    ForeignKey,
    ForeignObjectRel,
    ManyToManyDescriptor,
    ManyToManyField,
    ReverseManyToOneDescriptor,
)
from django.db.models.fields.reverse_related import ManyToManyRel
from django.db.models.query import QuerySet
from django.utils.functional import cached_property
from modelcluster.queryset import FakeQuerySet

def create_deferring_foreign_related_manager(related: ForeignObjectRel, original_manager_cls: type) -> type: ...

class ChildObjectsDescriptor(ReverseManyToOneDescriptor):
    def __get__(self, instance: Model | None, instance_type: type | None = None) -> Any: ...
    def __set__(self, instance: Model, value: Iterable[Model]) -> None: ...
    @cached_property
    def child_object_manager_cls(self) -> type: ...

class ParentalKey(ForeignKey):
    related_accessor_class: type[ChildObjectsDescriptor]
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def check(self, **kwargs: Any) -> list[checks.CheckMessage]: ...

def create_deferring_forward_many_to_many_manager(rel: ManyToManyRel, original_manager_cls: type) -> type: ...

class ParentalManyToManyDescriptor(ManyToManyDescriptor):
    def __get__(self, instance: Model | None, instance_type: type | None = None) -> Any: ...
    def __set__(self, instance: Model, value: Iterable[Model]) -> None: ...
    @cached_property
    def child_object_manager_cls(self) -> type: ...

class ParentalManyToManyField(ManyToManyField):
    related_accessor_class: type[ParentalManyToManyDescriptor]
    _need_commit_after_assignment: bool
    def contribute_to_class(self, cls: type[Model], name: str, **kwargs: Any) -> None: ...
    def value_from_object(self, obj: Model) -> FakeQuerySet | QuerySet[Model]: ...
