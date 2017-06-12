# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protobuf/act_samples.proto

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
  name='protobuf/act_samples.proto',
  package='data',
  syntax='proto2',
  serialized_pb=_b('\n\x1aprotobuf/act_samples.proto\x12\x04\x64\x61ta\x1a\x14protobuf/types.proto\"]\n\x0bPbSportInfo\x12\x0e\n\x06\x66\x61\x63tor\x18\x01 \x02(\x02\x12$\n\ntime_stamp\x18\x02 \x02(\x0b\x32\x10.PbLocalDateTime\x12\x18\n\x10sport_profile_id\x18\x03 \x01(\x04\"\xa6\x02\n\x0ePbActivityInfo\x12\x31\n\x05value\x18\x01 \x02(\x0e\x32\".data.PbActivityInfo.ActivityClass\x12$\n\ntime_stamp\x18\x02 \x02(\x0b\x32\x10.PbLocalDateTime\x12\x0e\n\x06\x66\x61\x63tor\x18\x03 \x01(\x02\"\xaa\x01\n\rActivityClass\x12\t\n\x05SLEEP\x10\x01\x12\r\n\tSEDENTARY\x10\x02\x12\t\n\x05LIGHT\x10\x03\x12\x17\n\x13\x43ONTINUOUS_MODERATE\x10\x04\x12\x19\n\x15INTERMITTENT_MODERATE\x10\x05\x12\x17\n\x13\x43ONTINUOUS_VIGOROUS\x10\x06\x12\x19\n\x15INTERMITTENT_VIGOROUS\x10\x07\x12\x0c\n\x08NON_WEAR\x10\x08\"?\n\x17PbInActivityTriggerInfo\x12$\n\ntime_stamp\x18\x01 \x02(\x0b\x32\x10.PbLocalDateTime\"v\n\x1ePbInActivityNonWearTriggerInfo\x12*\n\x10start_time_stamp\x18\x01 \x02(\x0b\x32\x10.PbLocalDateTime\x12(\n\x0e\x65nd_time_stamp\x18\x02 \x02(\x0b\x32\x10.PbLocalDateTime\"\x9b\x03\n\x11PbActivitySamples\x12$\n\nstart_time\x18\x01 \x02(\x0b\x32\x10.PbLocalDateTime\x12+\n\x16met_recording_interval\x18\x02 \x02(\x0b\x32\x0b.PbDuration\x12-\n\x18steps_recording_interval\x18\x03 \x02(\x0b\x32\x0b.PbDuration\x12\x13\n\x0bmet_samples\x18\x04 \x03(\x02\x12\x15\n\rsteps_samples\x18\x05 \x03(\r\x12%\n\nsport_info\x18\x06 \x03(\x0b\x32\x11.data.PbSportInfo\x12+\n\ractivity_info\x18\x07 \x03(\x0b\x32\x14.data.PbActivityInfo\x12\x39\n\x12inactivity_trigger\x18\x08 \x03(\x0b\x32\x1d.data.PbInActivityTriggerInfo\x12I\n\x1binactivity_non_wear_trigger\x18\t \x03(\x0b\x32$.data.PbInActivityNonWearTriggerInfo')
  ,
  dependencies=[protobuf_dot_types__pb2.DESCRIPTOR,])



_PBACTIVITYINFO_ACTIVITYCLASS = _descriptor.EnumDescriptor(
  name='ActivityClass',
  full_name='data.PbActivityInfo.ActivityClass',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SLEEP', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SEDENTARY', index=1, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LIGHT', index=2, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CONTINUOUS_MODERATE', index=3, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INTERMITTENT_MODERATE', index=4, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CONTINUOUS_VIGOROUS', index=5, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INTERMITTENT_VIGOROUS', index=6, number=7,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NON_WEAR', index=7, number=8,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=278,
  serialized_end=448,
)
_sym_db.RegisterEnumDescriptor(_PBACTIVITYINFO_ACTIVITYCLASS)


_PBSPORTINFO = _descriptor.Descriptor(
  name='PbSportInfo',
  full_name='data.PbSportInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='factor', full_name='data.PbSportInfo.factor', index=0,
      number=1, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='time_stamp', full_name='data.PbSportInfo.time_stamp', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sport_profile_id', full_name='data.PbSportInfo.sport_profile_id', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=58,
  serialized_end=151,
)


_PBACTIVITYINFO = _descriptor.Descriptor(
  name='PbActivityInfo',
  full_name='data.PbActivityInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='data.PbActivityInfo.value', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='time_stamp', full_name='data.PbActivityInfo.time_stamp', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='factor', full_name='data.PbActivityInfo.factor', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _PBACTIVITYINFO_ACTIVITYCLASS,
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=154,
  serialized_end=448,
)


_PBINACTIVITYTRIGGERINFO = _descriptor.Descriptor(
  name='PbInActivityTriggerInfo',
  full_name='data.PbInActivityTriggerInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='time_stamp', full_name='data.PbInActivityTriggerInfo.time_stamp', index=0,
      number=1, type=11, cpp_type=10, label=2,
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
  serialized_start=450,
  serialized_end=513,
)


_PBINACTIVITYNONWEARTRIGGERINFO = _descriptor.Descriptor(
  name='PbInActivityNonWearTriggerInfo',
  full_name='data.PbInActivityNonWearTriggerInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='start_time_stamp', full_name='data.PbInActivityNonWearTriggerInfo.start_time_stamp', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='end_time_stamp', full_name='data.PbInActivityNonWearTriggerInfo.end_time_stamp', index=1,
      number=2, type=11, cpp_type=10, label=2,
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
  serialized_start=515,
  serialized_end=633,
)


_PBACTIVITYSAMPLES = _descriptor.Descriptor(
  name='PbActivitySamples',
  full_name='data.PbActivitySamples',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='start_time', full_name='data.PbActivitySamples.start_time', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='met_recording_interval', full_name='data.PbActivitySamples.met_recording_interval', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='steps_recording_interval', full_name='data.PbActivitySamples.steps_recording_interval', index=2,
      number=3, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='met_samples', full_name='data.PbActivitySamples.met_samples', index=3,
      number=4, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='steps_samples', full_name='data.PbActivitySamples.steps_samples', index=4,
      number=5, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sport_info', full_name='data.PbActivitySamples.sport_info', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='activity_info', full_name='data.PbActivitySamples.activity_info', index=6,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='inactivity_trigger', full_name='data.PbActivitySamples.inactivity_trigger', index=7,
      number=8, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='inactivity_non_wear_trigger', full_name='data.PbActivitySamples.inactivity_non_wear_trigger', index=8,
      number=9, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=636,
  serialized_end=1047,
)

_PBSPORTINFO.fields_by_name['time_stamp'].message_type = protobuf_dot_types__pb2._PBLOCALDATETIME
_PBACTIVITYINFO.fields_by_name['value'].enum_type = _PBACTIVITYINFO_ACTIVITYCLASS
_PBACTIVITYINFO.fields_by_name['time_stamp'].message_type = protobuf_dot_types__pb2._PBLOCALDATETIME
_PBACTIVITYINFO_ACTIVITYCLASS.containing_type = _PBACTIVITYINFO
_PBINACTIVITYTRIGGERINFO.fields_by_name['time_stamp'].message_type = protobuf_dot_types__pb2._PBLOCALDATETIME
_PBINACTIVITYNONWEARTRIGGERINFO.fields_by_name['start_time_stamp'].message_type = protobuf_dot_types__pb2._PBLOCALDATETIME
_PBINACTIVITYNONWEARTRIGGERINFO.fields_by_name['end_time_stamp'].message_type = protobuf_dot_types__pb2._PBLOCALDATETIME
_PBACTIVITYSAMPLES.fields_by_name['start_time'].message_type = protobuf_dot_types__pb2._PBLOCALDATETIME
_PBACTIVITYSAMPLES.fields_by_name['met_recording_interval'].message_type = protobuf_dot_types__pb2._PBDURATION
_PBACTIVITYSAMPLES.fields_by_name['steps_recording_interval'].message_type = protobuf_dot_types__pb2._PBDURATION
_PBACTIVITYSAMPLES.fields_by_name['sport_info'].message_type = _PBSPORTINFO
_PBACTIVITYSAMPLES.fields_by_name['activity_info'].message_type = _PBACTIVITYINFO
_PBACTIVITYSAMPLES.fields_by_name['inactivity_trigger'].message_type = _PBINACTIVITYTRIGGERINFO
_PBACTIVITYSAMPLES.fields_by_name['inactivity_non_wear_trigger'].message_type = _PBINACTIVITYNONWEARTRIGGERINFO
DESCRIPTOR.message_types_by_name['PbSportInfo'] = _PBSPORTINFO
DESCRIPTOR.message_types_by_name['PbActivityInfo'] = _PBACTIVITYINFO
DESCRIPTOR.message_types_by_name['PbInActivityTriggerInfo'] = _PBINACTIVITYTRIGGERINFO
DESCRIPTOR.message_types_by_name['PbInActivityNonWearTriggerInfo'] = _PBINACTIVITYNONWEARTRIGGERINFO
DESCRIPTOR.message_types_by_name['PbActivitySamples'] = _PBACTIVITYSAMPLES
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PbSportInfo = _reflection.GeneratedProtocolMessageType('PbSportInfo', (_message.Message,), dict(
  DESCRIPTOR = _PBSPORTINFO,
  __module__ = 'protobuf.act_samples_pb2'
  # @@protoc_insertion_point(class_scope:data.PbSportInfo)
  ))
_sym_db.RegisterMessage(PbSportInfo)

PbActivityInfo = _reflection.GeneratedProtocolMessageType('PbActivityInfo', (_message.Message,), dict(
  DESCRIPTOR = _PBACTIVITYINFO,
  __module__ = 'protobuf.act_samples_pb2'
  # @@protoc_insertion_point(class_scope:data.PbActivityInfo)
  ))
_sym_db.RegisterMessage(PbActivityInfo)

PbInActivityTriggerInfo = _reflection.GeneratedProtocolMessageType('PbInActivityTriggerInfo', (_message.Message,), dict(
  DESCRIPTOR = _PBINACTIVITYTRIGGERINFO,
  __module__ = 'protobuf.act_samples_pb2'
  # @@protoc_insertion_point(class_scope:data.PbInActivityTriggerInfo)
  ))
_sym_db.RegisterMessage(PbInActivityTriggerInfo)

PbInActivityNonWearTriggerInfo = _reflection.GeneratedProtocolMessageType('PbInActivityNonWearTriggerInfo', (_message.Message,), dict(
  DESCRIPTOR = _PBINACTIVITYNONWEARTRIGGERINFO,
  __module__ = 'protobuf.act_samples_pb2'
  # @@protoc_insertion_point(class_scope:data.PbInActivityNonWearTriggerInfo)
  ))
_sym_db.RegisterMessage(PbInActivityNonWearTriggerInfo)

PbActivitySamples = _reflection.GeneratedProtocolMessageType('PbActivitySamples', (_message.Message,), dict(
  DESCRIPTOR = _PBACTIVITYSAMPLES,
  __module__ = 'protobuf.act_samples_pb2'
  # @@protoc_insertion_point(class_scope:data.PbActivitySamples)
  ))
_sym_db.RegisterMessage(PbActivitySamples)


# @@protoc_insertion_point(module_scope)
