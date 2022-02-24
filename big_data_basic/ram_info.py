import psutil

def ram_use_percent():
    return psutil.virtual_memory().percent