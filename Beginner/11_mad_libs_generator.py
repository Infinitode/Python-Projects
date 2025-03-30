# Create the main function for easy insertion
def mad_libs(story):
    words = {}
    for word_type in story["word_types"]:
        words[word_type] = input(f"Enter a {word_type}: ")

    filled_story = story["template"].format(**words)
    print(filled_story)

# Predefine some stories
stories = [
    {
        "name": "The Lost Something...",
        "word_types": ["adjective", "noun", "verb", "adverb", "place"],
        "template": "One day, a {adjective} {noun} decided to {verb} {adverb} to the {place}, never to be seen again..."
    },
    {
        "name": "The Birthday Party?",
        "word_types": ["adjective", "noun", "verb", "number", "food"],
        "template": "For my birthday, I had a {adjective} party with {number} {noun}s. We {verb} and ate lots of {food}."
    },
    {
        "name": "The School Trip...",
        "word_types": ["adjective", "noun", "verb", "place", "animal"],
        "template": "Our school trip was very {adjective}. We saw a {noun} {verb} at the {place} and even a {animal}! But then the {animal} wanted to {verb} us!"
    },
    {
        "name": "The Alien Invasion",
        "word_types": ["adjective", "noun", "verb", "adverb", "plural_noun"],
        "template": "Suddenly, a {adjective} spaceship landed in my backyard! A {noun} alien jumped out and started to {verb} {adverb} with my {plural_noun}! I didn't think {noun} aliens could do that."
    }
]


print("Welcome to Mad Libs!")
for i, story in enumerate(stories):
    print(f"{i+1}. {story['name']}")

while True:
    try:
        choice = int(input("Choose a story (1-4): "))
        if 1 <= choice <= len(stories):
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")
    except ValueError:
        print("Invalid input. Please enter a number.")

mad_libs(stories[choice - 1])