def replace_line(filename2, line_number, text):
    with open(filename2) as file:
        lines = file.readlines()


        if (line_number <= len(lines)):
    

            lines[line_number - 1] = text + "\n"
            with open(filename2, "w") as file:


                for line in lines:
                    file.write(line)
    
        else:
            print("Line", line_number, "not in file.")
            print("File has", len(lines), "lines.")

def wordcount(filename , list ):
    try:
        file = open(filename, "r")
        read = file.readlines()
        file.close()
        for word in list:
            lower = word.lower()
            count = 0
            lines = 0
            for sentence in read:
                line = sentence.split()
                lines = lines + 1
                for each in line:
                    line2 = each.lower()
                    line2 = line2.strip("%")
                    if lower == line2:
                        count = count + 1
                        if count >= 1:
                            replace_question = ("We already have a") + (" ") + (volunteer_name) + (" ") + ("in our system would you like to update previous entries? y or n:")
                            replace = input(replace_question)
                            if replace == "y":
                                print("Your results have been updated")
                                filename2 = "CoinCount.txt"
                                text = (volunteer_name) + ("  ") + (coin_type) + ("  ") + (accuracy)
                                print(replace_line(filename2 , lines , text))
    except FileExistsError:
        print("The file is not there")

user_continue = input("Would you like to add a bag of coins?  y or n:")
incorrect_attempts = 0
correct_attempts = 0
repeat = 0
while user_continue == "y":
    volunteer_name=str(input("Enter your name:"))
    num_bags = int(input("Enter the number of bags you want to add:"))
    for i in range (num_bags):
        coin_type=str(input("What is the value of the coin in your bag?  1p, 2p, 5p, 10p, 20p, 50p, £1, £2:"))
    
        while coin_type != "1p" and coin_type != "2p" and coin_type != "5p" and coin_type != "10p" and coin_type != "20p" and coin_type != "50p" and coin_type != "£1" and coin_type !="£2":
            coin_type = str(input("Invalid coin type please re-enter the value of your coin. 1p, 2p, 5p, 10p, 20p, 50p, £1, £2:"))
        weight_bag = int(input("Enter the weight of your bag:"))

        coin_list = ["1p" , "2p" , "5p" , "10p" , "20p" , "50p" , "£1" , "£2"]
        weight_list = [356 , 356, 235 , 325 , 250 , 160 , 175 , 120]
        coin_weight_list = [3.56 , 7.12 , 2.35 , 6.50 , 5.00 , 8.00 , 8.75 , 12.00]
        
        for i in range (len(coin_list)):
            if coin_type == coin_list[i]:
                if weight_bag == weight_list[i]:
                    print("Correct bag weight")
                    correct_attempts = correct_attempts + 1
                elif weight_bag < weight_list [i]:
                    coins_needed = weight_list[i] - weight_bag
                    added_coins = coins_needed // coin_weight_list[i]
                    added_coins= int(added_coins)
                    print("You will need" , added_coins , "more" , coin_list[i] , "coins to reach the required bag weight")
                    incorrect_attempts = incorrect_attempts + 1
                
                elif weight_bag > weight_list [i]:
                    excess_coins = weight_bag - weight_list[i]  
                    added_coins = excess_coins // coin_weight_list[i]
                    added_coins= int(added_coins)
                    print("You will need" , added_coins , "less" , coin_list[i] , "coins to reach the required bag weight")
                    incorrect_attempts= incorrect_attempts + 1
            
    total_attempts = incorrect_attempts + correct_attempts
    accuracy = (correct_attempts / total_attempts)*100
    accuracy = str(accuracy) + ("%")
        
    wordcount("CoinCount.txt",[volunteer_name])
    User_Question = str(input("Did you update previous results? y or n:"))
    if User_Question == "n":
        final_data = ("\n") + (volunteer_name) + ("  ") + (coin_type) + ("  ") + (accuracy)
        CoinCountInput=open("CoinCount.txt","a")
        New_data=CoinCountInput.write(final_data,)
        CoinCountInput.close()
    
    user_view=input("Would you like to view current results y or n:")
    if user_view == "y":
        CoinCountData=open('CoinCount.txt','r')
        data=CoinCountData.read()
        print(data)
        CoinCountData.close()
    user_continue = input("Would you like to add a bag of coins?  y or n:")