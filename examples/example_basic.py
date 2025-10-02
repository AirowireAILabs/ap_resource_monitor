from ap_resource_monitor import APResourceMonitor

with open("log.txt") as f:
    content = f.read()

monitor = APResourceMonitor(content)
monitor.print_report()
monitor.print_tables()