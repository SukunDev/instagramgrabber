import requests
from uuid import uuid4
from InstagramGrabber import helper, exceptions

def _excute(path, data=None, headers=None, cookies=None):
    base_headers =  {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
        "X-Asbd-Id": "129477",
        "X-Ig-App-Id": "936619743392459",
        "X-Ig-Www-Claim": "hmac.AR3meONALfvoNcB9btsTMnLiCXhMp65YRgAdrVj-6TNT6hGU"
    }
    if headers:
        base_headers.update(headers)
    if data is None:
        try:
            response = requests.get(f"https://www.instagram.com{path}", headers=base_headers, cookies=cookies)
        except Exception as e:
            raise exceptions.RequestsException(e)
    else:
        try:
            response = requests.post(f"https://www.instagram.com{path}", data=data, headers=base_headers, cookies=cookies)
        except Exception as e:
            raise exceptions.RequestsException(e)
    return response

def _login(username, password):
    if username is None or password is None:
        raise exceptions.InstagramError(f"username or password is None")
    response = requests.post(
        url=f'https://www.instagram.com/api/v1/accounts/login/', 
        headers={
                "User-Agent":
                "Instagram 159.0.0.28.123 (iPhone8,1; iOS 14_1; en_SA@calendar=gregorian; ar-SA; scale=2.00; 750x1334; 244425769) AppleWebKit/420+",
        }, 
        data={
            "username": username,
            "reg_login": "0",
            "enc_password": f"#PWD_INSTAGRAM:0:&:{password}",
            "device_id": str(uuid4()),
            "login_attempt_count": "0",
            "phone_id": str(uuid4())
    })
    if 'The password you entered is incorrect' in response.text:
        raise exceptions.InstagramError(f'Your password is incorrect')
    elif 'logged_in_user' in response.text:
        helper.save_cookies(response.cookies, cookies_name=username)
        return response
    else:
        js_res = helper.extract_json(response.text)
        raise exceptions.RequestsException(response.status_code, js_res['message'])