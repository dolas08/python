time = input("input your amount of seconds: ")
print(f"{int(time) // 3600:02d}:{int(time) % 3600 // 60:02d}:{int(time) % 3600 % 60:02d}")
