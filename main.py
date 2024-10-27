#!/usr/bin/env python3
import argparse
import random
import time
from src import keys

def main():
  parser = argparse.ArgumentParser(
    description="A game that helps you learn about musical keys"
  )

  parser.add_argument(
    "-m", "--minor",
    help="Whether to use minor keys (default is false)",
    action="store_true",
    default=False,
  )

  parser.add_argument(
    "-k", "--key",
    type=str,
    help="The musical key to learn about",
  )

  parser.add_argument(
    "-r", "--reps",
    type=int,
    help="The number of progressions to be tested on",
    default=5
  )

  args = parser.parse_args()

  selected_keys = keys.minor_keys if args.minor else keys.major_keys

  print(args.minor)

  if (args.key is None):
    args.key = random.choice(list(selected_keys))

  if (args.key not in selected_keys):
    print(f"Invalid key: {args.key}")
    return
  
  print(f"You're playing in the key of {args.key}")
  print(f"We will try {args.reps} progressions.")
  print("")

  chords = selected_keys[args.key]

  # Test a set of 5 random progressions.
  progressions = []

  possible_chord_numbers = range(1, len(chords) + 1)

  # Generate the random progressions.
  for i in range(args.reps):
    # For now, just do 4-chord progressions.
    progression = random.sample(possible_chord_numbers, 4)
    progressions.append({
      "question": progression,
      "answer": [chords[i-1] for i in progression]
    })

  input("Press enter to start the game!")

  start_time = time.time()

  for progression in progressions:
    while True:
      attempt = input(args.key + ":   " + "  ".join(list(map(str, progression["question"]))) + ' -> ')
      if attempt.split(' ') == progression["answer"]:
        print('Correct!\n')
        break
      else:
        print('Incorrect, try again.\n')
  
  end_time = time.time()

  print(f"Finished! You took {end_time - start_time:.2f} seconds.")

main()
