import random

def generate_knock_knock_joke():
    # Define lists of possible responses for each part of the joke
    knock_responses = ["Knock, knock!", "Who's there?", "Knock, knock!"]
    who_responses = ["Cow says.", "Hatch.", "Boo."]
    punchline_responses = [
        "No silly, cows say 'moo'!",
        "Bless you! Hatch is open!",
        "Aww, don't cry. It's just a joke, Boo!"
    ]
    
    # Randomly select a response from each list
    knock_response = random.choice(knock_responses)
    who_response = random.choice(who_responses)
    punchline_response = random.choice(punchline_responses)
    
    # Print the joke
    print(knock_response)
    input()
    print(who_response)
    input()
    print(punchline_response)

# Generate and display a knock-knock joke
generate_knock_knock_joke()
