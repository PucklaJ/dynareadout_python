from dynareadout_c import *

from lsst.utils import continueClass

@continueClass
class Binout:
  def read(self, path: str):
    type_id = self.get_type_id(path)
    if type_id == BinoutType.Int8:
      return self.read_i8(path)
    elif type_id == BinoutType.Int16:
      return self.read_i16(path)
    elif type_id == BinoutType.Int32:
      return self.read_i32(path)
    elif type_id == BinoutType.Int64:
      return self.read_i64(path)
    elif type_id == BinoutType.Uint8:
      return self.read_u8(path)
    elif type_id == BinoutType.Uint16:
      return self.read_u16(path)
    elif type_id == BinoutType.Uint32:
      return self.read_u32(path)
    elif type_id == BinoutType.Uint64:
      return self.read_u64(path)
    elif type_id == BinoutType.Float32:
      return self.read_f32(path)
    elif type_id == BinoutType.Float64:
      return self.read_f64(path)
    else:
      return list()