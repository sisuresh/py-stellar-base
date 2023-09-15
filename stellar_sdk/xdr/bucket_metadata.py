# This is an automatically generated file.
# DO NOT EDIT or your changes may be overwritten
from __future__ import annotations

import base64
from enum import IntEnum
from typing import List, Optional, TYPE_CHECKING
from xdrlib3 import Packer, Unpacker
from .base import Integer, UnsignedInteger, Float, Double, Hyper, UnsignedHyper, Boolean, String, Opaque
from .constants import *

from .uint32 import Uint32
from .bucket_metadata_ext import BucketMetadataExt
__all__ = ['BucketMetadata']
class BucketMetadata:
    """
    XDR Source Code::

        struct BucketMetadata
        {
            // Indicates the protocol version used to create / merge this bucket.
            uint32 ledgerVersion;

            // reserved for future use
            union switch (int v)
            {
            case 0:
                void;
            }
            ext;
        };
    """
    def __init__(
        self,
        ledger_version: Uint32,
        ext: BucketMetadataExt,
    ) -> None:
        self.ledger_version = ledger_version
        self.ext = ext
    def pack(self, packer: Packer) -> None:
        self.ledger_version.pack(packer)
        self.ext.pack(packer)
    @classmethod
    def unpack(cls, unpacker: Unpacker) -> BucketMetadata:
        ledger_version = Uint32.unpack(unpacker)
        ext = BucketMetadataExt.unpack(unpacker)
        return cls(
            ledger_version=ledger_version,
            ext=ext,
        )
    def to_xdr_bytes(self) -> bytes:
        packer = Packer()
        self.pack(packer)
        return packer.get_buffer()

    @classmethod
    def from_xdr_bytes(cls, xdr: bytes) -> BucketMetadata:
        unpacker = Unpacker(xdr)
        return cls.unpack(unpacker)

    def to_xdr(self) -> str:
        xdr_bytes = self.to_xdr_bytes()
        return base64.b64encode(xdr_bytes).decode()

    @classmethod
    def from_xdr(cls, xdr: str) -> BucketMetadata:
        xdr_bytes = base64.b64decode(xdr.encode())
        return cls.from_xdr_bytes(xdr_bytes)
    def __hash__(self):
        return hash((self.ledger_version, self.ext,))
    def __eq__(self, other: object):
        if not isinstance(other, self.__class__):
            return NotImplemented
        return self.ledger_version== other.ledger_version and self.ext== other.ext
    def __str__(self):
        out = [
            f'ledger_version={self.ledger_version}',
            f'ext={self.ext}',
        ]
        return f"<BucketMetadata [{', '.join(out)}]>"
