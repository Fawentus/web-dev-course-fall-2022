# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: user.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\nuser.proto\"9\n\x08UserData\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\x05\x12\x13\n\x0b\x63ount_trees\x18\x03 \x01(\x05\"\x17\n\x07Message\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\t\"\x12\n\x02ID\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\x05\x32Z\n\x04User\x12\x1c\n\x08Register\x12\t.UserData\x1a\x03.ID\"\x00\x12\x18\n\x05Plant\x12\x03.ID\x1a\x08.Message\"\x00\x12\x1a\n\x07\x43utDown\x12\x03.ID\x1a\x08.Message\"\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'user_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _USERDATA._serialized_start=14
  _USERDATA._serialized_end=71
  _MESSAGE._serialized_start=73
  _MESSAGE._serialized_end=96
  _ID._serialized_start=98
  _ID._serialized_end=116
  _USER._serialized_start=118
  _USER._serialized_end=208
# @@protoc_insertion_point(module_scope)