
sub_string = ["zero","one","two","three","four","five",
              "six","seven","eight","nine","1","2",
              "3","4","5","6","7","8","9","0"]


with open('Day 1 - Trebuchet\input.txt', 'r') as file:
    lines = file.readlines()

sum = 0

for line in lines:
    first = "none"
    last = "none"
    smallest_index = 100
    biggest_index = -1

    for sub in sub_string:
        f_index = line.find(sub)
        l_index = line.rfind(sub)

        if f_index != -1:

            if f_index < smallest_index:
                smallest_index = f_index
                first = sub

        if l_index != -1:

            if l_index > biggest_index:
                biggest_index = l_index
                last = sub

    print(f"{line}: first_number: {first} last_number: {last}")

    first_number = -1
    last_number = -1

    if first.isdigit():
        first_number = int(first)
    else:
        first_number = sub_string.index(first)

    if last.isdigit():
        last_number = int(last)
    else:
        last_number = sub_string.index(last)

    concatenated_number = str(first_number) + str(last_number)
    sum += int(concatenated_number)

print(sum)

     
    