# Store the narratives, strings...


class nothing:
    floor = [
        'It is nothing there.',
        'You tried to wipe away the dirt on the floor, though it is dirt under it.',
        'You found nothing special.', 'The is nothing at this spot, even wind.'
    ]
    wall = [
        'You can not find anything special on the wall.',
        'It is an acient wall, very tough.',
        'Cold wall beside another cold wall.'
    ]


class enter:
    portal = [
        'You passed the portal and fall on to a cold floor. It is hurt...',
        'There is no light on the other side of the portal. Or... very dim light from nowhere.',
        'Is there any way back? It is no way back. You are in an acient... building or dungeon?'
    ]


class floor:
    actions = ["   Look   ", "   Touch  ", "   Taste  ", "    Dig   "]
    narratives = {
        "   Look   ": [
            'It is nothing there.', 'You found nothing special.',
            'The is nothing at this spot, even wind.'
        ],
        "   Touch  ": [
            'You tried to wipe away the dirt on the floor, though it is dirt under it.',
            'It is a tight floor made with dry dirt, or something like sand stone.',
            'One thing you can tell is no one has been here for long time.'
        ],
        "   Taste  ": [
            'You put down your face and licked the floor... Are you nut?',
            'People losts minds like you... when they are in a such place.',
            'The dirt tates like a juicy steak... oh... Are you kidding me?'
        ],
        "    Dig   ":
        ['It is not smart to dig the floor like this with hands...']
    }


class wall:
    actions = ["   Look   ", "   Touch  ", "   Push   ", "   Kick   "]
    narratives = {
        "   Look   ": [
            'You can not find anything special on the wall.',
            'It is an acient wall, very tough.',
            'Cold wall beside another cold wall.'
        ],
        "   Touch  ": [
            'The wall is made with hard rocks, or bricks, I think...',
            'Small cracks on the wall. You can feel the bumpiness.',
            'It is a little bit wet, since water condensation.'
        ],
        "   Push   ": [
            'You push the wall inside with your two hands. It does not move.',
            'You do not feel you have the strength to move the wall.'
        ],
        "   Kick   ": [
            'It is not smart to kick the rock with your foot...',
            'If you break your leg, you will be stuck in this place.',
            'Are you sure?', 'Better to try something else... maybe bite it?'
        ]
    }


class joke:
    actions = ["   Look   ", "   Touch  ", "   Push   ", "   Kick   "]
    narratives = {
        "   Look   ": [
            'You found there are letters on the wall, and read them out slowly.',
            'The wall has a stone embedded in it. There are words on the stone.',
        ],
        "   Touch  ": [
            'It is a whole piece of stone embedded inside the wall',
            'Small letters carved on the wall. You can feel the bumpiness.',
            'It is a little bit wet, since water condensation.'
        ],
        "   Push   ": [
            'You push the wall inside with your two hands. It does not move.',
            'You do not feel you have the strength to move the wall.'
        ],
        "   Kick   ": [
            'It is not smart to kick the rock with your foot...',
            'If you break your leg, you will be stuck in this place.',
            'Are you sure?', 'Better to try something else... maybe bite it?'
        ]
    }


# Joke ['What did one ocean say to another ocean?Nothing they just waved', 'What do you call a belt made out of watches? A waist of time', 'What do you call a fish with no eyes? A fsh', 'What is Forrest Gump`s mail password? 1forrest1', 'What do you call a wizard who just ran a marathon? Ron Wheezly', 'A man ended up in hospital today, covered in wood and hay, with a horse inside him. His condition is described as stable', 'What do you call an aligator that can read maps? Navi-Gator ', 'The rotation of earth really makes my day', 'What do skeletons say before the start to eat? Bone appetite', 'What does the roof say to the house? I got you covered','What is Jafar when he is next to you? Ja-near', 'What do you call a plant you can see from far? Seaweed', 'My friend did not want to hang out because he had a pimple. I think that is a pore excuse', 'My keyboard is so messed up. I have lost ctrl', 'What did the eye say to the other eye? Something between us smells', ];
# http://random-ize.com/bad-jokes/


class stele:
    actions = ["   Look   ", "   Touch  ", "   Read   ", "   Kick   "]
    narratives = {
        "   Look   ": [
            'It is a huge stone plate standing on the floor.',
            'The big stone stele is about 2 people tall.',
            'There are a lot of words carved on the stone plate.'
        ],
        "   Touch  ": [
            'The material is felt like wood not as cold as stone, though it looks like stone.',
            'The made of the stele is something special, it is not stone, or at least common stones.',
            'It may need 3 people to hug around this big stuff.'
        ],
        "   Read   ": [
            '''
Traveller, welcome to my palace. If you came from the world of emojis, you are now in a new parralell universe.
You do not need go back to your world. You are encouraged to stay here forever and become a part of my palace. 
PUT MORE USER GUIDE HERE....

'''
        ],
        "   Kick   ": [
            'You kicked the stone stele hard. It is not as steady as you expected.',
            'Though it sounds not clever, kicking the big stele made it moved a little.',
            'It is not stone. You know it after kicking on it. It is not that heavy.'
        ]
    }
