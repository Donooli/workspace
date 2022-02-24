import psutil

def cpu_use_percent(interval):
    return psutil.cpu_percent(interval)