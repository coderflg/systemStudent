# -*- coding:utf-8 -*-
def jwt_response_payload_handler(token, user=None, request=None):
    return {
        'token': token,
        'username': user.username,
        'id': user.id,
        "email": user.email,
        'nickname': user.nickname
    }