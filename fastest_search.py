import time

start_time = time.time()

def check_device(device, devices_set):
    
    if device in devices_set:
        return f"Device found"
    else:
        return "Device not found"

devices_set ={"iphone", "android", "radio", "tv", "tablet", "pc", "laptop"}

print(check_device(input(), devices_set))

end_time = time.time()
difference = end_time - start_time
print(f'Time needed: {difference:.2f}')
