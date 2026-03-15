from typing import Any

from django.db.models import Model
from django.db.models.fields.related import ForeignKey
from django.db.models.query import QuerySet
from django.forms import Media
from django.forms.models import (
    BaseModelFormSet,
    ModelForm,
    ModelFormMetaclass,
    ModelFormOptions,
    _FormFieldCallback,
    _Widgets,
)
from django.forms.utils import _DataT, _FilesT
from django.utils.safestring import SafeString

from modelcluster.queryset import FakeQuerySet

class BaseTransientModelFormSet(BaseModelFormSet):
    changed_objects: list[tuple[Model, list[str]]]
    deleted_objects: list[Model]
    def save_existing_objects(self, commit: bool = True) -> list[Model]: ...

def transientmodelformset_factory(
    model: type[Model],
    formset: type[BaseTransientModelFormSet] = ...,
    **kwargs: Any,
) -> type[BaseTransientModelFormSet]: ...

class BaseChildFormSet(BaseTransientModelFormSet):
    fk: ForeignKey
    inherit_kwargs: list[str] | None
    instance: Model
    rel_name: str
    def __init__(
        self,
        data: _DataT | None = None,
        files: _FilesT | None = None,
        instance: Model | None = None,
        queryset: FakeQuerySet | QuerySet[Model] | None = None,
        **kwargs: Any,
    ) -> None: ...
    def save(self, commit: bool = True) -> list[Model]: ...
    def clean(self, *args: Any, **kwargs: Any) -> None: ...
    def validate_unique(self) -> None: ...

def childformset_factory(
    parent_model: type[Model],
    model: type[Model],
    form: type[ModelForm] = ...,
    formset: type[BaseChildFormSet] = ...,
    fk_name: str | None = None,
    fields: list[str] | None = None,
    exclude: list[str] | None = None,
    extra: int = 3,
    can_order: bool = False,
    can_delete: bool = True,
    max_num: int | None = None,
    validate_max: bool = False,
    formfield_callback: _FormFieldCallback | None = None,
    widgets: _Widgets | None = None,
    min_num: int | None = None,
    validate_min: bool = False,
    inherit_kwargs: list[str] | None = None,
    formsets: dict[str, Any] | list[str] | None = None,
    exclude_formsets: list[str] | None = None,
) -> type[BaseChildFormSet]: ...

class ClusterFormOptions(ModelFormOptions):
    formsets: dict[str, Any] | list[str] | None
    exclude_formsets: list[str] | None
    def __init__(self, options: type | None = None) -> None: ...

class ClusterFormMetaclass(ModelFormMetaclass):
    extra_form_count: int
    @classmethod
    def child_form(cls) -> type[ClusterForm]: ...
    def __new__(
        cls, name: str, bases: tuple[type, ...], attrs: dict[str, Any]
    ) -> type: ...

class ClusterForm(ModelForm, metaclass=ClusterFormMetaclass):
    formsets: dict[str, BaseChildFormSet]
    def __init__(
        self,
        data: _DataT | None = None,
        files: _FilesT | None = None,
        instance: Model | None = None,
        prefix: str | None = None,
        **kwargs: Any,
    ) -> None: ...
    def as_p(self) -> SafeString: ...
    def is_valid(self) -> bool: ...
    def is_multipart(self) -> bool: ...
    @property
    def media(self) -> Media: ...
    def save(self, commit: bool = True) -> Model: ...
    def has_changed(self) -> bool: ...

def clusterform_factory(
    model: type[Model],
    form: type[ClusterForm] = ...,
    **kwargs: Any,
) -> type[ClusterForm]: ...
