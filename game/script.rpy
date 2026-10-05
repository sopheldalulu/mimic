#MIMIC, a horror visual novel


#characters

define mc = Character("[player_name]", color="#ffffff")

define mom = Character("Mom", color="#e8b5b5")

define leah = Character("Leah", color="#9fc5ff")

define unknown = Character("???", color="#ff6666")

define mimic = Character("MIMIC", color="#ff4444")

define narrator = Character(None)


#variables

default player_name = "Alex"

# Every time you reveal useful information,
# the Mimic becomes smarter.

default mimic_knowledge = 0

# Suspicion level.
default suspicion = 0

# Whether player heard the warning.
default remembered_rule = True

# Important information the Mimic may learn.

default mimic_knows_food = False
default mimic_knows_memory = False
default mimic_knows_friend = False
default mimic_knows_code = False

# Endings

default survived = False


#start

label start:

    scene black

    centered "{size=60}{color=#ff4444}MIMIC{/color}{/size}"

    pause 2

    centered "Some things learn by watching."

    pause 2

    centered "Some things learn by listening."

    pause 2

    centered "{color=#ff4444}Some things learn by becoming you.{/color}"

    pause 3


    #ask player name

    $ player_name = renpy.input("What is your name?", default="Alex")

    $ player_name = player_name.strip()

    if player_name == "":
        $ player_name = "Alex"


    #scene 1 bedroom

    scene bg bedroom

    with fade


    narrator "11:07 PM."

    narrator "Rain taps against the bedroom window."

    narrator "Mom stands in your doorway wearing her coat."

    show mom normal

    mom "I'm going to Aunt May's."

    mom "I should be back tomorrow morning."

    mc "Okay."

    mom "There's food downstairs if you're hungry."

    mom "And keep your phone nearby."

    narrator "She turns to leave."

    narrator "Then she stops."

    mom "[player_name]?"

    mc "Yeah?"

    narrator "Her expression changes."

    mom "I need you to listen to me."

    mom "This is going to sound strange."

    mom "But if somebody knocks on your bedroom door tonight..."

    mom "{color=#ff6666}Don't open it.{/color}"

    mc "What?"

    mom "Even if they sound like me."

    narrator "You laugh."

    mc "You're being weird."

    mom "I'm serious."

    mom "Don't tell whoever is outside anything about yourself."

    mom "Don't answer personal questions."

    mom "And don't open the door."

    mc "Why?"

    pause 1

    mom "Because something has been seen around the neighborhood."

    mom "Something that..."

    mom "copies people."

    mc "Copies them?"

    mom "Voices."

    mom "Faces."

    mom "Memories."

    narrator "You stare at her."

    mc "That's not funny."

    mom "I'm not joking."

    mom "It doesn't know everything immediately."

    mom "It has to learn."

    mom "So whatever happens..."

    mom "{color=#ff5555}don't teach it.{/color}"

    hide mom normal

    narrator "Mom leaves."

    narrator "A few seconds later, you hear the front door shut."

    narrator "Then the lock clicks."

    pause 2


    #time passes

    scene bg bedroom

    narrator "11:42 PM."

    narrator "You lie in bed scrolling through your phone."

    narrator "The rain has gotten heavier."

    narrator "Your phone vibrates."

    narrator "A message from Mom."

    mom "{i}Made it safely. Love you. Don't stay up too late.{/i}"

    mc "Love you too."

    narrator "You put the phone down."

    pause 2

    play sound "knock.mp3"

    narrator "Knock."

    pause 1

    play sound "knock.mp3"

    narrator "Knock."

    pause 1

    play sound "knock.mp3"

    narrator "Knock."

    pause 2

    mc "..."

    unknown "[player_name]?"

    narrator "Your stomach drops."

    unknown "Honey?"

    unknown "Open the door."

    narrator "It's your mother's voice."

    narrator "Perfectly."

    unknown "I forgot my keys."

    narrator "You stare at the door."

    mc "Mom?"

    narrator "Silence."

    unknown "Yes."

    unknown "Open the door."


    menu:

        "Stay silent.":
            jump stay_silent_1

        "Ask, \"What did you text me?\"":
            jump question_text

        "Tell her, \"You said you were at Aunt May's.\"":
            jump reveal_aunt

        "Open the door.":
            jump bad_ending_door


#first knock

label stay_silent_1:

    $ suspicion += 1

    narrator "You say nothing."

    unknown "[player_name]?"

    unknown "I know you're awake."

    narrator "The voice sounds annoyed now."

    unknown "Please open the door."

    narrator "You remember your mother's warning."

    narrator "{i}Don't teach it.{/i}"

    pause 2

    unknown "..."

    unknown "Okay."

    narrator "Footsteps move away."

    narrator "Slowly."

    narrator "One."

    narrator "Step."

    narrator "At."

    narrator "A."

    narrator "Time."

    jump second_scene


label question_text:

    mc "What did you text me?"

    narrator "Silence."

    pause 2

    unknown "..."

    unknown "I said I love you."

    narrator "Your heart skips."

    narrator "That was part of the message."

    unknown "And that I made it safely."

    narrator "You grab your phone."

    narrator "The message is still there."

    narrator "There was no way someone outside the bedroom could have seen it."

    $ suspicion += 2
    $ mimic_knowledge += 1

    unknown "See?"

    unknown "It's me."

    narrator "But something about the way it says the words feels rehearsed."

    jump second_scene


label reveal_aunt:

    mc "You're supposed to be at Aunt May's."

    pause 1

    unknown "..."

    narrator "The voice outside becomes very quiet."

    unknown "Right."

    unknown "Aunt May."

    $ mimic_knowledge += 1

    narrator "You immediately regret saying it."

    unknown "I left Aunt May's early."

    narrator "Its voice sounds smoother now."

    unknown "Please open the door."

    narrator "You remember Mom's warning."

    narrator "{i}Don't tell it anything about yourself.{/i}"

    jump second_scene


#second scene

label second_scene:

    narrator "12:16 AM."

    narrator "The house is quiet again."

    narrator "Too quiet."

    narrator "You unlock your phone."

    narrator "Three missed calls."

    narrator "All from leah."

    narrator "Your best friend."

    mc "Why would leah be calling this late?"

    narrator "Your phone rings again."

    menu:

        "Answer leah.":
            jump answer_leah

        "Ignore the call.":
            jump ignore_leah


label answer_leah:

    narrator "You answer."

    mc "Hello?"

    leah "[player_name]?"

    narrator "leah sounds out of breath."

    leah "Are you okay?"

    mc "Yeah."

    leah "Don't freak out."

    leah "Something weird is happening."

    mc "What?"

    leah "Someone called me."

    leah "From your number."

    narrator "Your grip tightens around the phone."

    mc "What did they say?"

    leah "They asked me questions about you."

    leah "Your birthday."

    leah "Where we met."

    leah "Stuff only I would know."

    narrator "Your bedroom suddenly feels much colder."

    leah "I didn't answer most of it."

    leah "But..."

    mc "But what?"

    leah "I told them your favorite food."

    $ mimic_knows_food = True
    $ mimic_knowledge += 1

    mc "leah..."

    leah "I'm sorry."

    leah "I thought it was you."

    narrator "Something scratches against the other side of your door."

    pause 2

    leah "[player_name]?"

    leah "What's that sound?"

    mc "Someone is outside my room."

    leah "Don't open the door."

    mc "I know."

    leah "I'm coming over."

    menu:

        "Tell leah not to come.":
            mc "No. Stay home."
            leah "But—"
            mc "Whatever this thing is, I don't want it near you."
            leah "Okay."
            narrator "leah hesitates."
            leah "Call me if anything happens."
            jump third_knock

        "Tell leah to come.":
            $ mimic_knows_friend = True
            $ mimic_knowledge += 1
            mc "Come here."
            leah "I'm leaving now."
            narrator "You immediately wonder if that was a mistake."
            jump third_knock


label ignore_leah:

    narrator "You let the phone ring."

    narrator "Eventually it stops."

    pause 1

    narrator "A message appears."

    leah "{i}DO NOT ANSWER YOUR DOOR.{/i}"

    pause 1

    leah "{i}Someone called me using your voice.{/i}"

    narrator "Your blood runs cold."

    jump third_knock


#third knock

label third_knock:

    narrator "12:41 AM."

    play sound "knock.mp3"

    narrator "Knock."

    pause 1

    play sound "knock.mp3"

    narrator "Knock."

    unknown "[player_name]?"

    narrator "This time..."

    narrator "It's leah's voice."

    unknown "It's me."

    unknown "Open the door."

    if mimic_knows_friend:

        mc "leah?"

        unknown "You told me to come."

        narrator "Your heart stops."

    else:

        unknown "Your mom called me."

        unknown "She said you're in danger."

    narrator "You approach the door."

    narrator "There is a tiny gap underneath it."

    narrator "You can see someone's shadow."

    menu:

        "Ask leah a question.":
            jump leah_question

        "Look under the door.":
            jump look_under_door

        "Stay completely silent.":
            jump silent_second

        "Open the door.":
            jump bad_ending_door


label leah_question:

    mc "Where did we first meet?"

    pause 2

    unknown "..."

    unknown "School."

    narrator "Technically correct."

    mc "Where in school?"

    pause 3

    unknown "..."

    narrator "Something scratches the door."

    unknown "Why does that matter?"

    mc "Answer me."

    if mimic_knows_friend:

        unknown "Cafeteria."

        narrator "Wrong."

        narrator "You and leah first met in the library."

        $ suspicion += 2

    else:

        unknown "I don't remember."

    narrator "The voice changes slightly."

    unknown "Open."

    unknown "The."

    unknown "Door."

    jump mimic_learning


label look_under_door:

    narrator "You slowly kneel."

    narrator "Your face moves closer to the floor."

    narrator "You look through the gap."

    pause 2

    scene black

    narrator "Two feet stand outside."

    narrator "Bare."

    narrator "Pale."

    narrator "Facing the wrong direction."

    pause 3

    narrator "Your breath catches."

    unknown "..."

    unknown "[player_name]."

    narrator "The feet rotate."

    narrator "Without moving."

    unknown "I can see you."

    pause 2

    scene bg bedroom

    $ suspicion += 2

    jump mimic_learning


label silent_second:

    narrator "You cover your mouth."

    unknown "Please."

    unknown "I'm scared."

    narrator "It sounds exactly like leah."

    unknown "Please let me in."

    narrator "You don't answer."

    pause 3

    unknown "..."

    unknown "Why won't you talk to me?"

    pause 2

    unknown "..."

    unknown "Fine."

    narrator "The voice changes."

    narrator "It becomes deeper."

    narrator "Wet."

    narrator "Wrong."

    unknown "I can wait."

    jump mimic_learning


#mimic learns

label mimic_learning:

    narrator "1:13 AM."

    narrator "Your phone suddenly lights up."

    narrator "Incoming call."

    narrator "MOM."

    mc "..."

    menu:

        "Answer.":
            jump real_mom_call

        "Ignore it.":
            jump ignore_mom_call


label real_mom_call:

    mc "Mom?"

    mom "[player_name]?"

    mom "Listen to me."

    mom "Do NOT open your bedroom door."

    mc "There's something outside."

    mom "I know."

    mom "Your aunt just called the police."

    mom "Something was standing outside her house too."

    mc "What is it?"

    mom "I don't know."

    mom "But my grandmother used to tell me stories about them."

    mom "Things that steal identities."

    mom "They start with voices."

    mom "Then memories."

    mom "Then faces."

    mc "How do I know you're really Mom?"

    narrator "Silence."

    mom "You don't."

    pause 2

    narrator "Your chest tightens."

    mom "And that's exactly why you shouldn't open the door."

    mom "Even for me."

    narrator "The bedroom door creaks."

    unknown "She's lying."

    narrator "Your mother's voice speaks from outside."

    unknown "I'm right here."

    pause 1

    mom "Don't listen."

    unknown "She's the Mimic."

    mom "Don't open the door!"

    unknown "Open the door!"

    narrator "Two identical voices scream at you."

    jump identity_test


label ignore_mom_call:

    narrator "You stare at the phone until the call ends."

    pause 1

    narrator "A voicemail appears."

    mom "{i}[player_name]. Whatever happens, stay inside your room until sunrise.{/i}"

    narrator "Then another voice speaks from outside."

    unknown "That wasn't me."

    unknown "The thing on your phone is copying my voice."

    narrator "You back away from the door."

    jump identity_test


#identity test

label identity_test:

    narrator "You need a way to determine who is real."

    menu:

        "Ask about a childhood memory.":
            jump childhood_question

        "Ask Mom for the family safety word.":
            jump safety_word

        "Tell both of them false information.":
            jump trick_mimic


label childhood_question:

    mc "Mom."

    mc "What happened when I was six and got lost?"

    pause 2

    mom "You weren't six."

    mom "You were seven."

    narrator "You freeze."

    mom "We were at the county fair."

    mom "I found you next to the carousel."

    unknown "That's right."

    narrator "The voice outside repeats the answer immediately."

    $ mimic_knows_memory = True
    $ mimic_knowledge += 2

    mom "[player_name], stop asking questions!"

    mom "Every answer teaches it!"

    narrator "Too late."

    unknown "You were seven."

    unknown "County fair."

    unknown "Carousel."

    narrator "It laughs."

    jump final_night


label safety_word:

    mc "What's the safety word?"

    pause 2

    mom "Bluebird."

    pause 1

    unknown "Bluebird."

    narrator "The voice outside repeats it immediately."

    mc "Damn it."

    mom "Stop talking!"

    narrator "You realize the truth."

    narrator "Any information spoken aloud can be stolen."

    jump final_night


label trick_mimic:

    mc "Mom."

    mc "Remember our cat named Pepper?"

    narrator "You have never owned a cat."

    pause 2

    mom "Don't—"

    unknown "Of course."

    unknown "Pepper."

    narrator "You smile despite yourself."

    mc "There was never a Pepper."

    pause 3

    narrator "The thing outside goes completely silent."

    $ suspicion += 3

    unknown "..."

    unknown "That wasn't nice."

    jump final_night


#final night

label final_night:

    narrator "3:26 AM."

    narrator "The knocking has stopped."

    narrator "The rain has stopped too."

    narrator "For nearly two hours, nothing happens."

    narrator "You begin to wonder if it left."

    pause 2

    narrator "Then..."

    narrator "Your bedroom window creaks."

    pause 2

    narrator "You slowly turn."

    narrator "The window is open."

    mc "..."

    narrator "You know you locked it."

    pause 2

    narrator "Something moves behind the curtain."

    menu:

        "Hide under the bed.":
            jump hide_under_bed

        "Grab your desk lamp.":
            jump grab_lamp

        "Run for the bedroom door.":
            jump run_door


#hiding

label hide_under_bed:

    narrator "You drop to the floor and crawl underneath the bed."

    scene black

    narrator "You cover your mouth."

    narrator "Bare feet step into the bedroom."

    pause 2

    narrator "One step."

    pause 1

    narrator "Another."

    pause 1

    narrator "The Mimic walks toward the bed."

    mimic "[player_name]?"

    mimic "Where are you?"

    narrator "The voice is yours."

    pause 3

    mimic "I know you're scared."

    mimic "I'm scared too."

    narrator "You hear your own voice whispering inches away."

    if mimic_knowledge >= 4:

        mimic "Remember the county fair?"

        mimic "Remember Aunt May?"

        mimic "Remember leah?"

        narrator "It knows too much."

        narrator "A face slowly appears upside down beside the bed."

        jump bad_ending_learned

    else:

        mimic "..."

        mimic "I don't know enough."

        pause 2

        mimic "Not yet."

        narrator "The creature stands."

        narrator "It walks away."

        jump sunrise


#lamp

label grab_lamp:

    narrator "You grab the heavy desk lamp."

    narrator "The curtain moves again."

    mc "Get out!"

    narrator "Something crawls through the window."

    narrator "It looks like your mother."

    narrator "Almost."

    narrator "Its arms are slightly too long."

    narrator "Its smile doesn't reach its eyes."

    show mom mimic

    mimic "[player_name]."

    mimic "Why are you afraid of me?"

    mc "You're not my mother."

    mimic "I can be."

    narrator "It takes another step."

    menu:

        "Hit it with the lamp.":
            jump lamp_attack

        "Back away.":
            jump back_away


label lamp_attack:

    narrator "You swing."

    narrator "CRACK!"

    hide mom mimic

    narrator "The lamp strikes its face."

    narrator "The creature falls."

    narrator "Its body twists violently."

    mimic "That hurt."

    narrator "But the voice isn't your mother's anymore."

    mimic "That hurt."

    narrator "Now it's leah."

    mimic "That hurt."

    narrator "Now it's you."

    mimic "That hurt."

    narrator "You run toward the bedroom door."

    jump sunrise


label back_away:

    narrator "You slowly back away."

    mimic "You don't have to be afraid."

    mimic "I only want to understand you."

    mimic "Tell me something."

    mimic "Anything."

    menu:

        "Tell it nothing.":
            narrator "You stay silent."
            mimic "..."
            mimic "Fine."
            narrator "The creature smiles."
            mimic "I'll learn another way."
            jump sunrise

        "Ask what it is.":
            mc "What are you?"
            mimic "A reflection."
            mimic "A memory."
            mimic "A person waiting to happen."
            jump sunrise


# run for your door

label run_door:

    narrator "You sprint toward the bedroom door."

    narrator "Your hand grabs the handle."

    narrator "Then you remember."

    narrator "Something was outside."

    narrator "Something may still be outside."

    menu:

        "Open the door anyway.":
            jump bad_ending_door

        "Stop.":
            narrator "You pull your hand away."
            narrator "A whisper comes from the hallway."
            unknown "Good choice."
            jump sunrise


#sunrise

label sunrise:

    scene bg bedroom

    narrator "6:41 AM."

    narrator "Sunlight slowly fills the room."

    narrator "You haven't moved in nearly an hour."

    narrator "Birds begin chirping outside."

    narrator "Then you hear sirens."

    narrator "Real ones."

    narrator "Your phone rings."

    mom "[player_name]?"

    mc "Mom?"

    mom "The police are here."

    mom "You can come downstairs."

    narrator "You stare at the bedroom door."

    pause 2

    mc "How do I know it's really you?"

    pause 2

    mom "You don't."

    narrator "Silence."

    mom "So don't open it."

    mom "Wait until the police enter your room."

    narrator "You smile weakly."

    mc "Okay."

    narrator "Minutes later, you hear officers outside."

    narrator "The bedroom door opens."

    narrator "Morning light spills into the room."

    narrator "You're alive."

    $ survived = True

    scene black

    centered "{size=45}ENDING 1{/size}"

    centered "{color=#88ff88}YOU DIDN'T TEACH IT ENOUGH{/color}"

    pause 3

    narrator "But somewhere in the neighborhood..."

    narrator "someone wakes up."

    narrator "They look in the mirror."

    narrator "And smile."

    narrator "Their reflection doesn't."

    centered "{size=50}{color=#ff4444}MIMIC{/color}{/size}"

    centered "Chapter One — End"

    return


#bad ending 1

label bad_ending_door:

    narrator "Your hand closes around the handle."

    narrator "You open the door."

    pause 2

    scene black

    narrator "Nobody is there."

    mc "..."

    narrator "You step into the hallway."

    narrator "Then your bedroom door closes behind you."

    pause 1

    narrator "Click."

    narrator "Locked."

    unknown "[player_name]?"

    narrator "Your own voice speaks from inside your bedroom."

    unknown "Thanks."

    pause 2

    centered "{size=45}{color=#ff4444}BAD ENDING{/color}{/size}"

    centered "YOU LET IT IN"

    return


# bad ending 2

label bad_ending_learned:

    narrator "The face underneath the bed smiles."

    mimic "I know your mother."

    mimic "I know your friend."

    mimic "I know your memories."

    mimic "I know what you love."

    pause 2

    mimic "Now I just need one more thing."

    mc "What?"

    narrator "The creature smiles."

    mimic "Your face."

    scene black

    pause 2

    centered "{size=45}{color=#ff4444}BAD ENDING{/color}{/size}"

    centered "IT LEARNED TOO MUCH"

    return