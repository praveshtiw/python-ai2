from fuzzywuzzy import fuzz

def custom_token_set_ratio(s1, s2):
    # Tokenize the strings and remove common stopwords
    stopwords = set(['the', 'a', 'an', 'with'])
    words1 = [word for word in s1.lower().split() if word not in stopwords]
    words2 = [word for word in s2.lower().split() if word not in stopwords]
    
    # Calculate the token set ratio
    ratio = fuzz.token_set_ratio(' '.join(words1), ' '.join(words2))
    return ratio

def find_similar_hotels(target_name, hotel_names, min_ratio=70):
    similar_hotels = []
    for hotel_name in hotel_names:
        similarity_ratio = custom_token_set_ratio(target_name, hotel_name)
        if similarity_ratio >= min_ratio:
            similar_hotels.append(hotel_name)

    return similar_hotels

# Example usage:
all_hotel_names = ["Grand Hotel", "Green Plaza Inn", "The Royal Resort", "Hotel Supreme"]
target_hotel_name = "The Hotel Grnad  ABF with"  # A typo in the target hotel name with unsequential words

similar_hotels = find_similar_hotels(target_hotel_name, all_hotel_names)
print(similar_hotels)
