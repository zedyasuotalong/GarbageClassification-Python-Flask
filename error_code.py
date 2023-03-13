
OK = 0

# error codes for user
 
UNSUPPORTED_LOGIN_TYPE      = 1001
USER_ACCOUNT_NONEXISTS      = 1002
USER_ACCOUNT_EXISTS         = 1003
USER_PASSWORD_ERROR         = 1004
USER_VERIFY_CODE_ERROR      = 1005
USER_VERIFY_CODE_EXPIRED    = 1006

# error codes for garbage

# other error codes
DB_CONNECTION_ERROR         = 5001
REQUEST_DATA_FORMAT_ERROR   = 5002
MISSING_REQUIRED_PARAMS     = 5003
SEND_VERIFY_CODE_ERROR      = 5004

CODE_STR = {
  OK                          : "成功",
  UNSUPPORTED_LOGIN_TYPE      : "不支持的登录方式",
  USER_ACCOUNT_NONEXISTS      : "用户账户不存在",
  USER_ACCOUNT_EXISTS         : "用户账户已存在",
  USER_PASSWORD_ERROR         : "用户密码错误",
  USER_VERIFY_CODE_ERROR      : "用户验证码错误",
  USER_VERIFY_CODE_EXPIRED    : "用户验证码过期",
  DB_CONNECTION_ERROR         : "数据库连接错误",
  REQUEST_DATA_FORMAT_ERROR   : "请求数据格式错误",
  MISSING_REQUIRED_PARAMS     : "缺少必要参数",
  SEND_VERIFY_CODE_ERROR      : "发送验证码错误"
}