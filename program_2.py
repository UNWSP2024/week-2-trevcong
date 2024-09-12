#AUTHOR: Trevor Conger UNWSP
#DATE: 9/7/24 
#TITLE: 5 Friends ages / 5


# Function to print the average age of 5 friends
def average_age(friendOne, friendTwo, friendThree, friendFour, friendFive):
    sumAverage = float((friendOne + friendTwo + friendThree + friendFour + friendFive) / 5)
    print(sumAverage)

# Line which calls the above function.
average_age(17, 26, 23, 21, 19)