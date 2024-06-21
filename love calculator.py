import random

def love_calculator(name1, name2):
    # Combine names and convert to lowercase
    combined_names = (name1 + name2).lower()
    
    # Generate a random love score between 0 and 100
    love_score = random.randint(0, 100)
    
    # Create a message based on the love score
    if love_score > 80:
        message = "You two are made for each other!"
    elif love_score > 50:
        message = "There is potential here."
    else:
        message = "It might be a challenging relationship."

    return love_score, message

# Get user input
name1 = input("Enter the first name: ")
name2 = input("Enter the second name: ")

# Calculate the love score
score, message = love_calculator(name1, name2)

# Print the result
print(f"The love score between {name1} and {name2} is {score}%. {message}")
