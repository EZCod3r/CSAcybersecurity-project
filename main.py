def on_on_chat():
    player.say("§5Assembly is now in session.§r")
    player.execute("playsound lesson.assembly @a")
player.on_chat("assembly", on_on_chat)

def on_on_chat2():
    global post, Questpoints
    if post == 0:
        post = 1
        agent.teleport(world(-139, -22, -9), WEST)
        player.say("§aThink before you post! Your digital footprint lasts forever. Never share your location or travel plans.§r")
        player.execute("playsound lesson.post @s")
        Questpoints += 1
        music.play_sound(Sound.LEVEL_UP)
        loops.pause(1000)
        player.say("§3Quest Point  + 1")
        loops.pause(3000)
        gameplay.title(mobs.target(LOCAL_PLAYER),
            "" + str(Questpoints) + "of 7",
            "discovered")
        if Questpoints == 7:
            player.run_chat_command("WINNER")
            player.teleport(world(-265, -60, -40))
            agent.teleport(world(-233, -59, -40), WEST)
    else:
        player.say("§dYou have already discovered \"post\" ")
player.on_chat("post", on_on_chat2)

def on_on_chat3():
    global spot, Questpoints
    if spot == 0:
        spot = 1
        agent.teleport(world(-234, -60, -86), SOUTH)
        player.say("§aSpot the red flags! If an email creates a sense of panic or urgency, it's probably a trick.§r")
        player.execute("playsound lesson.spot @a")
        Questpoints += 1
        music.play_sound(Sound.LEVEL_UP)
        loops.pause(1000)
        player.say("§3Quest Point  + 1")
        loops.pause(3000)
        gameplay.title(mobs.target(LOCAL_PLAYER),
            "" + str(Questpoints) + "of 7",
            "discovered")
        if Questpoints == 7:
            player.run_chat_command("WINNER")
            player.teleport(world(-265, -60, -40))
            agent.teleport(world(-233, -59, -40), WEST)
    else:
        player.say("§dYou have already discovered \"spot\" ")
player.on_chat("spot", on_on_chat3)

def on_on_chat4():
    gameplay.title(mobs.target(LOCAL_PLAYER), "§6CYBER-HERO!", "")
    player.say("§6CONGRATULATIONS! You are a Cyber-Hero!")
    for index in range(5):
        mobs.spawn(CHICKEN, pos(0, 10, 0))
    music.play_sound(Sound.LEVEL_UP)
    player.execute("playsound lesson.congratulations @a")
    music.play_music(MusicDisc.OTHERSIDE)
player.on_chat("WINNER", on_on_chat4)

def on_on_chat5():
    global secure, Questpoints
    if secure == 0:
        secure = 1
        agent.teleport(world(-232, -60, -12), WEST)
        player.say("§aA secure password is long, unique, and never shared with friends. Keep your digital house locked!§r")
        player.execute("playsound lesson.secure @a")
        Questpoints += 1
        music.play_sound(Sound.LEVEL_UP)
        loops.pause(1000)
        player.say("§3Quest Point  + 1")
        loops.pause(3000)
        gameplay.title(mobs.target(LOCAL_PLAYER),
            "" + str(Questpoints) + "of 7",
            "discovered")
        if Questpoints == 7:
            player.run_chat_command("WINNER")
            player.teleport(world(-265, -60, -40))
            agent.teleport(world(-233, -59, -40), WEST)
    else:
        player.say("§dYou have already discovered \"secure\" ")
player.on_chat("secure", on_on_chat5)

def on_on_chat6():
    global phishing, Questpoints
    if phishing == 0:
        phishing = 1
        agent.teleport(world(-218, -60, -1), SOUTH)
        player.say("§aPhishing is when hackers go 'fishing' for your passwords using fake links. Don't bite the hook!§r")
        player.execute("playsound lesson.phishing @a")
        Questpoints += 1
        music.play_sound(Sound.LEVEL_UP)
        loops.pause(1000)
        player.say("§3Quest Point  + 1")
        loops.pause(3000)
        gameplay.title(mobs.target(LOCAL_PLAYER),
            "" + str(Questpoints) + "of 7",
            "discovered")
        if Questpoints == 7:
            player.run_chat_command("WINNER")
            player.teleport(world(-265, -60, -40))
            agent.teleport(world(-233, -59, -40), WEST)
    else:
        player.say("§dYou have already discovered \"phishing\" ")
player.on_chat("phishing", on_on_chat6)

def on_on_chat7():
    global aware, Questpoints
    if aware == 0:
        aware = 1
        agent.teleport(world(-236, -35, -7), SOUTH)
        player.say("§aCyber-Awareness means knowing that not everything online is real. Always double-check!§r")
        player.execute("playsound lesson.aware @a")
        Questpoints += 1
        music.play_sound(Sound.LEVEL_UP)
        loops.pause(1000)
        player.say("§3Quest Point  + 1")
        loops.pause(3000)
        gameplay.title(mobs.target(LOCAL_PLAYER),
            "" + str(Questpoints) + "of 7",
            "discovered")
        if Questpoints == 7:
            player.run_chat_command("WINNER")
            player.teleport(world(-265, -60, -40))
            agent.teleport(world(-233, -59, -40), WEST)
    else:
        player.say("§dYou have already discovered \"aware\" ")
player.on_chat("aware", on_on_chat7)

def Guide():
    agent.teleport(world(-295, -60, -30), WEST)
    agent.move(FORWARD, 6)
    player.execute("playsound lesson.hello1 @a")
    player.say("§6Hello! I am Nano, your helpful guide around KHS world.")
    loops.pause(4500)
    player.execute("playsound lesson.hello2 @a")
    player.say("§6Today, we are going to learn how cybersecurity impacts our daily lives.")
    loops.pause(4500)
    player.execute("playsound lesson.hello3 @a")
    player.say("§6Whenever you're ready, head over to the guard house and enter the school premises.")

def on_on_chat8():
    global deepfake, Questpoints
    if deepfake == 0:
        deepfake = 1
        agent.teleport(world(-216, -44, 47), SOUTH)
        player.say("§aDeepfakes use AI to make people look or say things they never did. Don't believe everything you see.§r")
        player.execute("playsound lesson.deepfake @a")
        Questpoints += 1
        music.play_sound(Sound.LEVEL_UP)
        loops.pause(1000)
        player.say("§3Quest Point  + 1")
        loops.pause(3000)
        gameplay.title(mobs.target(LOCAL_PLAYER),
            "" + str(Questpoints) + "of 7",
            "discovered")
        if Questpoints == 7:
            player.run_chat_command("WINNER")
            player.teleport(world(-265, -60, -40))
            agent.teleport(world(-233, -59, -40), WEST)
    else:
        player.say("§dYou have already discovered \"deepfake\" ")
player.on_chat("deepfake", on_on_chat8)

def on_on_chat9():
    global scam, Questpoints
    if scam == 0:
        scam = 1
        agent.teleport(world(-264, -45, -127), EAST)
        player.say("§aIf a stranger offers you 'Free Coins' or 'Prizes' in exchange for data, it is always a scam.§r")
        player.execute("playsound lesson.scam @a")
        Questpoints += 1
        music.play_sound(Sound.LEVEL_UP)
        loops.pause(1000)
        player.say("§3Quest Point  + 1")
        loops.pause(3000)
        gameplay.title(mobs.target(LOCAL_PLAYER),
            "" + str(Questpoints) + "of 7",
            "discovered")
        if Questpoints == 7:
            player.run_chat_command("WINNER")
            player.teleport(world(-265, -60, -40))
            agent.teleport(world(-233, -59, -40), WEST)
    else:
        player.say("§dYou have already discovered \"scam\" ")
player.on_chat("scam", on_on_chat9)

scam = 0
deepfake = 0
aware = 0
phishing = 0
secure = 0
spot = 0
post = 0
Questpoints = 0
Questpoints = 0
player.teleport(world(-306, -60, -30))
Guide()
gameplay.set_game_mode(CREATIVE, mobs.target(LOCAL_PLAYER))
