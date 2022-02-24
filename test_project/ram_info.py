import psutil

def ram_usage_percent():
    return psutil.virtual_memory().percent