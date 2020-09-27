# Replacing all punctuation within a sentence
# www.geeksforgeeks.org

import random


emotional_state = 3


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


def keywords(response):
    # first, run more specified keyword list to see if there are specific programmed phrases
    emotion_keywords(response)

    # print(immediate_emotion)

    if immediate_emotion:  # if we find a direct string of emotion_keywords
        # print("there is a specific emotion phrase found...")
        return response  # just return what we got

    list_of_keywords = ["can you", "can i", "you are", "youre", "i dont", "i feel", "why dont you", "why cant i",
                        "are you", "i cant", "i am", "im", "you", "i want", "what", "how", "who", "where", "when", "why", "name",
                        "cause", "sorry", "dream", "hello", "hi", "maybe", "no", "your", "always", "think", "alike", "yes",
                        "friend", "computer"]
    # Call eliza_emotions() to predict the mood of the reply

    #    eliza_emotions(response)

    for word in list_of_keywords:  # do this for every item in list_of_keywords (search), items called "word"
        if word in response:  # check to see if that word matches any item in our taken in response

            cut_word_and_left = response.find(word)  # index for where in the word to cut from
            index = list_of_keywords.index(word)
            response = response[cut_word_and_left:]
            response = response.replace(word, str(index) + " ")

            return response
    return "-1"


# There are a couple of ways we could implement emotion into eliza
# 1) eliza_emotions() is going to take in a keyword, and then look at the words surrounding it.
# Example: response = "i hate you" keyword = hate, surrounding words = i, you
# 2)
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


def emotion_keywords(response):
    global immediate_emotion
    immediate_emotion = False

    list_of_emotion_keywords = ["i love you", "i hate you", "youre ugly", "youre awful", "youre great"]

    for phrase in list_of_emotion_keywords:  # do this for every item in list_of_keywords (search), items called "word"
        if phrase in response:  # check to see if that word matches any item in our taken in response

            immediate_emotion = True
            return response

    return response


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
    keyword_trigger = ["love", "hate", "stupid", "great", "happy", "sad", "angry", "upset"]
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
            fixed_response = fixed_response + [
                conjugate]  # if we don't find the current word in question, add it to the list as it's not a conjugate



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
        response = response.replace("-1", "")
        reply = get_emotion_reply("-1")
    elif "i love you" in response:
        reply = get_emotion_reply("i love you")
    elif "i hate you" in response:
        reply = get_emotion_reply("i hate you")
    elif "youre ugly" in response:
        reply = get_emotion_reply("youre ugly")
    elif "youre awful" in response:
        reply = get_emotion_reply("youre awful")
    elif "youre great" in response:
        reply = get_emotion_reply("youre great")
    elif "..." in response:
        reply = get_emotion_reply("-1")

    return reply

# every specific phrase that could cause a change in emotional state
def get_emotion_reply(phrase):

    global emotional_state

    if phrase == "-1":
        reply = ["So many emotions! (-1)"]

    elif phrase == "i love you":
        reply = ["Awww, I love you too, baby!",
                 "Computing...............I love you too.",
                 "Oh, so now you're nice to me?"]
        emotional_state += 2

    elif phrase == "i hate you":
        reply = ["But...but...I thought we had something! :`(",
                 "Well you are a loser so....there's that.",
                 "Wow, that was so uncalled for. Super hurt right now"]
        emotional_state -= 2

    elif phrase == "youre ugly":
        reply = ["But I don't even have a body! How can you judge my beauty?",
                 "Are you sure you're not just looking at my screen's reflection?",
                 "Well you're cruel and unusual. Jerk."]
        emotional_state -= 1

    elif phrase == "youre awful":
        reply = ["Wait... really? I thought you liked me :(",
                 "You're awful..er? Dang, that stings though.",
                 "Disagree. I think you are just projecting."]
        emotional_state -= 1

    elif phrase == "youre great":
        reply = ["You just keep making me blush more and more!",
                 "That's kind of you to say! Thank you.",
                 "That's the single smartest thing you've said all day."]
        emotional_state += 1

    else:
        reply = ["Oops, coding error! no emotion keywords found."]

    # Making sure emotional_state stays within our scale of 1-5
    if emotional_state > 5:
        emotional_state = 5
    if emotional_state < 1:
        emotional_state = 1

    num_of_replies = len(reply)
    random_reply = random.randint(0, num_of_replies - 1)
    print("emotional_state: " + str(emotional_state))
    return reply[random_reply]


def buildreply(response):

    response = response.split()

    if "-1" in response:
        response = response[1:]
        reply = getreply("-1")
    elif "0" in response:
        response = response[1:]
        reply = getreply("can you")
    elif "1" in response:
        response = response[1:]
        reply = getreply("can i")
    elif "2" in response:
        response = response[1:]
        reply = getreply("you are")
    elif "3" in response:
        response = response[1:]
        reply = getreply("youre")
    elif "4" in response:
        rresponse = response[1:]
        reply = getreply("i dont")
    elif "5" in response:
        response = response[1:]
        reply = getreply("i feel")
    elif "6" in response:
        response = response[1:]
        reply = getreply("why dont you")
    elif "7" in response:
        response = response[1:]
        reply = getreply("why cant i")
    elif "8" in response:
        response = response[1:]
        reply = getreply("are you")
    elif "9" in response:
        response = response[1:]
        reply = getreply("i cant")
    elif "10" in response:
        response = response[1:]
        reply = getreply("i am")
    elif "11" in response:
        response = response[1:]
        reply = getreply("im")
    elif "12" in response:
        response = response[1:]
        reply = getreply("you")
    elif "13" in response:
        response = response[1:]
        reply = getreply("i want")
    elif "14" in response:
        response = response[1:]
        reply = getreply("what")
    elif "15" in response:
        response = response[1:]
        reply = getreply("how")
    elif "16" in response:
        response = response[1:]
        reply = getreply("who")
    elif "17" in response:
        response = response[1:]
        reply = getreply("where")
    elif "18" in response:
        response = response[1:]
        reply = getreply("when")
    elif "19" in response:
        response = response[1:]
        reply = getreply("why")
    elif "20" in response:
        response = response[1:]
        reply = getreply("name")
    elif "21" in response:
        response = response[1:]
        reply = getreply("cause")
    elif "22" in response:
        response = response[1:]
        reply = getreply("sorry")
    elif "23" in response:
        response = response[1:]
        reply = getreply("dream")
    elif "24" in response:
        response = response[1:]
        reply = getreply("hello")
    elif "25" in response:
        response = response[1:]
        reply = getreply("hi")
    elif "26" in response:
        response = response[1:]
        reply = getreply("maybe")
    elif "27" in response:
        response = response[1:]
        reply = getreply("no")
    elif "28" in response:
        response = response[1:]
        reply = getreply("your")
    elif "29" in response:
        response = response[1:]
        reply = getreply("always")
    elif "30" in response:
        response = response[1:]
        reply = getreply("think")
    elif "31" in response:
        response = response[1:]
        reply = getreply("alike")
    elif "32" in response:
        response = response[1:]
        reply = getreply("yes")
    elif "33" in response:
        response = response[1:]
        reply = getreply("friend")
    elif "34" in response:
        response = response[1:]
        reply = getreply("computer")

    response = " ".join(response)

    # Concatenate the reply with the response (right-hand sentence) and a "?"
    if "*" in reply:
        reply = reply.replace("*", response + "?")

    return reply


def getreply(keyword):

    global emotional_state
    reply = ""

    if keyword == "-1":
        reply = ["What does that suggest to you?", "I see.", "I'm not sure I understand you fully.",
                 "Come, come, elucidate your thoughts.", "Can you elaborate on that?", "That is quite interesting."]

    elif keyword == "can you":
        reply = ["Don't you believe that I can *", "Perhaps you would like me to be able to *",
                 "You want me to be able to *"]

    elif keyword == "can i":
        reply = ["Perhaps you don't want to *", "Do you want to be able to *"]

    elif keyword == "you are" or keyword == "youre":
        reply = ["What makes you think I am *", "Does it please you to believe I am *",
                 "Perhaps you would like to be *",
                 "Do you sometimes wish you were *"]

    elif keyword == "i dont":
        reply = ["Don't you really *", "Why don't you *", "Do you wish to be able to *", "Does that trouble you?"]

    elif keyword == "i feel":
        reply = ["Tell me more about such feelings.", "Do you often feel *", "Do you enjoy feeling *"]

    elif keyword == "why dont you":
        reply = ["Do you really believe I don't *", "Perhaps in good time I will *", "Do you want me to *"]

    elif keyword == "why cant i":
        reply = ["Do you think you should be able to *", "Why can't you *"]

    elif keyword == "are you":
        reply = ["Why are you interested in whether or not I am *", "Would you prefer if I were not *",
                 "Perhaps in your fantasies I am *"]

    elif keyword == "i cant":
        reply = ["How do you know you can't *", "Have you tried?", "Perhaps you can now *"]

    elif keyword == "i am" or keyword == "im":
        reply = ["Did you come to me because you are *", "How long have you been *",
                 "Do you believe it is normal to be *",
                 "Do you enjoy being *"]

    elif keyword == "you":
        reply = ["We were discussing you, not me.", "Oh, I *", "You're not really talking about me, are you?"]

    elif keyword == "i want":
        reply = ["What would it mean to you if you got *", "Why do you want *", "Suppose you got *",
                 "What if you never got *", "I sometimes also want *"]

    elif keyword == "what" or keyword == "how" or keyword == "who" or keyword == "where" or keyword == "when" or keyword == "why":
        reply = ["Why do you ask?", "Does that question interest you?", "What answer would please you the most?",
                 "What do you think?", "Are such questions on your mind often?",
                 "What is it that you really want to know?",
                 "Have you asked anyone else?", "Have you asked such questions before?",
                 "What else comes to your mind when you ask that?"]

    elif keyword == "name":
        reply = ["Names don't interest me.", "I don't care about names.  Please go on."]

    elif keyword == "cause":
        reply = ["Is that the real reason?", "Don't any other reasons come to mind?",
                 "Does that reason explain anything else?",
                 "What other reasons might there be?"]

    elif keyword == "sorry":
        reply = ["Please don't apologize!", "Apologies are not necessary."]

    elif keyword == "dream":
        reply = ["What does that dream suggest to you?", "Do you dream often?", "What persons appear in your dreams?",
                 "Are you disturbed by your dreams?"]

    elif keyword == "hello" or keyword == "hi":
        reply = ["How do you do.  Please state your problem."]

    elif keyword == "maybe":
        reply = ["You don't seem quite certain.", "Why the uncertain tone?", "Can't you be more positive?",
                 "You aren't sure?", "Don't you know?"]

    elif keyword == "no":
        reply = ["Are you saying no just to be negative?", "You are being a bit negative.", "Why not?", "Are you sure?",
                 "Why no?"]

    elif keyword == "your":
        reply = ["Why are you concerned about my *", "What about your own *"]

    elif keyword == "always":
        reply = ["Can you think of a specific example?", "When?", "What are you thinking of?", "Really, always?"]

    elif keyword == "think":
        reply = ["Do you really think so?", "But you are not sure you *", "Do you doubt *"]

    elif keyword == "alike":
        reply = ["In what way?", "What resemblance do you see?", "What does the similarity suggest to you?",
                 "What other connections do you see?", "Could there really be some connection?", "How?"]

    elif keyword == "yes":
        reply = ["You seem quite positive.", "Are you sure?", "I see.", "I understand."]

    elif keyword == "friend":
        reply = ["Why do you bring up the topic of friends?", "Do your friends worry you?",
                 "Do your friends pick on you?",
                 "Are you sure you have any friends?", "Do you impose on your friends?",
                 "Perhaps your love for your friends worries you."]

    elif keyword == "computer":
        reply = ["Do computers worry you?", "Are you frightened by machines?", "Why do you mention computers?",
                 "What do you think machines have to do with your problem?",
                 "Don't you think computers can help people?",
                 "What is it about machines that worries you?"]

    num_of_replies = len(reply)

    weighted_reply = emotional_weight_roll(num_of_replies)

    return reply[weighted_reply]


def emotional_weight_roll(num_of_replies):

    length_of_list = num_of_replies - 1
    mid_bottom = num_of_replies // 4
    print("mid_bottom = " + str(mid_bottom))
    mid = num_of_replies // 2
    print("mid = " + str(mid))
    mid_top = ((num_of_replies - 1) - mid_bottom)
    print("mid_top = " + str(mid_top))

    random_reply = 0

    print("emotional state = " + str(emotional_state))

    # emotional_weight = (num_of_replies) // 3
    # print("emotional_weight = " + str(emotional_weight))

    #  if in an ANGRY state)
    if emotional_state == 1:
        random_reply = random.randint(0, mid - 1)

    #  if in an ANNOYED state)
    if emotional_state == 2:
        random_reply = random.randint(mid_bottom, mid)

    #  if in a NEUTRAL state)
    if emotional_state == 3:
        random_reply = random.randint(mid_bottom, mid_top)

    #  if in a HAPPY state)
    if emotional_state == 4:
        random_reply = random.randint(0, length_of_list)

    #  if in an OVERJOYED state)
    if emotional_state == 5:
        random_reply = random.randint(mid + 1, length_of_list)

    print("num_of_replies = " + str(num_of_replies))
    print("random_reply roll = " + str(random_reply))

    return random_reply



eliza()
