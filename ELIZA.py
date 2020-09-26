# Replacing all punctuation within a sentence
# www.geeksforgeeks.org

import random

def eliza():

    print("Hello, my name is Eliza. Talk to me.")
    while True:
        response = input("> ")      # first step is getting the input sentence from the user and storing it in a 'response' variable
        response = preprocess(response)     # second step is to strip all punctuation and lowercase so we can more accurately find keywords
        if response == "bye" or response == "shut up":
            print("I don't like you anymore. Bye.")
            break
        else:
            common_response = common_phrases(response)
            if common_response == "-1": # This means there were no common phrases in response, so we proceed as normal.
                response = keywords(response)  # checks preprocessed sentence for specific keywords, found in 'list_of_keyword'
                if immediate_emotion:
                    response = build_emotion_reply(response)
                    print(response)
                else:
                    response = conjugate(response)  # throws
                    response = buildreply(response)
                    print(response)
            else:
                print(common_response)
                continue



def preprocess(response):
    punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    for item in response:
        if item in punctuation:
            response = response.replace(item, "")
    response = response.lower()
    return response


def common_phrases(response):

    if response == "how are you":
        reply = "Good, thank you."
        return reply
    elif response == "hello" or response == "hi" or response == "hello eliza" or response == "hi eliza":
        reply = "Hello. Nice to see you. What's on your mind?"
        return reply
    elif response == "nice to meet you" or response == "nice to meet you eliza":
        reply = "Nice to meet you as well."
        return reply
    elif response == "where are you from":
        reply = "I'm from Massachusetts."
        return reply
    elif response == "what do you do" or response == "what is your job" or response == "what do you do for a living":
        reply = "I am here to listen to your problems."
        return reply
    return "-1"  # Returning this means we did not find a common response, so we will proceed to keywords()


def keywords(response):

    # first, run more specified keyword list to see if there are specific programmed phrases
    emotion_keywords(response)

    #print(immediate_emotion)

    if immediate_emotion:   #if we find a direct string of emotion_keywords
       # print("there is a specific emotion phrase found...")
        return response     #just return what we got



    list_of_keywords = ["can you", "can i", "you are", "youre", "i dont", "i feel", "why dont you", "why cant i", "are you",
             "i cant", "i am", "im", "you", "i want", "what", "how", "who", "where", "when", "why", "name", "cause",
             "sorry", "dream", "hello", "hi", "maybe", "no", "your", "always", "think", "alike", "yes", "friend",
             "computer"]
    #Call eliza_emotions() to predict the mood of the reply

#    eliza_emotions(response)

    for word in list_of_keywords:   # do this for every item in list_of_keywords (search), items called "word"
        if word in response:    # check to see if that word matches any item in our taken in response

            cut_word_and_left = response.find(word)     # index for where in the word to cut from
            index = list_of_keywords.index(word)
            response = response[cut_word_and_left:]
            response = response.replace(word, str(index)+" ")

            return response
    return "-1"


def emotion_keywords(response):

    global immediate_emotion
    immediate_emotion = False

    list_of_emotion_keywords = ["i love you", "i hate you", "youre ugly", "youre awful", "youre great"]

    for phrase in list_of_emotion_keywords:   # do this for every item in list_of_keywords (search), items called "word"
        if phrase in response:    # check to see if that word matches any item in our taken in response

            immediate_emotion = True
            return response

    return response

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
            fixed_response = fixed_response + [conjugate]   # if we don't find the current word in question, add it to the list as it's not a conjugate

    for element in fixed_response:
        # if element in FR is the last element fixed_response[fixed_response.length()], CR = CR + element
        if element == fixed_response[len(fixed_response) - 1]:
            conjugated_response = conjugated_response + element
        else:
            conjugated_response = conjugated_response + element + " "  # now we build the string with the items in the word list

    return conjugated_response  # Returning a string

def build_emotion_reply(response):

    s = response
    reply = "-null reply-"

    if "-1" in response.split():
        response = response.replace("-1", "") #TODO I don't think this will work because you call this function BEFORE you find your keyword and put -1 or another number in.
        reply = get_emotion_reply(-1)
    elif "i love you" in response:
        reply = get_emotion_reply(0)
    elif "i hate you" in response:
        reply = get_emotion_reply(1)
    elif "youre ugly" in response:
        reply = get_emotion_reply(2)
    elif "youre awful" in response:
        reply = get_emotion_reply(3)
    elif "youre great" in response:
        reply = get_emotion_reply(4)
    elif "..." in response:
        reply = get_emotion_reply(5)

    return reply

def get_emotion_reply(number):


    if number == -1:
        reply = ["So many emotions! (-1)"]
    elif number == 0:
        reply = ["Awww,I love you too, baby!"]
    elif number == 1:
        reply = ["Wow, that was so uncalled for. Super hurt right now"]
    elif number == 2:
        reply = ["But I don't even have a body! How can you judge my beauty?"]
    elif number == 3:
        reply = ["Disagree. I think you are just projecting.", "You're awful..er? Dang, that stings though."]
    elif number == 4:
        reply = ["That's the single smartest thing you've said all day."]
    else:
        reply = ["Oops, coding error! no emotion keywords found."]


    num_of_replies = len(reply)
    random_reply = random.randint(0, num_of_replies - 1)
    return reply[random_reply]


def buildreply(response):

    response = response.split()

    if "-1" in response:
        response = response[1:]
        reply = getreply(-1)
    elif "0" in response:
        response = response[1:]
        reply = getreply(0)
    elif "1" in response:
        response = response[1:]
        reply = getreply(1)
    elif "2" in response:
        response = response[1:]
        reply = getreply(2)
    elif "3" in response:
        response = response[1:]
        reply = getreply(3)
    elif "4" in response:
        response = response[1:]
        reply = getreply(4)
    elif "5" in response:
        response = response[1:]
        reply = getreply(5)
    elif "6" in response:
        response = response[1:]
        reply = getreply(6)
    elif "7" in response:
        response = response[1:]
        reply = getreply(7)
    elif "8" in response:
        response = response[1:]
        reply = getreply(8)
    elif "9" in response:
        response = response[1:]
        reply = getreply(9)
    elif "10" in response:
        response = response[1:]
        reply = getreply(10)
    elif "11" in response:
        response = response[1:]
        reply = getreply(11)
    elif "12" in response:
        response = response[1:]
        reply = getreply(12)
    elif "13" in response:
        response = response[1:]
        reply = getreply(13)
    elif "14" in response:
        response = response[1:]
        reply = getreply(14)
    elif "15" in response:
        response = response[1:]
        reply = getreply(15)
    elif "16" in response:
        response = response[1:]
        reply = getreply(16)
    elif "17" in response:
        response = response[1:]
        reply = getreply(17)
    elif "18" in response:
        response = response[1:]
        reply = getreply(18)
    elif "19" in response:
        response = response[1:]
        reply = getreply(19)
    elif "20" in response:
        response = response[1:]
        reply = getreply(20)
    elif "21" in response:
        response = response[1:]
        reply = getreply(21)
    elif "22" in response:
        response = response[1:]
        reply = getreply(22)
    elif "23" in response:
        response = response[1:]
        reply = getreply(23)
    elif "24" in response:
        response = response[1:]
        reply = getreply(24)
    elif "25" in response:
        response = response[1:]
        reply = getreply(25)
    elif "26" in response:
        response = response[1:]
        reply = getreply(26)
    elif "27" in response:
        response = response[1:]
        reply = getreply(27)
    elif "28" in response:
        response = response[1:]
        reply = getreply(28)
    elif "29" in response:
        response = response[1:]
        reply = getreply(29)
    elif "30" in response:
        response = response[1:]
        reply = getreply(30)
    elif "31" in response:
        response = response[1:]
        reply = getreply(31)
    elif "32" in response:
        response = response[1:]
        reply = getreply(32)
    elif "33" in response:
        response = response[1:]
        reply = getreply(33)
    elif "34" in response:
        response = response[1:]
        reply = getreply(34)

    response = " ".join(response)
#Concatenate the reply with the response (right-hand sentence) and a "?"
    if "*" in reply:
        reply = reply.replace("*", response+"?")


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




eliza()