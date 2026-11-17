import requests

api_url = "http://10.135.232.30:5005"

def logar_user(email,senha):
    url = f"{api_url}/login"

    dados = {
        "email": email,
        "senha": senha
    }

    result = requests.post(url=url,json=dados)

    return result.json(), result.status_code


def get_viaturas():
    url = f"{api_url}/get_viaturas"

    result = requests.get(url=url)

    return result.json()