transform scrollBackground2:
    rotate -90
    yalign 0.5
    zoom 0.8
    xpos -170
    linear 5.0 xpos -1150

label actIntro:
    scene bg library
    show sam at center

    sam "Get ready to answer Questions!"

    menu:
        "Shall we begin?"

        "No, I need to go over the topics again.":
            scene bg jump:
                rotate -90
                yalign 0.5
                xpos -800
                zoom 1.4
                linear 10.0 xpos -2000
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

            jump actIntro

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