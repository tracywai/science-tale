import time

# how users may respond
yes = ["yes", "Yes", "Y", "y"]
no = ["no", "No", "N", "n"]
answer_A = ["A", "a"]
answer_B = ["B", "b"]
answer_C = ["C", "c"]

# start
def opener():
    name = input("What is your name?")
    print("Hi " + name + ", welcome to Cat and Fish's Birthday Surprise! Let\'s join their adventure.")
    time.sleep(1.5)

def scene_one():
    print("""\n Best friends Cat and Fish share the same birthday, and today is the day! They wonder how they\'re going to spend the day together...
    and they decide that they will surprise each other in their homes!
    \"I hope Fish will be ready for the best surprise ever!\" Cat says.
    \"I can’t wait to see the look on his face!\" Fish exclaims.""")
    print("\nCat dives into the pond to find Fish. On the other side, Fish jumps out of the water determined to visit Cat. \n And so their adventures begin!\n")
scene_one()

def start_again():
    answer_4 = input("Would you like to embark on this adventure again? Type yes to continue playing")
    if answer_4 in yes:
        opener()
    
    if answer_4 in no:
        exit()

def outro():
    print("Final Learning check, " + name + "! What are all the facts from today?")
    print("""
    1. Land animals can’t breathe underwater without bringing oxygen with them (scuba diving or snorkelling)
    2. Some aquatic animals, like Fish, can only breathe underwater using gills, that separate the oxygen from the water.
    3. Even if land animals bring oxygen underwater with them, they will eventually need to resurface to get more oxygen and to drink water.
    4. Aquatic animals are best suited for life underwater!
    5. Land animals are best suited for life on land! \n""")
    print("Thank you for celebrating Cat and Fish\'s birthday! See you next time!\n")
    start_again()

def scene_eight():
    print("""\"WAIT! How about a volleyball match! Over the pond! You can stay in the water while I stay on land.
    That way, I don\'t need to snorkel or hold my breath, and you can take in the oxygen from the water.” says Cat. \n
    \"Great idea! If you get thirsty or tired, you can have a drink of water without needing to leave the pond!
    And I won\'t be confined to a really small bowl that I cannot play in!\" Fish says.\n""")
    time.sleep(1)
    print("""For the rest of the day, Cat and Fish go on to play volleyball with the net at the edge of the pond.
    Fish smiles as she leaps out of the water to bounce the ball back over the net to Cat, who is on land. The two have lots of fun!\n""")
    time.sleep(1)
    print("""After the volleyball match, Cat and Fish part ways to their own homes-- Cat on land, and Fish in the water.\n
    \"See you tomorrow, Cat! I demand a rematch!\"
    \"Bye, Fish!\"\n""")
    time.sleep(2)
    print("The End!")
    outro()

def scene_seven():
    print("""\"Well, we can\'t lose hope. It’s not too late!\"
    Cat and Fish brainstorm and try out ideas for how they can spend the rest of the day together, despite needing different environments to breathe in.\n""")
    answer_3 = input("""What are possible ideas that allow Cat and Fish to play together?\n

    A. Cat and Fish can play volleyball along the shore.
    B. Cat and fish can watch a movie by the pond.
    C. Both ideas will work because Cat and Fish are in their natural environments. They are able to access oxygen easily.""")
    if answer_3 in answer_A:
        print("Incorrect. Try again!")
        scene_seven()
    
    elif answer_3 in answer_B:
        print("Incorrect. Try again!")
        scene_seven()

    elif answer_3 in answer_C:
        print("Yes, correct! Both ideas will work because Cat can stay on land and Fish in the water.")
        scene_eight()

    else:
        print("Sorry, I don\'t understand. Try again!")
        scene_seven()

def scene_six():
    print("""When they reach the pond, he finds Cat, who is still snorkelling!
    \"Hey Cat, is that you?\" Fish asks.""")
    time.sleep(1)
    print("""Cat’s head pops out of the water.
    \"I was looking for you, Fish, why are you on land?\" Cat says.
    \"I was going to surprise you for our birthday!\ Fish replies.""")
    time.sleep(1)
    print("""Fish says, \"I wish we could spend our birthdays together, but I can\'t last too long out of my pond. My gills only work underwater, and this glass is too small for me to swim in.\"
    \"Same, I tried snorkelling, but I got thirsty really quickly and I couldn\'t drink underwater! My lungs are made to breathe on land,\" Cat replies.""")
    time.sleep(1)
    scene_seven()

def scene_five():
    print("Fish\'s eyes light up, and he jumps into the glass.")
    time.sleep(1.5)
    print("""Beaver says, \"You were supposed to drink the water!\"
    \"No, Beaver, I need water to breathe through my gills.\" he sighs. \"I miss my home.\"

    \"I\'ll drop you off at your pond if you want,\" Beaver says.
    \"Yes, please!\"\n""")
    time.sleep(1.5)
    print("""Learning check!\n
    Remember that Fish cannot use water effectively outside of his pond because there is no oxygen to dissolve through his gills.
    Just like we would have trouble breathing if our air was too polluted, if Fish\'s pond is too polluted, she wouldn\'t be able to breathe because there is less oxygen to filter!
    That is why it is important to keep our environment clean - so that Cat and Fish can both breathe in our natural habitats!""")
    scene_six()


def scene_four():
    print("""\"Hey Cat, I know you don\'t have gills, and we don\'t have an oxygen tank nearby, but there\'s bamboo over there that you could use as a breathing tube!” suggests Snail.
    \"Great idea! Let\'s try it!\"\n""")
    time.sleep(1.5)
    print("""\"Whew! Swimming is tiring...\" Cat thinks to himself as he snorkels.\n
    Meanwhile, the sun is blazing down on Fish, who is hopping towards Cat\'s home. Soon, Fish is having trouble breathing and becomes tired.
    \"I need water,\" she says. \"Where can I find some?\"""")
    print("""Luckily, he runs into Beaver, who is holding a glass of water.
    \"Hey Fish, you look like you could use some of this!\" he says.\n""")
    answer_2 = input("""What do you think fish will do with the water?\n
    A. Fish will ask to drink the water.
    B. Fish does not need water and will continue her journey to find Cat.
    C. Fish will jump into the glass. """)
    if answer_2 in answer_A:
        print("Incorrect. Try again!\n")
        scene_four()

    elif answer_2 in answer_B:
        print("Incorrect. Try again!\n")
        scene_four()

    elif answer_2 in answer_C:
        print("Correct!\n")
        scene_five()
    
    else:
        print("Sorry, I didn\'t get that. Try again!")
        scene_four()
        

def scene_three():
    print("""Learning Check! 
     In order for land animals to do things underwater, we would need to bring oxygen with us.
     One way this could be possible is scuba diving - where we bring a tank of oxygen underwater and breathe through a tube connected to the oxygen.\n
     In Cat\'s situation, he can stay submerged in water longer by snorkelling. 
     You\'re equipped with a diving mask and breathing tube that connects to the outside environment, allowing you to swim along the surface of the pond.""")
    answer_1 = input("Understand the concept and ready to move on? (yes/no)\n ")
    if answer_1 in yes:
        print("Awesome! Excellent learning so far!")
        scene_four()
    
    elif answer_1 in no:
        print("That's okay! Type yes when you think you got it.")
        scene_three()

    else:
        print("Sorry, I didn\'t get that. Try again!")
        scene_three()

def scene_two():
    print("""Cat frowns.\"Where can I find gills? I want to breathe like Fish!
    \"Sorry, Cat, but land animals don\'t have any. Your lungs are made to take in oxygen directly from the air. You don\'t need to separate the oxygen from the water!\" says the snail.""")
    print("\n Fact! Humans and other land animals need oxygen not only to breathe, but for all our body functions as well - like our heart to pump and our brains to work!")
    answer = input("""\nCan you think of a way that would allow Cat to breathe underwater? 
    A. Cat can swim along the surface of the water and breathe through a tube.
    B. Cat does not use anything to breathe because he can last a very long time underwater.
    C. Cat can use his nose to breathe the same way as Fish.""")
    if answer in answer_A:
        print("That\'s right! There are sticks of bamboo at the shore that can act as a snorkel!")
        scene_three()
    
    elif answer in answer_B:
        print("Incorrect. Try again!")
        scene_two()

    elif answer in answer_C:
        print("Incorrect. Try again!")
        scene_two()     

    else:
        print("Sorry, I didn\'t get that. Try again!")
        scene_two()

def question_two():
    print("""\n Learning Check! What are gills?\n Gills are fish's lungs. They help breathe by filtering oxygen from the water and delivering it to the bloodstream!
    Imagine a flour sifter sifting out flour. The flour is the oxygen, and the sifter is the gill. It is important to rememeber that the fish do not drink the water!""")
    response = input("Understand the concept and ready to move on? (yes/no) ")
    if response in yes:
        print("Great!\n")
    scene_two()

    if response in no:
        print("That's okay! Type yes when you think you got it.")
        question_two()

    else:
        print("Sorry, I didn\'t get that. Try again!")
        question_two()
        
    
def question_one():
    response = input("""What do you think will happen to Cat when he jumps into the water?
    A. Cat will be able to breathe underwater.
    B. Cat will get a mouthful of water.
    C. Cat will start swimming like a fish""")
    if response in answer_B:
        print("Correct!\n")
        def first_scene():
            print("""Cat swims around looking for Fish. As he tries to call her, he gets a mouthful of water! 
            Cat quickly swims up to the surface.\n Gasping for air, Cat holds onto a rock where he meets a friendly snail.\n
            \"Why can't I breathe underwater?\" Cat pants.
            \"Well, Cat, it\'s because you don’t have gills!\" the snail replies.""")
            question_two()
        first_scene()
            
    elif response in answer_A:
        print("Incorrect. Try again!")
        question_one()

    elif response in answer_C:
        print("Incorrect. Try again!")
        question_one()

    else:
        print("Sorry, I didn't get that. Try again!")
        question_one()
question_one()



