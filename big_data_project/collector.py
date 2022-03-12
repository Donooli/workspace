import psutil


class Collector:
    def __init__(self):
        self.cpu_use_per = 0
        self.mem_use_per = 0
        self.disk_use_per = 0

    def cpu_use_per_col(self):
        self.cpu_use_per = psutil.cpu_percent(None)
        return self.cpu_use_per

    def mem_use_per_col(self):
        self.mem_use_per = psutil.virtual_memory().percent
        return self.mem_use_per

    def disk_use_per_col(self, drive_path):
        self.disk_use_per = psutil.disk_usage(drive_path).percent
        return self.disk_use_per
