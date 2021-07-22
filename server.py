from bot import telegram_chatbot

bot = telegram_chatbot()
update_id = None
from_ = None
message = None

def reply(msg, from_ = from_):
    bot.send_message(msg, from_)

def decide_mode(msg, from_):
    global update_id
    if msg.lower() == "/start":
        registration(msg, from_)
    else:
        reply("Sorry I don't understand you", from_)

def valid_response_checker(user_input, options):
    if user_input.lower() == "/quit" or user_input.lower() == "quit":
        return "quit"
    elif not options:
        return user_input
    elif user_input.lower() in options:
        return user_input
    else:
        return "invalid"


def get_response(options):
    global update_id
    responded = False
    while responded == False:
        updates = bot.get_updates(offset=update_id)
        updates = updates["result"]
        if updates:
            # Just take the last input
            item = updates[-1]
            update_id = item["update_id"]
            try:
                message = item["message"]["text"]
                print("message:",message)
            except:
                message = None
            from_ = item["message"]["from"]["id"]
            response = valid_response_checker(message,options)
            if(response == "invalid"):
                reply("Invalid Response, please try again", from_)
            elif(response == "quit"):
                reply("Quitting from here...", from_)
                exit()
            else:
                responded = True
                return response


def registration(msg, from_):
    global update_id
    reply("HELLO! This is me MELL, your diabetes buddy!", from_)
    reply("To get started we will set up your profile!", from_)
    reply("Are you signing up as a patient or a caregiver?", from_)
    reply("Reply with your option's number.\n1. Patient\n2. Caregiver", from_)
    user_input = get_response(["1","2"])
    reply("Would you like to add your caregiver and/or your registered medical team?", from_)
    reply("Reply with your option's number.\n1. Caregiver\n2. Medical Team\n3. Both Caregiver and Medical", from_)
    user_input = get_response(["1","2","3"])
    reply("Please enter your caregiver's number:", from_)
    user_input = get_response([])
    reply("Are you convidose or smart pillbox user. You can scan your convoid-dose qr code to automatically register your medications or you can manually enter your medication!", from_)


while True:
    updates = bot.get_updates(offset=update_id)
    updates = updates["result"]
    if updates:
        # Just take the last input
        item = updates[-1]
        print("item:",item)
        update_id = item["update_id"]
        try:
            message = item["message"]["text"]
        except:
            message = None
        from_ = item["message"]["from"]["id"]
        decide_mode(message, from_)



