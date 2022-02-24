import psutil

def cpu_usage_percent(itv):
    return psutil.cpu_percent(interval=itv)