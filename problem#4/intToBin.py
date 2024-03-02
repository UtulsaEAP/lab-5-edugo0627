''' problem 4 lab 5
Name: Emma Verdugo
lab time: @2pm
'''

def int_to_reverse_binary(user_input):
    binary_val = ''
#write your while loop here
    while user_input > 0:
        #write your code
        binary_val = binary_val + str(user_input %2)
        user_input = user_input // 2
    return binary_val


def string_reverse(input_string): 
    return input_string[::-1]

if __name__ == '__main__':
    user_input = int(input())
    input_string = int_to_reverse_binary(user_input)
    binary_string = str(string_reverse(input_string))
    
    print(binary_string)