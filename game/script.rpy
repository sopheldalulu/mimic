#the face beneath his


#characters

define h = Character("Hideo", color="#b6c6d8")
define oba = Character("Grandmother", color="#d9c2a0")
define woman = Character("Village Woman", color="#c8b9b2")
define ijo = Character("IJO Operator", color="#a8b5bc")
define unknown = Character("???", color="#9b8a8a")

default player_name = "Akari"

define mc = Character("[player_name]", color="#e8b7c6")


#variables

default hideo_affection = 0
default suspicion = 0
default courage = 0

default trusted_hideo = False
default asked_about_ijo = False
default knows_about_gata = False
default saw_hideo_secret = False
default visited_shrine = False


#start

label start:
    scene black
    with fade
    pause 1.0
    centered "{size=52}THE MIMIC{/size}"
    pause 1.5
    centered "{size=28}A Hideo Story{/size}"
    pause 2.0
    centered "{i}There was a time when monsters were only stories.{/i}"
    pause 2.0
    centered "{i}That time is over.{/i}"
    pause 2.5

    #player name input

    $ player_name = renpy.input(
        "What is your name?",
        default="Akari",
        length=16
    )

    $ player_name = player_name.strip()

    if player_name == "":
        $ player_name = "Akari"


    #lore intro

    scene black
    with fade

    narrator "For generations, Japan told stories of supernatural beings known as yōkai."

    narrator "Some were mischievous."

    narrator "Some were harmless."

    narrator "Others were dangerous enough to turn entire villages into ghost stories."

    pause 1.0

    narrator "For most of modern history, they were treated as legends."

    narrator "Folklore."

    narrator "Stories parents told their children."

    pause 1.5

    narrator "Then came 2022."

    scene bg city_ruins
    with dissolve

    narrator "A catastrophic outbreak of yōkai forced the world to accept what had once been impossible."

    narrator "The creatures from the old stories were real."

    narrator "And humanity was not prepared for them."

    scene black
    with fade

    narrator "In response, the Japanese government established a special organization."

    centered "{b}BUREAU OF ANOMALOUS COUNTERMEASURES{/b}\n\n{size=42}IJO{/size}"

    pause 2.0

    narrator "Its purpose was to investigate supernatural incidents..."

    narrator "...contain dangerous anomalies..."

    narrator "...protect civilians..."

    narrator "...and eliminate hostile yōkai."

    pause 1.0

    narrator "But the more the IJO studied them..."

    narrator "...the more disturbing the truth became."

    scene bg dark_corridor
    with dissolve

    narrator "Yōkai were not the only monsters."

    narrator "Under certain circumstances..."

    pause 1.0

    narrator "...humans could become monsters too."

    centered "{size=44}GATA{/size}"

    narrator "The IJO discovered creatures known as Gata."

    narrator "Humans consumed by extreme rage and madness..."

    narrator "...their bodies transformed into mutated yōkai."

    narrator "Those mutations could continue."

    narrator "Gata."

    narrator "Muki."

    narrator "Shiki."

    pause 1.5

    narrator "Each stage becoming something further removed from humanity."

    scene black
    with fade

    narrator "Even after years of research..."

    narrator "there were still things the IJO didn't understand."

    pause 1.0

    narrator "Old things."

    narrator "Things hidden beneath mountains."

    narrator "Things sealed away long before the IJO existed."

    pause 2.0

    narrator "And sometimes..."

    narrator "...the greatest danger was the thing standing beside you."

    pause 2.5


    centered "{size=40}CHAPTER ONE{/size}\n\nThe Village in the Mountains"

    pause 2.0

    jump chapter_one


#chapter one

label chapter_one:

    scene bg bus_rural_day
    with fade

    play music "audio/rural_day.ogg" fadein 2.0

    narrator "The bus had been climbing through the mountains for almost two hours."

    narrator "Every few stops, another passenger disappeared."

    narrator "Until eventually..."

    narrator "...you were the only person left."

    mc "..."

    narrator "Your phone showed one bar."

    narrator "Then none."

    mc "Perfect."

    narrator "Outside the window stretched endless cedar forests."

    narrator "Rice fields."

    narrator "Old wooden houses."

    narrator "Stone statues darkened by rain and moss."

    narrator "You hadn't visited this village since you were a child."

    narrator "Your grandmother still lived here."

    narrator "After months of begging you to visit..."

    narrator "...you finally agreed to spend the summer with her."

    mc "One summer."

    mc "How bad could it be?"

    scene black

    pause 0.5

    narrator "You would remember saying that."

    pause 1.5

    scene bg village_bus_stop
    with fade

    play sound "audio/bus_stop.ogg"

    narrator "The bus stopped beside an old wooden shelter."

    narrator "You stepped onto the road."

    centered "{b}KIRISAME VILLAGE{/b}"

    narrator "The sign looked older than you remembered."

    play sound "audio/bus_leave.ogg"

    narrator "The bus pulled away."

    narrator "Its engine slowly disappeared down the mountain."

    narrator "And then..."

    pause 1.0

    narrator "Silence."

    mc "..."

    mc "Okay."

    mc "Grandma's house."

    narrator "You unfold the directions she mailed you."

    mc "\"Continue past the old shrine and turn at the persimmon tree.\""

    mc "That's not an address."

    h "It is around here."

    narrator "You jump."

    mc "Ah!"

    show hideo neutral at right
    with dissolve

    narrator "A boy stands several feet behind you."

    narrator "Black hair."

    narrator "Relaxed expression."

    narrator "Hands in his pockets."

    narrator "He looks around your age."

    narrator "Maybe slightly older."

    narrator "You hadn't heard him approach."

    h "Sorry."

    mc "You scared me."

    h "Yeah."

    narrator "He doesn't seem very sorry."

    h "You're looking for the Fujimori house."

    mc "How did you know?"

    h "You're holding directions to the Fujimori house."

    narrator "You look down."

    narrator "Your grandmother's name is written across the top."

    mc "Oh."

    narrator "The boy smiles."

    h "I'm Hideo."

    mc "[player_name]."

    narrator "Something about his name feels familiar."

    narrator "You search your memory."

    mc "Wait."

    mc "Hideo?"

    h "Hm?"

    mc "Did we know each other when we were kids?"

    narrator "His smile changes."

    narrator "Only slightly."

    h "You remembered."

    mc "Barely."

    h "I'll try not to be offended."

    mc "You look completely different."

    h "So do you."

    mc "That's usually how growing up works."

    h "Usually."

    narrator "The word hangs strangely between you."

    mc "What does that mean?"

    h "Nothing."

    h "Come on."

    h "I'll take you to your grandmother's."

    narrator "He starts walking."

    mc "Are you always this bossy?"

    h "Only when people are lost."


#first walk with hideo

    scene bg village_path_day
    with dissolve

    show hideo neutral at right

    narrator "You follow him deeper into the village."

    narrator "Cicadas buzz loudly from the trees."

    narrator "Wind chimes hang beneath tiled roofs."

    narrator "A narrow irrigation canal runs beside the road."

    narrator "Everything feels strangely untouched."

    mc "This place hasn't changed at all."

    h "Some things have."

    mc "Like what?"

    h "You'll notice."

    menu:

        "Ask about Hideo.":
            $ hideo_affection += 1

            mc "What about you?"

            h "What about me?"

            mc "What have you been doing all these years?"

            h "School."

            h "Work."

            mc "Very detailed."

            h "I'm mysterious."

            mc "You're annoying."

            narrator "Hideo laughs quietly."

        "Tell him you're glad to see him.":
            $ hideo_affection += 2

            mc "I'm actually glad you're still here."

            narrator "Hideo looks at you."

            h "Yeah?"

            mc "At least I know one person."

            narrator "For a moment, he looks genuinely surprised."

            h "Then I'm glad you came back."

        "Ask why the village is so empty.":
            $ suspicion += 1

            mc "Where is everyone?"

            h "Home, probably."

            mc "It's the middle of the afternoon."

            h "People don't stay outside as much anymore."

            mc "Why?"

            pause 0.5

            h "Things changed."


# =========================================================
# FIRST HINT OF THE OUTBREAK
# =========================================================

    narrator "You pass a house with wooden boards covering two windows."

    mc "Was there a storm?"

    h "No."

    narrator "Another house has a red notice attached to its gate."

    narrator "You recognize the government symbol immediately."

    mc "Is that..."

    narrator "You stop."

    mc "IJO?"

    show hideo serious at right

    pause 0.5

    h "Yeah."

    mc "Why would the IJO be here?"

    h "Routine inspections."

    mc "The Bureau of Anomalous Countermeasures doesn't do routine inspections for fun."

    h "You know about them?"

    mc "Everyone knows about them."

    mc "They're on the news constantly."

    narrator "Hideo glances toward the house."

    h "There were sightings a few months ago."

    mc "Yōkai?"

    h "Maybe."

    menu:

        "Ask what kind.":
            $ asked_about_ijo = True
            $ suspicion += 1

            mc "What kind of yōkai?"

            h "Nobody knows."

            mc "That's reassuring."

            h "You're safe."

            mc "You sound awfully sure."

            h "I am."

        "Trust him.":
            $ trusted_hideo = True
            $ hideo_affection += 1

            mc "Okay."

            narrator "Hideo looks slightly surprised."

            h "That's it?"

            mc "What?"

            h "You're trusting me?"

            mc "Shouldn't I?"

            narrator "He doesn't answer immediately."

            h "Probably."

        "Make a joke.":
            $ hideo_affection += 1

            mc "If a yōkai eats me, I'm blaming you."

            h "That's fair."

            mc "You don't seem concerned."

            h "I'd stop it."

            mc "Very heroic."

            h "I have my moments."


# =========================================================
# DOG SCENE
# =========================================================

    scene bg village_lane
    with dissolve

    show hideo neutral at right

    play sound "audio/dog_growl.ogg"

    narrator "A dog chained outside a nearby house suddenly growls."

    mc "Whoa."

    narrator "Its fur stands on end."

    narrator "Its eyes aren't on you."

    narrator "They're fixed on Hideo."

    play sound "audio/dog_bark.ogg"

    mc "I don't think he likes you."

    h "He never has."

    mc "Why?"

    h "Bad personality, probably."

    mc "Yours or his?"

    h "Both."

    narrator "You laugh."

    narrator "The dog doesn't."

    narrator "It pulls against the chain."

    narrator "Whining."

    narrator "Desperate to get farther away from Hideo."

    mc "That's..."

    pause 0.5

    mc "...weird."

    narrator "Hideo looks at the animal."

    narrator "For just a second..."

    narrator "his relaxed expression disappears."

    h "Come on."


# =========================================================
# SHRINE
# =========================================================

    scene bg old_shrine_day
    with dissolve

    narrator "The road curves around the base of a forested hill."

    narrator "Stone steps climb between the trees."

    narrator "At the top stands an old shrine."

    narrator "Its torii gate is faded."

    narrator "Thick sacred rope hangs across part of the entrance."

    narrator "Paper talismans flutter against the wooden posts."

    mc "I remember this place."

    show hideo serious at right

    h "Do you?"

    mc "Kind of."

    mc "We used to play near here."

    narrator "Hideo goes strangely quiet."

    mc "Didn't we?"

    h "Near it."

    mc "Can we go up?"

    h "No."

    mc "Why not?"

    h "It's closed."

    mc "There's no gate."

    h "That doesn't mean it's open."

    mc "Hideo."

    h "[player_name]."

    narrator "His tone is different now."

    narrator "Still quiet."

    narrator "But serious."

    h "Don't go up there."

    menu:

        "Listen to him.":
            $ hideo_affection += 2
            $ trusted_hideo = True

            mc "Okay."

            narrator "His shoulders relax slightly."

            h "Thanks."

        "Ask what is there.":
            $ suspicion += 2

            mc "What's up there?"

            h "An old shrine."

            mc "That's not what I meant."

            h "I know."

            mc "Then answer me."

            pause 1.0

            h "I can't."

        "Say you'll go later.":
            $ courage += 1
            $ visited_shrine = True

            mc "Fine."

            mc "I'll explore it myself later."

            h "Don't."

            mc "You already said that."

            h "I'm serious."

            mc "Why do you care?"

            pause 1.0

            narrator "Hideo looks directly at you."

            h "Because I don't want you disappearing too."


# =========================================================
# DISAPPEARANCES
# =========================================================

    mc "..."

    mc "What do you mean, too?"

    narrator "Hideo looks away."

    h "Forget I said that."

    mc "Absolutely not."

    h "There have been disappearances."

    mc "Recently?"

    h "Over the past year."

    mc "And you're only mentioning this now?"

    h "You just got here."

    mc "How many people?"

    h "I don't know."

    narrator "The answer comes too quickly."

    mc "You're lying."

    h "Probably."

    mc "Hideo!"

    narrator "He gives you a faint smile."

    h "Your grandmother's going to wonder where you are."

    mc "You're changing the subject."

    h "I'm very good at that."

    mc "I'm noticing."


# =========================================================
# GRANDMOTHER'S HOUSE
# =========================================================

    scene bg grandmother_house_day
    with dissolve

    narrator "A traditional wooden house appears at the end of the lane."

    mc "That's it."

    show hideo neutral at right

    h "See?"

    h "Didn't get you lost."

    mc "Congratulations."

    mc "You've successfully walked down a road."

    h "I expect a reward."

    menu:

        "\"How about dinner?\"":
            $ hideo_affection += 3

            mc "How about dinner?"

            h "Dinner?"

            mc "Grandma always cooks too much."

            h "You're inviting me over already?"

            mc "Don't make it weird."

            narrator "He smiles."

            h "Tomorrow."

            mc "Tomorrow?"

            h "I'll come get you."

            mc "That sounds suspiciously like a date."

            h "Maybe it is."

            narrator "Your face feels suddenly warm."

        "\"Thanks, Hideo.\"":
            $ hideo_affection += 1

            mc "Seriously."

            mc "Thanks."

            h "Anytime."

        "\"You still owe me answers.\"":
            $ suspicion += 1

            mc "You still owe me answers."

            h "I know."

            mc "And?"

            h "Ask me tomorrow."

            mc "Why tomorrow?"

            h "Because then I have until tomorrow to think of better lies."


# =========================================================
# GRANDMOTHER
# =========================================================

    hide hideo

    show grandmother neutral at left

    oba "[player_name]!"

    narrator "Your grandmother steps onto the porch."

    mc "Grandma!"

    narrator "She wraps you in a hug."

    oba "Look at you!"

    oba "You've gotten so tall."

    mc "You say that every time."

    narrator "She notices Hideo."

    oba "Oh."

    pause 0.5

    narrator "Something changes in her face."

    oba "Hideo."

    show hideo neutral at right

    h "Good afternoon."

    narrator "Your grandmother stares at him longer than necessary."

    mc "He helped me find the house."

    oba "Did he?"

    h "She would've figured it out eventually."

    mc "Probably not."

    oba "You should come inside."

    mc "Hideo too?"

    oba "No."

    narrator "The answer is immediate."

    mc "Grandma?"

    oba "His family will be expecting him."

    narrator "Hideo doesn't seem offended."

    h "She's right."

    h "I'll see you tomorrow, [player_name]."

    mc "Okay."

    h "And remember what I told you."

    mc "About the shrine?"

    narrator "Your grandmother stiffens."

    h "Yeah."

    narrator "He walks away."

    narrator "Your grandmother watches him until he disappears."


# =========================================================
# GRANDMOTHER WARNING
# =========================================================

    scene bg grandmother_house_inside
    with dissolve

    show grandmother serious

    mc "Okay."

    mc "What was that?"

    oba "What?"

    mc "You looked at Hideo like he'd crawled out of a grave."

    oba "[player_name]."

    mc "What?"

    oba "You shouldn't spend too much time near that shrine."

    mc "That's exactly what Hideo said."

    narrator "Her expression darkens."

    oba "Hideo said that?"

    mc "Yes."

    oba "..."

    mc "Why is everyone being weird?"

    oba "This village has changed."

    mc "He said that too."

    oba "People have disappeared."

    mc "He told me."

    oba "There have been..."

    narrator "She hesitates."

    oba "...incidents."

    mc "Yōkai?"

    pause 1.0

    oba "The IJO came last winter."

    mc "I saw one of their notices."

    oba "They said there were Gata nearby."

    mc "Gata?"

    narrator "You recognize the name."

    narrator "Everyone does."

    oba "People."

    oba "Or people who used to be people."

    oba "Consumed by rage."

    oba "Changed into something else."

    $ knows_about_gata = True

    mc "Did they find any here?"

    oba "They wouldn't tell us."

    mc "That's comforting."

    oba "They searched the mountains."

    oba "The shrine."

    oba "Several abandoned houses."

    mc "And?"

    oba "Then they left."

    mc "So it's safe."

    narrator "Your grandmother doesn't answer."

    mc "Grandma?"

    oba "Lock your window tonight."


# =========================================================
# NIGHT ONE
# =========================================================

    scene bg bedroom_night
    with fade

    stop music fadeout 2.0

    play music "audio/night_ambience.ogg" fadein 2.0

    narrator "By midnight, the entire village is silent."

    narrator "No traffic."

    narrator "No voices."

    narrator "Only cicadas."

    narrator "And the occasional rustling of trees."

    mc "..."

    narrator "You lie awake staring at the ceiling."

    narrator "Your grandmother's warning keeps replaying in your mind."

    mc "\"Lock your window tonight.\""

    mc "Very normal."

    pause 1.0

    play sound "audio/tap_window.ogg"

    narrator "{i}Tap.{/i}"

    mc "..."

    pause 1.0

    play sound "audio/tap_window.ogg"

    narrator "{i}Tap.{/i}"

    narrator "You sit up."

    mc "No."

    narrator "Another sound."

    play sound "audio/tap_window.ogg"

    narrator "{i}Tap.{/i}"

    narrator "From your window."

    menu:

        "Look outside.":
            $ courage += 1
            jump look_outside

        "Stay in bed.":
            jump stay_in_bed


# =========================================================
# WINDOW BRANCH
# =========================================================

label look_outside:

    narrator "You slowly cross the room."

    narrator "The curtain moves slightly in the night breeze."

    mc "I locked that..."

    narrator "You pull it aside."

    scene bg window_forest_night
    with dissolve

    narrator "Nothing."

    narrator "Just the dark yard."

    narrator "Trees."

    narrator "Moonlight."

    narrator "Then..."

    pause 1.0

    narrator "Movement."

    mc "..."

    narrator "Someone is standing near the forest."

    narrator "A boy."

    mc "Hideo?"

    narrator "He is facing away from the house."

    narrator "Completely still."

    mc "What is he doing?"

    narrator "Something moves in front of him."

    narrator "Something tall."

    narrator "Too tall."

    narrator "Its arms hang almost to the ground."

    narrator "Its body bends forward at an unnatural angle."

    mc "..."

    narrator "Your stomach drops."

    mc "Gata."

    narrator "You've seen photographs."

    narrator "News footage."

    narrator "IJO warnings."

    narrator "You know what they look like."

    narrator "But this is the first time you've seen one alive."

    play sound "audio/creature_growl.ogg"

    narrator "The creature twitches."

    narrator "Hideo doesn't run."

    narrator "He doesn't even step back."

    mc "Hideo..."

    narrator "The Gata moves toward him."

    pause 1.0

    scene black

    play sound "audio/impact.ogg"

    pause 0.5

    narrator "You duck instinctively."

    mc "!"

    pause 1.0

    scene bg window_forest_night

    narrator "When you look again..."

    narrator "the Gata is gone."

    narrator "Hideo is still standing there."

    narrator "Alone."

    narrator "He slowly turns."

    narrator "Even from this distance..."

    narrator "you know he is looking directly at your window."

    pause 1.5

    show hideo shadow

    narrator "Then he raises one finger to his lips."

    h "..."

    narrator "{i}Don't say anything.{/i}"

    $ saw_hideo_secret = True
    $ suspicion += 3

    scene black
    with fade

    jump morning_after


# =========================================================
# STAY IN BED BRANCH
# =========================================================

label stay_in_bed:

    narrator "No."

    narrator "Absolutely not."

    narrator "You've watched enough horror movies to know how this works."

    narrator "You pull the blanket higher."

    play sound "audio/tap_window.ogg"

    narrator "{i}Tap.{/i}"

    mc "Not happening."

    pause 1.0

    narrator "The tapping stops."

    pause 2.0

    play sound "audio/distant_scream.ogg"

    narrator "A scream tears through the village."

    mc "..."

    narrator "You stop breathing."

    narrator "Then..."

    narrator "silence."

    scene black
    with fade

    jump morning_after


# =========================================================
# CHAPTER TWO
# =========================================================

label morning_after:

    scene bg village_morning
    with fade

    stop music fadeout 2.0

    play music "audio/rural_day.ogg" fadein 2.0

    centered "{size=40}CHAPTER TWO{/size}\n\nThings That Shouldn't Be Here"

    pause 2.0

    narrator "By morning, the village is filled with police."

    narrator "An ambulance blocks the main road."

    narrator "Three men wearing black uniforms stand near one of the houses."

    mc "..."

    narrator "You recognize the insignia immediately."

    centered "{b}IJO{/b}"

    narrator "Whatever happened last night..."

    narrator "it wasn't an animal attack."

    show grandmother serious

    oba "Stay here."

    mc "Grandma—"

    oba "Inside."

    mc "I'm not twelve."

    oba "And that thing outside doesn't care how old you are."

    narrator "Before you can answer..."

    h "[player_name]."

    hide grandmother

    show hideo neutral at right

    narrator "Hideo stands outside the gate."

    narrator "He looks completely normal."

    narrator "Clean clothes."

    narrator "Calm expression."

    narrator "No injuries."

    if saw_hideo_secret:

        narrator "Your eyes drop instinctively to his hands."

        narrator "Nothing."

        narrator "Not even a scratch."

        mc "You."

        h "Me."

        mc "We need to talk."

        h "I figured."

    else:

        mc "Did you hear what happened?"

        h "Yeah."

        mc "Someone screamed last night."

        h "I heard."

    narrator "An IJO vehicle passes behind him."

    mc "They came fast."

    h "They were already nearby."

    mc "How do you know?"

    narrator "Hideo pauses."

    h "Because..."

    narrator "He reaches into his pocket."

    narrator "And pulls out a black identification card."

    mc "..."

    narrator "The IJO insignia is printed across the front."

    mc "No way."

    h "It's complicated."

    mc "You're IJO?"

    h "Not officially."

    mc "That does not make this less confusing."

    h "I'm in training."

    mc "Since when?"

    h "A while."

    mc "And you just forgot to mention that yesterday?"

    h "You didn't ask."

    mc "Hideo!"

    narrator "He almost smiles."

    h "There you are."

    mc "What?"

    h "You used to yell my name exactly like that."

    narrator "You stare at him."

    mc "You're unbelievable."


# =========================================================
# ROMANCE MOMENT
# =========================================================

    scene bg river_path_day
    with dissolve

    show hideo neutral at right

    narrator "Hideo convinces your grandmother that you're safer with him than wandering around alone."

    narrator "Somehow..."

    narrator "she agrees."

    narrator "The two of you walk beside the river."

    mc "So."

    mc "IJO."

    h "Yeah."

    mc "You fight yōkai."

    h "Sometimes."

    mc "Gata?"

    h "Mostly lately."

    mc "Aren't they dangerous?"

    h "Very."

    mc "And you're saying that like you're talking about mosquitoes."

    h "Mosquitoes are worse."

    mc "Hideo."

    narrator "He laughs."

    menu:

        "Tell him you're worried about him.":
            $ hideo_affection += 3

            mc "I'm serious."

            mc "You could get hurt."

            narrator "Hideo's smile fades."

            h "You're worried about me?"

            mc "Obviously."

            narrator "He looks away."

            h "You shouldn't be."

            mc "Why?"

            pause 1.0

            h "Because I'm harder to hurt than you think."

        "Ask if he's killed one before.":
            $ suspicion += 1

            mc "Have you killed a Gata?"

            h "Yeah."

            mc "How many?"

            h "Enough."

            narrator "Something about his answer makes you stop asking."

        "Tease him.":
            $ hideo_affection += 2

            mc "So you're secretly some cool government monster hunter."

            h "Cool?"

            mc "Don't get excited."

            h "Too late."


# =========================================================
# HIDEO SECRET BUILDUP
# =========================================================

    narrator "You reach a small bridge."

    narrator "Hideo stops."

    h "[player_name]."

    mc "Hm?"

    h "Promise me something."

    mc "Depends."

    h "If the IJO tells you to leave the village..."

    h "leave."

    mc "What about you?"

    h "Don't worry about me."

    mc "That's not an answer."

    h "It's the only one I have."

    mc "What are you hiding?"

    narrator "Hideo goes quiet."

    if saw_hideo_secret:

        mc "I saw you last night."

        narrator "His expression freezes."

        mc "There was a Gata."

        mc "It was standing right in front of you."

        mc "And then it disappeared."

        h "You shouldn't have looked."

        mc "That is your explanation?"

        h "No."

        mc "Then explain."

        narrator "Hideo looks toward the river."

        h "I can't."

        mc "Can't or won't?"

        h "Both."

    else:

        mc "First the shrine."

        mc "Then the disappearances."

        mc "Now the IJO."

        mc "You know more than you're telling me."

        h "I do."

        mc "At least you're admitting it."

    narrator "He steps closer."

    h "There are things happening here that you don't understand."

    mc "Then help me understand."

    h "If I do..."

    pause 1.0

    h "...you might stop looking at me the same way."

    narrator "The playful Hideo from yesterday is gone."

    narrator "For the first time..."

    narrator "he looks afraid."

    mc "Hideo..."

    narrator "A radio crackles from his pocket."

    play sound "audio/radio_static.ogg"

    ijo "Unit Seven, respond."

    narrator "Hideo immediately pulls away."

    h "I have to go."

    mc "Wait—"

    h "Go home."

    mc "Hideo!"

    h "And stay away from the shrine."

    narrator "He runs toward the main road."

    narrator "Leaving you alone."


# =========================================================
# IJO INFORMATION SCENE
# =========================================================

    scene bg village_checkpoint
    with dissolve

    narrator "You don't go home."

    narrator "Obviously."

    narrator "Instead, you follow the road toward the IJO checkpoint."

    narrator "Several black vehicles are parked near the village entrance."

    narrator "Maps and warning notices cover a temporary command board."

    narrator "One catches your attention."

    centered "{b}ANOMALOUS ENTITY CLASSIFICATION{/b}"

    narrator "GATA — Stage One."

    narrator "Human origin."

    narrator "Associated with prolonged rage, madness, or severe negative emotional exposure."

    narrator "Low intelligence."

    narrator "Often hunts in groups."

    narrator "Potential progression..."

    centered "{b}GATA → MUKI → SHIKI{/b}"

    mc "..."

    narrator "Another notice shows a map."

    narrator "Most of the red markings surround the mountain."

    narrator "And the abandoned shrine."

    mc "Of course."

    narrator "You lean closer."

    narrator "One handwritten note is circled."

    centered "{i}Possible source beneath shrine complex.{/i}"

    mc "..."

    unknown "You shouldn't be reading that."

    narrator "You spin around."

    scene black
    with hpunch

    pause 1.0

    narrator "But before you can see who spoke..."

    play sound "audio/scream_close.ogg"

    narrator "A scream erupts from somewhere behind the houses."

    narrator "Then gunfire."

    play sound "audio/gunshots.ogg"

    mc "Hideo..."

    jump gata_attack


# =========================================================
# GATA ATTACK
# =========================================================

label gata_attack:

    scene bg village_attack
    with fade

    play music "audio/chase.ogg"

    narrator "People run toward you."

    woman "GET INSIDE!"

    mc "What's happening?!"

    woman "GATA!"

    play sound "audio/creature_growl.ogg"

    narrator "Something crashes through a wooden fence."

    narrator "A tall humanoid creature crawls into the road."

    narrator "Its limbs are far too long."

    narrator "Its skin is raw and distorted."

    narrator "Its mouth opens wider than any human mouth should."

    mc "..."

    narrator "For one horrible moment..."

    narrator "you notice scraps of clothing still hanging from its body."

    narrator "Human clothing."

    narrator "This thing used to be someone."

    play sound "audio/gunshot.ogg"

    narrator "A gunshot echoes."

    narrator "The creature jerks backward."

    show hideo serious at right
    with dissolve

    h "[player_name]!"

    mc "Hideo!"

    h "Get behind me!"

    narrator "He raises a handgun."

    play sound "audio/gunshot.ogg"

    narrator "Another shot."

    narrator "The Gata screams."

    mc "You have a gun?!"

    h "Not the best time!"

    narrator "The creature charges."

    h "MOVE!"

    scene black
    with hpunch

    play sound "audio/impact.ogg"

    pause 1.0

    narrator "You hit the ground."

    narrator "When you look up..."

    scene bg village_attack

    narrator "Hideo is between you and the Gata."

    narrator "The creature's claws have torn through his shirt."

    mc "HIDEO!"

    narrator "Blood stains the fabric."

    narrator "The Gata lunges again."

    pause 1.0

    narrator "And then..."

    narrator "stops."

    mc "..."

    narrator "Its body trembles."

    narrator "It stares at Hideo."

    narrator "Not with hunger."

    narrator "Not with rage."

    pause 1.0

    narrator "With fear."

    narrator "Hideo slowly raises his head."

    narrator "You can't see his face."

    h "..."

    narrator "The creature backs away."

    mc "Hideo?"

    narrator "His hand tightens around the gun."

    narrator "For one fraction of a second..."

    narrator "something about his silhouette looks wrong."

    narrator "Too tall."

    narrator "Too sharp."

    narrator "Not human."

    blink

    narrator "Then it's gone."

    narrator "Hideo fires."

    play sound "audio/gunshot.ogg"

    narrator "The Gata collapses."

    stop music fadeout 2.0

    narrator "Silence."

    mc "..."

    mc "Hideo."

    narrator "He turns toward you."

    show hideo hurt at right

    h "Are you hurt?"

    mc "No."

    mc "But you are."

    h "I'm fine."

    mc "Your shirt is covered in blood!"

    h "It's not as bad as it looks."

    narrator "He takes one step."

    narrator "Then another."

    narrator "You see the torn fabric move."

    mc "..."

    narrator "There should be deep claw marks beneath it."

    narrator "There aren't."

    narrator "The skin is already closing."

    mc "Hideo..."

    narrator "His eyes meet yours."

    pause 1.0

    h "Don't."

    mc "What are you?"

    pause 2.0

    narrator "He looks genuinely hurt by the question."

    h "I don't know how to answer that."

    scene black
    with fade

    centered "{i}That was the moment you understood.{/i}"

    pause 1.5

    centered "{i}The IJO wasn't the only one studying monsters.{/i}"

    pause 1.5

    centered "{i}Hideo had been studying them too.{/i}"

    pause 1.5

    centered "{i}Because somehow...{/i}"

    pause 1.0

    centered "{i}he was one of them.{/i}"

    pause 3.0


# =========================================================
# END OF DEMO
# =========================================================

    centered "{size=42}END OF CHAPTER TWO{/size}"

    pause 2.0

    centered "{i}To be continued...{/i}"

    return