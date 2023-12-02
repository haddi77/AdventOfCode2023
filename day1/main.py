ALPHANUMBERS = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}

lines = open('sample.txt', 'r', encoding='utf8').readlines()

sum = 0



for line in lines:
    line = line.lower()
    for key, value in ALPHANUMBERS.items():
        line = line.replace(key, key + str(value))

    calibration_value = ''
    for letter in line:
        if letter.isdigit():
            calibration_value += letter
            break

    for letter in reversed(line):
        if letter.isdigit():
            calibration_value += letter
            break
    print(calibration_value)
    sum += int(calibration_value)

print(sum)