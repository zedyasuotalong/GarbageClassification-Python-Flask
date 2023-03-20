# OK code
OK  =  0

# error codes for user
UNSUPPORTED_LOGIN_TYPE            = 1001
USER_ACCOUNT_NONEXISTS            = 1002
USER_ACCOUNT_EXISTS               = 1003
USER_PASSWORD_ERROR               = 1004
USER_PASSWORD_NOTSET              = 1005
USER_VERIFY_CODE_ERROR            = 1006
USER_VERIFY_CODE_EXPIRED          = 1007
REGISTER_USER_ERROR               = 1008
CHANGE_USER_INFO_ERROR            = 1009
UNSUPPORTED_USER_CHANGE_INFO_TYPE = 1010
DELETE_USER_INFO_ERROR            = 1011
# error codes for garbage
UNSUPPORTED_GARBAGE_TYPE = 2001
GARBAGE_INFO_NONEXISTS = 2002
GET_GARBAGE_INFO_ERROR = 2003
CHANGE_GARBAGE_INFO_ERROR = 2004
ADD_GARBAGE_INFO_ERROR = 2005
DELETE_GARBAGE_INFO_ERROR = 2006

# error codes for questions
QUESTION_NONEXISTS          = 3001
GET_QUESTION_INFO_ERROR     = 3002
CHANGE_QUESTION_INFO_ERROR  = 3003
ADD_QUESTION_INFO_ERROR     = 3004
DELETE_QUESTION_INFO_ERROR  = 3005

# other error codes
DB_CONNECTION_ERROR         = 5001
REQUEST_DATA_FORMAT_ERROR   = 5002
MISSING_REQUIRED_PARAMS     = 5003
SEND_VERIFY_CODE_ERROR      = 5004
FILE_TOO_LARGE           = 5005

CODE_STR = {
  OK                          : "成功",
  # error codes for user
  UNSUPPORTED_LOGIN_TYPE      : "不支持的登录方式",
  USER_ACCOUNT_NONEXISTS      : "用户账户不存在",
  USER_ACCOUNT_EXISTS         : "用户账户已存在",
  USER_PASSWORD_ERROR         : "用户密码错误",
  USER_PASSWORD_NOTSET        : "用户密码未设置",
  USER_VERIFY_CODE_ERROR      : "用户验证码错误",
  USER_VERIFY_CODE_EXPIRED    : "用户验证码过期",
  REGISTER_USER_ERROR         : "用户注册失败",
  CHANGE_USER_INFO_ERROR      : "用户修改信息失败",
  UNSUPPORTED_USER_CHANGE_INFO_TYPE : "不支持的用户修改信息类型",
  DELETE_USER_INFO_ERROR      : "用户删除信息失败",

  # error codes for garbage
  UNSUPPORTED_GARBAGE_TYPE    : "不支持的垃圾类型",
  GARBAGE_INFO_NONEXISTS      : "垃圾信息不存在",
  CHANGE_GARBAGE_INFO_ERROR   : "修改垃圾信息失败",
  ADD_QUESTION_INFO_ERROR     : "添加垃圾信息失败",
  DELETE_QUESTION_INFO_ERROR  : "删除垃圾信息失败",
  

  # error codes for questions
  QUESTION_NONEXISTS          : "问题不存在",
  GET_QUESTION_INFO_ERROR     : "获取问题信息失败",
  CHANGE_QUESTION_INFO_ERROR  : "修改问题失败",
  ADD_QUESTION_INFO_ERROR     : "添加问题失败",
  DELETE_QUESTION_INFO_ERROR  : "删除问题失败",
  # other error codes
  DB_CONNECTION_ERROR         : "数据库连接错误",
  REQUEST_DATA_FORMAT_ERROR   : "请求数据格式错误",
  MISSING_REQUIRED_PARAMS     : "缺少必要参数",
  SEND_VERIFY_CODE_ERROR      : "发送验证码错误",
  FILE_TOO_LARGE             : "文件过大"
}
