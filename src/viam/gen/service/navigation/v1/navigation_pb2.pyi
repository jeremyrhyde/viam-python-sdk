"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import collections.abc
from .... import common
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import sys
import typing
if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions
DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _Mode:
    ValueType = typing.NewType('ValueType', builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _ModeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_Mode.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    MODE_UNSPECIFIED: _Mode.ValueType
    MODE_MANUAL: _Mode.ValueType
    MODE_WAYPOINT: _Mode.ValueType

class Mode(_Mode, metaclass=_ModeEnumTypeWrapper):
    ...
MODE_UNSPECIFIED: Mode.ValueType
MODE_MANUAL: Mode.ValueType
MODE_WAYPOINT: Mode.ValueType
global___Mode = Mode

class GetModeRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    NAME_FIELD_NUMBER: builtins.int
    name: builtins.str

    def __init__(self, *, name: builtins.str=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['name', b'name']) -> None:
        ...
global___GetModeRequest = GetModeRequest

class GetModeResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    MODE_FIELD_NUMBER: builtins.int
    mode: global___Mode.ValueType

    def __init__(self, *, mode: global___Mode.ValueType=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['mode', b'mode']) -> None:
        ...
global___GetModeResponse = GetModeResponse

class SetModeRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    NAME_FIELD_NUMBER: builtins.int
    MODE_FIELD_NUMBER: builtins.int
    name: builtins.str
    mode: global___Mode.ValueType

    def __init__(self, *, name: builtins.str=..., mode: global___Mode.ValueType=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['mode', b'mode', 'name', b'name']) -> None:
        ...
global___SetModeRequest = SetModeRequest

class SetModeResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(self) -> None:
        ...
global___SetModeResponse = SetModeResponse

class Waypoint(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ID_FIELD_NUMBER: builtins.int
    LOCATION_FIELD_NUMBER: builtins.int
    id: builtins.str

    @property
    def location(self) -> common.v1.common_pb2.GeoPoint:
        ...

    def __init__(self, *, id: builtins.str=..., location: common.v1.common_pb2.GeoPoint | None=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['location', b'location']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['id', b'id', 'location', b'location']) -> None:
        ...
global___Waypoint = Waypoint

class GetLocationRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    NAME_FIELD_NUMBER: builtins.int
    name: builtins.str

    def __init__(self, *, name: builtins.str=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['name', b'name']) -> None:
        ...
global___GetLocationRequest = GetLocationRequest

class GetLocationResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    LOCATION_FIELD_NUMBER: builtins.int

    @property
    def location(self) -> common.v1.common_pb2.GeoPoint:
        ...

    def __init__(self, *, location: common.v1.common_pb2.GeoPoint | None=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['location', b'location']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['location', b'location']) -> None:
        ...
global___GetLocationResponse = GetLocationResponse

class GetWaypointsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    NAME_FIELD_NUMBER: builtins.int
    name: builtins.str

    def __init__(self, *, name: builtins.str=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['name', b'name']) -> None:
        ...
global___GetWaypointsRequest = GetWaypointsRequest

class GetWaypointsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    WAYPOINTS_FIELD_NUMBER: builtins.int

    @property
    def waypoints(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Waypoint]:
        ...

    def __init__(self, *, waypoints: collections.abc.Iterable[global___Waypoint] | None=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['waypoints', b'waypoints']) -> None:
        ...
global___GetWaypointsResponse = GetWaypointsResponse

class AddWaypointRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    NAME_FIELD_NUMBER: builtins.int
    LOCATION_FIELD_NUMBER: builtins.int
    name: builtins.str

    @property
    def location(self) -> common.v1.common_pb2.GeoPoint:
        ...

    def __init__(self, *, name: builtins.str=..., location: common.v1.common_pb2.GeoPoint | None=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['location', b'location']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['location', b'location', 'name', b'name']) -> None:
        ...
global___AddWaypointRequest = AddWaypointRequest

class AddWaypointResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(self) -> None:
        ...
global___AddWaypointResponse = AddWaypointResponse

class RemoveWaypointRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    NAME_FIELD_NUMBER: builtins.int
    ID_FIELD_NUMBER: builtins.int
    name: builtins.str
    id: builtins.str

    def __init__(self, *, name: builtins.str=..., id: builtins.str=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['id', b'id', 'name', b'name']) -> None:
        ...
global___RemoveWaypointRequest = RemoveWaypointRequest

class RemoveWaypointResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(self) -> None:
        ...
global___RemoveWaypointResponse = RemoveWaypointResponse