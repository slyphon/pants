# Copyright 2015 Pants project contributors (see CONTRIBUTORS.md).
# Licensed under the Apache License, Version 2.0 (see LICENSE).

python_library(
  name='addressable',
  sources=['addressable.py'],
  dependencies=[
    '3rdparty/python:six',
    ':objects',
    'src/python/pants/util:meta',
  ]
)

python_library(
  name='configuration',
  sources=['configuration.py'],
  dependencies=[
    ':addressable',
    ':objects',
  ]
)

python_library(
  name='graph',
  sources=['graph.py'],
  dependencies=[
    '3rdparty/python:six',
    ':addressable',
    ':mapper',
    ':objects',
    'src/python/pants/build_graph',
  ]
)

python_library(
  name='mapper',
  sources=['mapper.py'],
  dependencies=[
    ':objects',
    ':parsers',
    'src/python/pants/build_graph',
    'src/python/pants/util:memo',
  ]
)

python_library(
  name='objects',
  sources=['objects.py'],
  dependencies=[
    'src/python/pants/util:meta',
  ]
)

python_library(
  name='parsers',
  sources=['parsers.py'],
  dependencies=[
    '3rdparty/python:six',
    ':objects',
    'src/python/pants/util:memo',
  ]
)

python_library(
  name='targets',
  sources=['targets.py'],
  dependencies=[
    ':addressable',
    ':configuration',
  ]
)
