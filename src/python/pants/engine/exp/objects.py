# coding=utf-8
# Copyright 2015 Pants project contributors (see CONTRIBUTORS.md).
# Licensed under the Apache License, Version 2.0 (see LICENSE).

from __future__ import (absolute_import, division, generators, nested_scopes, print_function,
                        unicode_literals, with_statement)

import inspect
from abc import abstractmethod, abstractproperty

from pants.util.meta import AbstractClass


class Resolvable(AbstractClass):
  """Represents a resolvable object."""

  @abstractproperty
  def address(self):
    """Return the opaque address descriptor that this resolvable resolves."""

  @abstractmethod
  def resolve(self):
    """Resolve and return the resolvable object."""


class Serializable(AbstractClass):
  """Marks a class that can be serialized into and reconstituted from python builtin values."""

  @staticmethod
  def is_serializable(obj):
    """Return `True` if the given object conforms to the Serializable protocol.

    :rtype: bool
    """
    return isinstance(obj, Serializable) or (not inspect.isclass(obj) and hasattr(obj, '_asdict'))

  @staticmethod
  def is_serializable_type(type_):
    """Return `True` if the given type's instances conform to the Serializable protocol.

    :rtype: bool
    """
    return issubclass(type_, Serializable) or (inspect.isclass(type_) and hasattr(type_, '_asdict'))

  @abstractmethod
  def _asdict(self):
    """Return a dict mapping this class' properties.

    To meet the contract of a serializable the constructor must accept all the properties returned
    here as constructor parameters; ie the following must be true::

    >>> s = Serializable(...)
    >>> Serializable(**s._asdict()) == s

    Additionally the dict must also contain nothing except Serializables, python primitive values,
    ie: dicts, lists, strings, numbers, bool values, etc or Resolvables that resolve to Serilizables
    or primitive values.

    Any :class:`collections.namedtuple` satisfies the Serializable contract automatically via duck
    typing if it is composed of only primitive python values or Serializable values.
    """


class SerializableFactory(AbstractClass):
  """Creates :class:`Serializable` objects."""

  @abstractmethod
  def create(self):
    """Return a serializable object.

    :rtype: :class:`Serializable`
    """


class ValidationError(Exception):
  """Indicates an invalid configuration was provided."""

  def __init__(self, identifier, message):
    """Creates a validation error pertaining to the identified invalid object.

    :param object identifier: Any object whose string representation identifies the invalid object
                              that led to this validation error.
    :param string message: A message describing the invalid configuration.
    """
    super(ValidationError, self).__init__('Failed to validate {id}: {msg}'
                                          .format(id=identifier, msg=message))


class Validatable(AbstractClass):
  """Marks a class whose instances should validated post-construction."""

  @abstractmethod
  def validate(self):
    """Check this object's configuration is valid.

    :raises: :class:`ValidationError` if this object is invalid.
    """
