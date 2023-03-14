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
USER_REGISTER_ERROR               = 1008
USER_CHANGE_INFO_ERROR            = 1009
UNSUPPORTED_USER_CHANGE_INFO_TYPE = 1010
# error codes for garbage

# other error codes
DB_CONNECTION_ERROR         = 5001
REQUEST_DATA_FORMAT_ERROR   = 5002
MISSING_REQUIRED_PARAMS     = 5003
SEND_VERIFY_CODE_ERROR      = 5004

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
  USER_REGISTER_ERROR         : "用户注册失败",
  USER_CHANGE_INFO_ERROR      : "用户修改信息失败",
  UNSUPPORTED_USER_CHANGE_INFO_TYPE : "不支持的用户修改信息类型",

  # error codes for garbage

  # other error codes
  DB_CONNECTION_ERROR         : "数据库连接错误",
  REQUEST_DATA_FORMAT_ERROR   : "请求数据格式错误",
  MISSING_REQUIRED_PARAMS     : "缺少必要参数",
  SEND_VERIFY_CODE_ERROR      : "发送验证码错误"
}