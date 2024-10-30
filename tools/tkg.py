import requests
import uuid

def main():
   
    uid = input("Insert UID: ")
    pw = input("Insert Password: ")

    
    data = {
        'adid': str(uuid.uuid4()),
        'format': 'json',
        'device_id': str(uuid.uuid4()),
        'cpl': 'true',
        'family_device_id': str(uuid.uuid4()),
        'credentials_type': 'device_based_login_password',
        'error_detail_type': 'button_with_disabled',
        'source': 'device_based_login',
        'email': uid,  
        'password': pw,
        'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32',
        'generate_session_cookies': '1',
        'meta_inf_fbmeta': '',
        'advertiser_id': str(uuid.uuid4()),
        'currently_logged_in_userid': '0',
        'locale': 'en_US',
        'client_country_code': 'US',
        'method': 'auth.login',
        'fb_api_req_friendly_name': 'authenticate',
        'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler',
        'api_key': '62f8ce9f74b12f84c123cc23437a4a32',
    }

    # URL for the POST request
    url = 'https://graph.facebook.com/auth/login'

    # Sending the request and getting the response
    response = requests.post(url, data=data)
    a = response.json()

    # Extracting and printing only the access_token
    access_token = a.get('access_token')
    if access_token:
        print(f"Access Token: {access_token}")
    else:
        print("Access token not found in the response.")

if __name__ == "__main__":
    main()
