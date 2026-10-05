#the face beneath his

define h = Character("Hideo", color="#b7c5d8")
define old_woman = Character("Old Woman", color="#d8c6aa")
define narrator = Character(None)

default player_name = "Akari"

define mc = Character("[player_name]", color="#e8b9c8")

#variables

default hideo_affection = 0
default suspicion = 0
default courage = 0

default saw_shrine = False
default followed_hideo = False
default knows_rumor = False


label start:
    scene black with fade
    centered "{size=48}THE BOY BENEATH THE MASK{/size}"
    pause 2.0
    centered "{i}There are stories in old villages that no one tells after sunset.{/i}"

    pause 2.0

    centered "{i}Stories about spirits.{/i}"

    pause 1.0

    centered "{i}Monsters.{/i}"

    pause 1.0

    centered "{i}And things that learned how to look human.{/i}"

    pause 2.5


    # -----------------------------------------------------
    # PLAYER NAME
    # -----------------------------------------------------

    $ player_name = renpy.input(
        "What is your name?",
        default="Akari",
        length=16
    )

    $ player_name = player_name.strip()

    if player_name == "":
        $ player_name = "Akari"


    # -----------------------------------------------------
    # BASIC LORE FOR NEW PLAYERS
    # -----------------------------------------------------

    scene bg mountains_morning
    with dissolve

    narrator "Japan has always had stories about yōkai."

    narrator "Supernatural beings said to live in forests, rivers, mountains, abandoned homes, and forgotten shrines."

    narrator "Some were harmless."

    narrator "Some were mischievous."

    narrator "Others were said to hunt humans."

    narrator "The oldest stories warned that the most dangerous yōkai were not always the ones that looked like monsters."

    scene black
    with fade

    narrator "Some could imitate voices."

    narrator "Some could change shape."

    narrator "Some could wear the face of a human so perfectly..."

    pause 1.0

    narrator "...that even the person closest to them would never know."

    pause 2.0


    centered "{size=38}CHAPTER ONE{/size}\n\nThe Village at the End of the Road"

    pause 2.0

    jump chapter_one


label chapter_one:

    scene bg bus_rural_day
    with fade

    play music "audio/rural_day.ogg" fadein 2.0

    narrator "The bus had been climbing into the mountains for nearly two hours."

    narrator "Every few minutes, another passenger stepped off."

    narrator "Until eventually..."

    narrator "...you were the only one left."

    mc "..."

    narrator "Your phone had lost signal twenty minutes ago."

    narrator "Outside the window, endless cedar trees covered the mountains."

    narrator "Between them stood old wooden houses, small rice fields, and stone statues covered in moss."

    narrator "You had agreed to spend the summer here with your grandmother."

    narrator "She called it peaceful."

    narrator "You called it the middle of nowhere."

    scene bg village_road_day
    with fade

    narrator "The bus finally stopped beside a faded wooden sign."

    centered "{b}KIRISAME VILLAGE{/b}"

    narrator "Population: 312."

    narrator "Or at least..."

    narrator "That's what the sign said."

    play sound "audio/bus_leave.ogg"

    narrator "The bus disappeared down the mountain road."

    narrator "And suddenly the village became very quiet."

    mc "Great."

    mc "No signal."

    mc "No taxi."

    mc "No idea where I'm going."

    narrator "You pull out the handwritten directions your grandmother mailed you."

    mc "\"Walk past the shrine and turn left at the persimmon tree.\""

    mc "That is not an address."


    # -----------------------------------------------------
    # HIDEO FIRST APPEARANCE
    # -----------------------------------------------------

    show hideo neutral at right
    with dissolve

    h "You're going the wrong way."

    narrator "You nearly drop the paper."

    mc "Jesus!"

    narrator "A boy stands a few feet behind you."

    narrator "Around your age."

    narrator "Dark hair falls messily over his forehead."

    narrator "He wears a white shirt with the sleeves pushed up and an old school bag hanging from one shoulder."

    narrator "There is nothing particularly unusual about him."

    narrator "And yet..."

    narrator "You hadn't heard him approach."

    mc "Were you standing there the whole time?"

    h "No."

    mc "You walk really quietly."

    h "People tell me that."

    narrator "His eyes drift toward the paper in your hand."

    h "You're looking for the Fujimori house."

    mc "How did you know that?"

    h "Everyone knows when someone new arrives."

    narrator "He says it casually."

    narrator "You aren't sure why that makes you uncomfortable."

    h "I'm Hideo."

    menu:

        "Introduce yourself politely.":
            $ hideo_affection += 1

            mc "I'm [player_name]."

            h "[player_name]."

            narrator "He repeats your name slowly."

            h "I'll remember it."

        "Ask why he knows everyone.":
            $ suspicion += 1

            mc "Do you always keep track of strangers?"

            h "Only interesting ones."

            mc "And I'm interesting?"

            h "You got off the bus."

            h "That's enough."

        "Tease him.":
            $ hideo_affection += 2

            mc "So the village welcoming committee is just one weird boy?"

            narrator "Hideo blinks."

            narrator "Then he laughs."

            h "Unfortunately."


    h "Come on."

    mc "Where?"

    h "I'll show you the way."

    narrator "He begins walking before you agree."

    mc "You always order strangers around?"

    h "Only the lost ones."


    # -----------------------------------------------------
    # WALK THROUGH VILLAGE
    # -----------------------------------------------------

    scene bg village_path_day
    with dissolve

    show hideo neutral at right

    narrator "The village is smaller than you expected."

    narrator "Traditional houses sit between vegetable gardens and narrow roads."

    narrator "Wind chimes ring beneath wooden roofs."

    narrator "Somewhere nearby, cicadas scream from the trees."

    mc "It's pretty."

    h "You'll get tired of it."

    mc "You don't like living here?"

    h "I didn't say that."

    mc "Then what did you mean?"

    h "People get tired of places that don't change."

    narrator "You glance at him."

    mc "How long have you lived here?"

    pause 0.5

    h "A long time."

    mc "Your whole life?"

    pause 1.0

    h "Something like that."

    narrator "Before you can ask what that means, you notice something beside the road."


    # -----------------------------------------------------
    # SHRINE
    # -----------------------------------------------------

    scene bg old_shrine_day
    with dissolve

    narrator "A narrow stone staircase disappears into the forest."

    narrator "At the top stands an old shrine."

    narrator "Its torii gate is faded almost black."

    narrator "Thick shimenawa rope hangs across the entrance."

    narrator "White paper charms flutter in the breeze."

    mc "What's up there?"

    show hideo serious at right
    with dissolve

    h "Nothing."

    mc "That's obviously not true."

    h "It's an abandoned shrine."

    mc "Can we go see it?"

    narrator "For the first time since meeting him..."

    narrator "Hideo's expression changes."

    h "No."

    mc "Why?"

    h "Because people aren't supposed to go there."

    menu:

        "Respect the warning.":
            $ hideo_affection += 1

            mc "Okay."

            narrator "Hideo looks slightly relieved."

            h "Good."

        "Ask what happened there.":
            $ suspicion += 1
            $ knows_rumor = True

            mc "What happened there?"

            h "Nothing you need to worry about."

            mc "That is exactly what people say before something terrible happens."

            narrator "Hideo doesn't laugh."

        "Say you'll visit later.":
            $ courage += 1
            $ saw_shrine = True

            mc "Fine."

            mc "I'll come back by myself."

            narrator "Hideo turns toward you immediately."

            h "Don't."

            mc "Why do you care?"

            pause 1.0

            h "..."

            h "Because I don't want anything to happen to you."


    # -----------------------------------------------------
    # FIRST SUPERNATURAL HINT
    # -----------------------------------------------------

    scene bg village_path_day
    with dissolve

    show hideo neutral at right

    narrator "You continue walking."

    mc "So what's the big village secret?"

    h "There isn't one."

    mc "Every creepy mountain village has one."

    h "You've watched too many horror movies."

    mc "Missing tourists?"

    h "No."

    mc "Cursed shrine?"

    h "No."

    mc "Ancient monster living in the woods?"

    pause 0.5

    h "..."

    mc "Hideo?"

    h "No."

    narrator "You smile."

    narrator "He's clearly terrible at lying."

    play sound "audio/bell.ogg"

    narrator "A small bell rings somewhere in the forest."

    mc "What's that?"

    narrator "Hideo stops walking."

    h "What?"

    mc "The bell."

    pause 1.0

    narrator "His face goes strangely blank."

    h "You heard that?"

    mc "Yeah."

    narrator "Hideo looks toward the trees."

    narrator "For several seconds, he says nothing."

    h "We should go."

    mc "Why?"

    h "It's getting late."

    mc "It's four in the afternoon."

    h "Still."

    narrator "His hand closes gently around your wrist."

    narrator "His skin is cold."

    mc "Hideo..."

    narrator "Then you notice something beyond him."

    scene bg forest_edge_day
    with dissolve

    narrator "Between two cedar trees..."

    narrator "Someone is standing in the forest."

    narrator "A woman."

    narrator "At least..."

    narrator "You think it's a woman."

    narrator "Her white dress hangs loosely from her body."

    narrator "Her hair covers her face."

    narrator "She isn't moving."

    mc "Hideo..."

    narrator "You blink."

    narrator "The woman is gone."

    scene bg village_path_day
    with dissolve

    show hideo serious at right

    h "What did you see?"

    mc "There was someone in the woods."

    narrator "Hideo's grip tightens."

    h "If you see her again..."

    pause 1.0

    h "Don't speak to her."

    mc "You know who she is?"

    h "No."

    mc "You're lying."

    narrator "Hideo looks directly into your eyes."

    h "Yes."

    pause 1.0

    h "I am."

    jump end_chapter_one


label end_chapter_one:

    scene black
    with fade

    centered "{i}That was the first time Hideo lied to you.{/i}"

    pause 2.0

    centered "{i}It would not be the last.{/i}"

    pause 2.0

    centered "{size=38}END OF CHAPTER ONE{/size}"

    return