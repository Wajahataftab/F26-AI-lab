# Lab 2: Intelligent Agents & the PEAS Framework

**Course:** Artificial Intelligence (Lab)  
**Student Name:** Wajahat Aftab  
**Roll Number:** SU92-BSSEM-S25-002  
**Class:** BSSEM-4A  
**Instructor:** Sir. Rasikh Ali  

---

## 📋 Table of Contents
1. [Introduction & Objectives](#-introduction--objectives)
2. [Problem Statement](#-problem-statement)
3. [Concepts and Assumptions](#-concepts-and-assumptions)
4. [Repository Structure & Files](#-repository-structure--files)
5. [Task 1: PEAS Specifications](#-task-1-peas-specifications)
6. [Task 2: Environment Classification](#-task-2-environment-classification)
7. [Task 3: Stateful Agent & Mode-Transition Trace](#-task-3-stateful-agent--mode-transition-trace)
8. [Reflex vs. Stateful Agent Comparison](#-reflex-vs-stateful-agent-comparison)
9. [Failure / Edge-Case Analysis](#-failure--edge-case-analysis)
10. [How to Run the Scripts](#-how-to-run-the-scripts)
11. [Reflection & Conclusion](#-reflection--conclusion)

---

## 🎯 Introduction & Objectives
* This lab studies intelligent agents, rational actions, the PEAS framework, and the difference between a simple reflex agent and an agent that keeps a small amount of internal state[cite: 3]. 
* A smart classroom example is used to choose simulated operating modes based on temperature and occupancy without controlling real equipment[cite: 3].

---

## 🔍 Problem Statement
* A classroom cooling agent should support comfort while avoiding unnecessary energy use when the room is empty[cite: 3]. 
* It receives temperature and occupancy percepts and selects one of four target modes: `ECO`, `COOL`, `WARM`, or `IDLE`[cite: 3]. 
* The extended agent remembers its previous target and avoids sending the same control command repeatedly[cite: 3].

---

## ⚙️ Concepts and Assumptions
* An agent receives percepts through sensors or inputs and selects actions through actuators or tools[cite: 3]. 
* A rational agent chooses an action expected to perform well against its stated performance measure and available information[cite: 3]. 
* Temperature is measured in degrees Celsius; occupied is `True` or `False`[cite: 3]. 
* An empty room has priority and targets `ECO` regardless of temperature[cite: 3]. 
* For an occupied room: temperature $> 26$ means `COOL`; temperature $< 20$ means `WARM`; otherwise `IDLE`[cite: 3]. Therefore, exactly 20°C and 26°C both produce `IDLE`[cite: 3]. 
* The initial previous mode is `IDLE`[cite: 3]. A command is sent only when the target differs from the remembered previous mode[cite: 3]. 
* All modes are simulated labels[cite: 3]. No real air conditioner, fan, sensor, or building system is controlled[cite: 3].

---

## 🗂 Repository Structure
* **`lab2_percepts.py`**: Simple stateless reflex agent script mapping percepts directly to target operating modes[cite: 3].
* **`lab2_model.py`**: Stateful classroom agent that stores the previous target mode and returns whether a new command should be sent[cite: 3].
* **`lab2_check.py`**: Test-case verification script validating agent behavior with edge cases[cite: 3].
* **`Lab2_Report.docx`**: Detailed lab report containing problem descriptions, PEAS tables, environment classifications, trace outputs, and reflection[cite: 3].

---

## 📝 Task 1 — PEAS Specifications

### 4.1 Delivery Robot
* **Performance:** Deliver the correct parcel to the correct destination; avoid collisions and protect people; meet a reasonable delivery time; conserve battery[cite: 3].
* **Environment:** Campus paths and corridors; students and staff; doors, lifts and ramps; weather; delivery points and temporary obstacles[cite: 3].
* **Actuators:** Drive wheels or motors; steering; brakes; speaker/display for warnings; parcel compartment lock[cite: 3].
* **Sensors:** Camera; lidar or ultrasonic distance sensor; wheel encoders; GPS or indoor localization; battery sensor; parcel/destination scanner[cite: 3].

### 4.2 LLM-Based Student-Support Agent
* **Performance:** Give accurate answers grounded in approved course material; explain concepts clearly; protect student privacy; acknowledge uncertainty and refer difficult cases to staff[cite: 3].
* **Environment:** Student questions; course notes and policies; learning-management system context if authorized; changing deadlines; ambiguous or incomplete requests[cite: 3].
* **Actuators:** Generate a text response; ask a clarifying question; retrieve approved documents using a search tool; provide a source link; refer the student to a human adviser[cite: 3].
* **Sensors:** Input message processor; user text interface; context retriever; document search interface[cite: 3].

---

## 🌐 Task 2 — Environment Classification

| System / model boundary | Observability | Determinism | Justification and examples[cite: 3] |
| :--- | :--- | :--- | :--- |
| **Delivery robot in a real campus** | Partially observable[cite: 3] | Stochastic[cite: 3] | The robot may not see around corners or know a person's intention. Pedestrians, wheel slip, weather and blocked paths make outcomes uncertain[cite: 3]. |
| **Delivery robot in a simplified simulator** | Fully observable (if full simulated state is exposed)[cite: 3] | Deterministic (if rules are fixed)[cite: 3] | If the simulator exposes every position and each action has a fixed result, outcomes are predictable. This is a property of simulator assumptions, not the real campus[cite: 3]. |
| **LLM student-support agent in a real service** | Partially observable[cite: 3] | Stochastic[cite: 3] | The agent sees supplied messages/retrieved documents but not the student's full situation or unstated intent. Language generation and user interactions vary[cite: 3]. |
| **LLM agent in a fixed test harness** | Fully observable (w.r.t test inputs/accessible docs)[cite: 3] | Not guaranteed deterministic[cite: 3] | The test harness may expose test data, but this does not reveal every real-world fact. Tool retrieval and responses can still introduce uncertainty[cite: 3]. |

---

## 📊 Task 3 — Stateful Agent and Trace
The stateful agent stores the previous target mode, returning the previous mode, new target, and a Boolean indicating whether a command should be sent[cite: 3].

| Step | Previous mode | Percept (temp, occupied) | Target | Command outcome[cite: 3] |
| :---: | :---: | :---: | :---: | :--- |
| 1[cite: 3] | IDLE[cite: 3] | (29, True)[cite: 3] | COOL[cite: 3] | SEND[cite: 3] |
| 2[cite: 3] | COOL[cite: 3] | (29, True)[cite: 3] | COOL[cite: 3] | NO COMMAND[cite: 3] |
| 3[cite: 3] | COOL[cite: 3] | (20, True)[cite: 3] | IDLE[cite: 3] | SEND[cite: 3] |
| 4[cite: 3] | IDLE[cite: 3] | (26, True)[cite: 3] | IDLE[cite: 3] | NO COMMAND[cite: 3] |
| 5[cite: 3] | IDLE[cite: 3] | (19, True)[cite: 3] | WARM[cite: 3] | SEND[cite: 3] |
| 6[cite: 3] | WARM[cite: 3] | (29, False)[cite: 3] | ECO[cite: 3] | SEND[cite: 3] |
| 7[cite: 3] | ECO[cite: 3] | (29, False)[cite: 3] | ECO[cite: 3] | NO COMMAND[cite: 3] |

---

## 🔄 Reflex vs. Stateful Agent
| Aspect | Reflex agent | Stateful agent[cite: 3] |
| :--- | :--- | :--- |
| **Decision** | Maps current percept directly to a target mode[cite: 3]. | Uses current percept and remembers the previous target[cite: 3]. |
| **Repeated percept** | May output the same mode each time[cite: 3]. | Returns `NO COMMAND` when the target is unchanged[cite: 3]. |
| **Memory** | No internal mode memory in the simple version[cite: 3]. | Stores the previous target mode[cite: 3]. |
| **Limitation** | Can produce repeated commands[cite: 3]. | Does not learn and does not automatically prevent rapid switching near a threshold[cite: 3]. |

---

## ⚠️ Failure / Edge-Case Analysis
* **(29, True) repeated twice:** Reflex agent returns `COOL` twice; stateful agent sends only the first command because the policy has no memory of the previous target[cite: 3].
* **(20, True) and (26, True):** Both produce `IDLE` since conditions use `temp < 20` and `temp > 26`, so boundaries are not included in `WARM` or `COOL`[cite: 3].
* **Temperature fluctuates around 26°C (e.g., 26.1, 26.0, 26.1):** The target can alternate `COOL` and `IDLE`, causing mode switching. Remembering the previous mode suppresses identical commands but does not provide hysteresis[cite: 3].

---

## 🚀 How to Run the Scripts
Open your terminal or command prompt inside the project folder and run:

1. **Simple Reflex Agent:**
   ```bash
   python lab2_percepts.py