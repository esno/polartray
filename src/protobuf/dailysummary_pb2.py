# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protobuf/dailysummary.proto

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
  name='protobuf/dailysummary.proto',
  package='data',
  syntax='proto2',
  serialized_pb=_b('\n\x1bprotobuf/dailysummary.proto\x12\x04\x64\x61ta\x1a\x14protobuf/types.proto\"\xb8\x01\n\x15PbActivityGoalSummary\x12\x15\n\ractivity_goal\x18\x01 \x02(\x02\x12\x19\n\x11\x61\x63hieved_activity\x18\x02 \x02(\x02\x12\"\n\rtime_to_go_up\x18\x03 \x01(\x0b\x32\x0b.PbDuration\x12$\n\x0ftime_to_go_walk\x18\x04 \x01(\x0b\x32\x0b.PbDuration\x12#\n\x0etime_to_go_jog\x18\x05 \x01(\x0b\x32\x0b.PbDuration\"\xea\x02\n\x14PbActivityClassTimes\x12\"\n\rtime_non_wear\x18\x01 \x02(\x0b\x32\x0b.PbDuration\x12\x1f\n\ntime_sleep\x18\x02 \x02(\x0b\x32\x0b.PbDuration\x12#\n\x0etime_sedentary\x18\x03 \x02(\x0b\x32\x0b.PbDuration\x12(\n\x13time_light_activity\x18\x04 \x02(\x0b\x32\x0b.PbDuration\x12-\n\x18time_continuous_moderate\x18\x05 \x02(\x0b\x32\x0b.PbDuration\x12/\n\x1atime_intermittent_moderate\x18\x06 \x02(\x0b\x32\x0b.PbDuration\x12-\n\x18time_continuous_vigorous\x18\x07 \x02(\x0b\x32\x0b.PbDuration\x12/\n\x1atime_intermittent_vigorous\x18\x08 \x02(\x0b\x32\x0b.PbDuration\"\x93\x02\n\x0ePbDailySummary\x12\x15\n\x04\x64\x61te\x18\x01 \x02(\x0b\x32\x07.PbDate\x12\r\n\x05steps\x18\x02 \x01(\r\x12\x19\n\x11\x61\x63tivity_calories\x18\x03 \x01(\r\x12\x19\n\x11training_calories\x18\x04 \x01(\r\x12\x14\n\x0c\x62mr_calories\x18\x05 \x01(\r\x12:\n\x15\x61\x63tivity_goal_summary\x18\x06 \x01(\x0b\x32\x1b.data.PbActivityGoalSummary\x12\x38\n\x14\x61\x63tivity_class_times\x18\x07 \x01(\x0b\x32\x1a.data.PbActivityClassTimes\x12\x19\n\x11\x61\x63tivity_distance\x18\x08 \x01(\x02')
  ,
  dependencies=[protobuf_dot_types__pb2.DESCRIPTOR,])




_PBACTIVITYGOALSUMMARY = _descriptor.Descriptor(
  name='PbActivityGoalSummary',
  full_name='data.PbActivityGoalSummary',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='activity_goal', full_name='data.PbActivityGoalSummary.activity_goal', index=0,
      number=1, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='achieved_activity', full_name='data.PbActivityGoalSummary.achieved_activity', index=1,
      number=2, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='time_to_go_up', full_name='data.PbActivityGoalSummary.time_to_go_up', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='time_to_go_walk', full_name='data.PbActivityGoalSummary.time_to_go_walk', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='time_to_go_jog', full_name='data.PbActivityGoalSummary.time_to_go_jog', index=4,
      number=5, type=11, cpp_type=10, label=1,
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
  serialized_start=60,
  serialized_end=244,
)


_PBACTIVITYCLASSTIMES = _descriptor.Descriptor(
  name='PbActivityClassTimes',
  full_name='data.PbActivityClassTimes',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='time_non_wear', full_name='data.PbActivityClassTimes.time_non_wear', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='time_sleep', full_name='data.PbActivityClassTimes.time_sleep', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='time_sedentary', full_name='data.PbActivityClassTimes.time_sedentary', index=2,
      number=3, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='time_light_activity', full_name='data.PbActivityClassTimes.time_light_activity', index=3,
      number=4, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='time_continuous_moderate', full_name='data.PbActivityClassTimes.time_continuous_moderate', index=4,
      number=5, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='time_intermittent_moderate', full_name='data.PbActivityClassTimes.time_intermittent_moderate', index=5,
      number=6, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='time_continuous_vigorous', full_name='data.PbActivityClassTimes.time_continuous_vigorous', index=6,
      number=7, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='time_intermittent_vigorous', full_name='data.PbActivityClassTimes.time_intermittent_vigorous', index=7,
      number=8, type=11, cpp_type=10, label=2,
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
  serialized_start=247,
  serialized_end=609,
)


_PBDAILYSUMMARY = _descriptor.Descriptor(
  name='PbDailySummary',
  full_name='data.PbDailySummary',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='date', full_name='data.PbDailySummary.date', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='steps', full_name='data.PbDailySummary.steps', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='activity_calories', full_name='data.PbDailySummary.activity_calories', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='training_calories', full_name='data.PbDailySummary.training_calories', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='bmr_calories', full_name='data.PbDailySummary.bmr_calories', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='activity_goal_summary', full_name='data.PbDailySummary.activity_goal_summary', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='activity_class_times', full_name='data.PbDailySummary.activity_class_times', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='activity_distance', full_name='data.PbDailySummary.activity_distance', index=7,
      number=8, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=612,
  serialized_end=887,
)

_PBACTIVITYGOALSUMMARY.fields_by_name['time_to_go_up'].message_type = protobuf_dot_types__pb2._PBDURATION
_PBACTIVITYGOALSUMMARY.fields_by_name['time_to_go_walk'].message_type = protobuf_dot_types__pb2._PBDURATION
_PBACTIVITYGOALSUMMARY.fields_by_name['time_to_go_jog'].message_type = protobuf_dot_types__pb2._PBDURATION
_PBACTIVITYCLASSTIMES.fields_by_name['time_non_wear'].message_type = protobuf_dot_types__pb2._PBDURATION
_PBACTIVITYCLASSTIMES.fields_by_name['time_sleep'].message_type = protobuf_dot_types__pb2._PBDURATION
_PBACTIVITYCLASSTIMES.fields_by_name['time_sedentary'].message_type = protobuf_dot_types__pb2._PBDURATION
_PBACTIVITYCLASSTIMES.fields_by_name['time_light_activity'].message_type = protobuf_dot_types__pb2._PBDURATION
_PBACTIVITYCLASSTIMES.fields_by_name['time_continuous_moderate'].message_type = protobuf_dot_types__pb2._PBDURATION
_PBACTIVITYCLASSTIMES.fields_by_name['time_intermittent_moderate'].message_type = protobuf_dot_types__pb2._PBDURATION
_PBACTIVITYCLASSTIMES.fields_by_name['time_continuous_vigorous'].message_type = protobuf_dot_types__pb2._PBDURATION
_PBACTIVITYCLASSTIMES.fields_by_name['time_intermittent_vigorous'].message_type = protobuf_dot_types__pb2._PBDURATION
_PBDAILYSUMMARY.fields_by_name['date'].message_type = protobuf_dot_types__pb2._PBDATE
_PBDAILYSUMMARY.fields_by_name['activity_goal_summary'].message_type = _PBACTIVITYGOALSUMMARY
_PBDAILYSUMMARY.fields_by_name['activity_class_times'].message_type = _PBACTIVITYCLASSTIMES
DESCRIPTOR.message_types_by_name['PbActivityGoalSummary'] = _PBACTIVITYGOALSUMMARY
DESCRIPTOR.message_types_by_name['PbActivityClassTimes'] = _PBACTIVITYCLASSTIMES
DESCRIPTOR.message_types_by_name['PbDailySummary'] = _PBDAILYSUMMARY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PbActivityGoalSummary = _reflection.GeneratedProtocolMessageType('PbActivityGoalSummary', (_message.Message,), dict(
  DESCRIPTOR = _PBACTIVITYGOALSUMMARY,
  __module__ = 'protobuf.dailysummary_pb2'
  # @@protoc_insertion_point(class_scope:data.PbActivityGoalSummary)
  ))
_sym_db.RegisterMessage(PbActivityGoalSummary)

PbActivityClassTimes = _reflection.GeneratedProtocolMessageType('PbActivityClassTimes', (_message.Message,), dict(
  DESCRIPTOR = _PBACTIVITYCLASSTIMES,
  __module__ = 'protobuf.dailysummary_pb2'
  # @@protoc_insertion_point(class_scope:data.PbActivityClassTimes)
  ))
_sym_db.RegisterMessage(PbActivityClassTimes)

PbDailySummary = _reflection.GeneratedProtocolMessageType('PbDailySummary', (_message.Message,), dict(
  DESCRIPTOR = _PBDAILYSUMMARY,
  __module__ = 'protobuf.dailysummary_pb2'
  # @@protoc_insertion_point(class_scope:data.PbDailySummary)
  ))
_sym_db.RegisterMessage(PbDailySummary)


# @@protoc_insertion_point(module_scope)
