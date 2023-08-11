import json
import requests
import base64
# from career_studio.AES_CBC import AESCipher


class PayPal:
    @staticmethod
    def get_paypal_token(client_id, client_secret):
        '''
        create charge using paypal
        '''
        client_id = client_id
        client_secret = client_secret

        url = "https://api.sandbox.paypal.com/v1/oauth2/token"
        data = {
            "client_id": client_id,
            "client_secret": client_secret,
            "grant_type": "client_credentials"
        }
        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
            "Authorization": "Basic {0}".format(base64.b64encode((client_id + ":" + client_secret).encode()).decode())
        }
        token = requests.post(url, data, headers=headers)
        return token

    @staticmethod
    def checkout_order(token, appointment_id, success_url, cancel_url, amount):
        headers = {"Content-Type": "application/json", "Authorization": 'Bearer ' + token}
        url = 'https://api.sandbox.paypal.com/v2/checkout/orders'

        data = {
            "intent": "CAPTURE",
            "application_context": {
                "return_url": success_url,
                "cancel_url": cancel_url,
                "brand_name": "EXAMPLE INC",
                "landing_page": "BILLING",
                "user_action": "CONTINUE"
            },
            "purchase_units": [
                {
                    "reference_id": appointment_id,
                    "custom_id": appointment_id,
                    "soft_descriptor": "HighFashions",
                    "amount": {
                        "currency_code": "USD",
                        "value": amount
                    }
                }
            ]
        }
        data = json.dumps(data)
        result = requests.post(url, data, headers=headers)
        return result.json()
