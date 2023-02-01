from dynareadout_c import *

from lsst.utils import continueClass


@continueClass
class Binout:
    def read(self, path: str):
        real_path, type_id, timed = self.simple_path_to_real(path)
        real_path = str(real_path)

        if type_id == BinoutType.Int8:
            return self.read_i8(real_path)
        elif type_id == BinoutType.Int16:
            return self.read_i16(real_path)
        elif type_id == BinoutType.Int32:
            return self.read_i32(real_path)
        elif type_id == BinoutType.Int64:
            return self.read_i64(real_path)
        elif type_id == BinoutType.Uint8:
            return self.read_u8(real_path)
        elif type_id == BinoutType.Uint16:
            return self.read_u16(real_path)
        elif type_id == BinoutType.Uint32:
            return self.read_u32(real_path)
        elif type_id == BinoutType.Uint64:
            return self.read_u64(real_path)
        elif type_id == BinoutType.Float32:
            if timed:
                return self.read_timed_f32(real_path)
            return self.read_f32(real_path)
        elif type_id == BinoutType.Float64:
            if timed:
                return self.read_timed_f64(real_path)
            return self.read_f64(real_path)
        else:
            children = self.get_children(real_path)
            if str(children[-1]) == "metadata" and str(
                    children[0]) == "d000001":
                metadata = real_path + "/metadata"
                d000001 = real_path + "/d000001"
                metadata_children = self.get_children(metadata)
                d000001_children = self.get_children(d000001)

                metadata_children.extend(d000001_children)
                metadata_children.sort()
                return metadata_children
            return children
