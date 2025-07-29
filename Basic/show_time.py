import os
import time
from datetime import datetime


while True:
    
    now = datetime.now()

    current_time = now.strftime(" %I : %M : %S %p")

    os.system('cls' if os.name == 'nt' else 'clear')

    print(f"Current time : {current_time}")

    time.sleep(1)
