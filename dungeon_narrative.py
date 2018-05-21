# Store the narratives, strings...

class nothing:
    floor = ['It is nothing there.','You tried to wipe away the dirt on the floor, though it is dirt under it.',
            'You found nothing special.', 'The is nothing at this spot, even wind.']
    wall = ['You can not find anything special on the wall.',
            'It is an acient wall, very tough.',
            'Cold wall beside another cold wall.']

class enter:
    portal =['You passed the portal and fall on to a cold floor. It is hurt...',
             'There is no light on the other side of the portal. Or... very dim light from nowhere.',
             'Is there any way back? It is no way back. You are in an acient... building or dungeon?']
             
class floor:
    actions = [ "   Look   ",
                "   Touch  ",
                "   Taste  ",
                "    Dig   "]
    narratives = {
        "   Look   ":['It is nothing there.',
                        'You found nothing special.', 'The is nothing at this spot, even wind.'],
        "   Touch  ":['You tried to wipe away the dirt on the floor, though it is dirt under it.',
                        'It is a tight floor made with dry dirt, or something like sand stone.',
                        'One thing you can tell is no one has been here for long time.'],
        "   Taste  ":['You put down your face and licked the floor... Are you nut?',
                        'People losts minds like you... when they are in a such place.',
                        'The dirt tates like a juicy steak... oh... Are you kidding me?'],
        "    Dig   ":['It is not smart to dig the floor like this with hands...']
    }
    
class wall:
    actions = [ "   Look   ",
                "   Touch  ",
                "   Push   ",
                "   Kick   "]
    narratives = {
        "   Look   ":['You can not find anything special on the wall.',
                        'It is an acient wall, very tough.',
                        'Cold wall beside another cold wall.'],
        "   Touch  ":['The wall is made with hard rocks, or bricks, I think...',
                        'Small cracks on the wall. You can feel the bumpiness.',
                        'It is a little bit wet, since water condensation.'],
        "   Push   ":['You push the wall inside with your two hands. It does not move.',
                        'You do not feel you have the strength to move the wall.'],
        "   Kick   ":['It is not smart to kick the rock with your foot...',
                        'If you break your leg, you will be stuck in this place.',
                        'Are you sure?',
                        'Better to try something else... maybe bite it?']
    }