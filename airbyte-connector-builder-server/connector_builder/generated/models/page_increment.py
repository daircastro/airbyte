# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator  # noqa: F401
from connector_builder.generated.models.page_increment_all_of import PageIncrementAllOf


class PageIncrement(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    PageIncrement - a model defined in OpenAPI

        page_size: The page_size of this PageIncrement.
        start_from_page: The start_from_page of this PageIncrement [Optional].
    """

    page_size: int
    start_from_page: Optional[int] = None

PageIncrement.update_forward_refs()
