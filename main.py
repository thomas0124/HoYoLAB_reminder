import requests
import time
import schedule

class LINE_Notify:
    def __init__(self):
        self.API_url = 'https://notify-api.line.me/api/notify'
        self.access_token = 'YOUR_ACCESS_TOKEN'
        self.__headers = {'Authorization': 'Bearer ' + self.access_token}

    def send_message(self, message):
        payload = {'message': message}
        requests.post(self.API_url, headers=self.__headers, params=payload)

def get_login_notification():
    message = '今日もログインボーナスを受け取りましょう！'
    return message

def send_login_notification():
    line = LINE_Notify()
    message = get_login_notification()
    line.send_message(message)

if __name__ == '__main__':
    schedule.every().day.at("14:00").do(send_login_notification)
    while True:
        schedule.run_pending()
        time.sleep(1)
