import datetime

lines = None
with open("input.txt") as fp:
    lines = fp.read().split("\n")

parsed = sorted([(datetime.datetime.strptime(line.split("] ")[0][1:], '%Y-%m-%d %H:%M'),line.split("] ")[1]) for line in lines], key=lambda x:x[0])

sleep_minutes = {}
sleep_times = {}

current_guard = None
fell_asleep_at_minute = None
    
for dt,command in parsed:
    if(command.endswith("begins shift")):
        fell_asleep_at_minute = None
        
        _,guard_no,_,_ = command.split()
        current_guard = guard_no
        
    elif(command == "falls asleep"):
        fell_asleep_at_minute = dt.minute
        
    elif(command == "wakes up"):
        time_asleep = dt.minute - fell_asleep_at_minute
        if(current_guard in sleep_minutes):
            sleep_minutes[current_guard] = sleep_minutes[current_guard] + time_asleep
        else:
            sleep_minutes[current_guard] = time_asleep
        
        if(current_guard in sleep_times):
            for i in range(fell_asleep_at_minute, dt.minute):
                sleep_times[current_guard][i] = sleep_times[current_guard][i]+1
        else:
            temp = {i:0 for i in range(60)}
            for i in range(fell_asleep_at_minute, dt.minute):
                temp[i] = temp[i]+1
            sleep_times[current_guard] = temp

guards_name_to_minute_spent_most_asleep_to_frequency = [(i, max(sleep_times[i].items(), key=lambda x:x[1])) for i in sleep_times]
highest_frequency_guard = max(guards_name_to_minute_spent_most_asleep_to_frequency,key = lambda x:x[1][1])
guard_id, (minute,_) = highest_frequency_guard

print(int(guard_id[1:]) * minute)