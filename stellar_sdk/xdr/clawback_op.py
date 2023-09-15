# This is an automatically generated file.
# DO NOT EDIT or your changes may be overwritten
from __future__ import annotations

import base64
from enum import IntEnum
from typing import List, Optional, TYPE_CHECKING
from xdrlib3 import Packer, Unpacker
from .base import Integer, UnsignedInteger, Float, Double, Hyper, UnsignedHyper, Boolean, String, Opaque
from .constants import *

from .asset import Asset
from .muxed_account import MuxedAccount
from .int64 import Int64
__all__ = ['ClawbackOp']
class ClawbackOp:
    """
    XDR Source Code::

        struct ClawbackOp
        {
            Asset asset;
            MuxedAccount from_;
            int64 amount;
        };
    """
    def __init__(
        self,
        asset: Asset,
        from_: MuxedAccount,
        amount: Int64,
    ) -> None:
        self.asset = asset
        self.from_ = from_
        self.amount = amount
    def pack(self, packer: Packer) -> None:
        self.asset.pack(packer)
        self.from_.pack(packer)
        self.amount.pack(packer)
    @classmethod
    def unpack(cls, unpacker: Unpacker) -> ClawbackOp:
        asset = Asset.unpack(unpacker)
        from_ = MuxedAccount.unpack(unpacker)
        amount = Int64.unpack(unpacker)
        return cls(
            asset=asset,
            from_=from_,
            amount=amount,
        )
    def to_xdr_bytes(self) -> bytes:
        packer = Packer()
        self.pack(packer)
        return packer.get_buffer()

    @classmethod
    def from_xdr_bytes(cls, xdr: bytes) -> ClawbackOp:
        unpacker = Unpacker(xdr)
        return cls.unpack(unpacker)

    def to_xdr(self) -> str:
        xdr_bytes = self.to_xdr_bytes()
        return base64.b64encode(xdr_bytes).decode()

    @classmethod
    def from_xdr(cls, xdr: str) -> ClawbackOp:
        xdr_bytes = base64.b64decode(xdr.encode())
        return cls.from_xdr_bytes(xdr_bytes)
    def __hash__(self):
        return hash((self.asset, self.from_, self.amount,))
    def __eq__(self, other: object):
        if not isinstance(other, self.__class__):
            return NotImplemented
        return self.asset== other.asset and self.from_== other.from_ and self.amount== other.amount
    def __str__(self):
        out = [
            f'asset={self.asset}',
            f'from_={self.from_}',
            f'amount={self.amount}',
        ]
        return f"<ClawbackOp [{', '.join(out)}]>"
