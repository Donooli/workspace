import psutil

def disk_use_percent():
    return psutil.disk_usage("c://").percent