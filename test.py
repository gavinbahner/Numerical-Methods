print("Hello test")
import psutil as ps
# print(ps.cpu_times())
# print(ps.cpu_count())

# print(ps.virtual_memory())

# print(ps.sensors_battery())
# print(ps.users())

# print(ps.pids())
p = ps.Process(74625)
print(p.name())
print(p.memory_info())
print(p.memory_percent())
print(p.num_threads())