"""
Tests for the AttrMap class.
"""
import pytest
from attrdictionary.mapping import AttrMap


def test_repr():
    assert repr(AttrMap()) == "AttrMap({})"
    assert repr(AttrMap({'foo': 'bar'})) == "AttrMap({'foo': 'bar'})"
    assert repr(AttrMap({1: {'foo': 'bar'}})) == "AttrMap({1: {'foo': 'bar'}})"
    assert repr(AttrMap({1: AttrMap({'foo': 'bar'})})) == "AttrMap({1: AttrMap({'foo': 'bar'})})"
