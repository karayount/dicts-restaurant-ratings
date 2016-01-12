restaurant_rating_file = "scores.txt"

def read_ratings_file(restaurant_rating_file):
    """Creates dictionary of restaurant name keys to rating values from file"""

    restaurant_ratings = {}
    with open(restaurant_rating_file) as restaurant_rating_text:
        for line in restaurant_rating_text:
            rating_tokens = line.rstrip().split(":")
            restaurant_ratings[rating_tokens[0]] = int(rating_tokens[1])
    return restaurant_ratings


def print_ratings(ratings):    
    """Prints alphabetized restaurant names with their rating from input dictionary"""

    restaurant_names = sorted(ratings.keys())
    for restaurant in restaurant_names:
        print "%s is rated at %d." % (restaurant, ratings[restaurant])


restaurant_ratings = read_ratings_file(restaurant_rating_file)
print_ratings(restaurant_ratings)


def user_add_restaurant(ratings):
    """Promts user for new restaurant and its rating, ensures it's not duplicated, then adds them to dictionary"""

    new_restaurant = raw_input("What is the new restaurant's name? ")
    while new_restaurant in ratings:
        new_restaurant = raw_input("That restaurant is already listed. \nWhat is the NEW restaurant's name? ")
    ratings[new_restaurant] = int(raw_input("Rate {} from 1 to 5: ".format(new_restaurant)))
    return ratings


user_add_restaurant(restaurant_ratings)
print_ratings(restaurant_ratings)



# for a rainy day
#main user input function
#   ask them if they want to enter a new restaurant or a new rating
#   call new restaurant function to add new
#   call modify rating function to change rating
#   do they want to add/modify another restaurant/rating?