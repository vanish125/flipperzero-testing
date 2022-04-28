# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: system.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='system.proto',
  package='PB_System',
  syntax='proto3',
  serialized_options=b'\n\"com.flipperdevices.protobuf.system',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0csystem.proto\x12\tPB_System\"\x1b\n\x0bPingRequest\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\x0c\"\x1c\n\x0cPingResponse\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\x0c\"m\n\rRebootRequest\x12\x31\n\x04mode\x18\x01 \x01(\x0e\x32#.PB_System.RebootRequest.RebootMode\")\n\nRebootMode\x12\x06\n\x02OS\x10\x00\x12\x07\n\x03\x44\x46U\x10\x01\x12\n\n\x06UPDATE\x10\x02\"\x13\n\x11\x44\x65viceInfoRequest\"0\n\x12\x44\x65viceInfoResponse\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\"\x15\n\x13\x46\x61\x63toryResetRequest\"\x14\n\x12GetDateTimeRequest\"<\n\x13GetDateTimeResponse\x12%\n\x08\x64\x61tetime\x18\x01 \x01(\x0b\x32\x13.PB_System.DateTime\";\n\x12SetDateTimeRequest\x12%\n\x08\x64\x61tetime\x18\x01 \x01(\x0b\x32\x13.PB_System.DateTime\"s\n\x08\x44\x61teTime\x12\x0c\n\x04hour\x18\x01 \x01(\r\x12\x0e\n\x06minute\x18\x02 \x01(\r\x12\x0e\n\x06second\x18\x03 \x01(\r\x12\x0b\n\x03\x64\x61y\x18\x04 \x01(\r\x12\r\n\x05month\x18\x05 \x01(\r\x12\x0c\n\x04year\x18\x06 \x01(\r\x12\x0f\n\x07weekday\x18\x07 \x01(\r\"\x1d\n\x1bPlayAudiovisualAlertRequest\"\x18\n\x16ProtobufVersionRequest\"7\n\x17ProtobufVersionResponse\x12\r\n\x05major\x18\x01 \x01(\r\x12\r\n\x05minor\x18\x02 \x01(\r\"(\n\rUpdateRequest\x12\x17\n\x0fupdate_manifest\x18\x01 \x01(\t\"\x12\n\x10PowerInfoRequest\"/\n\x11PowerInfoResponse\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\tB$\n\"com.flipperdevices.protobuf.systemb\x06proto3'
)



_REBOOTREQUEST_REBOOTMODE = _descriptor.EnumDescriptor(
  name='RebootMode',
  full_name='PB_System.RebootRequest.RebootMode',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='OS', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DFU', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='UPDATE', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=154,
  serialized_end=195,
)
_sym_db.RegisterEnumDescriptor(_REBOOTREQUEST_REBOOTMODE)


_PINGREQUEST = _descriptor.Descriptor(
  name='PingRequest',
  full_name='PB_System.PingRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='PB_System.PingRequest.data', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
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
  serialized_start=27,
  serialized_end=54,
)


_PINGRESPONSE = _descriptor.Descriptor(
  name='PingResponse',
  full_name='PB_System.PingResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='PB_System.PingResponse.data', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
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
  serialized_start=56,
  serialized_end=84,
)


_REBOOTREQUEST = _descriptor.Descriptor(
  name='RebootRequest',
  full_name='PB_System.RebootRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='mode', full_name='PB_System.RebootRequest.mode', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _REBOOTREQUEST_REBOOTMODE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=86,
  serialized_end=195,
)


_DEVICEINFOREQUEST = _descriptor.Descriptor(
  name='DeviceInfoRequest',
  full_name='PB_System.DeviceInfoRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
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
  serialized_start=197,
  serialized_end=216,
)


_DEVICEINFORESPONSE = _descriptor.Descriptor(
  name='DeviceInfoResponse',
  full_name='PB_System.DeviceInfoResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='PB_System.DeviceInfoResponse.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='PB_System.DeviceInfoResponse.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=218,
  serialized_end=266,
)


_FACTORYRESETREQUEST = _descriptor.Descriptor(
  name='FactoryResetRequest',
  full_name='PB_System.FactoryResetRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
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
  serialized_start=268,
  serialized_end=289,
)


_GETDATETIMEREQUEST = _descriptor.Descriptor(
  name='GetDateTimeRequest',
  full_name='PB_System.GetDateTimeRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
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
  serialized_start=291,
  serialized_end=311,
)


_GETDATETIMERESPONSE = _descriptor.Descriptor(
  name='GetDateTimeResponse',
  full_name='PB_System.GetDateTimeResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='datetime', full_name='PB_System.GetDateTimeResponse.datetime', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=313,
  serialized_end=373,
)


_SETDATETIMEREQUEST = _descriptor.Descriptor(
  name='SetDateTimeRequest',
  full_name='PB_System.SetDateTimeRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='datetime', full_name='PB_System.SetDateTimeRequest.datetime', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=375,
  serialized_end=434,
)


_DATETIME = _descriptor.Descriptor(
  name='DateTime',
  full_name='PB_System.DateTime',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='hour', full_name='PB_System.DateTime.hour', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='minute', full_name='PB_System.DateTime.minute', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='second', full_name='PB_System.DateTime.second', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='day', full_name='PB_System.DateTime.day', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='month', full_name='PB_System.DateTime.month', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='year', full_name='PB_System.DateTime.year', index=5,
      number=6, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='weekday', full_name='PB_System.DateTime.weekday', index=6,
      number=7, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=436,
  serialized_end=551,
)


_PLAYAUDIOVISUALALERTREQUEST = _descriptor.Descriptor(
  name='PlayAudiovisualAlertRequest',
  full_name='PB_System.PlayAudiovisualAlertRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
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
  serialized_start=553,
  serialized_end=582,
)


_PROTOBUFVERSIONREQUEST = _descriptor.Descriptor(
  name='ProtobufVersionRequest',
  full_name='PB_System.ProtobufVersionRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
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
  serialized_start=584,
  serialized_end=608,
)


_PROTOBUFVERSIONRESPONSE = _descriptor.Descriptor(
  name='ProtobufVersionResponse',
  full_name='PB_System.ProtobufVersionResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='major', full_name='PB_System.ProtobufVersionResponse.major', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='minor', full_name='PB_System.ProtobufVersionResponse.minor', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=610,
  serialized_end=665,
)


_UPDATEREQUEST = _descriptor.Descriptor(
  name='UpdateRequest',
  full_name='PB_System.UpdateRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='update_manifest', full_name='PB_System.UpdateRequest.update_manifest', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=667,
  serialized_end=707,
)


_POWERINFOREQUEST = _descriptor.Descriptor(
  name='PowerInfoRequest',
  full_name='PB_System.PowerInfoRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
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
  serialized_start=709,
  serialized_end=727,
)


_POWERINFORESPONSE = _descriptor.Descriptor(
  name='PowerInfoResponse',
  full_name='PB_System.PowerInfoResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='PB_System.PowerInfoResponse.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='PB_System.PowerInfoResponse.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=729,
  serialized_end=776,
)

_REBOOTREQUEST.fields_by_name['mode'].enum_type = _REBOOTREQUEST_REBOOTMODE
_REBOOTREQUEST_REBOOTMODE.containing_type = _REBOOTREQUEST
_GETDATETIMERESPONSE.fields_by_name['datetime'].message_type = _DATETIME
_SETDATETIMEREQUEST.fields_by_name['datetime'].message_type = _DATETIME
DESCRIPTOR.message_types_by_name['PingRequest'] = _PINGREQUEST
DESCRIPTOR.message_types_by_name['PingResponse'] = _PINGRESPONSE
DESCRIPTOR.message_types_by_name['RebootRequest'] = _REBOOTREQUEST
DESCRIPTOR.message_types_by_name['DeviceInfoRequest'] = _DEVICEINFOREQUEST
DESCRIPTOR.message_types_by_name['DeviceInfoResponse'] = _DEVICEINFORESPONSE
DESCRIPTOR.message_types_by_name['FactoryResetRequest'] = _FACTORYRESETREQUEST
DESCRIPTOR.message_types_by_name['GetDateTimeRequest'] = _GETDATETIMEREQUEST
DESCRIPTOR.message_types_by_name['GetDateTimeResponse'] = _GETDATETIMERESPONSE
DESCRIPTOR.message_types_by_name['SetDateTimeRequest'] = _SETDATETIMEREQUEST
DESCRIPTOR.message_types_by_name['DateTime'] = _DATETIME
DESCRIPTOR.message_types_by_name['PlayAudiovisualAlertRequest'] = _PLAYAUDIOVISUALALERTREQUEST
DESCRIPTOR.message_types_by_name['ProtobufVersionRequest'] = _PROTOBUFVERSIONREQUEST
DESCRIPTOR.message_types_by_name['ProtobufVersionResponse'] = _PROTOBUFVERSIONRESPONSE
DESCRIPTOR.message_types_by_name['UpdateRequest'] = _UPDATEREQUEST
DESCRIPTOR.message_types_by_name['PowerInfoRequest'] = _POWERINFOREQUEST
DESCRIPTOR.message_types_by_name['PowerInfoResponse'] = _POWERINFORESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PingRequest = _reflection.GeneratedProtocolMessageType('PingRequest', (_message.Message,), {
  'DESCRIPTOR' : _PINGREQUEST,
  '__module__' : 'system_pb2'
  # @@protoc_insertion_point(class_scope:PB_System.PingRequest)
  })
_sym_db.RegisterMessage(PingRequest)

PingResponse = _reflection.GeneratedProtocolMessageType('PingResponse', (_message.Message,), {
  'DESCRIPTOR' : _PINGRESPONSE,
  '__module__' : 'system_pb2'
  # @@protoc_insertion_point(class_scope:PB_System.PingResponse)
  })
_sym_db.RegisterMessage(PingResponse)

RebootRequest = _reflection.GeneratedProtocolMessageType('RebootRequest', (_message.Message,), {
  'DESCRIPTOR' : _REBOOTREQUEST,
  '__module__' : 'system_pb2'
  # @@protoc_insertion_point(class_scope:PB_System.RebootRequest)
  })
_sym_db.RegisterMessage(RebootRequest)

DeviceInfoRequest = _reflection.GeneratedProtocolMessageType('DeviceInfoRequest', (_message.Message,), {
  'DESCRIPTOR' : _DEVICEINFOREQUEST,
  '__module__' : 'system_pb2'
  # @@protoc_insertion_point(class_scope:PB_System.DeviceInfoRequest)
  })
_sym_db.RegisterMessage(DeviceInfoRequest)

DeviceInfoResponse = _reflection.GeneratedProtocolMessageType('DeviceInfoResponse', (_message.Message,), {
  'DESCRIPTOR' : _DEVICEINFORESPONSE,
  '__module__' : 'system_pb2'
  # @@protoc_insertion_point(class_scope:PB_System.DeviceInfoResponse)
  })
_sym_db.RegisterMessage(DeviceInfoResponse)

FactoryResetRequest = _reflection.GeneratedProtocolMessageType('FactoryResetRequest', (_message.Message,), {
  'DESCRIPTOR' : _FACTORYRESETREQUEST,
  '__module__' : 'system_pb2'
  # @@protoc_insertion_point(class_scope:PB_System.FactoryResetRequest)
  })
_sym_db.RegisterMessage(FactoryResetRequest)

GetDateTimeRequest = _reflection.GeneratedProtocolMessageType('GetDateTimeRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETDATETIMEREQUEST,
  '__module__' : 'system_pb2'
  # @@protoc_insertion_point(class_scope:PB_System.GetDateTimeRequest)
  })
_sym_db.RegisterMessage(GetDateTimeRequest)

GetDateTimeResponse = _reflection.GeneratedProtocolMessageType('GetDateTimeResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETDATETIMERESPONSE,
  '__module__' : 'system_pb2'
  # @@protoc_insertion_point(class_scope:PB_System.GetDateTimeResponse)
  })
_sym_db.RegisterMessage(GetDateTimeResponse)

SetDateTimeRequest = _reflection.GeneratedProtocolMessageType('SetDateTimeRequest', (_message.Message,), {
  'DESCRIPTOR' : _SETDATETIMEREQUEST,
  '__module__' : 'system_pb2'
  # @@protoc_insertion_point(class_scope:PB_System.SetDateTimeRequest)
  })
_sym_db.RegisterMessage(SetDateTimeRequest)

DateTime = _reflection.GeneratedProtocolMessageType('DateTime', (_message.Message,), {
  'DESCRIPTOR' : _DATETIME,
  '__module__' : 'system_pb2'
  # @@protoc_insertion_point(class_scope:PB_System.DateTime)
  })
_sym_db.RegisterMessage(DateTime)

PlayAudiovisualAlertRequest = _reflection.GeneratedProtocolMessageType('PlayAudiovisualAlertRequest', (_message.Message,), {
  'DESCRIPTOR' : _PLAYAUDIOVISUALALERTREQUEST,
  '__module__' : 'system_pb2'
  # @@protoc_insertion_point(class_scope:PB_System.PlayAudiovisualAlertRequest)
  })
_sym_db.RegisterMessage(PlayAudiovisualAlertRequest)

ProtobufVersionRequest = _reflection.GeneratedProtocolMessageType('ProtobufVersionRequest', (_message.Message,), {
  'DESCRIPTOR' : _PROTOBUFVERSIONREQUEST,
  '__module__' : 'system_pb2'
  # @@protoc_insertion_point(class_scope:PB_System.ProtobufVersionRequest)
  })
_sym_db.RegisterMessage(ProtobufVersionRequest)

ProtobufVersionResponse = _reflection.GeneratedProtocolMessageType('ProtobufVersionResponse', (_message.Message,), {
  'DESCRIPTOR' : _PROTOBUFVERSIONRESPONSE,
  '__module__' : 'system_pb2'
  # @@protoc_insertion_point(class_scope:PB_System.ProtobufVersionResponse)
  })
_sym_db.RegisterMessage(ProtobufVersionResponse)

UpdateRequest = _reflection.GeneratedProtocolMessageType('UpdateRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEREQUEST,
  '__module__' : 'system_pb2'
  # @@protoc_insertion_point(class_scope:PB_System.UpdateRequest)
  })
_sym_db.RegisterMessage(UpdateRequest)

PowerInfoRequest = _reflection.GeneratedProtocolMessageType('PowerInfoRequest', (_message.Message,), {
  'DESCRIPTOR' : _POWERINFOREQUEST,
  '__module__' : 'system_pb2'
  # @@protoc_insertion_point(class_scope:PB_System.PowerInfoRequest)
  })
_sym_db.RegisterMessage(PowerInfoRequest)

PowerInfoResponse = _reflection.GeneratedProtocolMessageType('PowerInfoResponse', (_message.Message,), {
  'DESCRIPTOR' : _POWERINFORESPONSE,
  '__module__' : 'system_pb2'
  # @@protoc_insertion_point(class_scope:PB_System.PowerInfoResponse)
  })
_sym_db.RegisterMessage(PowerInfoResponse)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)