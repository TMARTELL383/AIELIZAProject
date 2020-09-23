# Replacing all punctuation within a sentence
# www.geeksforgeeks.org

import random

def eliza():
    print("Hello, my name is Eliza. Talk to me.")
    while True:
        response = input("> ")
        response = preprocess(response)
        if response == "bye" or response == "shut up":
            print("I don't like you anymore. Bye.")
            break
        else:
            response = keywords(response)
            print("The response is ", response)
            response = conjugate(response)
            response = buildreply(response)
            print(response)





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
    #Call eliza_emotions() to predict the mood of the reply

#    eliza_emotions(response)

    for word in list_of_keywords:
        if word in response:

            cut_word_and_left = response.find(word)
            index = list_of_keywords.index(word)
            response = response[cut_word_and_left:]
            response = response.replace(word, str(index))

            return response
    return "-1"


# There are a couple of ways we could implement emotion into eliza
# 1) eliza_emotions() is going to take in a keyword, and then look at the words surrounding it.
# Example: response = "i hate you" keyword = hate, surrounding words = i, you
# 2)
def eliza_emotions(response):
    # look at sentence and see if there are any keyword triggers (i hate you)
    # Then write an if statement that will see what kind of emotion that keyword will trigger
    # You can then modify the code once you have the initial setup to look at the surrounding words (like 'i' or 'you')
    # Then make a conclusion as to what kind of emotion eliza will convey
    # This function should return a boolean value.
    # Then depending on the emotion, eliza will look at certain replies, can make a new reply function or make a
    # separate reply list within our reply functions

    # Neutral will be the default emotion
    neutral = False
    happy, sad, angry = False
    emotions = [happy, sad, angry, "upset", "joyful", "fearful", "disgusted", "interested", "confused",
                "sympathetic", "surprised", "excited"]
    keyword_trigger = ["love", "hate", "stupid",  "great", "happy", "sad", "angry", "upset"]
    for word in response:
        if word in keyword_trigger:
            index = keyword_trigger.index(word)
    else:
        index = -1

    # The index will determine the returned emotion/boolean
    if index == -1:
        neutral = True
    elif index == 0:
        emotions[0] = True
    elif index == 1:
        emotions[1] = True



def conjugate(new_response):

    words = new_response.split()

    fixed_response = []
    conjugated_response = ""

    for conjugate in words:
        if conjugate == "are":
            fixed_response = fixed_response + ["am"]
        elif conjugate == "am":
            fixed_response = fixed_response + ["are"]
        elif conjugate == "were":
            fixed_response = fixed_response + ["was"]
        elif conjugate == "was":
            fixed_response = fixed_response + ["were"]
        elif conjugate == "you":
            fixed_response = fixed_response + ["I"]
        elif conjugate == "i":
            fixed_response = fixed_response + ["you"]
        elif conjugate == "your":
            fixed_response = fixed_response + ["my"]
        elif conjugate == "my":
            fixed_response = fixed_response + ["your"]
        elif conjugate == "ive":
            fixed_response = fixed_response + ["you've"]
        elif conjugate == "youve":
            fixed_response = fixed_response + ["I've"]
        elif conjugate == "im":
            fixed_response = fixed_response + ["you're"]
        elif conjugate == "youre":
            fixed_response = fixed_response + ["I'm"]
        elif conjugate == "me":
            fixed_response = fixed_response + ["you"]
        else:
            fixed_response = fixed_response + [conjugate]



    for conjugate in fixed_response:
            conjugated_response = conjugated_response + conjugate + " "

    #print(conjugated_response)
    return conjugated_response


def buildreply(response):
    if response[0:1] == "-1":
        response = response.replace("-1", "")
        reply = getreply(-1)
    elif "0" in response:
        response = response.replace("0", "")
        reply = getreply(0)
    elif "1" in response:
        response = response.replace("1", "")
        reply = getreply(1)
    elif "2" in response:
        response = response.replace("2", "")
        reply = getreply(2)
    elif "3" in response:
        response = response.replace("3", "")
        reply = getreply(3)
    elif "4" in response:
        response = response.replace("4", "")
        reply = getreply(4)
    elif "5" in response:
        response = response.replace("5", "")
        reply = getreply(5)
    elif "6" in response:
        response = response.replace("6", "")
        reply = getreply(6)
    elif "7" in response:
        response = response.replace("7", "")
        reply = getreply(7)
    elif "8" in response:
        response = response.replace("8", "")
        reply = getreply(8)
    elif "9" in response:
        response = response.replace("9", "")
        reply = getreply(9)
    elif "10" in response:
        response = response.replace("10", "")
        reply = getreply(10)
    elif "11" in response:
        response = response.replace("11", "")
        reply = getreply(11)
    elif "12" in response:
        response = response.replace("12", "")
        reply = getreply(12)
    elif "13" in response:
        response = response.replace("13", "")
        reply = getreply(13)
    elif "14" in response:
        response = response.replace("14", "")
        reply = getreply(14)
    elif "15" in response:
        response = response.replace("15", "")
        reply = getreply(15)
    elif "16" in response:
        response = response.replace("16", "")
        reply = getreply(16)
    elif "17" in response:
        response = response.replace("17", "")
        reply = getreply(17)
    elif "18" in response:
        response = response.replace("18", "")
        reply = getreply(18)
    elif "19" in response:
        response = response.replace("19", "")
        reply = getreply(19)
    elif "20" in response:
        response = response.replace("20", "")
        reply = getreply(20)
    elif "21" in response:
        response = response.replace("21", "")
        reply = getreply(21)
    elif "22" in response:
        response = response.replace("22", "")
        reply = getreply(22)
    elif "23" in response:
        response = response.replace("23", "")
        reply = getreply(23)
    elif "24" in response:
        response = response.replace("24", "")
        reply = getreply(24)
    elif "25" in response:
        response = response.replace("25", "")
        reply = getreply(25)
    elif "26" in response:
        response = response.replace("26", "")
        reply = getreply(26)
    elif "27" in response:
        response = response.replace("27", "")
        reply = getreply(27)
    elif "28" in response:
        response = response.replace("28", "")
        reply = getreply(28)
    elif "29" in response:
        response = response.replace("29", "")
        reply = getreply(29)
    elif "30" in response:
        response = response.replace("30", "")
        reply = getreply(30)
    elif "31" in response:
        response = response.replace("31", "")
        reply = getreply(31)
    elif "32" in response:
        response = response.replace("32", "")
        reply = getreply(32)
    elif "33" in response:
        response = response.replace("33", "")
        reply = getreply(33)
    elif "34" in response:
        response = response.replace("34", "")
        reply = getreply(34)

#Concatenate the reply with the response (right-hand sentence) and a "?"
    if "*" in reply:
        reply = reply.replace(" *", response+"?")

    return reply


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
        reply = ["In what way?","What resemblance do you see?","What does the similarity suggest to you?",
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
    random_reply = random.randint(0, num_of_replies - 1)
    return reply[random_reply]





#whats up Tyler?!


eliza()