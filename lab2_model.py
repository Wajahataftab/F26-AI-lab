
class StatefulClassroomAgent:
    def __init__(self):
        self.previous_mode = "IDLE"

    def act(self, temp, occupied):
        if not occupied:
            target_mode = "ECO"
        elif temp > 26:
            target_mode = "COOL"
        elif temp < 20:
            target_mode = "WARM"
        else:
            target_mode = "IDLE"

        previous_mode = self.previous_mode

        if target_mode != previous_mode:
            command = "SEND"
        else:
            command = "NO COMMAND"

        self.previous_mode = target_mode

        return previous_mode, target_mode, command


agent = StatefulClassroomAgent()

percepts = [
    (29, True),
    (29, True),
    (20, True),
    (26, True),
    (19, True),
    (29, False),
    (29, False)
]

for step, percept in enumerate(percepts, 1):
    temp, occupied = percept

    previous, target, command = agent.act(temp, occupied)

    print(
        "Step:", step,
        "| Previous mode:", previous,
        "| Percept:", percept,
        "| Target mode:", target,
        "| Command:", command
    )

