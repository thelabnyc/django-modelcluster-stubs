import datetime

from django import forms

TIMEFIELD_TRANSFORM_EXPRESSIONS: set[str]
DATEFIELD_TRANSFORM_EXPRESSIONS: set[str]
DATETIMEFIELD_TRANSFORM_EXPRESSIONS: set[str]
TRANSFORM_FIELD_TYPES: dict[str, type[forms.Field]]

def derive_from_value(
    value: datetime.datetime | datetime.date | datetime.time, expr: str
) -> datetime.date | datetime.time | int | None: ...
def derive_from_time(value: datetime.time, expr: str) -> int: ...
def derive_from_date(value: datetime.date, expr: str) -> int: ...
def derive_from_datetime(
    value: datetime.datetime, expr: str
) -> datetime.date | datetime.time | int: ...
