restaurant_rating_file = "scores.txt"

def read_ratings_file(restaurant_rating_file):
    restaurant_ratings = {}
    with open(restaurant_rating_file) as restaurant_rating_text:
        for line in restaurant_rating_text:
            rating_tokens = line.rstrip().split(":")
            # check to see whether entry is already in dictionary
            # add restaurant to dictionary as key, and assign rating to value (perhaps make value a number, not string)
            restaurant_ratings[rating_tokens[0]] = int(rating_tokens[1])
    return restaurant_ratings


restaurant_ratings = read_ratings_file(restaurant_rating_file)
print restaurant_ratings
# A
# assign sorted list of keys to a variable

# loop through list printing that key in dictionary with its value
# 
# B
# get tuples of items in dictionary
# sort that list of tuples
# loop through, printing items


