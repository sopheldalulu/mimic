# =========================================================
# THE MIMIC: HIDEO AU
# Horror / Romance / Supernatural Visual Novel
#
# Background files:
# - shrine day.png
# - forest night.png
# - bedroom night.png
# - house inside day.png
#
# Hideo sprites:
# - hideo normal.png
# - hideo odd.png
# =========================================================


# ---------------------------------------------------------
# IMAGE DEFINITIONS
# ---------------------------------------------------------

image bg shrine_day = "images/shrine day.jpeg"
image bg forest_night = "images/forest night.jpeg"
image bg bedroom_night = "images/bedroom night.jpeg"
image bg house_inside_day = "images/house inside day.jpeg"

image hideo normal = "images/hideo normal.png"
image hideo odd = "images/hideo odd.png"


# ---------------------------------------------------------
# CHARACTERS
# ---------------------------------------------------------

define h = Character("Hideo", color="#b6c6d8")
define grandma = Character("Grandmother", color="#d9c2a0")
define ijo = Character("IJO Operator", color="#a8b5bc")
define woman = Character("Village Woman", color="#c8b9b2")
define unknown = Character("???", color="#9b8a8a")

default player_name = "Akari"

define mc = Character("[player_name]", color="#e8b7c6")


# ---------------------------------------------------------
# VARIABLES
# ---------------------------------------------------------

default hideo_affection = 0
default suspicion = 0
default courage = 0

default trusted_hideo = False
default knows_about_gata = False
default saw_hideo_secret = False
default visited_shrine = False


# =========================================================
# START
# =========================================================

label start:

    scene black
    with fade

    centered "{size=52}THE MIMIC{/size}"

    pause 1.5

    centered "{size=28}A Hideo Story{/size}"

    pause 2.0

    centered "{i}There was a time when monsters were only stories.{/i}"

    pause 2.0

    centered "{i}That time is over.{/i}"

    pause 2.0


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


    # =====================================================
    # LORE INTRO
    # =====================================================

    scene black
    with fade

    narrator "For generations, Japan told stories of supernatural beings known as yōkai."

    narrator "Some were harmless."

    narrator "Others were dangerous."

    narrator "For most people, they were nothing more than folklore."

    pause 1.0

    narrator "Then came 2022."

    narrator "A catastrophic outbreak of yōkai forced humanity to accept the impossible."

    narrator "The creatures from the old stories were real."

    narrator "And people were dying."

    pause 1.0

    narrator "In response, the Japanese government formed a specialized organization."

    centered "{b}BUREAU OF ANOMALOUS COUNTERMEASURES{/b}\n\n{size=42}IJO{/size}"

    pause 2.0

    narrator "The IJO investigated supernatural incidents."

    narrator "Contained dangerous entities."

    narrator "Protected civilians."

    narrator "And eliminated hostile yōkai."

    pause 1.0

    narrator "But yōkai were not the only monsters."

    centered "{size=42}GATA{/size}"

    narrator "Some humans could transform."

    narrator "Extreme rage and madness could distort the body and mind."

    narrator "Turning a person into something barely recognizable."

    narrator "A Gata."

    pause 1.0

    narrator "And sometimes..."

    narrator "...the transformation didn't stop there."

    centered "{b}GATA → MUKI → SHIKI{/b}"

    pause 2.0

    narrator "Even after years of research..."

    narrator "there were still things the IJO didn't understand."

    narrator "Old things."

    narrator "Things buried beneath villages and shrines."

    narrator "Things that had existed long before the IJO."

    pause 2.0

    narrator "And sometimes..."

    narrator "...the thing beside you was far more dangerous than the thing hiding in the dark."

    pause 2.0

    centered "{size=40}CHAPTER ONE{/size}\n\nThe Village in the Mountains"

    pause 2.0

    jump chapter_one


# =========================================================
# CHAPTER ONE
# =========================================================

label chapter_one:

    scene bg house_inside_day
    with fade

    narrator "You arrived at your grandmother's village that afternoon."

    narrator "The bus ride had taken hours."

    narrator "Your phone lost signal halfway through the mountains."

    narrator "By the time you reached the village, you were already regretting agreeing to spend the summer here."

    mc "One summer."

    mc "How bad could it be?"

    narrator "Your grandmother had left the front door unlocked for you."

    narrator "Her house looked almost exactly the way you remembered it."

    narrator "Old wood."

    narrator "Tatami floors."

    narrator "A faint smell of tea."

    narrator "And absolutely no Wi-Fi."

    mc "This is going to be a long summer."

    h "Probably."

    mc "!"

    show hideo normal at right
    with dissolve

    narrator "You spin around."

    narrator "A boy is standing just outside the doorway."

    narrator "Black hair."

    narrator "Calm expression."

    narrator "Hands casually in his pockets."

    narrator "You hadn't heard him approach."

    mc "You scared me!"

    h "Sorry."

    narrator "He doesn't sound sorry."

    mc "Do I know you?"

    narrator "He smiles slightly."

    h "You used to."

    mc "..."

    mc "Hideo?"

    h "Took you long enough."

    narrator "The name pulls at an old memory."

    narrator "A boy you used to play with when you visited the village as a child."

    mc "You look different."

    h "So do you."

    mc "That's usually what happens when people grow up."

    h "Usually."

    mc "What does that mean?"

    h "Nothing."

    narrator "He smiles again."

    narrator "Something about him feels familiar."

    narrator "But something else feels..."

    pause 0.5

    narrator "...wrong."


    # =====================================================
    # FIRST CONVERSATION
    # =====================================================

    menu:

        "Tell him you're happy to see him.":

            $ hideo_affection += 2

            mc "I'm actually glad you're still here."

            narrator "Hideo looks surprised."

            h "Yeah?"

            mc "At least I know someone."

            h "Then I'm glad you came back."


        "Tease him.":

            $ hideo_affection += 1

            mc "Still creepy, I see."

            h "You remembered that too?"

            mc "Unfortunately."

            narrator "Hideo laughs quietly."


        "Ask why he came here.":

            $ suspicion += 1

            mc "How did you even know I arrived?"

            h "Small village."

            mc "That's not an answer."

            h "It's the only one you're getting."


    # =====================================================
    # SHRINE
    # =====================================================

    scene bg shrine_day
    with dissolve

    show hideo normal at right

    narrator "Later, Hideo offers to show you around."

    narrator "The village itself isn't very large."

    narrator "A few houses."

    narrator "Fields."

    narrator "Dense forest."

    narrator "And an old shrine sitting near the edge of the mountain."

    mc "I remember this."

    narrator "The shrine looks older than everything around it."

    narrator "Its wood is dark."

    narrator "Paper talismans hang from the entrance."

    narrator "A thick rope stretches across part of the path."

    mc "Didn't we play here when we were little?"

    hide hideo normal
    show hideo odd at right

    h "Near here."

    mc "Can we go inside?"

    h "No."

    mc "Why?"

    h "It's closed."

    mc "There's nothing blocking the entrance."

    h "That doesn't mean you should enter."

    mc "Hideo."

    narrator "His expression changes."

    h "I'm serious."

    h "Don't go inside that shrine."

    menu:

        "Listen to him.":

            $ hideo_affection += 2
            $ trusted_hideo = True

            mc "Fine."

            h "Thank you."

            narrator "His expression softens."

            hide hideo odd
            show hideo normal at right


        "Ask what's inside.":

            $ suspicion += 2

            mc "What's in there?"

            h "Nothing you need to see."

            mc "That sounds extremely suspicious."

            h "It should."


        "Say you'll come back later.":

            $ courage += 1
            $ visited_shrine = True

            mc "Maybe I'll come back without you."

            narrator "Hideo immediately looks at you."

            h "Don't."

            mc "Why do you care?"

            pause 1.0

            h "Because people disappear around here."


    # =====================================================
    # IJO DISCUSSION
    # =====================================================

    mc "Disappear?"

    narrator "Hideo looks toward the shrine."

    h "The IJO came here last winter."

    mc "The IJO?"

    h "Yeah."

    mc "Why?"

    h "Reports of yōkai."

    mc "What kind?"

    h "Mostly Gata."

    mc "Mostly?"

    h "That's what they said."

    narrator "Something about the way he says it bothers you."

    mc "You know more than you're telling me."

    h "Probably."

    mc "You're terrible."

    h "I've been told."

    mc "Are Gata still around?"

    narrator "Hideo is quiet."

    h "Sometimes."

    mc "And nobody thought they should tell me this before I came here?"

    h "Your grandmother probably didn't want to scare you."

    mc "Are you scared?"

    pause 0.5

    h "No."

    mc "You answered that way too fast."

    h "Did I?"


    # =====================================================
    # BACK AT GRANDMOTHER'S HOUSE
    # =====================================================

    scene bg house_inside_day
    with dissolve

    hide hideo odd
    hide hideo normal

    narrator "By the time you return to your grandmother's house, the sun is beginning to set."

    grandma "You were with Hideo."

    mc "Yeah."

    narrator "Your grandmother doesn't look pleased."

    mc "What's wrong?"

    grandma "Nothing."

    mc "That's obviously not true."

    grandma "[player_name]..."

    narrator "She hesitates."

    grandma "Stay away from the shrine."

    mc "Hideo said the same thing."

    pause 1.0

    grandma "He did?"

    mc "Why is everyone being weird about it?"

    grandma "That place isn't safe anymore."

    mc "Because of the Gata?"

    grandma "Partly."

    mc "Partly?"

    grandma "The IJO searched the shrine last winter."

    mc "And?"

    grandma "They never told us what they found."

    narrator "Your grandmother looks toward the window."

    grandma "People started disappearing before they arrived."

    mc "How many?"

    grandma "Enough."

    narrator "You stare at her."

    grandma "Lock your window tonight."

    mc "What?"

    grandma "Just do it."


    # =====================================================
    # NIGHT
    # =====================================================

    scene bg bedroom_night
    with fade

    narrator "That night, you can't sleep."

    narrator "The room is too quiet."

    narrator "The village is too quiet."

    narrator "No cars."

    narrator "No voices."

    narrator "Just the occasional sound of insects outside."

    mc "This place is officially creepy."

    pause 1.0

    narrator "You turn over."

    pause 1.0

    narrator "{i}Tap.{/i}"

    mc "..."

    pause 1.0

    narrator "{i}Tap.{/i}"

    narrator "The sound comes from your window."

    mc "Nope."

    pause 1.0

    narrator "{i}Tap.{/i}"

    menu:

        "Look outside.":

            $ courage += 1

            jump window_scene


        "Stay in bed.":

            jump stay_in_bed


# =========================================================
# WINDOW SCENE
# =========================================================

label window_scene:

    narrator "Against every instinct telling you not to..."

    narrator "you walk toward the window."

    narrator "Your hand closes around the curtain."

    mc "This is such a bad idea."

    narrator "You pull it aside."

    scene bg forest_night
    with dissolve

    narrator "The forest is almost completely black."

    narrator "For a moment..."

    narrator "you see nothing."

    pause 1.0

    narrator "Then you notice someone standing between the trees."

    mc "..."

    narrator "A boy."

    show hideo odd at right
    with dissolve

    mc "Hideo?"

    narrator "He is standing completely still."

    narrator "Facing away from you."

    mc "What is he doing out there?"

    narrator "Something shifts deeper in the forest."

    narrator "Something tall."

    narrator "Something bent."

    narrator "Something human-shaped..."

    narrator "...but not human."

    mc "..."

    narrator "A Gata."

    narrator "You've seen pictures online."

    narrator "IJO warning videos."

    narrator "But seeing one in front of you is completely different."

    narrator "Its limbs are too long."

    narrator "Its movements are wrong."

    narrator "It slowly approaches Hideo."

    mc "Hideo..."

    narrator "He doesn't move."

    narrator "The creature stops."

    pause 1.0

    narrator "Then something strange happens."

    narrator "The Gata backs away."

    mc "..."

    narrator "It's afraid."

    narrator "Hideo slowly turns his head."

    narrator "Even from this distance..."

    narrator "you know he's looking directly at you."

    h "..."

    narrator "He raises one finger to his lips."

    narrator "{i}Don't say anything.{/i}"

    $ saw_hideo_secret = True
    $ suspicion += 3

    scene black
    with fade

    jump next_morning


# =========================================================
# STAY IN BED
# =========================================================

label stay_in_bed:

    mc "Absolutely not."

    narrator "You pull the blanket over your head."

    narrator "{i}Tap.{/i}"

    mc "No."

    pause 1.0

    narrator "The tapping suddenly stops."

    pause 2.0

    narrator "Then..."

    narrator "A scream tears through the village."

    mc "..."

    narrator "You freeze."

    narrator "After that..."

    narrator "you don't sleep at all."

    scene black
    with fade

    jump next_morning


# =========================================================
# NEXT MORNING
# =========================================================

label next_morning:

    scene bg house_inside_day
    with fade

    narrator "The next morning, your grandmother is listening to the radio."

    ijo "Residents are advised to remain indoors until further notice."

    ijo "An anomalous entity was sighted near the eastern forest."

    ijo "Do not approach the shrine."

    mc "..."

    grandma "You heard them."

    grandma "You're staying here."

    mc "Sure."

    narrator "You have absolutely no intention of staying here."

    narrator "A knock sounds at the door."

    grandma "Who is it?"

    h "Hideo."

    mc "..."

    show hideo normal at right
    with dissolve

    narrator "He steps inside."

    narrator "He looks completely normal."

    narrator "Like nothing happened."

    if saw_hideo_secret:

        mc "You."

        h "Morning."

        mc "Don't 'morning' me."

        h "I figured this was coming."

        mc "What were you doing in the forest?"

        narrator "Hideo glances toward your grandmother."

        h "Can we talk outside?"

        mc "Absolutely."

    else:

        mc "Did you hear what happened?"

        h "Yeah."

        mc "The IJO said there was something in the forest."

        h "I heard."

        mc "You don't seem worried."

        h "Should I be?"

    narrator "Your grandmother watches Hideo carefully."

    grandma "Don't go near the shrine."

    h "We won't."

    narrator "He says it too quickly."


    # =====================================================
    # PRIVATE TALK
    # =====================================================

    scene bg shrine_day
    with dissolve

    show hideo normal at right

    narrator "You and Hideo stop near the shrine."

    mc "Of all places, you brought me here?"

    h "Nobody else is around."

    mc "Comforting."

    if saw_hideo_secret:

        mc "I saw you last night."

        h "I know."

        mc "There was a Gata."

        h "Yeah."

        mc "It was scared of you."

        narrator "Hideo looks away."

        mc "Why?"

        h "I don't know."

        mc "You're lying."

        h "Probably."

        mc "Stop doing that!"

        hide hideo normal
        show hideo odd at right

        narrator "His expression changes."

        h "You need to stop asking questions."

        mc "Why?"

        h "Because the more you know..."

        pause 1.0

        h "...the more dangerous this gets."

        mc "For me?"

        pause 1.0

        h "For both of us."

    else:

        mc "What is happening here?"

        h "I told you."

        h "Gata."

        mc "You also told me 'mostly Gata.'"

        mc "So what else is here?"

        hide hideo normal
        show hideo odd at right

        narrator "Hideo's expression darkens."

        h "Something older."

        mc "Older than what?"

        h "The IJO."

        mc "That's not helpful."

        h "It's not supposed to be."


    # =====================================================
    # ROMANCE CHOICE
    # =====================================================

    menu:

        "Tell him you trust him.":

            $ hideo_affection += 3
            $ trusted_hideo = True

            mc "I trust you."

            narrator "Hideo stares at you."

            h "You shouldn't."

            mc "Maybe."

            mc "But I do."

            narrator "For once..."

            narrator "Hideo doesn't have a clever response."

            hide hideo odd
            show hideo normal at right

            h "You're going to make this difficult."


        "Tell him you're scared of him.":

            $ suspicion += 2

            mc "You're scaring me."

            narrator "Hideo goes still."

            hide hideo odd
            show hideo normal at right

            h "..."

            h "I'm sorry."

            narrator "For the first time..."

            narrator "he genuinely sounds like he means it."


        "Ask if he's even human.":

            $ suspicion += 3

            mc "Hideo."

            mc "Are you even human?"

            pause 2.0

            hide hideo odd
            show hideo normal at right

            narrator "He smiles."

            narrator "But it doesn't reach his eyes."

            h "What do you think?"

            mc "That's not an answer."

            h "I know."


    # =====================================================
    # CLIFFHANGER
    # =====================================================

    narrator "Before you can continue..."

    narrator "A bell rings from somewhere inside the shrine."

    mc "..."

    mc "Was that you?"

    hide hideo normal
    show hideo odd at right

    narrator "Every trace of warmth disappears from Hideo's face."

    h "No."

    narrator "The bell rings again."

    narrator "Once."

    narrator "Twice."

    narrator "Three times."

    h "[player_name]."

    mc "What?"

    h "Run."

    mc "What?"

    h "NOW."

    scene black
    with fade

    narrator "Something moves behind the shrine doors."

    narrator "Something scratches against the wood."

    narrator "And for the first time..."

    narrator "you realize Hideo isn't watching the shrine."

    pause 1.0

    narrator "He's watching you."

    pause 1.0

    narrator "Like he's afraid of what might happen..."

    narrator "...if whatever is inside recognizes you."

    pause 2.0

    centered "{size=42}END OF CHAPTER ONE{/size}"

    pause 2.0

    centered "{i}To be continued...{/i}"

    return