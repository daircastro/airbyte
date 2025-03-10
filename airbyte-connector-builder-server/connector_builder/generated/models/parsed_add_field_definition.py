# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator  # noqa: F401
from connector_builder.generated.models.interpolated_string import InterpolatedString


class ParsedAddFieldDefinition(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    ParsedAddFieldDefinition - a model defined in OpenAPI

        path: The path of this ParsedAddFieldDefinition.
        value: The value of this ParsedAddFieldDefinition.
    """

    path: List[str]
    value: InterpolatedString

ParsedAddFieldDefinition.update_forward_refs()
