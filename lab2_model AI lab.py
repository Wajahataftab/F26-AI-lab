
class ClassroomReflexAgent:
    def act(self, temp, occupied):
        if not occupied:
            return "ECO"
        elif temp > 26:
            return "COOL"
        elif temp < 20:
            return "WARM"
        else:
            return "IDLE"
class ClassroomStatefulAgent:
    def __init__(self):
        self.previous_mode = None
    def act(self, temp, occupied):
        old_mode = self.previous_mode
        if not occupied:
            target_mode = "ECO"
        elif temp > 26:
            target_mode = "COOL"
        elif temp < 20:
            target_mode = "WARM"
        else:
            target_mode = "IDLE"
        if target_mode != self.previous_mode:
            send_command = True
        else:
            send_command = False
        self.previous_mode = target_mode
        return old_mode, target_mode, send_command
