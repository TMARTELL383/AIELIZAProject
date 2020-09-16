# Replacing all punctuation within a sentence
# www.geeksforgeeks.org

import random

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
    return "-1"

def conjugate():
    print("Hello World")

def getreply(number):
    if number == -1:
        reply = ["What does that suggest to you?","I see.","I'm not sure I understand you fully.",
                 "Come, come, elucidate your thoughts.","Can you elaborate on that?","That is quite interesting."]
    elif number == 0:
        reply = ["Don't you believe that I can *","Perhaps you would like me to be able to *","You want me to be able to *"]
    elif number == 1:
        reply = ["Perhaps you don't want to *","Do you want to be able to *"]
    elif number == 2 or number == 3:
        reply = ["What makes you think I am *","Does it please you to believe I am *","Perhaps you would like to be *",
                 "Do you sometimes wish you were *"]
    elif number == 4:
        reply = ["Don't you really *", "Why don't you *", "Do you wish to be able to *", "Does that trouble you?"]
    elif number == 5:
        reply = ["Tell me more about such feelings.","Do you often feel *","Do you enjoy feeling *"]
    elif number == 6:
        reply = ["Do you really believe I don't *","Perhaps in good time I will *","Do you want me to *"]
    elif number == 7:
        reply = ["Do you think you should be able to *","Why can't you *"]
    elif number == 8:
        reply = ["Why are you interested in whether or not I am *","Would you prefer if I were not *",
                 "Perhaps in your fantasies I am *"]
    elif number == 9:
        reply = ["How do you know you can't *","Have you tried?","Perhaps you can now *"]
    elif number == 10 or number == 11:
        reply = ["Did you come to me because you are *","How long have you been *","Do you believe it is normal to be *",
                 "Do you enjoy being *"]
    elif number == 12:
        reply = ["We were discussing you, not me.","Oh, I *","You're not really talking about me, are you?"]
    elif number == 13:
        reply = ["What would it mean to you if you got *","Why do you want *","Suppose you got *",
                 "What if you never got *","I sometimes also want *"]
    elif number == 14 or number == 15 or number == 16 or number == 17 or number == 18 or number == 19:
        reply = ["Why do you ask?","Does that question interest you?","What answer would please you the most?",
                 "What do you think?","Are such questions on your mind often?","What is it that you really want to know?",
                 "Have you asked anyone else?","Have you asked such questions before?",
                 "What else comes to your mind when you ask that?"]
    elif number == 20:
        reply = ["Names don't interest me.","I don't care about names.  Please go on."]
    elif number == 21:
        reply = ["Is that the real reason?","Don't any other reasons come to mind?","Does that reason explain anything else?",
                 "What other reasons might there be?"]
    elif number == 22:
        reply = ["Please don't apologize!","Apologies are not necessary."]
    elif number == 23:
        reply = ["What does that dream suggest to you?","Do you dream often?","What persons appear in your dreams?",
                 "Are you disturbed by your dreams?"]
    elif number == 24 or number == 25:
        reply = ["How do you do.  Please state your problem."]
    elif number == 26:
        reply = ["You don't seem quite certain.","Why the uncertain tone?","Can't you be more positive?",
                 "You aren't sure?","Don't you know?"]
    elif number == 27:
        reply = ["Are you saying no just to be negative?", "You are being a bit negative.", "Why not?", "Are you sure?",
         "Why no?"]
    elif number == 28:
        reply = ["Why are you concerned about my *","What about your own *"]
    elif number == 29:
        reply = ["Can you think of a specific example?","When?","What are you thinking of?","Really, always?"]
    elif number == 30:
        reply = ["Do you really think so?","But you are not sure you *","Do you doubt *"]
    elif number == 31:
        reply = ["In what way?","What resemblence do you see?","What does the similarity suggest to you?",
                 "What other connections do you see?","Could there really be some connection?","How?"]
    elif number == 32:
        reply = ["You seem quite positive.","Are you sure?","I see.","I understand."]
    elif number == 33:
        reply = ["Why do you bring up the topic of friends?","Do your friends worry you?","Do your friends pick on you?",
                 "Are you sure you have any friends?","Do you impose on your friends?",
                 "Perhaps your love for your friends worries you."]
    elif number == 34:
        reply = ["Do computers worry you?","Are you frightened by machines?","Why do you mention computers?",
                 "What do you think machines have to do with your problem?","Don't you think computers can help people?",
                 "What is it about machines that worries you?"]
    num_of_replies = len(reply)
    random_reply = random.randint(0, num_of_replies)
    return reply[random_reply]

eliza()