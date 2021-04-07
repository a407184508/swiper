import random

import requests

from swiper import config



def gen_verify_code(length=6):
    '''生成验证码'''
    return random.randrange(10 ** (length - 1), 10 ** length)


def send_verify_code(phonenum, message)
    '''发送验证码请求'''

    sms_config = config.SMS_CONTENT.copy()
    vcode = gen_verify_code()
    sms_config['context'] = sms_config['context'] % vcode
    sms_config['mobile'] = phonenum
    response = requests.post(config.SMS_URL, data=sms_config)
    return response
    



