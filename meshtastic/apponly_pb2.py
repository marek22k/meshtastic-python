# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: apponly.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import channel_pb2 as channel__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='apponly.proto',
  package='',
  syntax='proto3',
  serialized_options=b'\n\023com.geeksville.meshB\rAppOnlyProtosH\003Z!github.com/meshtastic/gomeshproto',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\rapponly.proto\x1a\rchannel.proto\"0\n\nChannelSet\x12\"\n\x08settings\x18\x01 \x03(\x0b\x32\x10.ChannelSettingsBI\n\x13\x63om.geeksville.meshB\rAppOnlyProtosH\x03Z!github.com/meshtastic/gomeshprotob\x06proto3'
  ,
  dependencies=[channel__pb2.DESCRIPTOR,])




_CHANNELSET = _descriptor.Descriptor(
  name='ChannelSet',
  full_name='ChannelSet',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='settings', full_name='ChannelSet.settings', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=32,
  serialized_end=80,
)

_CHANNELSET.fields_by_name['settings'].message_type = channel__pb2._CHANNELSETTINGS
DESCRIPTOR.message_types_by_name['ChannelSet'] = _CHANNELSET
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ChannelSet = _reflection.GeneratedProtocolMessageType('ChannelSet', (_message.Message,), {
  'DESCRIPTOR' : _CHANNELSET,
  '__module__' : 'apponly_pb2'
  # @@protoc_insertion_point(class_scope:ChannelSet)
  })
_sym_db.RegisterMessage(ChannelSet)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
