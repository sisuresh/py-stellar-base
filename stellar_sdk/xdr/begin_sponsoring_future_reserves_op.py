# This is an automatically generated file.
# DO NOT EDIT or your changes may be overwritten
from __future__ import annotations

import base64
from enum import IntEnum
from typing import List, Optional, TYPE_CHECKING
from xdrlib3 import Packer, Unpacker
from .base import Integer, UnsignedInteger, Float, Double, Hyper, UnsignedHyper, Boolean, String, Opaque
from .constants import *

from .account_id import AccountID
__all__ = ['BeginSponsoringFutureReservesOp']
class BeginSponsoringFutureReservesOp:
    """
    XDR Source Code::

        struct BeginSponsoringFutureReservesOp
        {
            AccountID sponsoredID;
        };
    """
    def __init__(
        self,
        sponsored_id: AccountID,
    ) -> None:
        self.sponsored_id = sponsored_id
    def pack(self, packer: Packer) -> None:
        self.sponsored_id.pack(packer)
    @classmethod
    def unpack(cls, unpacker: Unpacker) -> BeginSponsoringFutureReservesOp:
        sponsored_id = AccountID.unpack(unpacker)
        return cls(
            sponsored_id=sponsored_id,
        )
    def to_xdr_bytes(self) -> bytes:
        packer = Packer()
        self.pack(packer)
        return packer.get_buffer()

    @classmethod
    def from_xdr_bytes(cls, xdr: bytes) -> BeginSponsoringFutureReservesOp:
        unpacker = Unpacker(xdr)
        return cls.unpack(unpacker)

    def to_xdr(self) -> str:
        xdr_bytes = self.to_xdr_bytes()
        return base64.b64encode(xdr_bytes).decode()

    @classmethod
    def from_xdr(cls, xdr: str) -> BeginSponsoringFutureReservesOp:
        xdr_bytes = base64.b64decode(xdr.encode())
        return cls.from_xdr_bytes(xdr_bytes)
    def __hash__(self):
        return hash((self.sponsored_id,))
    def __eq__(self, other: object):
        if not isinstance(other, self.__class__):
            return NotImplemented
        return self.sponsored_id== other.sponsored_id
    def __str__(self):
        out = [
            f'sponsored_id={self.sponsored_id}',
        ]
        return f"<BeginSponsoringFutureReservesOp [{', '.join(out)}]>"
