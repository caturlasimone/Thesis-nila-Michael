define ari = Character("Ari", color="#c92a5a")
define lina = Character("Lina", color="#311c4b")
define sam = Character("Sam", color="#864317")

default player = None
default gender = None

image playerSprite = ConditionSwitch(
    "gender == 'f'", "Laura.png",
    "gender == 'm'", "Dante.png"
)

image white = Solid("#FFFFFF")
image gray = Solid("#F3F3F3")

transform left:
    zoom 0.8
    ypos 130
    xpos 500

transform right:
    zoom 0.8
    ypos 130
    xpos 1100

transform center:
    zoom 0.8
    ypos 130
    xalign 0.5

transform character_hover:
    on idle:
        ease 0.3 zoom 1.0 ypos 60
    on hover:
        ease 0.3 zoom 1.05 ypos 70

transform flipped:
    xzoom -1.0

transform scrollBackground:
    rotate -90
    yalign 0.5
    zoom 1.4
    xpos -800
    linear 10.0 xpos -2000

transform scrollBackground2:
    rotate -90
    yalign 0.5
    zoom 0.8
    xpos -170
    linear 5.0 xpos -1150


label start:
    scene bg hallway

    "Hello there! Welcome to Pose! Where you will be able to refine your skills and knowledge about making animation."

    "Please select your character's gender"
    window hide

    call screen myCharacter

    window show

    if gender == "f":
        show laura at center with dissolve
        $ playerName = renpy.input("What is your name?")
        $ playerName = playerName.strip()
        if playerName == "":
            $ playerName = "Laura"

        $ player = Character(playerName, color="#ecaaaa")
        
    else:
        show dante at center with dissolve
        $ playerName = renpy.input("What is your name?")
        $ playerName = playerName.strip()
        if playerName == "":
            $ playerName = "Dante"

        $ player = Character(playerName, color="#58a95f")

    "Pleased to meet you, [playerName]!"

    scene bg hallway with fade

    jump intro

    return

label intro:
    #scene bg bedroom with fade
    scene

    show playerSprite at center
    player "Oh no! I'm late for school!"


    scene bg outside with fade

    show playerSprite at center

    "[playerName] is walking around campus."

    menu:
        "[playerName] sees a classmate on their way to class. What will you do?"
        
        "Interact with classmate.":
            $ interaction = True
            jump extraDiag
        
        "Ignore classmate.":
            "I'm running late. I dont have time for this!"
            jump startClass

    return

label startClass:
    scene bg library with fade
    show sam at center
    sam "Good morning Everyone!"
    sam "Today, we're diving into one of the fundamental techniques in animation: Pose-to-Pose Keyframing."
    # may nagflash daw sa screen
    show sam at left with move
    show sam at left, flipped
    sam "This is the method most professional animators use to create structured, deliberate movement."
    sam "What is Pose-to-Pose? Can anybody answer?"

    show playerSprite at right

    menu:
        "Disrupt the class":
            player "ITS A JOJO REFERENCE!"
            sam "..."
        "Ask a question":
            player "Is it like modeling?"
            sam "Not quite."
        "Answer accurately":
            player "It means to focus on the most important, or Key, moments of an action first, and then we fill in the frames between them."
            sam "Thats right! Thank you for answering."

    hide playerSprite

    jump keyposes

    return    

'''
label review:
    scene bg library
    menu:
        sam "Is everthing clear to you, class?"

        "Yes, that was super helpful!":
            show sam at center
            sam "Great to hear! Now, let’s put that into practice with a quick activity."
        "Could we go over KEY POSES again?":
            show sam at center
            sam "Sure!"
        "Could you explain BREAKDOWN again?":
            show sam at center
            sam "Sure!"
        "Can we revisit the part about TIMING AND SPACING?":
            show sam at center
            sam "Sure!"
        "Can you run through SLOW IN & SLOW OUT again?":
            show sam at center
            sam "Sure!" 
    
    return
'''

label keyposes:
    sam "It is when you make the key moments or poses of a character’s movement."
    sam "Think of it like a choreographer planning a dance: they set the main positions before worrying about the smooth transitions."
    sam "So let’s go ahead and define the Key Poses."
    sam "Our first step is called Blocking."
    sam "We're going to create the character's most extreme and necessary poses. Let's imagine our character is going to jump up and then land."

    hide sam with dissolve

    scene bg jump:
        rotate -90
        yalign 0.5
        zoom 1.4
        xpos -800
    

    sam "This is our initial position. For a jump, it's the anticipation pose—knees bent, arms back, and ready to launch."
    sam "Make sure to adjust the character's body into the starting pose."

    scene bg jump:
        rotate -90
        yalign 0.5
        zoom 1.4
        xpos -2290

    sam "This is the highest point of the jump, where the character is suspended in the air. Adjust the character's position and pose to show them floating at the peak of the jump. We want a clear contrast from the first pose."

    scene bg jump:
        rotate -90
        yalign 0.5
        zoom 1.4
        xpos -3100
    
    sam "This is the final pose, the resolution of the action. For us, it’s the landing, likely a lower, 'settling' pose with some follow-through. Position the character in the final landing pose."

    scene bg jump at scrollBackground
    sam "Now, if you scrub the timeline, you’ll see the character pop instantly between these three poses. That’s okay! This is our Block."
    sam "It allows us to review the overall action, timing, and silhouettes immediately, before doing any extra drawing."
    sam "The animation looks jerky because the software is just moving in a straight line between our Keys."

    scene bg library
    show sam at center

    menu:
        sam "Is everthing clear to you, class?"

        "Yes, lets have an activity!":
            jump actIntro
        "No, can we go over KEY POSES again?":
            jump keyposes

    return

label actIntro:
    scene bg library
    show sam at center

    sam "Get ready to answer Questions!"

    menu:
        "Shall we begin?"

        "No, I need to go over the topics again.":
            scene bg jump at scrollBackground
            sam "This is an example of Keyposes."

            scene bg breakdown at scrollBackground2
            sam "This is an example of Breakdown."

            scene white
            show bg slowin:
                rotate -90
                yalign 0.5
                xalign 0.5
                zoom 0.55
            sam "This is an example of Slow in"

            show bg slowout
            sam "This is an example of Slow out"

            jump act1

        "Yes, I'm ready!":
            show sam at center
            sam "Let's get started!"
            sam "For the activity, we are going to be providing you with the Key Poses for the animation, and you have to choose the correct In-Between or breakdown for the main keyframes."
            sam "Don’t worry, we know that you got it! Here you go!"

            scene gray
            show bg sample1:
                yalign 0.25
                xalign 0.5
                zoom 2.0
            sam "So in this sample picture, we have already laid out the key poses, and it is up to you to complete these masterpieces!"

            scene gray
            show bg sample2:
                yalign 0.25
                xalign 0.5
                zoom 2.0
            sam "But be careful! there are one Amongus on the choices Like this! In this picture, notice each frame in the picture, the legs and arms doesn’t show fluidity and consistency, which is wrong."

            scene gray
            show bg sample3:
                yalign 0.25
                xalign 0.5
                zoom 2.0
            sam "In this picture, notice how the arms and legs smoothly correspond to the movement of the walk. Which is correct."

            scene bg library
            show sam at center
            sam "After we have shown you some of the example of the quiz, I believe in you!"
            jump act1

    return


label act1:
    default ans = None
    scene white
    show bg q1:
        yalign 0.25
        xalign 0.5
        zoom 3.0

    window hide
    "Complete the drawing by choosing the appropriate keyframes."
    window show

    call screen answers

    scene bg library
    show sam at center
    if ans == "right":
        sam "Thats right!"
    else:
        sam "Try again."
        jump act1

    return

screen answers():
    modal True
    zorder 100
    default ans = None

    imagebutton:
        yalign -700
        xalign 0.2
        idle Transform("right1.jpg", matrixcolor=BrightnessMatrix(0.1))
        hover "right1.jpg"
        action [SetVariable("ans", "right"), Return()]
        focus_mask True
        at character_hover

    imagebutton:
        yalign -700
        xalign 0.8
        idle Transform("wrong1.png", matrixcolor=BrightnessMatrix(0.1))
        hover "wrong1.png"
        action [SetVariable("ans", "wrong"), Return()]
        focus_mask True
        at character_hover



screen myCharacter():
    modal True

    imagebutton:
        ypos 130
        xpos 100
        idle Transform("Laura.png", matrixcolor=SaturationMatrix(0.0))
        hover "Laura.png"
        action [SetVariable("gender", "f"), Return()]
        focus_mask True
        at character_hover
    
    imagebutton:
        ypos 100
        xpos 1000
        idle Transform("Dante.png", matrixcolor=SaturationMatrix(0.0))
        hover "Dante.png"
        action [SetVariable("gender", "m"), Return()]
        focus_mask True
        at character_hover

label extraDiag:
    show playerSprite at left

    show ari at right, flipped
    player "Hello!"
    ari "Oh, hi!"
    player "Are you in the Class for ANI 2, 2D, 3D Methodology and Principles?"
    ari "Yes!"
    player "We are both very late! Do you know what the class is about? I wasn’t able to read into it."
    ari "Yeah, unfortunately HAHA. Oh I think it’s gonna be about Pose-to-pose keyframing for animation. It’s about an animation technique where animators draw key poses."

    jump startClass

    return


