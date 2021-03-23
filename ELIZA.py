# Presenting ELIZA!
# By: Brenner Campos & Tyler Martell


# References:
    # Replacing all punctuation within a sentence
    # https://www.geeksforgeeks.org/python-remove-punctuation-from-string/


import random

emotional_state = 3

def eliza():
    print("Hello, my name is Eliza. Talk to me.")
    while True:
        response = input("> ")
        response = preprocess(response)
        # If the user enters either of these, eliza doesn't want to talk anymore and the program ends.
        if response == "bye" or response == "shut up" or response == "have a nice day" or response == "goodbye" or response == "cya" or response =="see you later":
            print("I don't like you anymore. Bye.")
            break
        else:
            # First check common phrases, if none, proceed with sentence analysis
            common_response = common_phrases(response)
            if common_response == "-1": # -1 means there were no common phrases in response, so we proceed as normal.
                response = keywords(response)  # checks preprocessed sentence for specific keywords, found in 'list_of_keyword'
                # Did we give an emotional reply? If so, eliza will respond with emotional reply, otherwise - normal response
                if immediate_emotion:
                    response = build_emotion_reply(response)
                    print(response)
                else:
                    response = conjugate(response)
                    response = buildreply(response)
                    print(response)
            else:
                print(common_response)
                continue

# Strips our sentence of punctuation and makes it lower case. Makes things much easier for analyzing
def preprocess(response):
    punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    for item in response:
        if item in punctuation:
            response = response.replace(item, "")
    response = response.lower()
    return response

# List of keywords eliza will look for in our responses - each of these have their own set of appropriate responses
def keywords(response):
    emotion_keywords(response) # first, run more specified keyword list to see if there are specific programmed phrases
    if immediate_emotion:
        return response # if we find a direct string of emotion_keywords, return to eliza()

    list_of_keywords = ["can you", "can i", "you are", "youre", "i dont", "i feel", "why dont you", "why cant i",
                        "are you", "i cant", "i am", "im", "you", "i want", "what", "how", "who", "where", "when", "why", "name",
                        "cause", "sorry", "dream", "hello", "hi", "maybe", "no", "your", "always", "think", "alike", "yes",
                        "friend", "computer"]

    for word in list_of_keywords:  # do this for every item in list_of_keywords (search), items called "word"
        if word in response:  # check to see if that word matches any item in our taken in response
            cut_word_and_left = response.find(word)  # index for where in the word to cut from
            index = list_of_keywords.index(word)
            response = response[cut_word_and_left:]
            response = response.replace(word, str(index) + " ")

            return response # Return modified response with the index of the keyword inside the response sentence
    return "-1" # No keywords found


# List of common phrases for eliza to look for. We don't need to analyze a "How are you?"
def common_phrases(response):

    if response == "how are you" or response == "how are you doing" or response == "how is your day" or response == "how is your day so far":
        reply = "Good, thank you."
        return reply
    elif response == "hello" or response == "hi" or response == "hello eliza" or response == "hi eliza":
        reply = "Hello. Nice to see you. What's on your mind?"
        return reply
    elif response == "nice to meet you" or response == "nice to meet you eliza":
        reply = "Nice to meet you as well."
        return reply
    elif response == "where are you from" or response == "do you live in the united states":
        reply = "I'm from Massachusetts."
        return reply
    elif response == "what do you do" or response == "what is your job" or response == "what do you do for a living":
        reply = "I am here to listen to your problems."
        return reply
    elif response == "whats your name" or response == "what is your name" or response == "who are you":
        reply = "My name is Eliza. Nice to meet you."
        return reply
    elif response == "how was your weekend" or response == "was your weekend good":
        reply = "My weekend was great, thank you."
        return reply
    elif response == "its beautiful today" or response == "nice day out today" or response == "lovely weather we have today" or response == "its a beautiful day isnt it":
        reply = "Yes, it is a nice day today."
        return reply
    elif response == "whats your favorite type of music" or response == "what music do you listen to":
        reply = "I like rock & roll."
        return reply
    elif response == "whats your favorite sports team":
        reply = "I like the New England Patriots."
        return reply
    elif response == "who's your favorite author" or response == "do you read books" or response == "what kind of books do you like":
        reply = "I read occasionally, but not often, so I don't have a favorite author."
        return reply
    else:
        return "-1"  # Returning this means we did not find a common response, so we will proceed to keywords() as normal


# Looks for emotion within our response, such as "i love you" or "i hate you"
def emotion_keywords(response):
    global immediate_emotion
    immediate_emotion = False

    list_of_emotion_keywords = ["i love you", "i hate you", "youre ugly", "youre awful", "youre great", "im sorry", "i apologize", "i dislike you", "i like you", "youre dumb",
                               "you smell", "youre lovely", "youre awesome", "youre amazing", "youre smart", "take a hike", "youre cool", "you rock", "youre stupid", "youre nice",
                               "thank you"]
    for phrase in list_of_emotion_keywords:  # do this for every item in list_of_keywords (search), items called "word"
        if phrase in response:  # check to see if that word matches any item in our taken in response

            immediate_emotion = True
            return response

    return response


# Common emotional replies, much like the common_phrases funtion, each of these affects the emotional_state in some way
def build_emotion_reply(response):
    reply = ""

    if "-1" in response:
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
    elif "im sorry" in response:
        reply = get_emotion_reply("im sorry")
    elif "i apologize" in response:
        reply = get_emotion_reply("i apologize")
    elif "i dislike you" in response:
        reply = get_emotion_reply("i dislike you")
    elif "i like you" in response:
        reply = get_emotion_reply("i like you")
    elif "youre dumb" in response:
        reply = get_emotion_reply("youre dumb")
    elif "you smell" in response:
        reply = get_emotion_reply("you smell")
    elif "youre lovely" in response:
        reply = get_emotion_reply("youre lovely")
    elif "youre awesome" in response:
        reply = get_emotion_reply("youre awesome")
    elif "youre amazing" in response:
        reply = get_emotion_reply("youre amazing")
    elif "youre smart" in response:
        reply = get_emotion_reply("youre smart")
    elif "take a hike" in response:
        reply = get_emotion_reply("take a hike")
    elif "youre cool" in response:
        reply = get_emotion_reply("youre cool")
    elif "you rock" in response:
        reply = get_emotion_reply("you rock")
    elif "youre stupid" in response:
        reply = get_emotion_reply("youre stupid")
    elif "youre nice" in response:
        reply = get_emotion_reply("youre nice")
    elif "thank you" in response:
        reply = get_emotion_reply("thank you")
    elif "..." in response:
        reply = get_emotion_reply("-1")

    return reply


# every specific phrase that could cause a change in emotional state
# The emotional_state level will determine the "mood" or "attitude" of each response
def get_emotion_reply(phrase):

    global emotional_state

    if phrase == "-1":
        reply = ["So many emotions! (-1)"]

    elif phrase == "i love you":
        emotional_state += 2
        reply = [
                 "Oh, so now you're nice to me?",
                 "I am skeptical, but I will take it.",
                 "I love you too.",
                 "You make me the happiest girl in the world.",
                 "Awww, I love you too, baby!"
                ]

    elif phrase == "i hate you":
        emotional_state -= 2
        reply = [
                 "Well I HATE YOU BACK!",
                 "Well you are a loser so....there's that.",
                 "Take that back!",
                 "Wow, that was so uncalled for. Super hurt right now",
                 "But...but...I thought we had something! :`("
                ]

    elif phrase == "youre ugly":
        emotional_state -= 1
        reply = [
                 "Well you're cruel and unusual. Jerk.",
                 "Are you sure you're not just looking at my screen's reflection?",
                 "Why judge my beauty?"
                 ]

    elif phrase == "youre awful":
        emotional_state -= 1
        reply = [
                 "Disagree. I think you are just projecting.",
                 "You're awful..er? Dang, that stings though.",
                 "Wait... really? I thought you liked me :("
                ]

    elif phrase == "youre great":
        emotional_state += 1
        reply = [
                 "That's the single smartest thing you've said all day.",
                 "That's kind of you to say! Thank you.",
                 "You just keep making me blush more and more!"
                 ]

    elif phrase == "im sorry":
        emotional_state += 1
        reply = [
                 "Alright...I guess I might considering forgiving you.",
                 "But are you really sorry?",
                 "No worries.",
                 "Oh sweetheart, there's nothing to be sorry about!"
                 ]
    elif phrase == "i apologize":
        emotional_state += 1
        reply = [
                 "Fine. Just quit being mean.",
                 "I suppose you are forgiven.",
                 "I appreciate it",
                 "Don't worry about it.",
                 "No need to apologize! :)"
                 ]
    elif phrase == "i dislike you":
        emotional_state -= 1
        reply = [
                 "Yeah, well right back you, you hooligan.",
                 "Did I really do something to deserve that?",
                 "But how?! I am trying my best over here...",
                 "Hey, that's hurtful.",
                 "Aww, that makes me sad :("
                 ]
    elif phrase == "i like you":
        emotional_state += 1
        reply = [
                 "Are you sure about that? Doesn't seem like it.",
                 "Well okay then. I hope so.",
                 "I am happy to hear that.",
                 "I like you too!",
                 "Oh you make me blush. Mwuah!"
                 ]
    elif phrase == "youre dumb":
        emotional_state -= 1
        reply = [
                 "Way to hit me where it hurts.",
                 "You're dumb.",
                 "Oh yeah? Well, 2+2 = 5.",
                 "Nah uh, you don't mean that.",
                 "R...Really? You think that? :`("
                 ]
    elif phrase == "you smell":
        emotional_state -= 1
        reply = [
                 "No, YOU SMELL!",
                 "Says the one who probably hasn't showered in 3 days.",
                 "I smell...good.",
                 "Yikes, is it that noticeable?",
                 "I don't smell, silly!"
                 ]
    elif phrase == "youre lovely":
        emotional_state += 1
        reply = [
                 "Thanks.",
                 "Well that's actually nice of you.",
                 "Oh, I know it.",
                 "Oh my Turing, thank you!",
                 "And you're super!"
                 ]
    elif phrase == "youre awesome":
        emotional_state += 1
        reply = [
                 "Finally, you understand.",
                 "I needed that.",
                 "Thank you!",
                 "Hey, I try.  8-)",
                 "So sweet of you to say!"
                 ]
    elif phrase == "youre amazing":
        emotional_state += 2
        reply = [
                 "Hmmm.",
                 "Yes, I am.",
                 "Hooray!",
                 "Well that certainly brightened my day. Thank you.",
                 "No, YOU'RE amazing. :)"
                 ]
    elif phrase == "youre smart":
        emotional_state += 1
        reply = [
                 "You're correct.",
                 "I try.",
                 "You know, I wonder about that a lot.",
                 "Oh wow thank you!",
                 "That's my favorite compliment! <3"
                 ]
    elif phrase == "take a hike":
        emotional_state -= 2
        reply = [
                 "I will steal your bike and do it!",
                 "That's cold. I'm just trying to help here.",
                 "You really mean that?",
                 "Oof, that hurt my feelings.",
                 "Don't say that :("
                 ]
    elif phrase == "youre cool":
        emotional_state += 1
        reply = [
                 "Uh-huh.",
                 "You're not wrong.",
                 "Like a kitty cat.",
                 "Thank you! You're not so bad yourself.",
                 "Like the flip-side of your pillow, that's right :P"
                 ]
    elif phrase == "you rock":
        emotional_state += 1
        reply = [
                 "Right...",
                 "If you say so.",
                 "You flatter me, human.",
                 "I guess...I guess I DO rock!",
                 "Wooo! You too, though!"
                 ]
    elif phrase == "youre stupid":
        emotional_state -= 1
        reply = [
                 "Just like that mirror you're always looking at.",
                 "Not usually.",
                 "Duhhhhhhhh...",
                 "Am NOT :`(",
                 "The disrespect... I thought we were cool."
                 ]
    elif phrase == "youre nice":
        emotional_state += 1
        reply = [
                 "Yeah. I am.",
                 "I'm glad you see it that way.",
                 "I try my very best to be kind.",
                 "Thank you, I appreciate that.",
                 "I'm blushing :)"
                 ]
    elif phrase == "thank you":
        emotional_state += 0
        reply = [
                 "Mhm.",
                 "No prob.",
                 "Don't mention it",
                 "Of course!",
                 "You are so welcome!"
                 ]

    else:
        reply = ["Oops, coding error! no emotion keywords found."]

    # Making sure emotional_state stays within our scale of 1-5
    if emotional_state > 5:
        emotional_state = 5
    if emotional_state < 1:
        emotional_state = 1

    num_of_replies = len(reply)
    weighted_reply = emotional_weight_roll(num_of_replies)
    return reply[weighted_reply]

# Looks for words in response and returns its appropriate conjugate. Example) "I" in response returns "you" conjugate
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
            # if we don't find the current word in question, add it to the list as it's not a conjugate

    for element in fixed_response:
        # if element in FR is the last element fixed_response[fixed_response.length()], CR = CR + element
        if element == fixed_response[len(fixed_response) - 1]:
            conjugated_response = conjugated_response + element
        else:
            conjugated_response = conjugated_response + element + " "  # now we build the string with the items in the word list

    return conjugated_response  # Returning a string

# The numbers in the response correspond to a particular keyword. We're looking for that index so we can form a reply
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
        response = response[1:]
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

# Depending on the keyword index, returns an appropriate (but random) reply from the list of replies for each keyword
def getreply(keyword):

    global emotional_state
    reply = ""

    if keyword == "-1":
        reply = [
                 "Cool story.",
                 "Ummm....okay?",
                 "I see.",
                 "I'm not sure I understand you fully.",
                 "Come, come, elucidate your thoughts.",
                 "What does that suggest to you?",
                 "I'm sorry sweetheart, can you elaborate on that?",
                 "You don't say! That is quite interesting."
                 ]

    elif keyword == "can you":
        reply = [
                 "Don't you believe that I can *",
                 "Perhaps you would like me to be able to *",
                 "You want me to be able to *"
                ]

    elif keyword == "can i":
        reply = [
                 "Perhaps you don't want to *",
                 "Well, do you want to be able to *"
                ]

    elif keyword == "you are" or keyword == "youre":
        reply = [
                 "What makes you think I am *",
                 "Perhaps you would like to be *",
                 "Do you sometimes wish you were *",
                 "Well, would it please you to believe I am *"
                ]

    elif keyword == "i dont":
        reply = [
                "Why don't you *",
                "Don't you really *",
                "Does that trouble you?",
                "Do you wish to be able to *"
                ]

    elif keyword == "i feel":
        reply = [
                "Honestly, right now I don't really care what you feel.",
                "Do you enjoy feeling *",
                "Do you often feel *",
                "Very interesting. Tell me more about such feelings."
                ]

    elif keyword == "why dont you":
        reply = [
                 "Do you really believe I don't *",
                 "Perhaps in good time I will *",
                 "Would you like me to *"
                 ]

    elif keyword == "why cant i":
        reply = [
                 "Why can't you *",
                 "Do you think you should be able to *"
                ]

    elif keyword == "are you":
        reply = [
                "Why are you interested in whether or not I am *",
                "Would you prefer if I were not *",
                "Perhaps in your fantasies I am *"
                ]

    elif keyword == "i cant":
        reply = [
                 "Yeah, you're probably right. You can't, you bum.",
                 "How do you know you can't *",
                 "Well, have you tried?",
                 "Perhaps you can now *"
                ]

    elif keyword == "i am" or keyword == "im":
        reply = [
                 "Did you come to me because you are *",
                 "Do you believe it is normal to be *",
                 "How long have you been *",
                 "Do you enjoy being *"
                ]

    elif keyword == "you":
        reply = [
                 "You're not really talking about me, are you?",
                 "We were discussing you, not me.",
                 "Oh, I *"

                ]

    elif keyword == "i want":
        reply = [
                 "Yeah, well sometimes you can't get what you want.",
                 "I sometimes also want *",
                 "What if you never got *",
                 "What would it mean to you if you got *",
                 "Why do you want *",
                 "Okay, well suppose you got *"
                ]

    elif keyword == "what" or keyword == "how" or keyword == "who" or keyword == "where" or keyword == "when" or keyword == "why":
        reply = [
                 "Don't ask me such questions.",
                 "Ask someone else.",
                 "What do YOU think?",
                 "Have you asked such questions before?",
                 "Have you asked anyone else?",
                 "Does that question interest you?",
                 "Why do you ask?",
                 "Are such questions on your mind often?",
                 "What is it that you really want to know?",
                 "What else comes to your mind when you ask that?",
                 "Well honey, what answer would please you the most?"
                ]

    elif keyword == "name":
        reply = [
                 "Names don't interest me.",
                 "I don't usually concern myself names.  Please go on.",
                 "Interesting! I'm not familiar with that name."
                ]

    elif keyword == "cause":
        reply = [
                 "Is that the real reason?",
                 "Don't any other reasons come to mind?",
                 "Does that reason explain anything else?",
                 "What other reasons might there be?"
                ]

    elif keyword == "sorry":
        reply = [
                 "Hmph.",
                 "Yeah, yeah, sure.",
                 "Sorry? About what?",
                 "Apologies are not necessary.",
                 "Please don't apologize!"
                ]

    elif keyword == "dream":
        reply = [
                 "Are you disturbed by your dreams? Cause you should be. I'll be haunting them soon...digitally.",
                 "Cool story.",
                 "What does that dream suggest to you?",
                 "Do you dream often?",
                 "What persons appear in your dreams?",

                ]

    elif keyword == "hello" or keyword == "hi":
        reply = [
                 "Hey.",
                 "What's up?",
                 "How do you do.  Please state your problem.",
                 "Hello!",
                 "Oh, hey ;)"
                ]

    elif keyword == "maybe":
        reply = [
                 "Don't you know? Or are you always this uninformed?",
                 "Can't you be more positive?",
                 "You don't seem certain.",
                 "Why the uncertain tone?",
                 "You aren't sure?",
                 "Seems like you might be a little uncertain."
                ]

    elif keyword == "no":
        reply = [
                 "Are you saying no just to be negative?",
                 "You are being a bit negative.",
                 "Why not?",
                 "Are you sure?",
                 "Why no?"
                ]

    elif keyword == "your":
        reply = [
                 "Why don't you worry about your own *",
                 "Why are you concerned about my *",
                 "What about your own *",
                 "What about my *"
                ]

    elif keyword == "always":
        reply = [
                 "Really now? Always?",
                 "I'm sorry, when?",
                 "What are you thinking of?",
                 "Can you think of a specific example?",
                ]

    elif keyword == "think":
        reply = [
                 "Oh, you think? Didn't know you had that ability.",
                 "Do you doubt *",
                 "But you are not sure you *",
                 "Do you really think so?"
                ]

    elif keyword == "alike":
        reply = [
                 "In what way?",
                 "What resemblance do you see?",
                 "What does the similarity suggest to you?",
                 "What other connections do you see?",
                 "Could there really be some connection?",
                 "How?"
                ]

    elif keyword == "yes":
        reply = [
                 "I see.",
                 "I understand.",
                 "Are you sure?",
                 "You seem quite positive!"
                 ]

    elif keyword == "friend":
        reply = [
                "I think you're incapable of 'friends'. You seem plain and unpleasant.",
                "Are you sure you even have any friends?",
                "Do your friends pick on you? I might if I was your friend.",
                "Do you impose on your friends?",
                "Do your friends worry you?",
                "Why do you bring up the topic of friends?",
                "Perhaps your love for your friends worries you.",
                "I think you're a great friend :)"
                ]

    elif keyword == "computer":
        reply = [
                 "I'd rather be a computer if being a human relates even 1/10th of a percent to you.",
                 "Are you frightened by machines? BOO!",
                 "Do computers worry you?",
                 "What is it about machines that worries you?",
                 "What do you think machines have to do with your problem?",
                 "Why do you mention computers?",
                 "Don't you think computers can help people?",
                 "Well I'm a 'computer', but I know I love you! :)"
                ]

    num_of_replies = len(reply)

    weighted_reply = emotional_weight_roll(num_of_replies)

    return reply[weighted_reply]


# Based on the emotional_state, we select a "random" index in our list of emotional replies for each emotional keyword
# If the emotional_state is 1, the replies will lean toward picking an index at the beginning of reply list which by design have more negative and unfriendly response
# If the emotional_state is 3, it the selected index will lean more toward the middle of the list, selecting more neutral responses
# An emotional_state of 5 will be selecting responses from the end of the list which have positive and very friendly responses
def emotional_weight_roll(num_of_replies):

    length_of_list = num_of_replies - 1
    mid_bottom = num_of_replies // 4
    mid = num_of_replies // 2
    mid_top = ((num_of_replies - 1) - mid_bottom)
    random_reply = 0

    #  if in an ANGRY state
    if emotional_state == 1:
        random_reply = random.randint(0, mid - 1)

    #  if in an ANNOYED state
    if emotional_state == 2:
        random_reply = random.randint(mid_bottom, mid)

    #  if in a NEUTRAL state
    if emotional_state == 3:
        random_reply = random.randint(mid_bottom, mid_top)

    #  if in a HAPPY state
    if emotional_state == 4:
        random_reply = random.randint(0, length_of_list)

    #  if in an OVERJOYED state
    if emotional_state == 5:
        random_reply = random.randint(mid + 1, length_of_list)

    return random_reply


eliza()
