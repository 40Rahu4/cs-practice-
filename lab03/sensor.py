threshold = float(input())
n = int(input())
errors = 0
correct_cnt = 0
exceed = 0
maxi = 0
total = 0

for i in range(n):
    value = input() 
    if value == 'error':
        errors += 1
    else:
        temperature = float(value)
        correct_cnt += 1
        total += temperature

        if temperature > threshold:
            exceed += 1
        if correct_cnt == 1:
            maxi = temperature
        else:
            if maxi < temperature:
                maxi = temperature
average = total / correct_cnt

print(n)
print(errors)
print(exceed)
print(f'{maxi:.1f}')
print(f'{average:.1f}')