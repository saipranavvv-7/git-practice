# main.py

# Import the functions we need from each module
from message import message, mood
from suggestion import get_recommendations, random_movie_suggestion
from farewell import get_farewell_message, get_encouragement, get_final_signoff

def main():
    print("=== Movie Night Plannerr ===\n")
    
    # Get user's name
    name = input("What's your name? ").strip()
    if not name:
        name = "Movie fannn"
    
    # Greeting
    print("\n" + message(name))
    
    # Ask for mood and respond
    user_mood = input("\nHow are you feeling today? (happy / tired / excited / sad / other): ").strip()
    print(mood(user_mood))
    
    # Ask for genre and show recommendations
    print("\n" + "-" * 40)
    genre = input("What movie genre are you in the mood for? (action / comedy / drama / horror / sci-fi): ").strip()
    
    recommendations = get_recommendations(genre)
    
    print("\nHere are some movie suggestions:")
    if isinstance(recommendations, list) and all(isinstance(m, str) for m in recommendations):
        for i, movie in enumerate(recommendations, 1):
            print(f"  {i}. {movie}")
    else:
        print("  " + recommendations[0])  # error message case
    
    # Show one completely random suggestion as bonus
    print("\nCan't decide? Random pick just for fun:", random_movie_suggestion())
    
    # Farewell section
    print("\n" + "=" * 40)
    print(get_farewell_message(name))
    print(get_encouragement())
    print(get_final_signoff())
    print("=" * 40)


# This makes sure main() runs only when you run this file directly
if __name__ == "__main__":
    main()





import random
#random.seed(1)
l=[random.randint(1,3) for x in range(500)]
vote={}
for i in range(1,4):
    vote[i]=l.count(i)
print(vote)
print(vote.items())
    
