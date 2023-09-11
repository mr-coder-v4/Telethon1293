"""File generated by TLObjects' generator. All changes will be ERASED"""
from ...tl.tlobject import TLObject
from ...tl.tlobject import TLRequest
from typing import Optional, List, Union, TYPE_CHECKING
import os
import struct
from datetime import datetime
if TYPE_CHECKING:
    from ...tl.types import TypeInputUser, TypeSecureValueError



class GetFullUserRequest(TLRequest):
    CONSTRUCTOR_ID = 0xb60f5918
    SUBCLASS_OF_ID = 0x83df9df5

    # noinspection PyShadowingBuiltins
    def __init__(self, id: 'TypeInputUser'):
        """
        :returns users.UserFull: Instance of UserFull.
        """
        self.id = id

    async def resolve(self, client, utils):
        self.id = utils.get_input_user(await client.get_input_entity(self.id))

    def to_dict(self):
        return {
            '_': 'GetFullUserRequest',
            'id': self.id.to_dict() if isinstance(self.id, TLObject) else self.id
        }

    def _bytes(self):
        return b''.join((
            b'\x18Y\x0f\xb6',
            self.id._bytes(),
        ))

    @classmethod
    def from_reader(cls, reader):
        _id = reader.tgread_object()
        return cls(id=_id)


class GetStoriesMaxIDsRequest(TLRequest):
    CONSTRUCTOR_ID = 0xca1cb9ab
    SUBCLASS_OF_ID = 0x5026710f

    # noinspection PyShadowingBuiltins
    def __init__(self, id: List['TypeInputUser']):
        """
        :returns Vector<int>: This type has no constructors.
        """
        self.id = id

    async def resolve(self, client, utils):
        _tmp = []
        for _x in self.id:
            _tmp.append(utils.get_input_user(await client.get_input_entity(_x)))

        self.id = _tmp

    def to_dict(self):
        return {
            '_': 'GetStoriesMaxIDsRequest',
            'id': [] if self.id is None else [x.to_dict() if isinstance(x, TLObject) else x for x in self.id]
        }

    def _bytes(self):
        return b''.join((
            b'\xab\xb9\x1c\xca',
            b'\x15\xc4\xb5\x1c',struct.pack('<i', len(self.id)),b''.join(x._bytes() for x in self.id),
        ))

    @classmethod
    def from_reader(cls, reader):
        reader.read_int()
        _id = []
        for _ in range(reader.read_int()):
            _x = reader.tgread_object()
            _id.append(_x)

        return cls(id=_id)

    @staticmethod
    def read_result(reader):
        reader.read_int()  # Vector ID
        return [reader.read_int() for _ in range(reader.read_int())]


class GetUsersRequest(TLRequest):
    CONSTRUCTOR_ID = 0xd91a548
    SUBCLASS_OF_ID = 0x406da4d

    # noinspection PyShadowingBuiltins
    def __init__(self, id: List['TypeInputUser']):
        """
        :returns Vector<User>: This type has no constructors.
        """
        self.id = id

    async def resolve(self, client, utils):
        _tmp = []
        for _x in self.id:
            _tmp.append(utils.get_input_user(await client.get_input_entity(_x)))

        self.id = _tmp

    def to_dict(self):
        return {
            '_': 'GetUsersRequest',
            'id': [] if self.id is None else [x.to_dict() if isinstance(x, TLObject) else x for x in self.id]
        }

    def _bytes(self):
        return b''.join((
            b'H\xa5\x91\r',
            b'\x15\xc4\xb5\x1c',struct.pack('<i', len(self.id)),b''.join(x._bytes() for x in self.id),
        ))

    @classmethod
    def from_reader(cls, reader):
        reader.read_int()
        _id = []
        for _ in range(reader.read_int()):
            _x = reader.tgread_object()
            _id.append(_x)

        return cls(id=_id)


class SetSecureValueErrorsRequest(TLRequest):
    CONSTRUCTOR_ID = 0x90c894b5
    SUBCLASS_OF_ID = 0xf5b399ac

    # noinspection PyShadowingBuiltins
    def __init__(self, id: 'TypeInputUser', errors: List['TypeSecureValueError']):
        """
        :returns Bool: This type has no constructors.
        """
        self.id = id
        self.errors = errors

    async def resolve(self, client, utils):
        self.id = utils.get_input_user(await client.get_input_entity(self.id))

    def to_dict(self):
        return {
            '_': 'SetSecureValueErrorsRequest',
            'id': self.id.to_dict() if isinstance(self.id, TLObject) else self.id,
            'errors': [] if self.errors is None else [x.to_dict() if isinstance(x, TLObject) else x for x in self.errors]
        }

    def _bytes(self):
        return b''.join((
            b'\xb5\x94\xc8\x90',
            self.id._bytes(),
            b'\x15\xc4\xb5\x1c',struct.pack('<i', len(self.errors)),b''.join(x._bytes() for x in self.errors),
        ))

    @classmethod
    def from_reader(cls, reader):
        _id = reader.tgread_object()
        reader.read_int()
        _errors = []
        for _ in range(reader.read_int()):
            _x = reader.tgread_object()
            _errors.append(_x)

        return cls(id=_id, errors=_errors)

