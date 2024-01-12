#!/usr/bin/env python3
""" Type-annotated function to kv """
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ returns the tuple"""
    return (k, v**2)
