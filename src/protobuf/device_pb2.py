# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protobuf/device.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='protobuf/device.proto',
  package='data',
  syntax='proto2',
  serialized_pb=_b('\n\x15protobuf/device.proto\x12\x04\x64\x61ta\"K\n\tPbVersion\x12\r\n\x05major\x18\x01 \x02(\r\x12\r\n\x05minor\x18\x02 \x02(\r\x12\r\n\x05patch\x18\x03 \x02(\r\x12\x11\n\tspecifier\x18\x04 \x01(\t\"\xc1\x02\n\x0cPbDeviceInfo\x12+\n\x12\x62ootloader_version\x18\x01 \x01(\x0b\x32\x0f.data.PbVersion\x12)\n\x10platform_version\x18\x02 \x01(\x0b\x32\x0f.data.PbVersion\x12\'\n\x0e\x64\x65vice_version\x18\x03 \x01(\x0b\x32\x0f.data.PbVersion\x12\x0f\n\x07svn_rev\x18\x04 \x01(\r\x12 \n\x18\x65lectrical_serial_number\x18\x05 \x01(\t\x12\x10\n\x08\x64\x65viceID\x18\x06 \x01(\t\x12\x12\n\nmodel_name\x18\x07 \x01(\t\x12\x15\n\rhardware_code\x18\x08 \x01(\t\x12\x15\n\rproduct_color\x18\t \x01(\t\x12\x16\n\x0eproduct_design\x18\n \x01(\t\x12\x11\n\tsystem_id\x18\x0b \x01(\t')
)




_PBVERSION = _descriptor.Descriptor(
  name='PbVersion',
  full_name='data.PbVersion',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='major', full_name='data.PbVersion.major', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='minor', full_name='data.PbVersion.minor', index=1,
      number=2, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='patch', full_name='data.PbVersion.patch', index=2,
      number=3, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='specifier', full_name='data.PbVersion.specifier', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=31,
  serialized_end=106,
)


_PBDEVICEINFO = _descriptor.Descriptor(
  name='PbDeviceInfo',
  full_name='data.PbDeviceInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='bootloader_version', full_name='data.PbDeviceInfo.bootloader_version', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='platform_version', full_name='data.PbDeviceInfo.platform_version', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='device_version', full_name='data.PbDeviceInfo.device_version', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='svn_rev', full_name='data.PbDeviceInfo.svn_rev', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='electrical_serial_number', full_name='data.PbDeviceInfo.electrical_serial_number', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='deviceID', full_name='data.PbDeviceInfo.deviceID', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='model_name', full_name='data.PbDeviceInfo.model_name', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='hardware_code', full_name='data.PbDeviceInfo.hardware_code', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='product_color', full_name='data.PbDeviceInfo.product_color', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='product_design', full_name='data.PbDeviceInfo.product_design', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='system_id', full_name='data.PbDeviceInfo.system_id', index=10,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=109,
  serialized_end=430,
)

_PBDEVICEINFO.fields_by_name['bootloader_version'].message_type = _PBVERSION
_PBDEVICEINFO.fields_by_name['platform_version'].message_type = _PBVERSION
_PBDEVICEINFO.fields_by_name['device_version'].message_type = _PBVERSION
DESCRIPTOR.message_types_by_name['PbVersion'] = _PBVERSION
DESCRIPTOR.message_types_by_name['PbDeviceInfo'] = _PBDEVICEINFO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PbVersion = _reflection.GeneratedProtocolMessageType('PbVersion', (_message.Message,), dict(
  DESCRIPTOR = _PBVERSION,
  __module__ = 'protobuf.device_pb2'
  # @@protoc_insertion_point(class_scope:data.PbVersion)
  ))
_sym_db.RegisterMessage(PbVersion)

PbDeviceInfo = _reflection.GeneratedProtocolMessageType('PbDeviceInfo', (_message.Message,), dict(
  DESCRIPTOR = _PBDEVICEINFO,
  __module__ = 'protobuf.device_pb2'
  # @@protoc_insertion_point(class_scope:data.PbDeviceInfo)
  ))
_sym_db.RegisterMessage(PbDeviceInfo)


# @@protoc_insertion_point(module_scope)
