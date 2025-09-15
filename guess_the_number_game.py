import random

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def divisibility_hints(n):
    divisors = [2, 3, 4, 5, 6, 7, 9, 10]
    hints = []
    for d in divisors:
        if n % d == 0:
            hints.append(f"divisible by {d}")
    return hints

def guess_the_number_game():
    answer = random.randint(0, 100)
    max_tries = 5
    print("Guess the number (between 0 and 100). You have 5 tries!")

    for attempt in range(1, max_tries+1):
        try:
            guess = int(input(f"Try {attempt}: Your guess? "))
        except ValueError:
            print("Please enter a valid integer.")
            continue

        if guess == answer:
            print("Congrats! You win! You know numbers!")
            return
        else:
            if guess < answer:
                print("Your guess is lower than the answer.")
            else:
                print("Your guess is higher than the answer.")
            
            # Provide hints about the answer
            parity = "even" if answer % 2 == 0 else "odd"
            prime_hint = "prime" if is_prime(answer) else "not prime"
            divisibility = divisibility_hints(answer)
            hints = [parity, prime_hint] + divisibility
            print("Hint about the answer: " + ", ".join(hints))
    
    print(f"Game over! The answer was {answer}.")

if __name__ == "__main__":
    guess_the_number_game()