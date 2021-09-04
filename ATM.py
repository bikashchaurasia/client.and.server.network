print("welcome to axis bank !!")
pin = 7255
Chances = 3
balance = 50000
while Chances != 0:
    user_pin = int(input("please enter the four digit pin"))
    if user_pin != pin :
        Chances -= 1
        print("wrong pin number")
        print(f"you have{Chances} Chances left")
    else:
        user_Choices = input("B : balanceeeee, D : deposit, W : withdraw")
        if user_Choices  == "B":
            print(f"your total balance is RS.{balance}")

        if user_Choices == "D":
            deposit_user = int(input("Enter the amount that you would like to deposit :"))
            total_balance = deposit_user + balance
            print(f"you have deposited RS.{deposit_user}")
            print(f"your total balance is {total_balance}")

        if user_Choices == "w":
            withdraw_user = int(input("Enter the amount you want to withdraw"))
            total_balance = balance - withdraw_user
            print(f"you have withdraw RS.{withdraw_user}")
            print(f"your total balance is RS.{total_balance}")
        user_exit = input("would you like to exit? Yes/No")

        if user_exit == "Yes":
            print("thankyou for using axis bank !!")
            break
        else:
            continue










