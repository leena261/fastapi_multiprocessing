from datetime import datetime

def get_cur_time():
    # Get the current datetime
    current_datetime = datetime.now()

    # Extract the time part from the current datetime
    current_time = current_datetime.time().replace(microsecond=0)
    return  current_time
