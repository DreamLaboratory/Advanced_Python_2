import requests

def send_msg(text:str) -> bool:
    base_url = "https://api.telegram.org/bot"
    chat_id = "CHAT_ID"
    url = f"{base_url}TOKEN/sendMessage?chat_id={chat_id}&text={text}"
    response = requests.get(url)
    return response.status_code == 200

if __name__ == "__main__":
    try:
        21/0
    except Exception as e:
        send_msg(str(e))
