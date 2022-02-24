import psutil

def disk_usage_percent(dp):
    return psutil.disk_usage(dp).percent