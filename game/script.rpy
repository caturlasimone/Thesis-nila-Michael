define ari = Character("Ari", color="#c92a5a")
define lina = Character("Lina", color="#311c4b")
define sam = Character("Sam", color="#864317")

default player = None
default gender = None

image playerSprite = ConditionSwitch(
    "gender == 'f'", "Laura.png",
    "gender == 'm'", "Dante.png"
)

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

    jump story

    return

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

label story:
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
            player " it means to focus on the most important, or Key, moments of an action first, and then we fill in the frames between them."
            sam "Thats right! Thank you for answering."

    hide playerSprite

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
    return

label extraDiag:
    show playerSprite at left

    show ari at right, flipped
    player "Hello!"
    ari "Oh, hi!"
    player "Are you in the Class for ANI 2, 2D, 3D Methodology and Principles?"
    ari "Yes!"
    player "We are both very late! Do you know what the class is about? I wasn’t able to read into it."
    ari "Yeah, unfortunately HAHA. Oh I think it’s gonna be about Pose-to-pose keyframing for animation. It’s about an animation technique where animators draw key poses."

    return

