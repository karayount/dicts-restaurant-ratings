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




# print method B
# get tuples of items in dictionary
# sort that list of tuples
# loop through, printing items


