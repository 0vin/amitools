INVALID_BOOT_BLOCK = 1
INVALID_ROOT_BLOCK = 2
INVALID_USER_DIR_BLOCK = 3
INVALID_FILE_HEADER_BLOCK = 4
INVALID_FILE_LIST_BLOCK = 5
INVALID_FILE_DATA_BLOCK = 6
NO_FREE_BLOCKS = 7
UNSUPPORTED_DIR_BLOCK = 8
INVALID_FILE_NAME = 9
NAME_ALREADY_EXISTS = 10
INVALID_SEQ_NUM = 11

error_names = {
  INVALID_BOOT_BLOCK : "Invalid Boot Block",
  INVALID_ROOT_BLOCK : "Invalid Root Block",
  INVALID_USER_DIR_BLOCK : "Invalid UserDir Block",
  INVALID_FILE_HEADER_BLOCK : "Invalid FileHeader Block",
  INVALID_FILE_LIST_BLOCK : "Invalid FileList Block",
  INVALID_FILE_DATA_BLOCK : "Invalid FileData Block",
  NO_FREE_BLOCKS : "No Free Blocks",
  UNSUPPORTED_DIR_BLOCK : "Unsupported Dir Block",
  INVALID_FILE_NAME : "Invalid File Name",
  NAME_ALREADY_EXISTS : "Name already exists",
  INVALID_SEQ_NUM : "Invalid Sequence Number"
}

class FSError(Exception):
  def __init__(self, code, node=None, block=None, file_name=None, extra=None):
    self.code = code
    self.node = node
    self.block = block
    self.file_name = file_name
    self.extra = None
  def __str__(self):
    if error_names.has_key(self.code):
      code_str = error_names[self.code]
    else:
      code_str = "?"
    srcs = []
    if self.node != None:
      srcs.append("node=" + str(self.node))
    if self.block != None:
      srcs.append("block=" + str(self.block))
    if self.file_name != None:
      srcs.append("file_name='%s'" % self.file_name)
    if self.exta != None:
      srcs.append(self.extra)
    return "%s(%d):%s" % (code_str, self.code, ",".join(srcs))

    