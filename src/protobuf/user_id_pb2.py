# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protobuf/user_id.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from protobuf import types_pb2 as protobuf_dot_types__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='protobuf/user_id.proto',
  package='data',
  syntax='proto2',
  serialized_pb=_b('\n\x16protobuf/user_id.proto\x12\x04\x64\x61ta\x1a\x14protobuf/types.proto\"3\n\x0fPbPasswordToken\x12\r\n\x05token\x18\x01 \x02(\x0c\x12\x11\n\tencrypted\x18\x02 \x02(\x08\"\xd6\x01\n\x10PbUserIdentifier\x12\x19\n\x11master_identifier\x18\x01 \x01(\x04\x12\r\n\x05\x65mail\x18\x02 \x01(\t\x12-\n\x0epassword_token\x18\x03 \x01(\x0b\x32\x15.data.PbPasswordToken\x12\x10\n\x08nickname\x18\x04 \x01(\t\x12\x12\n\nfirst_name\x18\x05 \x01(\t\x12\x11\n\tlast_name\x18\x06 \x01(\t\x12\x30\n\x15user_id_last_modified\x18\x64 \x01(\x0b\x32\x11.PbSystemDateTime')
  ,
  dependencies=[protobuf_dot_types__pb2.DESCRIPTOR,])




_PBPASSWORDTOKEN = _descriptor.Descriptor(
  name='PbPasswordToken',
  full_name='data.PbPasswordToken',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='token', full_name='data.PbPasswordToken.token', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='encrypted', full_name='data.PbPasswordToken.encrypted', index=1,
      number=2, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=54,
  serialized_end=105,
)


_PBUSERIDENTIFIER = _descriptor.Descriptor(
  name='PbUserIdentifier',
  full_name='data.PbUserIdentifier',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='master_identifier', full_name='data.PbUserIdentifier.master_identifier', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='email', full_name='data.PbUserIdentifier.email', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='password_token', full_name='data.PbUserIdentifier.password_token', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='nickname', full_name='data.PbUserIdentifier.nickname', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='first_name', full_name='data.PbUserIdentifier.first_name', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='last_name', full_name='data.PbUserIdentifier.last_name', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='user_id_last_modified', full_name='data.PbUserIdentifier.user_id_last_modified', index=6,
      number=100, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=108,
  serialized_end=322,
)

_PBUSERIDENTIFIER.fields_by_name['password_token'].message_type = _PBPASSWORDTOKEN
_PBUSERIDENTIFIER.fields_by_name['user_id_last_modified'].message_type = protobuf_dot_types__pb2._PBSYSTEMDATETIME
DESCRIPTOR.message_types_by_name['PbPasswordToken'] = _PBPASSWORDTOKEN
DESCRIPTOR.message_types_by_name['PbUserIdentifier'] = _PBUSERIDENTIFIER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PbPasswordToken = _reflection.GeneratedProtocolMessageType('PbPasswordToken', (_message.Message,), dict(
  DESCRIPTOR = _PBPASSWORDTOKEN,
  __module__ = 'protobuf.user_id_pb2'
  # @@protoc_insertion_point(class_scope:data.PbPasswordToken)
  ))
_sym_db.RegisterMessage(PbPasswordToken)

PbUserIdentifier = _reflection.GeneratedProtocolMessageType('PbUserIdentifier', (_message.Message,), dict(
  DESCRIPTOR = _PBUSERIDENTIFIER,
  __module__ = 'protobuf.user_id_pb2'
  # @@protoc_insertion_point(class_scope:data.PbUserIdentifier)
  ))
_sym_db.RegisterMessage(PbUserIdentifier)


# @@protoc_insertion_point(module_scope)