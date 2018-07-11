from tabulate import tabulate

class Speed:
    def __init__(self, speed, phase_1, phase_2, phase_3, phase_4, phase_5, ram_dmg):
        self.speed = speed
        self.phase_1 = phase_1
        self.phase_2 = phase_2
        self.phase_3 = phase_3
        self.phase_4 = phase_4
        self.phase_5 = phase_5
        self.ram_dmg = ram_dmg

class Move_Chart:
    def __init__(self):
        self.speeds = []
        for i in range(61):
            self.speeds.append(Speed(
                i * 5,  # your speed
                self.calc_move(i * 5, 1),  # phase 1 movement
                self.calc_move(i * 5, 2),  # 2
                self.calc_move(i * 5, 3),  # 3
                self.calc_move(i * 5, 4),  # 4
                self.calc_move(i * 5, 5),  # 5,
                self.calc_ram(i * 5)       # ramming damage
            ))

    def calc_move(self, speed, phase):
        # Brute Force - Fix Later
        adjuster_2 = [10, 5, 0, 0, 0]
        if phase == 1 and speed == 5:
            return 0.5
        if phase == 1 and speed == 10:
            return 1
        if phase == 2 and speed == 35:
            return 0.5

        # Adusts to fit chart in rule book
        adjuster = [10, 35, 10, 40, 20, ]
        if speed - adjuster[phase - 1] >= 0:  # Safety prevents negative numbers
            speed -= adjuster[phase - 1]     # making weird shit
        else:
            speed = 0

        if speed == 0:
            return 0
        move = (speed / 50) + 1
        move -= ((move / 1) - (move // 1))
        move += 0.5 if (speed + adjuster_2[phase - 1]) % 50 == 5 else 0
        return move

    def calc_ram(self, speed):
        if speed >= 30:
            return (speed / 5) - 5
        elif speed == 25 or speed == 20:
            return 1
        elif speed == 5:
            return -4
        elif speed == 10:
            return -2
        elif speed == 15:
            return -1
        else:
            return 0

mc = Move_Chart()
'''
print("Speed    Phase 1     Phase 2     Phase 3")
for s in mc.speeds:
    print(str(s.speed) + "      " + str(s.phase_1) + "          " + str(s.phase_2))
    '''
test = []
for s in mc.speeds:
    test.append(
        [
            s.speed,
            s.phase_1,
            s.phase_2,
            s.phase_3,
            s.phase_4,
            s.phase_5,
            s.ram_dmg
        ]
    )
print(tabulate(
    test, 
    headers = [
        'Speed', 
        'Phase 1', 
        'Phase 2', 
        'Phase 3', 
        'Phase 4', 
        'Phase 5',
        'Ram Damage'
    ]
))