# AUTO GENERATED, PLEASE DO NOT MODIFY BY HAND

from __future__ import annotations

from enum import Enum
from typing import List, Optional, Union

from pydantic import BaseModel, Field


class TableCellHeight(Enum):
    sm = 'sm'
    md = 'md'
    lg = 'lg'


class TableFooterOptions(BaseModel):
    show: bool
    reducer: List[str]
    fields: Optional[List[str]] = None
    enablePagination: Optional[bool] = None
    countRows: Optional[bool] = None


class Show(Enum):
    boolean_False = False


class CountRows(Enum):
    boolean_False = False


class Reducer(Enum):
    array___ = []


class FooterItem(BaseModel):
    show: Show = Field(..., description='Controls whether the footer should be shown')
    countRows: CountRows = Field(
        ...,
        description='Controls whether the footer should show the total number of rows on Count calculation',
    )
    reducer: Union[List, Reducer] = Field(
        ..., description='Represents the selected calculations'
    )


class TableSortByFieldState(BaseModel):
    displayName: str = Field(
        ..., description='Sets the display name of the field to sort by'
    )
    desc: Optional[bool] = Field(
        None, description='Flag used to indicate descending sort order'
    )


class PanelOptions(BaseModel):
    frameIndex: float = Field(
        ..., description='Represents the index of the selected frame'
    )
    showHeader: bool = Field(
        ..., description='Controls whether the panel should show the header'
    )
    showTypeIcons: Optional[bool] = Field(
        False,
        description='Controls whether the header should show icons for the column types',
    )
    sortBy: Optional[List[TableSortByFieldState]] = Field(
        None, description='Used to control row sorting'
    )
    footer: Optional[Union[TableFooterOptions, FooterItem]] = Field(
        {'show': False, 'countRows': False, 'reducer': []},
        description='Controls footer options',
    )
    cellHeight: Optional[TableCellHeight] = Field(
        None, description='Controls the height of the rows'
    )


class TablePanelCfg(BaseModel):
    PanelOptions: PanelOptions