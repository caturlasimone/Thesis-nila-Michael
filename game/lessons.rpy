transform scrollBackground:
    rotate -90
    yalign 0.5

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

    scene bg jump at scrollBackground:
        xpos -800
        zoom 1.4
        linear 10.0 xpos -2000
    sam "Now, if you scrub the timeline, you’ll see the character pop instantly between these three poses. That’s okay! This is our Block."
    sam "It allows us to review the overall action, timing, and silhouettes immediately, before doing any extra drawing."
    sam "The animation looks jerky because the software is just moving in a straight line between our Keys."

    scene bg library
    show sam at center

    menu:
        sam "Is everthing clear to you, class?"

        "Yes, lets discuss the next topic!":
            jump breakdown
        "No, can we go over KEY POSES again?":
            jump keyposes

    return

label breakdown:
    sam "Our next topic is 'Breakdowns'."
    sam "A 'Breakdown' is a pose that defines the path and feel of the transition between two Key Poses."

    hide sam with dissolve

    scene bg jump2 at scrollBackground:
        xpos -210
        zoom 0.8
        linear 13.0 xpos -1100

    sam "Let's look between Key Pose 1 (Anticipation) and Key Pose 2 (Apex). The character needs an explosive launch frame."
    sam "This pose should show the character's body fully stretched out, pushing off the ground, emphasizing the force of the jump. This Breakdown controls the beginning of the movement."
    sam "We can also add Breakdowns to manage arcs. Remember the principle of Arcs—motion should generally follow a curved path. Our Breakdown should ensure the jump isn't a straight vertical line."
    sam "Once you have your Key Poses and Breakdowns, you have the main structure. The final step is filling in the smaller gaps—the In-betweens—and adjusting the Timing and Spacing."

    scene bg library
    show sam at center

    menu:
        sam "Is everthing clear to you, class?"

        "Yes, lets discuss the next topic!":
            jump inbetween
        "No, can we go over BREAKDOWN again?":
            jump breakdown

    return

label inbetween:
    scene white
    show inbtwn1:
        yalign 0.8
        xalign 0.5
        rotate -90
        zoom 0.5

    sam "The inbetween are the drawings or frames that fill the gaps between Keyframes and Breakdowns, created to smooth out the transition."

    #scene white
    show inbtwn2:
        yalign 0.7
        xalign 0.5
        rotate -90
        zoom 0.5

    sam "This will create the illusion of fluid, continuous motion and is responsible for the subtleties of speed and weight."

    scene bg library
    show sam at center

    menu:
        sam "Is everthing clear to you, class?"

        "Yes, lets discuss the next topic!":
            jump timing
        "No, can we go over BREAKDOWN again?":
            jump inbetween

    return

label timing:
    sam "Timing refers to how long the movement will be."
    sam "If the jump feels too slow, you move the Key Poses closer together on the timeline. If it’s too fast, spread them out."
    sam "The Spacing on the other hand, is how it moves. The space between the poses tells us the speed."

    scene white
    show bg slowin:
        rotate -90
        yalign 0.5
        xalign 0.5
        zoom 0.55

    sam "The Slow-in is usually placed near the beginning of a movement."
    sam "More Keyframe drawings are placed close to the initial pose to show a gradual acceleration."

    show bg slowout

    sam "Meanwhile, the Slow-out is usually placed near the end of a movement."
    sam "More Keyframe drawings are placed close to the final pose to show a gradual deceleration."

    jump outro

label outro:
    scene bg library
    show sam at center

    sam "By controlling your Key Poses, Breakdowns, and finally your spacing and timing, you get complete control over the illusion of life!"
    sam "Pose-to-Pose is a planning process that guarantees a strong performance."

    menu:
        sam "Is everthing clear to you, class?"

        "Yes, that was super helpful!":
            sam "Great to hear! Now, let’s put that into practice with a quick activity."
            jump actIntro
        "Could we go over KEY POSES again?":
            sam "Sure!"
            jump keyposes
        "Could you explain BREAKDOWN again?":
            sam "Sure!"
            jump breakdown
        "Can we revisit the part about TIMING AND SPACING?":
            sam "Sure!"
            jump timing
        #"Can you run through SLOW IN & SLOW OUT again?":
        #    sam "Sure!" 
    
    return
