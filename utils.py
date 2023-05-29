def convert_to_hms(times_in_seconds):
    hours, remainder = divmod(times_in_seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return "{:02}|{:02}|{:02}".format(hours, minutes, seconds)
