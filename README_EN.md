# LINE Notify Login Notification

This is a Python script that uses the LINE Notify API to send a daily login notification. It sends a message reminder to a specified LINE account at a specified time every day.

## Prerequisites

Before using this script, make sure you have the following:

- Python 3.x installed on your machine.
- The `requests` library installed. You can install it using pip:
  ```
  pip install requests
  ```

## Getting Started

1. Clone or download the script to your local machine.

2. Obtain a LINE Notify access token:
   - Visit the [LINE Notify](https://notify-bot.line.me/) website.
   - Login with your LINE account.
   - Create a new token by clicking on the "Generate token" button.
   - Give it a name and select the desired notification settings.
   - Copy the generated access token.

3. Open the script in a text editor and replace the `access_token` variable value with your own access token.
   ```python
   self.access_token = 'YOUR_ACCESS_TOKEN'
   ```

## Usage

To use the script, follow these steps:

1. Open a terminal or command prompt.

2. Navigate to the directory where the script is located.

3. Run the script using the following command:
   ```
   python main.py
   ```
   You can also use the docker command:
    ```
    docker-compose build
    docker-compose up
    ```

4. The script will start running and check for login notifications to send at the specified time every day (14:00 in the provided example).

## Customization

You can customize the script to suit your needs:

- **Change the notification time**: Modify the `schedule.every().day.at("14:00").do(send_login_notification)` line to specify a different time for the login notification.

- **Modify the notification message**: Edit the `get_login_notification()` function to change the message content.

- **Adjust the notification frequency**: By default, the script sends the notification once per day. You can modify the schedule to send notifications more or less frequently.

- **Extend the functionality**: You can enhance the script by adding additional notifications or integrating it with other services.

## License

This script is released under the [MIT License](LICENSE). Feel free to modify and distribute it as needed.

## Acknowledgements

This script utilizes the [LINE Notify API](https://notify-bot.line.me/doc/) to send notifications. Special thanks to the developers of LINE Notify for providing the API service.