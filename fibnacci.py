def fibonacci():
    # Default values
    sequence = [0, 1]
    default_upper = 10000
    default_lower = 0
    is_int = False
    int_index = 0

    def print_mem():
        print({'key index': ['integer', 'index', 'sequence']})
        for key in memory_dict:
            print({key: memory_dict[key]})
        print('Access specific key: ', end='')
        while True:
            accessed_key = input()
            if accessed_key.isdigit():
                if int(accessed_key) in memory_dict:
                    print(memory_dict[int(accessed_key)])
                else:
                    break
            else:
                break

    # Ask for upper bound, lower bound, and/or an integer to check if it is in sequence.
    print('May enter \'quit\', \'memory/mem\', or nothing for each input.')
    upper = input('Upper limit: ')
    if upper.isdigit():
        upper = int(upper)
    elif upper == '' or upper.isspace():
        upper = default_upper
    elif upper.lower() == 'memory' or upper.lower() == 'mem':
        print_mem()
        return True
    elif upper.lower() == 'quit':
        return False
    else:
        print('Invalid input.')
        return True

    lower = input('Lower limit: ')
    if lower.isdigit():
        lower = int(lower)
        if lower > upper:
            print('Invalid input.')
            return True
    elif lower == '' or lower.isspace():
        lower = default_lower
    elif lower.lower() == 'memory' or lower.lower() == 'mem':
        print_mem()
        return True
    elif lower.lower() == 'quit':
        return False
    else:
        print('Invalid input.')
        return True

    integer_input = input('Check if a number is in sequence: ')
    if integer_input.isdigit():
        integer_input = int(integer_input)
        is_int = True
    elif integer_input == '' or integer_input.isspace():
        integer_input = None
    elif integer_input.lower() == 'memory' or integer_input.lower() == 'mem':
        print_mem()
        return True
    elif integer_input.lower() == 'quit':
        return False
    else:
        print('Invalid input.')
        return True

    # Generate sequence up to upper bound
    while True:
        num = sequence[-1] + sequence[-2]
        if num > upper:
            break
        sequence.append(num)
        
    # Remove lower range
    while len(sequence) > 0: 
        if sequence[0] < lower:
            del sequence[0]
        else:
            break

    # Print the sequence
    print(sequence)

    # Check if number is in sequence; if so, return index
    if is_int:
        if integer_input in sequence:
            int_index = sequence.index(integer_input)
            print(f'{integer_input} is at index {int_index}.')
            
        else:
            print(f'{integer_input} is not in the sequence.')

    # Update memory dictionary
    memory_dict.update({
       key_index : [integer_input, int_index, sequence]
    })
    return True

# Create an empty dictionary
memory_dict = {}
key_index = 0
check = True
while check:
    print()
    check = fibonacci()
    key_index += 1