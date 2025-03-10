import itertools
import random

# Define constants
CODE_LENGTH = 4
NUM_COLORS = 8


def generate_secret_code(length, num_colors):
    """Generate a random secret code of given length using specified number of colors."""
    return [random.randint(1, num_colors) for _ in range(length)]


def get_feedback(guess, secret_code):
    """Calculate the number of black and white pegs for a given guess."""
    black_pegs = sum(g == c for g, c in zip(guess, secret_code))
    white_pegs = (
        sum(min(guess.count(x), secret_code.count(x)) for x in set(secret_code))
        - black_pegs
    )
    return black_pegs, white_pegs


def is_consistent(proposal, past_guesses):
    """Check if a proposal is consistent with the feedback from past guesses."""
    for past_guess, (black_pegs, white_pegs) in past_guesses:
        feedback = get_feedback(proposal, past_guess)
        if feedback != (black_pegs, white_pegs):
            return False
    return True


def mastermind_solver(secret_code, code_length, num_colors):
    """Solve the mastermind game using a brute-force approach."""
    attempts = 0
    past_guesses = []
    all_possible_guesses = list(
        itertools.product(range(1, num_colors + 1), repeat=code_length)
    )

    while True:
        # Randomly select a guess from the remaining possibilities
        guess = random.choice(all_possible_guesses)
        black_pegs, white_pegs = get_feedback(guess, secret_code)
        attempts += 1

        print(
            f"Attempt {attempts}: {guess} -> {black_pegs} black pegs, {white_pegs} white pegs"
        )

        # Check if the guess is correct
        if black_pegs == code_length:
            print(f"Code found in {attempts} attempts!")
            break

        # Store the guess and feedback
        past_guesses.append((guess, (black_pegs, white_pegs)))

        # Filter out guesses that are inconsistent with previous feedback
        all_possible_guesses = [
            g for g in all_possible_guesses if is_consistent(g, past_guesses)
        ]


if __name__ == "__main__":
    # Generate a secret code and solve the game
    secret_code = generate_secret_code(CODE_LENGTH, NUM_COLORS)
    print(f"Secret code (hidden for real play): {secret_code}")
    mastermind_solver(secret_code, CODE_LENGTH, NUM_COLORS)
