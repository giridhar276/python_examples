"""
Program 20:
Third-party library: psutil methods.

Install before running:
pip install psutil
"""

try:
    import psutil

    print("CPU Percentage:", psutil.cpu_percent(interval=1))
    print("CPU Count:", psutil.cpu_count())

    memory = psutil.virtual_memory()
    print("Total Memory:", memory.total)
    print("Available Memory:", memory.available)
    print("Memory Usage Percentage:", memory.percent)

    disk = psutil.disk_usage("/")
    print("Disk Total:", disk.total)
    print("Disk Used:", disk.used)
    print("Disk Free:", disk.free)
    print("Disk Usage Percentage:", disk.percent)

except ImportError:
    print("psutil is not installed.")
    print("Please install it using: pip install psutil")
