
from lab2_model import ClassroomReflexAgent, ClassroomStatefulAgent
percepts = [
    (29, True),
    (29, True),
    (26, True),
    (20, True),
    (19, True),
    (29, False),
    (29, False)
]
reflex = ClassroomReflexAgent()
stateful = ClassroomStatefulAgent()
print("TASK 3: SMART CLASSROOM AGENT")
print("------------------------------")
print("\nREFLEX AGENT RESULTS")
for temp, occupied in percepts:
    target = reflex.act(temp, occupied)
    print(
        "Percept:", (temp, occupied),
        "| Target:", target
    )
print("\nSTATEFUL AGENT COMMAND TRACE")
for temp, occupied in percepts:
    old_mode, target, send_command = stateful.act(
        temp, occupied
    )
    if send_command:
        outcome = "Send Command"
    else:
        outcome = "No Command"
    print(
        "Previous Mode:", old_mode,
        "| Percept:", (temp, occupied),
        "| Target:", target,
        "| Outcome:", outcome
    )
