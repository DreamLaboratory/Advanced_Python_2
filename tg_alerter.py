import requests

def send_msg(text:str) -> bool:
    base_url = "https://api.telegram.org/bot"
    token = "6240825083:AAGUobsTY4ZcwWtmjO7f2kR_5h3afjCQTR4"
    chat_id = "-1001763162190"
    url = base_url + token + "/sendMessage?chat_id=" + chat_id + "&text=" + text
    response = requests.get(url)
    return response.status_code == 200

if __name__ == "__main__":
    try:
        21/0
    except Exception as e:
        send_msg(str(e))
