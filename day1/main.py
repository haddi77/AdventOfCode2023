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

lines = open('input.txt', 'r', encoding='utf8').readlines()

sum = 0



for line in lines:
    line = line.lower().strip()
    # for key, value in ALPHANUMBERS.items():
    #     line = line.replace(key, key + str(value))

    calibration_value = ''
    for idx, letter in enumerate(line):
        if letter.isdigit():
            calibration_value += letter
            break

        for key, value in ALPHANUMBERS.items():
            try:
                found_alphanumber = line.index(key,idx)

            except ValueError:
                continue

            if found_alphanumber == idx:
                calibration_value += str(value)
                break

        if len(calibration_value) > 0:
            break


    for idx, letter in enumerate(reversed(line)):
        if letter.isdigit():
            calibration_value += letter
            break

        for key, value in ALPHANUMBERS.items():
            try:
                found_alphanumber = line.index(key,len(line)-1-idx)

            except ValueError:
                continue

            if found_alphanumber == len(line)-1-idx:
                calibration_value += str(value)
                break

        if len(calibration_value) > 1:
            break

    print(calibration_value)
    sum += int(calibration_value)

print(sum)