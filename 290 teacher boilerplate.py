from controller import Robot, Keyboard

bot = Robot()
keyboard = Keyboard()

timestep = 64

# Arm joints
shoulder_lift = bot.getDevice('shoulder_lift_joint')
shoulder_pan = bot.getDevice('shoulder_pan_joint')
elbow = bot.getDevice('elbow_joint')
wrist_1 = bot.getDevice('wrist_1_joint')
wrist_2 = bot.getDevice('wrist_2_joint')
wrist_3 = bot.getDevice('wrist_3_joint')

# finger 1 joints
finger_1 = bot.getDevice('palm_finger_1_joint')
finger_1_lower_knuckle = bot.getDevice('finger_1_joint_1')
finger_1_middle_knuckle = bot.getDevice('finger_1_joint_2')
finger_1_upper_knuckle = bot.getDevice('finger_1_joint_3')

# finger 2 joints
finger_2 = bot.getDevice('palm_finger_2_joint')
finger_2_lower_knuckle = bot.getDevice('finger_2_joint_1')
finger_2_middle_knuckle = bot.getDevice('finger_2_joint_2')
finger_2_upper_knuckle = bot.getDevice('finger_2_joint_3')

# finger middle joints
finger_3_lower_knuckle = bot.getDevice('finger_middle_joint_1')
finger_3_middle_knuckle = bot.getDevice('finger_middle_joint_2')
finger_3_upper_knuckle = bot.getDevice('finger_middle_joint_3')

# enabling devices
keyboard.enable(timestep)

# method to move the arm
def move_bot(a = 0, b = 0, c = 0, d = 0, e = 0, f = 0, 
             g = 0.17, h = 0.05, i = 0, j = -0.06):
    
    # arm joints
    shoulder_lift.setPosition(a)
    shoulder_pan.setPosition(b)
    elbow.setPosition(c)
    wrist_1.setPosition(d)
    wrist_2.setPosition(e)
    wrist_3.setPosition(f)
    
    # finger palm joints
    finger_1.setPosition(g)
    finger_2.setPosition(g)
    
    # finger lower knuckle motor
    finger_1_lower_knuckle.setPosition(h)
    finger_2_lower_knuckle.setPosition(h)
    finger_3_lower_knuckle.setPosition(h)
    
    # finger middle knuckle motor
    finger_1_middle_knuckle.setPosition(i)
    finger_2_middle_knuckle.setPosition(i)
    finger_3_middle_knuckle.setPosition(i)
    
    # finger upper knuckle motor
    finger_1_upper_knuckle.setPosition(j)
    finger_2_upper_knuckle.setPosition(j)
    finger_3_upper_knuckle.setPosition(j)
    

# moving bot at initial positions
move_bot()

# variables to track joint positions
shoulder_lift_pos = 0
shoulder_pan_pos = 0
elbow_pos = 0
wrist_1_pos = 0
wrist_2_pos = 0
wrist_3_pos = 0
finger_pos = 0.17
lower_knuckle_pos = 0.05
middle_knuckle_pos = 0
upper_knuckle_pos = -0.06

while bot.step(timestep)  !=  -1:
    
    keypressed = keyboard.getKey() 
        
    if keypressed  ==  317:                # down key is pressed
        shoulder_lift_pos += 0.01
    elif keypressed  ==  315:              # up key is pressed
        shoulder_lift_pos -= 0.01
    elif keypressed  ==  314:              # left key is pressed
        shoulder_pan_pos += 0.01
    elif keypressed  ==  316:              # right key is pressed
        shoulder_pan_pos -= 0.01
    elif keypressed  ==  87:               # w key is pressed
        elbow_pos -= 0.01
    elif keypressed  ==  83:               # s key is pressed
        elbow_pos += 0.01
    elif keypressed  ==  65:               # a key is pressed
        wrist_1_pos += 0.01
    elif keypressed  ==  68:               # d key is pressed
        wrist_1_pos -= 0.01
    elif keypressed  ==  49:               # 1 key is pressed
        wrist_2_pos += 0.01
    elif keypressed  ==  50:               # 2 key is pressed
        wrist_2_pos -= 0.01
    elif keypressed  ==  51:               # 3 key is pressed
        wrist_3_pos += 0.01
    elif keypressed  ==  52:               # 4 key is pressed
        wrist_3_pos -= 0.01
    elif keypressed  ==  53:               # 5 is pressed
        finger_pos += 0.01
    elif keypressed  ==  54:               # 6 is pressed
        finger_pos -= 0.01
    elif keypressed  ==  55:               #  7 is pressed
        lower_knuckle_pos += 0.01
    elif keypressed  ==  56:               #  8 is pressed
        lower_knuckle_pos -= 0.01
    elif keypressed  ==  57:               #  9 is pressed
        middle_knuckle_pos += 0.01
    elif keypressed  ==  48:               #  0 is pressed
        middle_knuckle_pos -= 0.01
    elif keypressed  ==  45:               # - is pressed
        upper_knuckle_pos -= 0.01
    elif keypressed  ==  61:               #  + is pressed
        upper_knuckle_pos += 0.01
        
    
    move_bot(0.15, 1.57, -0.1, 
             -0.04, wrist_2_pos, wrist_3_pos, finger_pos,
             0.3, 0.3, upper_knuckle_pos)