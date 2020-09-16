#Replacing all punctuation within a sentence
#www.geeksforgeeks.org


def eliza():
    while True:
        response = input("> ")
        edited_response = preprocess(response)
        if edited_response == "bye" or edited_response == "shut up":
            break
        else:
            print(keywords(edited_response))


def preprocess(response):
    punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    for item in response:
        if item in punctuation:
            response = response.replace(item, "")
    response = response.lower()
    return response

def keywords(response):
    list_of_keywords = ["can you", "can i", "you are", "youre", "i dont", "i feel", "why dont you", "why cant i", "are you",
             "i cant", "i am", "im ", "you ", "i want", "what", "how", "who", "where", "when", "why", "name", "cause",
             "sorry", "dream", "hello", "hi ", "maybe", "no", "your", "always", "think", "alike", "yes", "friend",
             "computer"]
    for word in list_of_keywords:
        if word in response:
            index = response.find(word)
            new_response = response[index:]
            new_response = new_response.replace(word, str(index))
            return new_response
    #Still need a way of replacing all words before my keyword
    return "-1"

def conjugate():




eliza()