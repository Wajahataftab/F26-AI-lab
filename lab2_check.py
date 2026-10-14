
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

        send_command = target_mode != self.previous_mode
        self.previous_mode = target_mode

        return target_mode, send_command


agent = StatefulClassroomAgent()

test_cases = [
    ("Hot classroom", 29, True, "COOL", True),
    ("Repeated hot reading", 29, True, "COOL", False),
    ("Lower boundary", 20, True, "IDLE", True),
    ("Upper boundary", 26, True, "IDLE", False),
    ("Cold classroom", 19, True, "WARM", True),
    ("Empty classroom", 29, False, "ECO", True),
    ("Repeated empty reading", 29, False, "ECO", False)
]

for name, temp, occupied, expected_mode, expected_send in test_cases:
    actual_mode, actual_send = agent.act(temp, occupied)

    passed = (
        actual_mode == expected_mode
        and actual_send == expected_send
    )

    print(
        name,
        "| Expected:", expected_mode, expected_send,
        "| Actual:", actual_mode, actual_send,
        "|", "PASS" if passed else "FAIL"
    )

