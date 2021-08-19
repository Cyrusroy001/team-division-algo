import random

occured_in_team1 = {'Cyrus':0, 'Awantika':0, 'Saksham':0, 'Samarth':0, 'Aayush':0, 'Rajesh':0, 
'Siddharth':0, 'Pranay':0, 'Anand':0, 'Shishir':0, 'Chandra':0}
occured_in_team2 = {'Cyrus':0, 'Awantika':0, 'Saksham':0, 'Samarth':0, 'Aayush':0, 'Rajesh':0, 
'Siddharth':0, 'Pranay':0, 'Anand':0, 'Shishir':0, 'Chandra':0}
occured_in_team3 = {'Cyrus':0, 'Awantika':0, 'Saksham':0, 'Samarth':0, 'Aayush':0, 'Rajesh':0, 
'Siddharth':0, 'Pranay':0, 'Anand':0, 'Shishir':0, 'Chandra':0}

fin_team1 = []
fin_team2 = []
fin_team3 = []

t = 100
while(t):
    my_dict = {'Cyrus':9, 'Awantika':9, 'Saksham':9, 'Samarth':9, 'Aayush':9, 'Rajesh':9, 
    'Siddharth':9, 'Pranay':9, 'Anand':9, 'Shishir':9, 'Chandra':9}

    nums = [1,1,1,1,2,2,2,2,3,3,3]
    random.shuffle(nums)

    i = 0
    for key in my_dict:
        my_dict[key] = nums[i]
        i += 1

    team1 = [key for key in my_dict if my_dict[key] == 1]
    team2 = [key for key in my_dict if my_dict[key] == 2]
    team3 = [key for key in my_dict if my_dict[key] == 3]

    print("round: "+ str(t) + "\n")
    print(team1)
    print(team2)
    print(team3)
    print("\n")

    for person in team1:
        occured_in_team1[person] += 1
    for person in team2:
        occured_in_team2[person] += 1
    for person in team3:
        occured_in_team3[person] += 1

    t -= 1

for key in my_dict:
    info = str(occured_in_team1[key]) + ", " + str(occured_in_team2[key]) + ", " + str(occured_in_team3[key])
    print(key + " "+ info)