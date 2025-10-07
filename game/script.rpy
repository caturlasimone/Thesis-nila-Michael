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


