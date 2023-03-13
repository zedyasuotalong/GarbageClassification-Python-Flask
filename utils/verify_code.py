import sys

from typing import List
from utils.debug import DEBUG
from error_code import *

from alibabacloud_dysmsapi20170525.client import Client as Dysmsapi20170525Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dysmsapi20170525 import models as dysmsapi_20170525_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

def create_client(
    access_key_id: str,
    access_key_secret: str,
) -> Dysmsapi20170525Client:
    """
    使用AK&SK初始化账号Client
    @param access_key_id:
    @param access_key_secret:
    @return: Client
    @throws Exception
    """
    config = open_api_models.Config(
        # 必填，您的 AccessKey ID,
        access_key_id=access_key_id,
        # 必填，您的 AccessKey Secret,
        access_key_secret=access_key_secret
    )
    # 访问的域名
    config.endpoint = f'dysmsapi.aliyuncs.com'
    return Dysmsapi20170525Client(config)

def send_code(code):

    if DEBUG: print('verify code:{}'.format(code))

    dic = dict()
    dic['code'] = code
    
    client = create_client('LTAI5tQGLxbLg1qEEzzSgu7N', 'DR1yyMIJhg76GyyGqcU3hfUrrqFkra')
    send_sms_request = dysmsapi_20170525_models.SendSmsRequest(
        sign_name='阿里云短信测试',
        template_code='SMS_154950909',
        # template_code='SMS_273070101',
        phone_numbers='18362975343',
        template_param=str(dic)
        # template_param='{"code":"1234"}'
    )
    runtime = util_models.RuntimeOptions()
    try:
        # 复制代码运行请自行打印 API 的返回值
        response = client.send_sms_with_options(send_sms_request, runtime)
        if DEBUG: print(response)
        return 0
    except Exception as error:
        # 如有需要，请打印 error
        UtilClient.assert_as_string(error.message)
        return SEND_VERIFY_CODE_ERROR