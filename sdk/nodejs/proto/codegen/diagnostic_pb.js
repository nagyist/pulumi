// source: pulumi/codegen/diagnostic.proto
/**
 * @fileoverview
 * @enhanceable
 * @suppress {missingRequire} reports error on implicit type usages.
 * @suppress {messageConventions} JS Compiler reports an error if a variable or
 *     field starts with 'MSG_' and isn't a translatable message.
 * @public
 */
// GENERATED CODE -- DO NOT EDIT!
/* eslint-disable */
// @ts-nocheck

var jspb = require('google-protobuf');
var goog = jspb;
var global = (function() { return this || window || global || self || Function('return this')(); }).call(null);

goog.exportSymbol('proto.pulumirpc.codegen.Diagnostic', null, global);
goog.exportSymbol('proto.pulumirpc.codegen.DiagnosticSeverity', null, global);
goog.exportSymbol('proto.pulumirpc.codegen.Pos', null, global);
goog.exportSymbol('proto.pulumirpc.codegen.Range', null, global);
/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.pulumirpc.codegen.Pos = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.pulumirpc.codegen.Pos, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  /**
   * @public
   * @override
   */
  proto.pulumirpc.codegen.Pos.displayName = 'proto.pulumirpc.codegen.Pos';
}
/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.pulumirpc.codegen.Range = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.pulumirpc.codegen.Range, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  /**
   * @public
   * @override
   */
  proto.pulumirpc.codegen.Range.displayName = 'proto.pulumirpc.codegen.Range';
}
/**
 * Generated by JsPbCodeGenerator.
 * @param {Array=} opt_data Optional initial data array, typically from a
 * server response, or constructed directly in Javascript. The array is used
 * in place and becomes part of the constructed object. It is not cloned.
 * If no data is provided, the constructed object will be empty, but still
 * valid.
 * @extends {jspb.Message}
 * @constructor
 */
proto.pulumirpc.codegen.Diagnostic = function(opt_data) {
  jspb.Message.initialize(this, opt_data, 0, -1, null, null);
};
goog.inherits(proto.pulumirpc.codegen.Diagnostic, jspb.Message);
if (goog.DEBUG && !COMPILED) {
  /**
   * @public
   * @override
   */
  proto.pulumirpc.codegen.Diagnostic.displayName = 'proto.pulumirpc.codegen.Diagnostic';
}



if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * Optional fields that are not set will be set to undefined.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     net/proto2/compiler/js/internal/generator.cc#kKeyword.
 * @param {boolean=} opt_includeInstance Deprecated. whether to include the
 *     JSPB instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @return {!Object}
 */
proto.pulumirpc.codegen.Pos.prototype.toObject = function(opt_includeInstance) {
  return proto.pulumirpc.codegen.Pos.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Deprecated. Whether to include
 *     the JSPB instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.pulumirpc.codegen.Pos} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.pulumirpc.codegen.Pos.toObject = function(includeInstance, msg) {
  var f, obj = {
    line: jspb.Message.getFieldWithDefault(msg, 1, 0),
    column: jspb.Message.getFieldWithDefault(msg, 2, 0),
    pb_byte: jspb.Message.getFieldWithDefault(msg, 3, 0)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.pulumirpc.codegen.Pos}
 */
proto.pulumirpc.codegen.Pos.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.pulumirpc.codegen.Pos;
  return proto.pulumirpc.codegen.Pos.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.pulumirpc.codegen.Pos} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.pulumirpc.codegen.Pos}
 */
proto.pulumirpc.codegen.Pos.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = /** @type {number} */ (reader.readInt64());
      msg.setLine(value);
      break;
    case 2:
      var value = /** @type {number} */ (reader.readInt64());
      msg.setColumn(value);
      break;
    case 3:
      var value = /** @type {number} */ (reader.readInt64());
      msg.setByte(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.pulumirpc.codegen.Pos.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.pulumirpc.codegen.Pos.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.pulumirpc.codegen.Pos} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.pulumirpc.codegen.Pos.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getLine();
  if (f !== 0) {
    writer.writeInt64(
      1,
      f
    );
  }
  f = message.getColumn();
  if (f !== 0) {
    writer.writeInt64(
      2,
      f
    );
  }
  f = message.getByte();
  if (f !== 0) {
    writer.writeInt64(
      3,
      f
    );
  }
};


/**
 * optional int64 line = 1;
 * @return {number}
 */
proto.pulumirpc.codegen.Pos.prototype.getLine = function() {
  return /** @type {number} */ (jspb.Message.getFieldWithDefault(this, 1, 0));
};


/**
 * @param {number} value
 * @return {!proto.pulumirpc.codegen.Pos} returns this
 */
proto.pulumirpc.codegen.Pos.prototype.setLine = function(value) {
  return jspb.Message.setProto3IntField(this, 1, value);
};


/**
 * optional int64 column = 2;
 * @return {number}
 */
proto.pulumirpc.codegen.Pos.prototype.getColumn = function() {
  return /** @type {number} */ (jspb.Message.getFieldWithDefault(this, 2, 0));
};


/**
 * @param {number} value
 * @return {!proto.pulumirpc.codegen.Pos} returns this
 */
proto.pulumirpc.codegen.Pos.prototype.setColumn = function(value) {
  return jspb.Message.setProto3IntField(this, 2, value);
};


/**
 * optional int64 byte = 3;
 * @return {number}
 */
proto.pulumirpc.codegen.Pos.prototype.getByte = function() {
  return /** @type {number} */ (jspb.Message.getFieldWithDefault(this, 3, 0));
};


/**
 * @param {number} value
 * @return {!proto.pulumirpc.codegen.Pos} returns this
 */
proto.pulumirpc.codegen.Pos.prototype.setByte = function(value) {
  return jspb.Message.setProto3IntField(this, 3, value);
};





if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * Optional fields that are not set will be set to undefined.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     net/proto2/compiler/js/internal/generator.cc#kKeyword.
 * @param {boolean=} opt_includeInstance Deprecated. whether to include the
 *     JSPB instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @return {!Object}
 */
proto.pulumirpc.codegen.Range.prototype.toObject = function(opt_includeInstance) {
  return proto.pulumirpc.codegen.Range.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Deprecated. Whether to include
 *     the JSPB instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.pulumirpc.codegen.Range} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.pulumirpc.codegen.Range.toObject = function(includeInstance, msg) {
  var f, obj = {
    filename: jspb.Message.getFieldWithDefault(msg, 1, ""),
    start: (f = msg.getStart()) && proto.pulumirpc.codegen.Pos.toObject(includeInstance, f),
    end: (f = msg.getEnd()) && proto.pulumirpc.codegen.Pos.toObject(includeInstance, f)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.pulumirpc.codegen.Range}
 */
proto.pulumirpc.codegen.Range.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.pulumirpc.codegen.Range;
  return proto.pulumirpc.codegen.Range.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.pulumirpc.codegen.Range} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.pulumirpc.codegen.Range}
 */
proto.pulumirpc.codegen.Range.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = /** @type {string} */ (reader.readString());
      msg.setFilename(value);
      break;
    case 2:
      var value = new proto.pulumirpc.codegen.Pos;
      reader.readMessage(value,proto.pulumirpc.codegen.Pos.deserializeBinaryFromReader);
      msg.setStart(value);
      break;
    case 3:
      var value = new proto.pulumirpc.codegen.Pos;
      reader.readMessage(value,proto.pulumirpc.codegen.Pos.deserializeBinaryFromReader);
      msg.setEnd(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.pulumirpc.codegen.Range.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.pulumirpc.codegen.Range.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.pulumirpc.codegen.Range} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.pulumirpc.codegen.Range.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getFilename();
  if (f.length > 0) {
    writer.writeString(
      1,
      f
    );
  }
  f = message.getStart();
  if (f != null) {
    writer.writeMessage(
      2,
      f,
      proto.pulumirpc.codegen.Pos.serializeBinaryToWriter
    );
  }
  f = message.getEnd();
  if (f != null) {
    writer.writeMessage(
      3,
      f,
      proto.pulumirpc.codegen.Pos.serializeBinaryToWriter
    );
  }
};


/**
 * optional string filename = 1;
 * @return {string}
 */
proto.pulumirpc.codegen.Range.prototype.getFilename = function() {
  return /** @type {string} */ (jspb.Message.getFieldWithDefault(this, 1, ""));
};


/**
 * @param {string} value
 * @return {!proto.pulumirpc.codegen.Range} returns this
 */
proto.pulumirpc.codegen.Range.prototype.setFilename = function(value) {
  return jspb.Message.setProto3StringField(this, 1, value);
};


/**
 * optional Pos start = 2;
 * @return {?proto.pulumirpc.codegen.Pos}
 */
proto.pulumirpc.codegen.Range.prototype.getStart = function() {
  return /** @type{?proto.pulumirpc.codegen.Pos} */ (
    jspb.Message.getWrapperField(this, proto.pulumirpc.codegen.Pos, 2));
};


/**
 * @param {?proto.pulumirpc.codegen.Pos|undefined} value
 * @return {!proto.pulumirpc.codegen.Range} returns this
*/
proto.pulumirpc.codegen.Range.prototype.setStart = function(value) {
  return jspb.Message.setWrapperField(this, 2, value);
};


/**
 * Clears the message field making it undefined.
 * @return {!proto.pulumirpc.codegen.Range} returns this
 */
proto.pulumirpc.codegen.Range.prototype.clearStart = function() {
  return this.setStart(undefined);
};


/**
 * Returns whether this field is set.
 * @return {boolean}
 */
proto.pulumirpc.codegen.Range.prototype.hasStart = function() {
  return jspb.Message.getField(this, 2) != null;
};


/**
 * optional Pos end = 3;
 * @return {?proto.pulumirpc.codegen.Pos}
 */
proto.pulumirpc.codegen.Range.prototype.getEnd = function() {
  return /** @type{?proto.pulumirpc.codegen.Pos} */ (
    jspb.Message.getWrapperField(this, proto.pulumirpc.codegen.Pos, 3));
};


/**
 * @param {?proto.pulumirpc.codegen.Pos|undefined} value
 * @return {!proto.pulumirpc.codegen.Range} returns this
*/
proto.pulumirpc.codegen.Range.prototype.setEnd = function(value) {
  return jspb.Message.setWrapperField(this, 3, value);
};


/**
 * Clears the message field making it undefined.
 * @return {!proto.pulumirpc.codegen.Range} returns this
 */
proto.pulumirpc.codegen.Range.prototype.clearEnd = function() {
  return this.setEnd(undefined);
};


/**
 * Returns whether this field is set.
 * @return {boolean}
 */
proto.pulumirpc.codegen.Range.prototype.hasEnd = function() {
  return jspb.Message.getField(this, 3) != null;
};





if (jspb.Message.GENERATE_TO_OBJECT) {
/**
 * Creates an object representation of this proto.
 * Field names that are reserved in JavaScript and will be renamed to pb_name.
 * Optional fields that are not set will be set to undefined.
 * To access a reserved field use, foo.pb_<name>, eg, foo.pb_default.
 * For the list of reserved names please see:
 *     net/proto2/compiler/js/internal/generator.cc#kKeyword.
 * @param {boolean=} opt_includeInstance Deprecated. whether to include the
 *     JSPB instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @return {!Object}
 */
proto.pulumirpc.codegen.Diagnostic.prototype.toObject = function(opt_includeInstance) {
  return proto.pulumirpc.codegen.Diagnostic.toObject(opt_includeInstance, this);
};


/**
 * Static version of the {@see toObject} method.
 * @param {boolean|undefined} includeInstance Deprecated. Whether to include
 *     the JSPB instance for transitional soy proto support:
 *     http://goto/soy-param-migration
 * @param {!proto.pulumirpc.codegen.Diagnostic} msg The msg instance to transform.
 * @return {!Object}
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.pulumirpc.codegen.Diagnostic.toObject = function(includeInstance, msg) {
  var f, obj = {
    severity: jspb.Message.getFieldWithDefault(msg, 1, 0),
    summary: jspb.Message.getFieldWithDefault(msg, 2, ""),
    detail: jspb.Message.getFieldWithDefault(msg, 3, ""),
    subject: (f = msg.getSubject()) && proto.pulumirpc.codegen.Range.toObject(includeInstance, f),
    context: (f = msg.getContext()) && proto.pulumirpc.codegen.Range.toObject(includeInstance, f)
  };

  if (includeInstance) {
    obj.$jspbMessageInstance = msg;
  }
  return obj;
};
}


/**
 * Deserializes binary data (in protobuf wire format).
 * @param {jspb.ByteSource} bytes The bytes to deserialize.
 * @return {!proto.pulumirpc.codegen.Diagnostic}
 */
proto.pulumirpc.codegen.Diagnostic.deserializeBinary = function(bytes) {
  var reader = new jspb.BinaryReader(bytes);
  var msg = new proto.pulumirpc.codegen.Diagnostic;
  return proto.pulumirpc.codegen.Diagnostic.deserializeBinaryFromReader(msg, reader);
};


/**
 * Deserializes binary data (in protobuf wire format) from the
 * given reader into the given message object.
 * @param {!proto.pulumirpc.codegen.Diagnostic} msg The message object to deserialize into.
 * @param {!jspb.BinaryReader} reader The BinaryReader to use.
 * @return {!proto.pulumirpc.codegen.Diagnostic}
 */
proto.pulumirpc.codegen.Diagnostic.deserializeBinaryFromReader = function(msg, reader) {
  while (reader.nextField()) {
    if (reader.isEndGroup()) {
      break;
    }
    var field = reader.getFieldNumber();
    switch (field) {
    case 1:
      var value = /** @type {!proto.pulumirpc.codegen.DiagnosticSeverity} */ (reader.readEnum());
      msg.setSeverity(value);
      break;
    case 2:
      var value = /** @type {string} */ (reader.readString());
      msg.setSummary(value);
      break;
    case 3:
      var value = /** @type {string} */ (reader.readString());
      msg.setDetail(value);
      break;
    case 4:
      var value = new proto.pulumirpc.codegen.Range;
      reader.readMessage(value,proto.pulumirpc.codegen.Range.deserializeBinaryFromReader);
      msg.setSubject(value);
      break;
    case 5:
      var value = new proto.pulumirpc.codegen.Range;
      reader.readMessage(value,proto.pulumirpc.codegen.Range.deserializeBinaryFromReader);
      msg.setContext(value);
      break;
    default:
      reader.skipField();
      break;
    }
  }
  return msg;
};


/**
 * Serializes the message to binary data (in protobuf wire format).
 * @return {!Uint8Array}
 */
proto.pulumirpc.codegen.Diagnostic.prototype.serializeBinary = function() {
  var writer = new jspb.BinaryWriter();
  proto.pulumirpc.codegen.Diagnostic.serializeBinaryToWriter(this, writer);
  return writer.getResultBuffer();
};


/**
 * Serializes the given message to binary data (in protobuf wire
 * format), writing to the given BinaryWriter.
 * @param {!proto.pulumirpc.codegen.Diagnostic} message
 * @param {!jspb.BinaryWriter} writer
 * @suppress {unusedLocalVariables} f is only used for nested messages
 */
proto.pulumirpc.codegen.Diagnostic.serializeBinaryToWriter = function(message, writer) {
  var f = undefined;
  f = message.getSeverity();
  if (f !== 0.0) {
    writer.writeEnum(
      1,
      f
    );
  }
  f = message.getSummary();
  if (f.length > 0) {
    writer.writeString(
      2,
      f
    );
  }
  f = message.getDetail();
  if (f.length > 0) {
    writer.writeString(
      3,
      f
    );
  }
  f = message.getSubject();
  if (f != null) {
    writer.writeMessage(
      4,
      f,
      proto.pulumirpc.codegen.Range.serializeBinaryToWriter
    );
  }
  f = message.getContext();
  if (f != null) {
    writer.writeMessage(
      5,
      f,
      proto.pulumirpc.codegen.Range.serializeBinaryToWriter
    );
  }
};


/**
 * optional DiagnosticSeverity severity = 1;
 * @return {!proto.pulumirpc.codegen.DiagnosticSeverity}
 */
proto.pulumirpc.codegen.Diagnostic.prototype.getSeverity = function() {
  return /** @type {!proto.pulumirpc.codegen.DiagnosticSeverity} */ (jspb.Message.getFieldWithDefault(this, 1, 0));
};


/**
 * @param {!proto.pulumirpc.codegen.DiagnosticSeverity} value
 * @return {!proto.pulumirpc.codegen.Diagnostic} returns this
 */
proto.pulumirpc.codegen.Diagnostic.prototype.setSeverity = function(value) {
  return jspb.Message.setProto3EnumField(this, 1, value);
};


/**
 * optional string summary = 2;
 * @return {string}
 */
proto.pulumirpc.codegen.Diagnostic.prototype.getSummary = function() {
  return /** @type {string} */ (jspb.Message.getFieldWithDefault(this, 2, ""));
};


/**
 * @param {string} value
 * @return {!proto.pulumirpc.codegen.Diagnostic} returns this
 */
proto.pulumirpc.codegen.Diagnostic.prototype.setSummary = function(value) {
  return jspb.Message.setProto3StringField(this, 2, value);
};


/**
 * optional string detail = 3;
 * @return {string}
 */
proto.pulumirpc.codegen.Diagnostic.prototype.getDetail = function() {
  return /** @type {string} */ (jspb.Message.getFieldWithDefault(this, 3, ""));
};


/**
 * @param {string} value
 * @return {!proto.pulumirpc.codegen.Diagnostic} returns this
 */
proto.pulumirpc.codegen.Diagnostic.prototype.setDetail = function(value) {
  return jspb.Message.setProto3StringField(this, 3, value);
};


/**
 * optional Range subject = 4;
 * @return {?proto.pulumirpc.codegen.Range}
 */
proto.pulumirpc.codegen.Diagnostic.prototype.getSubject = function() {
  return /** @type{?proto.pulumirpc.codegen.Range} */ (
    jspb.Message.getWrapperField(this, proto.pulumirpc.codegen.Range, 4));
};


/**
 * @param {?proto.pulumirpc.codegen.Range|undefined} value
 * @return {!proto.pulumirpc.codegen.Diagnostic} returns this
*/
proto.pulumirpc.codegen.Diagnostic.prototype.setSubject = function(value) {
  return jspb.Message.setWrapperField(this, 4, value);
};


/**
 * Clears the message field making it undefined.
 * @return {!proto.pulumirpc.codegen.Diagnostic} returns this
 */
proto.pulumirpc.codegen.Diagnostic.prototype.clearSubject = function() {
  return this.setSubject(undefined);
};


/**
 * Returns whether this field is set.
 * @return {boolean}
 */
proto.pulumirpc.codegen.Diagnostic.prototype.hasSubject = function() {
  return jspb.Message.getField(this, 4) != null;
};


/**
 * optional Range context = 5;
 * @return {?proto.pulumirpc.codegen.Range}
 */
proto.pulumirpc.codegen.Diagnostic.prototype.getContext = function() {
  return /** @type{?proto.pulumirpc.codegen.Range} */ (
    jspb.Message.getWrapperField(this, proto.pulumirpc.codegen.Range, 5));
};


/**
 * @param {?proto.pulumirpc.codegen.Range|undefined} value
 * @return {!proto.pulumirpc.codegen.Diagnostic} returns this
*/
proto.pulumirpc.codegen.Diagnostic.prototype.setContext = function(value) {
  return jspb.Message.setWrapperField(this, 5, value);
};


/**
 * Clears the message field making it undefined.
 * @return {!proto.pulumirpc.codegen.Diagnostic} returns this
 */
proto.pulumirpc.codegen.Diagnostic.prototype.clearContext = function() {
  return this.setContext(undefined);
};


/**
 * Returns whether this field is set.
 * @return {boolean}
 */
proto.pulumirpc.codegen.Diagnostic.prototype.hasContext = function() {
  return jspb.Message.getField(this, 5) != null;
};


/**
 * @enum {number}
 */
proto.pulumirpc.codegen.DiagnosticSeverity = {
  DIAG_UNDEFINED: 0,
  DIAG_ERROR: 1,
  DIAG_WARNING: 2
};

goog.object.extend(exports, proto.pulumirpc.codegen);
