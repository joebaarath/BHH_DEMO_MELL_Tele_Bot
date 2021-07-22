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
    if msg == None:
        return
    elif msg.lower() == "/start":
        registration()
    else:
        reply("Sorry I don't understand you")

def valid_response_checker(user_input, options):
    if user_input == None:
        return None
    elif user_input.lower() == "/quit" or user_input.lower() == "quit":
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
def reminder():
    global update_id
    global from_
    reply("Hey John! It's time to take")
    reply("1 - English\n2 - 中文\n3 - Melayu\n4 - தமிழ்")
    user_input = get_response(["1"])

def registration():
    global update_id
    global from_
    reply("Please select your language preference by entering the corresponding number\n\n请通过输入相应的数字来选择您的语言偏好\n\nPilih pilihan bahasa anda dengan memasukkan nombor yang sesuai\n\nதொடர்புடைய எண்ணை உள்ளிட்டு உங்கள் மொழி விருப்பத்தைத் தேர்ந்தெடுக்கவும்")
    reply("1 - English\n2 - 中文\n3 - Melayu\n4 - தமிழ்")
    user_input = get_response(["1"])
    reply("HELLO! This is me MELL, your diabetes buddy!")
    reply("To get started we will set up your profile!")
    reply("Are you signing up as a patient or a caregiver?")
    reply("Reply with your option's number:\n1 - Patient\n2 - Caregiver")
    user_input = get_response(["1","2"])
    reply("Would you like to add your caregiver and/or your registered medical team?")
    reply("Reply with your option's number:\n1 - Caregiver\n2 - Medical Team\n3 - Both Caregiver and Medical")
    user_input = get_response(["1","2","3"])
    reply("Please enter your caregiver's name:")
    user_input = get_response([])
    caregiver_name = user_input
    reply("Please enter your caregiver's phone number:")
    user_input = get_response([])
    reply("Are you currently enrolled with a Multi-Dose Medication Management (MMM) user (E.g. Convidose)?")
    reply("Reply with your option's number:\n1 - Yes\n2 - No")
    user_input = get_response([])
    reply("You can take a photo of your convoid-dose qr code to automatically register your medications")
    reply("Please upload a photo of your qr code with us")
    user_input = get_response([])
    reply("The following Medication are registered:")
    reply("*Metformin* 500 mg to be taken 3 times daily after meals")
    ## DISPLAY PHOTO
    reply("Would you like to manually add other medications?")
    reply("Reply with your option's number:\n1 - Yes\n2 - No")
    user_input = get_response([])
    reply("Please enter one of your medication's detail at a time in the following format seperated with a comma: \n\n*Medication_Name*,*Optional_Medication_Alias*,*Dosage_with_units*,*Frequency_per_day*,*Before\After (meals)*\n\nE.g. Sulfonylureas,Small White Oval Pill,1 mg,3,before")
    reply("Please enter one of your medication's detail:")
    user_input = get_response([])
    temp_medication = user_input.split(',')
    reply("Do you have a photo of " + temp_medication[0] +"?\nThis photo can be used to assist with reminding you which medication to take")
    reply("Reply with your option's number:\n1 - Yes\n2 - No")
    user_input = get_response([])
    reply("Please upload or take a photo of " + temp_medication[0])
    user_input = get_response([])
    reply("The following Medication have been registered:")
    temp_med_response = "*" + temp_medication[1] + "* (*" + temp_medication[0] + "*) " + temp_medication[2] + " to be taken " + temp_medication[3] + " times daily " + temp_medication[4] + " meals"
    reply(temp_med_response)
    ## Display photo of medication
    reply("Do you have any other medications to add?")
    reply("Reply with your option's number:\n1 - Yes\n2 - No")
    user_input = get_response([])
    reply("Here's your complete list of registered medications:")
    reply("*Metformin* 500 mg to be taken 3 times daily after meals\n" + temp_med_response)
    reply("Reply with your option's number:\n1 - Confirm Medication Details\n2 - Modify Medication Details")
    user_input = get_response([])
    reply("Are you a smart pillbox user?")
    reply("Reply with your option's number:\n1 - Yes\n2 - No")
    user_input = get_response([])
    reply("You may register smart pillbox integration by clicking on the link:\nhttp://MELLDiabetesBot.com.sg/intergationAPI=123")
    reply("Please return back to whatsapp and complete registration of MELL, once your smart pillbox integeration is completed")
    reply("To estimate medication timings, please let us know your meal timings")
    reply("What time do you usually have breakfast? e.g. 0800")
    user_input = get_response([])
    reply("What time do you usually have lunch? e.g. 1200")
    user_input = get_response([])
    reply("What time do you usually have dinner? e.g. 1700")
    user_input = get_response([])
    reply("How would you like to be reminded?")
    reply("Reply with your option's number:\n1 - Remind Medication Schedule in the Morning\n2 - Remind 30 Minutes Before Meal Timing\n3 - Remind at Medication Timing\n4 - Set Custom Time Reminder\n5 - Do not set reminders. I will manually update MELL\n6 - Send reminder 1 hour after medication timing, if I have missed manually updating MELL")
    user_input = get_response([])
    reply("The following is your daily medication schedule:")
    reply("*Small White Oval Pill* (*Sulfonylureas*) 1 mg at 0730\n*Metformin* 500 mg at 0800\n*Small White Oval Pill* (*Sulfonylureas*) 1 mg at 1130\n*Metformin* 500 mg at 1200\n*Small White Oval Pill* (*Sulfonylureas*) 1 mg at 1630\n*Metformin* 500 mg at 1700")
    reply("Reply with your option's number:\n1 - Confirm Medication Schedule\n2 - Modify Medication Schedule")
    user_input = get_response([])
    reply("Registration Complete! Yay!")
    reply("Now you can just sit back and relax. I will be assisting you with your medicine from now on!")
    reply("You can ask me anything about your medication or about diabetes")
    reply("Remember that you gain points by building a streak of taking your medication on time!")
    reply(caregiver_name + ", your medical team and I, will be looking out for you!")
    reply("Catch you later!")

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



