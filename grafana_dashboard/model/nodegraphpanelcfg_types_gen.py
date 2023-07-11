# AUTO GENERATED, PLEASE DO NOT MODIFY BY HAND

from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, Field


class ArcOption(BaseModel):
    field: Optional[str] = Field(
        None,
        description='Field from which to get the value. Values should be less than 1, representing fraction of a circle.',
    )
    color: Optional[str] = Field(None, description='The color of the arc.')


class EdgeOptions(BaseModel):
    mainStatUnit: Optional[str] = Field(
        None,
        description='Unit for the main stat to override what ever is set in the data frame.',
    )
    secondaryStatUnit: Optional[str] = Field(
        None,
        description='Unit for the secondary stat to override what ever is set in the data frame.',
    )


class NodeOptions(BaseModel):
    mainStatUnit: Optional[str] = Field(
        None,
        description='Unit for the main stat to override what ever is set in the data frame.',
    )
    secondaryStatUnit: Optional[str] = Field(
        None,
        description='Unit for the secondary stat to override what ever is set in the data frame.',
    )
    arcs: Optional[List[ArcOption]] = Field(
        None,
        description='Define which fields are shown as part of the node arc (colored circle around the node).',
    )


class PanelOptions(BaseModel):
    nodes: Optional[NodeOptions] = None
    edges: Optional[EdgeOptions] = None


class NodeGraphPanelCfg(BaseModel):
    ArcOption: ArcOption
    NodeOptions: NodeOptions
    EdgeOptions: EdgeOptions
    PanelOptions: PanelOptions
