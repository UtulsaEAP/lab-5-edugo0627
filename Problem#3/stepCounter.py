''' problem 3 lab 5
Name: Emma Verdugo
Lab time: @2pm
'''

def feet_to_steps(user_feet):
   #write your code here
   steps_walked = user_feet // 2.5
   return (int(steps_walked))

if __name__ == '__main__':
    #take input feet steps here
    #store it into the function
    user_feet = float(input())
    steps_walked = feet_to_steps(user_feet)
    #print your steps here
    print(steps_walked)