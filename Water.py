import time
from plyer import notification
while True:
    notification.notify(
        title ="Drink Water",
        message ="Benefits of drinking water : \n 1 Aiding digestion \n 2 Stabilizing the heartbeat",
        app_icon="C:\\Users\\atish\\OneDrive\\Documents\\Codes\\icon.ico",
        timeout = 10
    )
    time.sleep(60*60)