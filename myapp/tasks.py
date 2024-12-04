from celery import shared_task
import logging
import datetime
import time  # Importing time to add a delay
from myapp.serializers import MyModelSerializer

# Configure logging
# logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

@shared_task
def add(x, y, validated_data):
    print('-------------------- start ----------------------')

    start_time = datetime.datetime.now()
    print(f"Task 'add({x},{y})' started at {start_time}.")
    delay_sec = 5 # seconds
    time.sleep(delay_sec)
    print(f"Delay of {delay_sec} seconds")

    result = x + y # perform actual task

    end_time = datetime.datetime.now()
    MyModelSerializer().create(validated_data)
    # You can look at dbeaver, spam refresh (myapp_model dbtable)
    print(f"Data just got created --- RAHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHh")
    print(f"Task 'add({x},{y})' completed at {end_time}. Result: {result}")
    print(f"Task duration: {end_time - start_time}")

    print('-------------------- end ----------------------')
    return result
