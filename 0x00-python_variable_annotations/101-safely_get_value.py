#!/usr/bin/env python3
""" type annotations  """

from typing import Mapping, Any, Sequence, Union, TypeVar


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[TypeVar('T'), None] = None
                     ) -> Union[Any, T]:
    """ retrieve value """
    if key in dct:
        return dct[key]
    else:
        return default
