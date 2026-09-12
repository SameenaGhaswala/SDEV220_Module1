secret = int(input("Enter the secret number between 1 and 10: "))
guess = int(input("Enter the guess number between 1 and 10: "))

if guess < secret:
    print("Your guess is too low.")
elif guess > secret:
    print("Your guess is too high.")
else:
    print("Your guess is correct.")

