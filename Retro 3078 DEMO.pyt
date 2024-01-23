import sys

def start():
    print("Welcome to Retro 3078! This world is based on a dream I had once where I woke up in the future. Let's see where this story takes us...")
    print("Rules and Notes: 1. Type your responses exactly as shown 2. Responses are not case sensitive 3. None of your actions are final, so explore freely! 4. Please enjoy the game and story.")
    print("Rated 13+ due to mild violence and mature ideas. Please keep that in mind as you play.")
    print("This game was programed using the Python lanuage on Visual Studio Code. Retro 3078 does not only take place in 3078, it also takes place in 3082.")
    print("Type 'Begin' to start")

    action = input("> ")
    if action == "Begin":
        game()
    else:
        begin()

def begin():
    print("Do you even want to play?")
    print("Well you are already here so lets try again.")
    print("Type 'Begin' to start the story, no second chances!")

    action = input("> ")
    if action == "Begin":
        game()
    else:
        print("Ok then.")
        ending("Ending achieved: End it before it starts.")


def Victory(reason):
    print(reason)
    print("Congrats! You Win!")
    sys.exit()

def game_over(reason):
    print(reason)
    print("Game Over!")
    sys.exit()

def ending(reason):
    print(reason)
    print("The End.")
    sys.exit()

def partners_in_arms():
    print("You explain how they were friends of yours when you were all children and they moved here before everything that went down.")
    print("Josh and Alex wake up and ask what was going on. You explain that they had been programing their lives out. As you explain, you can tell that memories were comming back to them.")
    print("The person thanks you for the explination and goes into another room.")
    demo_end()

def game():
    print("You get off your plane at the airport, as you walk to the exit, you see several security guards wearing headphones.")
    print("You reach the exit but a security guard stops you and tells you to wait for an important anouncement.")
    print("What do you do? (Type 'wait' or 'run')")
    
    action = input("> ")
    
    if action == "wait":
        captured()
    elif action == "run":
        escaped()
    else:
        captured2()
        
def captured():
    print("You stay and wait. The security guard says that the prestigous mayor is going to be on the PA any second.")
    print("You hear a horrible noise and fall unconcious...")
    print("What do you do? (type 'wake up' or 'sleep peacefully')")
    
    action = input("> ")
    
    if action == "sleep peacefully":
        game_over("You decide not to resist. You have allowed yourself to be captured indefinetly.")
    elif action == "wake up":
        your_room()
    else:
        game_over("Because of your indesiveness, you never get the chance to try to wake up. You were captured indefinetly.")

def captured2():
    print("Your indeciciveness prompts you to wait and you hear a horrible noise and fall unconcious...")
    print("What do you do? (type 'wake up' or 'sleep peacefully')")
    
    action = input("> ")
    
    if action == "sleep peacefully":
        game_over("You decide not to resist. You have allowed yourself to be captured indefinetly.")
    elif action == "wake up":
        your_room()
    else:
        game_over("Because of your indesiveness, you never get the chance to try to wake up. You were captured indefinetly.")

def your_room():
    print("You resist the urge to sleep and force yourself awake. You find yourself in a room like your own")
    print("You notice you are in front of a computer screen making a game in serpaint. You check the code and name of the programe: Retro 3078.pyt")
    print("You scan the code and see yourself making the code of yourself!")
    print("Armed with this knoledge, you attempt to alter the code to the best ending. But you fail.")
    print("What next? (type 'try again', 'explore', or 'reset')")

    action = input("> ")

    if action == "try again":
        game_over("You keep going at the code but can't seem to get it right. In frustration you slam your fist down on the keyboard, altering the code. In doing so, the simulation corrupts, you scream and are deleted forever. Turns out dying in the game means dying in real life!")
    elif action == "explore":
        explore()
    elif action == "reset":
        print("You reset the code back to the start of the simulation. You feel weird and feel your memories being erased... You wake up again on the plane as it lands at the airport.")
        game()
    else:
        game_over("You are lost in thought, in your thought, you slam your fist down on the keyboard, altering the code. In doing so, the simulation corrupts, you scream and are deleted forever. Turns out dying in the game means dying in real life!")

def explore():
    print("You wander around the room looking for clues or ways to alter the code for the better.")
    print("As you search the room, you find a door, calender with the year 3082 , and a plate of apple slices.")
    print("What do you investigate? (type 'door', or 'apple slices')")

    action = input("> ")

    if action == "apple slices":
        print("You look at the apple slices on your PC, there is a note that says 'Dont forget to eat healthy!  -Susan'")
        print("You grab one and take a bite, after doing this, you realize how hungry you are and eat half of them in a minute.")
        print("You hear an electronic beep and see that a calorie intake for the day number increased.")
        print("You decide to explore the door.")
        print("You go to the door, it has a family photo on it quite like your own.")
        print("You turn the knob and push. Nothing happens...")
        print("Confused, you check the code and realize you need to pull open the door.")
        print("You pull open the door and you open to a hallway like your own.")
        hallway()
    elif action == "door":
        print("You go to the door, it has a family photo on it quite like your own.")
        print("You turn the knob and push. Nothing happens...")
        print("Confused, you check the code and realize you need to pull open the door.")
        print("You pull open the door and you open to a hallway like your own.")
        hallway()
    else:
        print("You dont know what to do so you check the code again.")
        print("You find out that you should end up in the hallway either way so you go and poen the door and enter the hallway.")
        hallway()

def hallway():
    print("You go down the hallway and find a person quite like your mother there.")
    print("'How is the new game going my dear' she asks.")
    print("How do you respond? (type 'Where am I?', 'Its going well.', 'You know Im programing myself?', 'How did I get here?', or 'Who are you?')")

    action = input("> ")

    if action == "Where an I?":
        print("'This is your home. You know this silly!'")
        mother_questioning()

    elif action == "Its going well.":
        print ("'Thats good to hear!'")
        mother_questioning()

    elif action == "You know Im programing myself?":
        print("'Ha Ha Liam, Very funny.'")
        mother_questioning()

    elif action == "How did I get here?":
        print("'You got off the bus from school remember?'")
        mother_questioning()

    elif action == "Who are you?":
        print("'What do you mean who am I? I am your mother!'")
        mother_questioning()

    else:
        print("'Do you have anything you really need to ask me?'")
        mother_questioning()

def mother_questioning():
    print("'Is there anything else dear?' (type 'Where am I?', 'Its going well.', 'You know Im programing myself?', 'How did I get here?', 'Who are you?', or 'Nothing else.')")

    action = input("> ")

    if action == "Where an I?":
        print("'This is your home. You know this silly!'")
        mother_questioning()
    elif action == "Its going well.":
        print ("'Thats good to hear!'")
        mother_questioning()
    elif action == "You know Im programing myself?":
        print("'Ha Ha Liam, Very funny.'")
        mother_questioning()
    elif action == "How did I get here?":
        print("'You got off the bus from school remember?'")
        mother_questioning()
    elif action == "Who are you?":
        print("'What do you mean who am I? I am your mother!'")
        mother_questioning()
    elif action == "Nothing else.":
        print("'You will adress me as 'mom' at least young man.'")
        print("'Sorry mom' you say reluctently.")
        outside()
    else:
        print("'Do you have anything you really need to ask me? If not, just say so. Okay?'")
        mother_questioning
    

def escaped():
    print("You take off running as you hear a horrible noise behind you.")
    print("You clamp your ears shut and keep running untill you can't hear the noise anymore.")
    print("You find yourself at an intersection. 'LEFT: City, RIGHT: Forest' (type 'Left' or 'Right')")
    
    action = input("> ")
    
    if action == "Left":
        escaped_city()
    elif action == "Right":
        escaped_forest()
    else:
        game_over("You ponder the options but cannot decide. In your hesitation, the opportunity is lost. Guards find and capture you by playing the noise in your ear. You have no chance of escape.")

def escaped_city():
    print("You reach the city safely but have no idea where to go next...")
    print("You wander the city lost and alone.")
    print("You are grabbed and pulled inside a borded up home and are held at gunpoint.")
    print("A man says 'What is the best way to live your life?' (type 'under a strong ruler' or 'as a free person')")

    action = input("> ")

    if action == "under a strong ruler":
        game_over("The man gets angry and shoots you. Maybe freedom is better afterall...")
    elif action == "as a free person":
        refugee()
    else:
        game_over("Failing to answer his question, the man shoots you. 'Next time answer the dang question'")

def escaped_forest():
    print("You run towards the forest and you run for a few hours untill you are exhausted. You find shelter under a large tree and fall asleep.")
    print("You wake up feeling rested but lost, your memory of the past day is fuzzy.")
    print("You wander through the forest and you find a cabin in a clearing ahead.")
    print("What do you do? (type 'approach cabin' or 'keep wandering')")

    action = input("> ")
    if action == "approach cabin":
        cabin()
    elif action == "keep wandering":
        game_over("You decide to keep your distance and continue wandering through the forest. The sun begins to set and it gets harder to see. You trip over a root and tumble down a slope, you bang your head very hard at the bottom. You dont wake up.")
    else:
        print("You fail to decide and its getting dark. Your choice is forced")
        cabin()
    
def cabin():
    print("You approach the cabin cautiously and knock on the door. It falls open and turns to dust.")
    print("Inside you find it rather cozy and well stocked with food and supplies. You decide to rest and regain your strength here.")
    print("After resting, you realize you need a plan. Where will you go from here? (type 'go to city' or 'explore woods')")

    action = input("> ")
    if action == "go to city":
        escaped_city()
    elif action == "explore woods":
        explore_woods()
    else:
        print("You have no idea where to go next so you just start walking.")
        explore_woods()

def refugee():
    print("The man lowers his gun and tells you to stay as long as you need. You have found shelter for now...")
    print("You realize there is more to this than you thought. You decide to ask the man more about the situation.")
    print("What do you ask? (type 'What was the noise at the airport?' or 'Why are you helping me?' or 'What is happening here?')")

    action = input("> ")

    if action == "What was the noise at the airport?":
        print("The man sighs and says 'It was the sound of our freedom dying. The mayor has been taking control bit by bit for years. That noise was them using a new weapon to keep us under his controll. He calls it the 'Noise of Obedience'.")
        questions()
    elif action == "Why are you helping me?":
        print("Im the leader of the resistance, we accept civilians who are caught in the crossfire. I help because freedom is worth fighting for, even if it seems hopeless sometimes.")
        questions()
    elif action == "What is happening here?":
        print("A civil war, thats what.")
        questions()
    else:
        game_over("Your hesitance to ask anything makes the leader suspicious. He shoots you before you can react. 'I can't risk you being a spy, goodbye.'")

def questions():
    print("The leader is patient and kind. 'Ask whatever you need, we're all in this together now.'")
    print("What else do you need to know? (type 'What was the noise at the airport?' or 'Why are you helping me?' or 'What is happening here?' or 'Nothing else')")

    action = input("> ")

    if action == "What was the noise at the airport?":
        print("The man sighs and says 'It was the sound of our freedom dying. The mayor has been taking control bit by bit for years. That noise was them using a new weapon to keep us under his controll. He calls it the 'Noise of Obedience'.")
        questions()
    elif action == "Why are you helping me?":
        print("Im the leader of the resistance, we accept civilians who are caught in the crossfire. I help because freedom is worth fighting for, even if it seems hopeless sometimes.")
        questions()
    elif action == "What is happening here?":
        print("A civil war, thats what.")
        questions()
    elif action == "Nothing else":
        refugee_acceptance()
    else:
        print("That is not something I can answer.")
        questions()

def refugee_acceptance():
    print("You thank the man for answering your question and helpiing you. You decide you want to help the resistance in their fight.")
    print("The man smiles, 'We could use all the help we can get. Welcome to the resistance, what skills can you offer us?'")
    print("What do you tell the man? (type 'medical skills', 'tech skills', or 'fighting skills')")

    action = input("> ")
    if action == "medical skills":
        medical_prof()
    elif action == "tech skills":
        tech_prof()
    elif action == "fighting skills":
        fighting_prof()
    else:
        print("'So you have none of the main skills we need?' the man said, 'you shall be a cook!") 
        cooking_learn()

def medical_prof():
    print("You tell the resistance leader that you were a doctor for 10 years before arriving.")
    print("He says that he is pleased to be able to have such a skilled medical professional on his side.")
    print("You are told to enter the main chamber with the rest of the medical team. When you enter, you see about 40 people laying on sleeping bags with varyous notes alerting to why they are there.")
    print("A woman comes up to you and asks 'Are you a new medical member?' You respond by saying yes and she takes you to a set of paitents.")
    print("She says that she is the medical leader of the resistance and need me to put the people here in casts where needed. She jestures at the people infront of you.")
    print("Using the resources provided, you make each of the paitents casts and they are able to leave with crutches.")
    print("The head medic comes and congradulates you for your quick work and gives you two options on your nesxt task.")
    print("'You can either pass soup around from the kitchens or treat our cyborgs of a software virus.")
    print("Which task will you take on? (Type 'Soup' or 'Software')")

    action = input("> ")

    if action == "Soup":
        soup_passer()
    elif action == "Software":
        software_fixer()
    else:
        print("So you dont want either of them? Ok then...")
        print("We will put you on the field recovery when we do the frontal assult on the courthome behind the city hall.")
        field_recovery()


def soup_passer():
    print("You say that you want to pass soup to the sick. The medical leader says that you could start right away.")
    ending("Ending Achieved: Soup Passer.")

def software_fixer():
    print("You tell the medical leader that you want to fix the virus on the cyborgs. She says that you can start right away.")
    ending("Ending Achieved: Tech Savvy Medic.")

def field_recovery():
    print("You are instructed to work as the assistant head medic untill the assult on the courthome.")
    print("Two years later...")
    print("The day of the assult...")
    print("You are taken to the front lines and you are left as head of field recovery team. You are given a chart with a map on it.")
    print("Your task is to get the people to the right medical tent for treatment.")
    print("15 minutes after the assult begins...")
    print("The first few people start arriving to the medical point.")
    print("TENT MAP: 1 = Bullet and puncture wounds. 2 = Broken bones, torn ligaments, and dislocated joints. 3 = Major injuries. 4 = Spontaniuos infection. 5 = Missing body parts.")
    print("You need to send each paitent to the right tent by typing the number of the tent they need to go to.")
    field_recovery_start()

def field_recovery_start():
    ans=0
    
    print("A paitent comes in missing an arm.")
    question = input("Where do you send them? > ")
    if question == "5":
        ans += 1
        print("You send them to the #" + question + " tent")
    else:
        print("You send them to the #" + question + " tent")

    print("A paitent comes in with a virus.")
    question = input("Where do you send them? > ")
    if question == "4":
        ans += 1
        print("You send them to the #" + question + " tent")
    else:
        print("You send them to the #" + question + " tent")
        
    print("A paitent comes in with their gun as crutches.")
    question = input("Where do you send them? > ")
    if question == "2":
        ans += 1
        print("You send them to the #" + question + " tent")
    else:
        print("You send them to the #" + question + " tent")

    print("A paitent comes in with a massive gash across their face.")
    question = input("Where do you send them? > ")
    if question == "3":
        ans += 1
        print("You send them to the #" + question + " tent")
    else:
        print("You send them to the #" + question + " tent")

    print("A paitent comes in with their arm bending backwards.")
    question = input("Where do you send them? > ")
    if question == "2":
        ans += 1
        print("You send them to the #" + question + " tent")
    else:
        print("You send them to the #" + question + " tent")

    print("A paitent comes in with a 129 degree fever.")
    question = input("Where do you send them? > ")
    if question == "4":
        ans += 1
        print("You send them to the #" + question + " tent")
    else:
        print("You send them to the #" + question + " tent")

    print("A paitent comes in missing half of their legs.")
    question = input("Where do you send them? > ")
    if question == "5":
        ans += 1
        print("You send them to the #" + question + " tent")
    elif question == "3":
        ans += 1
        print("You send them to the #" + question + " tent")
    else:
        print("You send them to the #" + question + " tent")

    print("A paitent comes in with about 40 small holes in their body.")
    question = input("Where do you send them? > ")
    if question == "1":
        ans += 1
        print("You send them to the #" + question + " tent")
    else:
        print("You send them to the #" + question + " tent")

    print("A paitent comes in with their skull somewhat showing.")
    question = input("Where do you send them? > ")
    if question == "3":
        ans += 1
        print("You send them to the #" + question + " tent")
    else:
        print("You send them to the #" + question + " tent")

    print("A paitent comes in on fire.")
    question = input("Where do you send them? > ")
    if question == "3":
        ans += 1
        print("You send them to the #" + question + " tent")
    else:
        print("You send them to the #" + question + " tent")
    
    print("You got " + str(ans) + " out of 10 tent locations correct.")
    print("The fight is over. The resistance lost and most of the fighters are dead.")
    print("The new leader of the now failing resistance is the medical leader.")
    
    if ans == 10:
        print("The new leader of the resistance gives you a medal and the title of 'Leader of the Medical Division'.")
        Victory("Ending Achieved: Ultimate Field Recovery.")
    elif ans <= 9 and ans >= 8:
        print("The new leader of the resistance gives you the title of 'Co-Leader of the Medical Division'.")
        ending("Ending Achieved: Great Field Recovery.")
    elif ans <= 7 and ans >= 5:
        print("The new Leader has you stay in the field recovery team as Chief Executive.")
        ending("Ending Achieved: Chief Executive Field Recovery.")
    else:
        print("You were fired from the field recovery team.")
        game_over("You Failed.")


def tech_prof():
    print("You tell the resistance leader that you practaced hacking in your spare time since you were 9 years old. He takes you into a darkened room with 19 other people.")
    print("'This is the hacking division, AKA the tech division. You sit here.' The man said. 'You are very lucky, this is the last slot avalable.'")
    print("The man explains the use of the computer in front of you and gives you 2 things you can do. 'You can either hack their main frame to get intel or hack their secuity to make it harder for us to be noticed.")
    print("Which task will you take on? (Type 'Intel' or 'Security')")
    demo_end()

def fighting_prof():
    print("You tell the resistance leader that you got a black belt in karate and did boxing in high school. He said that unless someone gets closer that 40 feet to you that wont matter.")
    print("The resistance leader takes you into the largest room, this room was transformed into a shooting range.")
    print("You are given the choice of three guns, a sniper, an assult rifle, and a minigun.")
    print("The resistance informs you that sniper training is 1 year, AR training is 6 months, and minigun training was 2 years.")
    print("Which firearm course do you take? (Type 'Sniper', 'AR', or 'Minigun')")
    demo_end()

def cooking_learn():
    print("The man takes you into the kitchen which has been expanded to make a massive resturant scale kitchen.")
    print("You are given an apiron and are given to an instructor.")
    print("You do very well in your first lesson and are given two station choices. Making soup for the sick or making pizza for the tech division.")
    print("Which station do you pick? (Type 'Soup' or 'Pizza')")
    demo_end()

def explore_woods():
    print("You wander deeper into the forest, keeping the cabin in sight behind you. The trees grow thicker.")
    print("After a few hours you realize you are lost. Night is falling and you need to find shelter.")
    print("You are presented with 2 options: a familiar looking tree and beneth a small overhang.")
    print("Where will you spend the night? (type 'tree' or 'overhang')")

    action = input("> ")
    if action == "tree":
        tree()
    elif action == "overhang":
        overhang()
    else:
        game_over("You decide to sleep under some leaves, unfortunately, after you fall asleep, a pack of wolves find you and kill you.")


def tree():
    print("You climb high into the familiar looking tree and find a sturdy branch to sleep on.")
    print("When you wake, you notice the airport from hence you arived in this twisted place in the distance. Perhaps exploring there will reveal clues about the current situation.")
    print("You think that there may be guards there though and it could be dangerous. What do you do? (type 'explore airport', 'stay in tree', or 'go to city')")

    action = input("> ")
    if action == "explore airport":
        print("You climb carefully down the tree and make your way towards the airport. As you get closer you can see guards patrolling the perimeter.")
        print("How will you get past the guards? (type 'sneak past', 'distract guards', or 'wait for nightfall')")

        action = input("> ")
        if action == "sneak past":
            game_over("You tried to sneak past the guards but weren't stealthy enough. They spotted and captured you before you could escape.")
        elif action == "distract guards":
            print("You throw rocks in the opposite direction to draw the guards away. With their attention diverted, you slip past unseen and begin exploring the airport.")
            airport()
        elif action == "wait for nightfall":
            game_over("You waited until nightfall, but the guards had heightened security at night. You were spotted and captured before you could escape.")
        else:
            game_over("You decide the risk is too great and choose to try to escape to the city, but during the escape a guard noticed and captured you.")
    elif action == "stay in tree":
        game_over("You decide to stay in the tree for a few days. Eventually without food or water you pass out and fall from the tree, breaking your neck. Look on the bright side, you would have lost even if you hadnt broke your neck as the guards would have captured you or put you out of your misery.")
    else:
        game_over("You cant decide and forget to hang on to the tree, you fall from the tree, breaking your neck. Look on the bright side, you would have lost even if you hadnt broke your neck as the guards would have captured you or put you out of your misery.")

def overhang():
    print("You crawl under the small overhang and huddle in the corner for warmth.")
    print("It is very uncomfortable and you don't sleep well, constantly worrying about wild animals discovering your hiding place.")
    print("In the morning, you leave the overhang and need to do something (type 'climb tree', 'explore area' or 'try to get sleep')")

    action = input("> ")
    if action == "climb tree":
        print("You try to climb the tree, you attempts were very pathetic.")
        game_over("Eventually you get a good 15-20 feet above the ground when you half fall asleep. You fall to the ground and guards from the airport capture you.")
    elif action == "explore area":
        print("You walk around sleepily untill you find the airport you came from.")
        game_over("Because of your fatigue, you fail to notice 5 guards that are guarding the perimeter. They capture you with ease.")
    elif action == "try to get sleep":
        print("You walk over to the tree and lay down. You fall asleep instantly.")
        print("You wake up at dusk feeling very well rested and ready to move on.")
        print("What is next? (type 'Explore' or 'Stay')")

        action = input("> ")
        if action == "Explore":
            print("You walk around and find the airport you came from and decide to explore it.")
            print("However you dont know when to explore it. When do you try to explore? (Type 'Now' or 'Dawn')")
            action = ("> ")
            if action == "Now":
                game_over("You try to sneak by the guards. However there are too many guards to pass by. You are captured.")
            elif action == "Dawn":
                print("You go back to sleep and wake up at the crack of dawn and there are less guards than the night.")
                print("You sneak past them with ease and enter the airport.")
                airport()
            else:
                game_over("You hesitate and are noticed by the guards who capture imeadietly.")
        elif action == "stay":
            print("You stay beneith the familiar tree for a while, as you sit you begin to remember why the tree was so familiar.")
            print("Your ever growing hunger and thirst is making it fuzzy but you remember sleeping under this tree the first day you were here.")
            print("What should you do now? (type 'Find airport' or 'Go to city')")

            action = input("> ")
            if action == "Find airport":
                print("You get up and look around for the airport you arrived from.")
                print("Once you find it, you sneak past the guards with ease.")
                airport()
            elif action == "Go to city":
                print("You find the intercection that you chose to go to the forest from.")
                print("You go towards the city in the distance.")
                escaped_city()
            else:
                print("In vain of deciding, you choose to go back into the forest and live your life there.")
                ending("Ending achieved: Forest Dweller.")
    else:
        game_over("Your extensive thinking plus your tiredness caused you to pass out. You dont wake back up.")

def airport():
    print("You enter the airport and look around. You no longer had a reason to hide as the airport was completely packed with people.")
    print("You see a security guard usher another like you away from the exit. You hear the security guard mention an important anouncement that was about to be broadcast.")
    print("You need to make a decision before you find out what the noise was from previously! (Type 'Run', 'Stay', or 'Grab the person and go')")

    action = input("> ")
    if action == "Run":
        escaped()
    elif action == "Stay":
        captured()
    elif action == "Grab the person and go":
        companion()
    else:
        captured2()

def companion():
    print("You grab the person and run out the door again, they try to break from you grasp.")
    print("Despite their efforts, you keep your grasp on them very firm and instruct them to cover their ears.")
    print("You cover your ears at the last second as the noise plays once again and you and the person keep running.")
    print("You both only stop running once you no longer hear the noise. The person you grabbed slaps you across the face. 'What is wrong with you!?' he asks.")
    print("What do you say? (type 'Run now, talk later', 'I just saved your skin', 'Shut up and head to the forest', or 'We need to go to the city')")

    action = input("> ")
    if action == "Run now, talk later":
        print("The person you saved agrees and you both run untill you reach the junction.")
        print("He asks you where we went next. What do you say? (type 'To the city' or 'Get cover in the woods')")
        action = input("> ")
        if action == "To the city":
            companion_city()
        elif action == "Get cover in the woods":
            companion_woods()
        else:
            print("'What do you mean you dont know!' The man said. 'FINE, We will go to the woods'")
            companion_woods()
    elif action == "I just saved your skin":
        print("'Saved me from what??' the man asked")
        print("What do you respond with? (Type 'Truth' or 'Lie')")
        if action == "Truth":
            print("You explain everything you know. He apologyzes for not trusting you")
            print("You tell him that there may be help in the city so you both should head there.")
            companion_city()
        elif action == "Lie":
            print("You lie to the person you saved and say you have no clue what was going on.")
            print("You say that you heard the noise every few days and the people that came out were lifeless, like a sleepwalker.")
            print("As you talk, he falls for your lie. You feel bad for lying but are too deep into the lie to back out.")
            print("He said that you both needed to return to your home in the woods.")
            print("What do you say? (type 'Continue with lie' or 'Confess')")
            action = input("> ")
            if action == "Continue with lie":
                companion_woods_lie()
            elif action == "Confess":
                print("You break under the pressure and tell the man you were lying.")
                print("He punches you in the face and runs off.")
                print("You decide to go to the city.")
                escaped_city()
        else:
            print("You both stare at eachother for a few seconds. . .")
            print("Suddenly, the person you saved runs into the woods, you follow close behind.")
            companion_woods()
    elif action == "Shut up and head to the forest":
        companion_woods()
    elif action == "We need to go to the city":
        companion_city()

def companion_city():
    print("You both run to the city and are huddled over to a boarded up home.")
    print("The person you saved recognized the man and pulled you inside. The man who beckoned you both in thanked you for saving the person from the airport and revealed that they were a person that wanted to be part of a resitance that was growing in the town.")
    print("The man says that he would provide you shelter for your help and allow you into any part of the resistance.")
    print("Which resistance division do you join? (You may pick 'medical', 'tech', or 'fighting' ")
    action = input("> ")
    if action == "medical":
        medical_prof()
    elif action == "tech":
        tech_prof()
    elif action == "fighting":
        fighting_prof()

def companion_woods():
    print("You both enter the woods and find the cabin. 'Does someone really live out here!?' the man asks.")
    print("You tell the man you have no clue if someone lives out here. The man suggests you go to the city.")
    print("What do you say? (type 'Go to the city' or 'Go back to the cabin')")
    demo_end()


def companion_woods_lie():
    print("You both enter the woods and find the cabin. 'Is this really where you live!?' the man asks.")
    print("You tell the man that you didnt usually live here but you owned the building. You still feel ashamed for lying.")
    print("You both enter the cabin togeather. The man asks if you had room for two.")
    print("What do you say? (type 'Yes' or 'No')")

    action = input("> ")
    if action == "Yes":
        print("You tell the man that you had room for two and you grab a blanket and a pillow to make a small bed on the floor.")
        print("You ask if he wants to help get wood for the bed.")
        ending("Ending Achieved: Companion life in the woods as a liar.")
    elif action == "No":
        print("You explain that you had no room for two. The man suggests that he build himself a cabin and one for anyone else they saved.")
        print("You still feel bad for lying.")
        ending("Ending Achieved: Refugee camp.")
    


def outside():
    print("You tell the mother figure that you were going to go outside for a while.")
    print("She tells you to have fun and gets back to cooking")
    print("You go outside and see a number of things.")
    print("Where do you go? (type 'Neighbors home', 'Gas station store', 'Playground', 'Post office', 'Police station', or 'Town hall')")

    action = input("> ")

    if action == "Neighbors home":
        print("You walk across the street to an identical home to yours and knock onthe door. You see a familiar friend answer.")
        print("'Hiya Liam!' He said. You respond with 'Whats good Josh?' as you replied as you saw a much shorter person come up to the door and ask Josh who it was.")
        print("'Liam is at the door' Josh said. 'Liam, you remember Alex right?")
        print("What do you say? (type 'Yes' or 'No')")
        action = ("> ")
        if action == "Yes":
            explination()
        elif action == "No":
            print("Josh filles you in about Alex.")
            explination()
        else:
            print("What was that?")
            re_ask()
    elif action == "Gas station store":
        print("You walk to the neighborhood Gas station and store and enter. You hear the gas station worker welcome you brightly.")
        print("You decide to buy something. What do you buy? (You may buy one drink and one food!)")
        print("Items you can buy: Coke. Pepsi. Sprite. Water. Potato Chips. Apple. Hot dog. Candy. (You will buy multible items like this (Water.Apple))")

        action = input("> ")
        if action == "Coke":
            print("You bought the coke.")
            print("You finished it before you left the store.")
            gone_to_store()
        elif action == "Pepsi":
            print("You bought the pepsi.")
            print("You finished it before you left the store.")
            gone_to_store()
        elif action == "Sprite":
            print("You bought the sprite.")
            print("You finished it before you left the store.")
            gone_to_store()
        elif action == "Water":
            print("You bought the water.")
            print("You finished it before you left the store.")
            gone_to_store()
        elif action == "Potato Chips":
            print("You bought the potato chips.")
            print("You finished them before you left the store.")
            gone_to_store()
        elif action == "Apple":
            print("You bought the apple.")
            print("You finished it before you left the store.")
            gone_to_store()
        elif action == "Hot dog":
            print("You bought the hot dog.")
            print("You finished it before you left the store.")
            gone_to_store()
        elif action == "Candy":
            print("You bought the candy.")
            print("You finished it before you left the store.")
            gone_to_store()
        elif action == "Coke.Potato Chips":
            print("You bought the coke and potato chips.")
            print("You finished them before you left the store.")
            gone_to_store()
        elif action == "Coke.Apple":
            print("You bought the coke and apple.")
            print("You finished them before you left the store.")
            gone_to_store()
        elif action == "Coke.Hot dog":
            print("You bought the coke and hot dog.")
            print("You finished them before you left the store.")
            gone_to_store()
        elif action == "Coke.Candy":
            print("You bought the coke and candy.")
            print("You finished them before you left the store.")
            gone_to_store()
        elif action == "Pepsi.Potato Chips":
            print("You bought the pepsi and potato chips.")
            print("You finished them before you left the store.")
            gone_to_store()
        elif action == "Pepsi.Apple":
            print("You bought the pepsi and apple.")
            print("You finished them before you left the store.")
            gone_to_store()
        elif action == "Pepsi.Hot dog":
            print("You bought the pepsi and hot dog.")
            print("You finished them before you left the store.")
            gone_to_store()
        elif action == "Pepsi.Candy":
            print("You bought the pepsi and candy.")
            print("You finished them before you left the store.")
            gone_to_store()
        elif action == "Sprite.Potato Chips":
            print("You bought the sprite and potato chips.")
            print("You finished them before you left the store.")
            gone_to_store()
        elif action == "Sprite.Apple":
            print("You bought the sprite and apple.")
            print("You finished them before you left the store.")
            gone_to_store()
        elif action == "Sprite.Hot dog":
            print("You bought the sprite and hot dog.")
            print("You finished them before you left the store.")
            gone_to_store()
        elif action == "Sprite.Candy":
            print("You bought the sprite and candy.")
            print("You finished them before you left the store.")
            gone_to_store()
        elif action == "Water.Potato Chips":
            print("You bought the water and potato chips.")
            print("You finished them before you left the store.")
            gone_to_store()
        elif action == "Water.Apple":
            print("You bought the water and apple.")
            print("You finished them before you left the store.")
            gone_to_store()
            print("Your mother would be proud!")
        elif action == "Water.Hot dog":
            print("You bought the water and hot dog.")
            print("You finished them before you left the store.")
            gone_to_store()
        elif action == "Water.Candy":
            print("You bought the water and candy.")
            print("You finished them before you left the store.")
            gone_to_store()
        

def re_ask():
    action = input("> ")
    if action == "Yes":
            explination()
    elif action == "No":
            print("Josh filles you in about Alex.")
            explination()
    else:
            print("What was that?")
            re_ask()

def explination():
    print("You explain your situation from the begining. When you are done, you ask if they have been making a game.")
    print("They both respond with 'Yes' and you know that they have programing their lives and needed to wake up.")
    print("You tell them both to wake up and pinch them both on the arm.")
    print("They both fall to the ground asleep. One minute later they both wake up, confused.")
    print("Suddenly you and your friends are grabbed and pulled into a sewer. A man asks you how you woke them up.")
    partners_in_arms()

def gone_to_store():
     print("Where do you go? (type 'Neighbors home', 'Playground', 'Post office', 'Police station', or 'Town hall')")
     demo_end()
           


def demo_end():
    print("You are at the end of the Retro 3078 demo.")
    print("To play the demo again, type 'play again'.")
    print("To exit the demo, type 'exit'.")

    action = input("> ")
    if action == "play again":
        start()
    elif action == "exit":
        ending("Demo Finished!")
    else:
        print("What was that?")
        demo_end()
        
start()