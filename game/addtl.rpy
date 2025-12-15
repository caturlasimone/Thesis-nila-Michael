define lina = Character("Lina", color="#311c4b")

label sceneSix:
    scene bg stairs

    "After class, you decided to do your assignment at a nearby cafe..."

    scene bg otwcafe:
        zoom 1.5

    "As you walk on the way to the cafe, you hear someone calling your name..."

    show lina at center
    "Hey! [playerName] wait up!"

    show lina at left with move
    show playerSprite at right

    player "Oh! Hey... you are?"
    lina "Wait, let me catch my breath..."
    player "..."
    lina "Phew!"
    lina "I'm Lina, we're in Mr. Sam's class together."
    lina "I think this is yours?"

    "Proceeds to hand over your sketch pad."

    player "Oh! I didn't notice I forgot to get it at my table. I was in such a rush!"
    lina "Yeah I noticed it when you left. I gotta admit that I have taken a look inside your sketch book"
    lina "and your drawings are impressive!"
    player "Oh! Thank you…"
    lina "By the way, are you going to do your assignment at this cafe?"
    player "Yes, I just thought of doing it in a different environment and also I get distracted at home."
    player "That's why I decided to do our assignment at a cafe."

    menu:
        lina "Oh! Can I join you?"

        "Yes!":
            lina "Yay! Thank you! It's better to work with someone"
            jump sceneSeven

        "I would like to work alone…":
            lina "Oh, come on! You’ll need my help, somehow, I promise!"
            player "Ok fineee"
            jump sceneSeven

    return

label sceneSeven:
    hide lina
    hide playerSprite

    "You both continued your way to the cafe."

    scene bg cafe
    "After a couple minutes, as you make progress on your assignment, you show frustration to your own work."

    "Lina notices your frustration."
    show lina at center
    lina "What's wrong, [playerName]?"

    show lina at left with move
    show playerSprite at right

    player "My characters don't feel alive"
    player "They don't have a story. They just... exist."

    "Lina smiled and pulled up a chair."

    lina "I can help with that."
    lina " A way to make your characters move is called pose-to-pose animation. It's all about storytelling through action."

    "You tilt your head."

    player "Pose-to-pose?"

    "Lina grabbed your pencil."

    lina "Think of it like this: every story has key moments."
    lina "In animation, we call these key poses. These are the most important, dramatic poses that tell the story of the action."
    lina "The poses in between the key poses, the ones that smooth out the action, are called in-betweens."

    "Lina drew a stick figure leaping through the air."

    lina "First, you draw the character at the very start of the action—this is your starting key pose."

    "Lina drew a character preparing to jump."

    lina "Then, you draw them at the very peak of the action—that's your mid-action key pose."

    "Lina drew the figure at the top of its leap."

    lina "And finally, you draw them at the end of the action—your ending key pose."

    "Lina drew the figure landing softly."
    "Lina continued, drawing the little transition poses between the key poses."

    lina "They're like the sentences that connect the most important parts of a story."
    lina "Without them, you get a disjointed set of moments. With them, you get a smooth, flowing narrative."

    "Your eyes lit up and you finally understood."
    "The pose-to-pose method wasn't just about drawing. It was about thinking of a story as a series of impactful moments."

    hide lina
    show playerSprite at center with move
    "Lina went back to her desk and you began a new drawing: 'A girl was reaching for a book on a high shelf'"

    jump sceneEight
    
    return

label sceneEight:
    "What is the proper sequence of your drawing?"
    #Last Activity

    "You  drew the key poses first, then filled in the in-betweens, carefully drawing the way her hand moved, the way her body shifted."
    "When he was done, the girl didn't just exist; she was alive. She had a story. She was reaching, straining, and finally, succeeding."

    "You looked at your own drawing. It wasn't just a picture of a girl with a book."
    "It was a story of determination and success, told one pose at a time."
    "From that day on, your drawings never felt stiff again. They were full of life, action, and, most importantly, a story."

    jump rollCredits
    
    return

label rollCredits:
    window hide

    #scene black
    scene expression Solid("#f08daf")

    show screen creditscreen with fade
    pause 100 # or however long it takes to scroll through in a reasonable speed
    pause

    hide screen creditscreen

    return
