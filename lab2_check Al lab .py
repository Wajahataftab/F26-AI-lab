

from lab2_model import ClassroomReflexAgent
agent = ClassroomReflexAgent()
test_cases = [
    {
        "name": "Hot and occupied",
        "input": (29, True),
        "expected": "COOL"
    },
    {
        "name": "Normal temperature",
        "input": (24, True),
        "expected": "IDLE"
    },
    {
        "name": "Low temperature",
        "input": (19, True),
        "expected": "WARM"
    },
    {
        "name": "Empty classroom",
        "input": (29, False),
        "expected": "ECO"
    },
    {
        "name": "Upper boundary",
        "input": (26, True),
        "expected": "IDLE"
    },
    {
        "name": "Lower boundary",
        "input": (20, True),
        "expected": "IDLE"
    }
]
passed = 0
for case in test_cases:
    temp, occupied = case["input"]
    actual = agent.act(temp, occupied)
    print("\nTest Case:", case["name"])
    print("Input:", case["input"])
    print("Expected:", case["expected"])
    print("Actual:", actual)
    if actual == case["expected"]:
        print("Test Passed")
        passed = passed + 1
    else:
        print("Test Failed")
print("\nTotal Tests:", len(test_cases))
print("Passed:", passed)
print("Failed:", len(test_cases) - passed)
