from bot import telegram_chatbot

bot = telegram_chatbot()
update_id = None
from_ = None
message = None

def reply(msg):
    global from_
    bot.send_message(msg, from_)

def decide_mode(msg):
    global update_id
    global from_
    if msg.lower() == "/start":
        registration()
    else:
        reply("Sorry I don't understand you")

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
                reply("Invalid Response, please try again")
            elif(response == "quit"):
                reply("Quitting from here...")
                exit()
            else:
                responded = True
                return response


def registration():
    global update_id
    global from_
    reply("HELLO! This is me MELL, your diabetes buddy!")
    reply("To get started we will set up your profile!")
    reply("Are you signing up as a patient or a caregiver?")
    reply("Reply with your option's number.\n1. Patient\n2. Caregiver")
    user_input = get_response(["1","2"])
    reply("Would you like to add your caregiver and/or your registered medical team?")
    reply("Reply with your option's number.\n1. Caregiver\n2. Medical Team\n3. Both Caregiver and Medical")
    user_input = get_response(["1","2","3"])
    reply("Please enter your caregiver's number:")
    user_input = get_response([])
    reply("Are you convidose or smart pillbox user. You can scan your convoid-dose qr code to automatically register your medications or you can manually enter your medication!")


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
        decide_mode(message)



