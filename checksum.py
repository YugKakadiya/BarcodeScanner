def check_binary_string (binary_number):
    binary_number = str(binary_number)
    check_sum = binary_number[0]
    print(check_sum)
    binary_number = binary_number[1:]
    print(binary_number)
    zeros = 0
    ones = 0


    for num in binary_number:
        if num == "0" :
            zeros = zeros +1
        if num == "1":
            ones = ones +1
    
    if zeros == ones :
        binary_number = str(0) + binary_number

    else :
        binary_number = str(1) + binary_number

    return binary_number

print(check_binary_string("011100"))