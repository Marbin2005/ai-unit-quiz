import streamlit as st
import random
import time

# ==========================================
# 1. FULL QUESTION BANK (All 50 Questions)
# ==========================================
QUESTIONS = [
    # --- Section A: Foundations, Turing Test & Rational Agents (1-10) ---
    {"q": "What is the primary goal of a Rational Agent in AI?", "options": ["To think like a human", "To maximize its expected performance measure", "To pass the Turing Test", "To process natural language"], "ans": "To maximize its expected performance measure", "hint": "It seeks the optimal outcome.", "explanation": "A rational agent always chooses the action that maximizes its expected performance measure given its percept sequence."},
    {"q": "The Turing Test is designed strictly to test if an AI can solve complex mathematical equations faster than a human.", "options": ["True", "False"], "ans": "False", "hint": "It tests conversational ability.", "explanation": "The Turing Test assesses a machine's ability to exhibit intelligent conversational behavior indistinguishable from that of a human, not its math skills."},
    {"q": "An agent operates in an environment through ________ and ________.", "options": ["Sensors, Actuators", "Keyboards, Mice", "CPU, RAM", "Memory, Disk"], "ans": "Sensors, Actuators", "hint": "How it perceives and acts.", "explanation": "An agent perceives its environment via sensors (e.g., cameras) and acts upon it via actuators (e.g., motors)."},
    {"q": "Which of the following is NOT a required capability to pass the standard Turing Test?", "options": ["Natural Language Processing", "Knowledge Representation", "Computer Vision", "Automated Reasoning"], "ans": "Computer Vision", "hint": "The standard test is text-based.", "explanation": "The standard Turing Test is text-only. Computer Vision is only required for the 'Total Turing Test' which includes physical interaction."},
    {"q": "Assertion: A rational agent always does the right thing.\nReason: Rationality is based on actual success, not expected success given percepts.", "options": ["Both True", "Assertion True, Reason False", "Assertion False, Reason True", "Both False"], "ans": "Both False", "hint": "Rationality is about 'expected' success, and no agent is omniscient.", "explanation": "Both are false. A rational agent maximizes 'expected' success, not actual success (perfection), because it cannot predict the future with 100% certainty."},
    {"q": "Which Python library is primarily used for multidimensional arrays and matrices in machine learning?", "options": ["Pandas", "NumPy", "Matplotlib", "Flask"], "ans": "NumPy", "hint": "Numerical Python.", "explanation": "NumPy (Numerical Python) is the core library for scientific computing and handling multidimensional arrays."},
    {"q": "A reflex agent acts based only on the current percept, ignoring the rest of the percept history.", "options": ["True", "False"], "ans": "True", "hint": "It has no memory.", "explanation": "Simple reflex agents select actions based purely on the current state, ignoring past history completely."},
    {"q": "What defines 'Good Behavior' in an intelligent agent?", "options": ["Fast execution time", "High memory allocation", "Maximizing the performance measure", "Passing the Turing test"], "ans": "Maximizing the performance measure", "hint": "Focus on the definition of rationality.", "explanation": "Good behavior is defined by the objective performance measure given by the designer, which the agent tries to maximize."},
    {"q": "'PEAS' in agent design stands for Performance, Environment, Actuators, and ________.", "options": ["Sensors", "Systems", "Software", "States"], "ans": "Sensors", "hint": "How it receives input.", "explanation": "PEAS stands for Performance measure, Environment, Actuators, and Sensors."},
    {"q": "A utility-based agent is different from a goal-based agent because it:", "options": ["Has no goals", "Considers how 'happy' or efficient a state is", "Only uses reflexes", "Cannot operate in observable environments"], "ans": "Considers how 'happy' or efficient a state is", "hint": "It measures the 'quality' of success.", "explanation": "While a goal agent just wants to reach a destination, a utility agent wants to reach it in the safest, fastest, or cheapest way possible."},

    # --- Section B: Real-World Scenarios & Applications (11-20) ---
    {"q": "[Scenario] A Self-Driving Car encounters rain, obscuring its camera vision. How is this environment classified?", "options": ["Fully Observable", "Partially Observable", "Deterministic", "Episodic"], "ans": "Partially Observable", "hint": "Some information is hidden.", "explanation": "Because the rain hides parts of the environment, the sensors cannot capture the complete state, making it partially observable."},
    {"q": "[Scenario] An AI medical diagnosis system is evaluating a patient. The next state of the patient depends on unpredictable factors. This environment is:", "options": ["Stochastic", "Deterministic", "Static", "Fully Observable"], "ans": "Stochastic", "hint": "Involves randomness.", "explanation": "Stochastic environments involve randomness and unpredictable outcomes, unlike deterministic ones where the next state is guaranteed."},
    {"q": "[Scenario] You are designing a spam filter. It reads an email and classifies it as spam or not. The next email does not depend on the previous one. This is:", "options": ["Sequential", "Episodic", "Continuous", "Dynamic"], "ans": "Episodic", "hint": "Standalone tasks.", "explanation": "In episodic environments, the agent's experience is divided into independent episodes; the action in one does not affect the next."},
    {"q": "[Scenario] In an automated Chess-playing AI, the environment changes only when the agent or opponent makes a move. This is:", "options": ["Dynamic", "Continuous", "Discrete and Static", "Stochastic"], "ans": "Discrete and Static", "hint": "Nothing happens while you think.", "explanation": "Chess is discrete (fixed states) and static (the board doesn't change while the AI is computing its move)."},
    {"q": "[Scenario] An automated stock trading bot buys and sells shares based on market fluctuations. What is the most appropriate Performance Measure?", "options": ["Number of trades made", "Network bandwidth used", "Profit or ROI", "Number of news articles read"], "ans": "Profit or ROI", "hint": "What is the ultimate goal of trading?", "explanation": "The ultimate goal of a trading bot is to make money, so Profit/Return on Investment (ROI) is the objective performance measure."},
    {"q": "[Scenario] A smart thermostat adjusts the temperature based on room occupancy. What type of agent is this primarily?", "options": ["Simple reflex agent", "Learning agent", "Utility-based agent", "Goal-based agent"], "ans": "Simple reflex agent", "hint": "Condition-Action rule.", "explanation": "It operates on a simple IF-THEN rule (IF room is occupied, THEN turn on AC), making it a simple reflex agent."},
    {"q": "[Scenario] A Mars Rover AI is exploring a crater. Its environment is unknown and changes as rocks fall. This environment is:", "options": ["Fully Observable, Deterministic", "Partially Observable, Stochastic, Dynamic", "Fully Observable, Episodic", "Partially Observable, Static"], "ans": "Partially Observable, Stochastic, Dynamic", "hint": "It's chaotic and hidden.", "explanation": "The crater is partially observable (can't see everything), stochastic (rocks fall randomly), and dynamic (changes while the rover thinks)."},
    {"q": "[Scenario] A conversational AI uses a search algorithm to find the quickest route to a hospital. This search navigates a:", "options": ["State Space", "Turing Test", "Constraint Satisfaction Problem", "Means-End Analysis"], "ans": "State Space", "hint": "A mathematical graph of possibilities.", "explanation": "Finding a route involves navigating through a State Space graph of interconnected nodes (locations)."},
    {"q": "[Scenario] A warehouse robot uses A* search to navigate around moving forklifts. The moving forklifts make the environment:", "options": ["Static", "Dynamic", "Episodic", "Discrete"], "ans": "Dynamic", "hint": "Things are moving.", "explanation": "An environment is Dynamic if it can change while the agent is deliberating its next action."},
    {"q": "[Scenario] In a facial recognition system at an airport, the camera is the:", "options": ["Actuator", "Sensor", "Environment", "Performance measure"], "ans": "Sensor", "hint": "It takes input.", "explanation": "Cameras gather data from the environment, functioning as the agent's sensors."},

    # --- Section C: Search & State-Space Problems (21-25) ---
    {"q": "[Problem] In the Water Jug problem (4L and 3L jugs, goal to get 2L), which of the following represents a valid state transition from (0,0) if we fill the 4L jug?", "options": ["(0, 3)", "(4, 0)", "(4, 3)", "(2, 0)"], "ans": "(4, 0)", "hint": "Fill the first jug.", "explanation": "Starting from both empty (0,0), filling the 4L jug entirely results in the state (4,0)."},
    {"q": "[Problem] In the 8-puzzle problem, what is the maximum number of operators (moves) available to the blank space when it is located in the center?", "options": ["2", "3", "4", "8"], "ans": "4", "hint": "Up, down, left, right.", "explanation": "When the blank tile is in the exact center, it can move Up, Down, Left, or Right (4 moves)."},
    {"q": "[Problem] A state space search graph has a branching factor of 'b' and depth 'd'. What is the maximum number of nodes generated by Breadth-First Search?", "options": ["b + d", "b * d", "O(b^d)", "O(d^b)"], "ans": "O(b^d)", "hint": "It grows exponentially.", "explanation": "BFS keeps every node in memory layer by layer, resulting in an exponential space complexity of O(b^d)."},
    {"q": "[Problem] In the Missionaries and Cannibals problem (3M, 3C), if the boat holds 2 people, which initial move will NOT result in immediate failure?", "options": ["Sending 2 Missionaries", "Sending 1 Missionary and 1 Cannibal", "Sending 3 Cannibals", "Sending 2 Cannibals and 1 Missionary"], "ans": "Sending 1 Missionary and 1 Cannibal", "hint": "Keep the balance.", "explanation": "Sending 1M and 1C leaves 2M and 2C on the starting bank, which is safe. Sending 2M leaves 1M with 3C, resulting in failure."},
    {"q": "[Problem] You are mapping a route from City A to D. A->B(cost 2), A->C(cost 5), B->D(cost 4), C->D(cost 1). Which path will DFS likely find first if it expands alphabetically?", "options": ["A->B->D", "A->C->D", "A->D", "A->B->C"], "ans": "A->B->D", "hint": "DFS dives deep on the first available alphabetical node.", "explanation": "DFS will expand 'A', see 'B' and 'C', pick 'B' (alphabetically first), and immediately dive to 'D', finding the path A->B->D."},

    # --- Section D: Problems, Search Issues & Production Systems (26-30) ---
    {"q": "A production system consists of a set of rules, a knowledge database, and a control strategy.", "options": ["True", "False"], "ans": "True", "hint": "The core components of expert systems.", "explanation": "A production system is built on IF-THEN rules, working memory (database), and a control strategy to decide which rule to fire."},
    {"q": "Match characteristics: 1. Decomposable, 2. Ignorable, 3. Recoverable.\nOptions:\nA: Theorem (Recoverable), 8-puzzle (Ignorable), Integration (Decomposable)\nB: Integration (Decomposable), Theorem (Ignorable), 8-puzzle (Recoverable)", "options": ["A", "B", "Neither", "Both"], "ans": "B", "hint": "8-puzzle is recoverable.", "explanation": "Integration problems can be broken down (Decomposable). Theorem proving steps can be ignored (Ignorable). 8-puzzle mistakes can be undone (Recoverable)."},
    {"q": "Assertion: State space search requires an initial state, operations, and a goal test.\nReason: State space limits the search to only optimal paths.", "options": ["Both true", "Assertion true, Reason false", "Assertion false, Reason true", "Both false"], "ans": "Assertion true, Reason false", "hint": "State space contains ALL paths, not just optimal ones.", "explanation": "State spaces contain all possible paths, including terrible ones. It does not automatically limit the search to optimal paths."},
    {"q": "Which issue in search program design deals with avoiding exploring the same states repeatedly?", "options": ["Direction of search", "Topology of search process", "Representing nodes", "Cycle detection/Repeated states"], "ans": "Cycle detection/Repeated states", "hint": "Preventing infinite loops.", "explanation": "Repeated states cause infinite loops and waste memory, so cycle detection (using a 'Closed List' or 'Explored Set') is critical."},
    {"q": "A problem space is represented as a directed ________ where nodes are states and edges are operators.", "options": ["Graph", "Array", "Stack", "Queue"], "ans": "Graph", "hint": "Nodes connected by lines.", "explanation": "Problem spaces are mathematically represented as Directed Graphs, where nodes equal states and edges equal transitions/actions."},

    # --- Section E: Uninformed Search (BFS, DFS, IDDFS) (31-38) ---
    {"q": "Breadth-First Search (BFS) is implemented using which data structure?", "options": ["Stack", "Queue", "Priority Queue", "Tree"], "ans": "Queue", "hint": "First In, First Out.", "explanation": "A FIFO queue ensures nodes are expanded layer by layer."},
    {"q": "Depth-First Search (DFS) is implemented using which data structure?", "options": ["Stack", "Queue", "Priority Queue", "Linked List"], "ans": "Stack", "hint": "Last In, First Out.", "explanation": "A LIFO stack allows the algorithm to dive deep before backtracking."},
    {"q": "DFS is guaranteed to find the optimal shortest path in an unweighted graph.", "options": ["True", "False"], "ans": "False", "hint": "DFS just finds 'a' path.", "explanation": "DFS is not optimal. It will return the first path it finds, even if a much shorter path exists."},
    {"q": "Iterative Deepening Search (IDDFS) combines the benefits of which two algorithms?", "options": ["BFS and A*", "DFS and Hill Climbing", "BFS and DFS", "A* and AO*"], "ans": "BFS and DFS", "hint": "Memory of one, completeness of the other.", "explanation": "IDDFS has the low memory footprint of DFS and the completeness/optimality of BFS."},
    {"q": "Assertion: IDDFS takes much less memory than BFS.\nReason: IDDFS acts like DFS at each iteration.", "options": ["Both True and Reason is correct", "Both True but Reason is incorrect", "Assertion True, Reason False", "Both False"], "ans": "Both True and Reason is correct", "hint": "It wipes the slate clean each loop.", "explanation": "Because it uses DFS under the hood, IDDFS only stores the current path in memory, keeping space complexity linear O(bd) instead of exponential."},
    {"q": "Breadth-First Search is optimal if all step costs are ________.", "options": ["Zero", "Infinite", "Equal", "Random"], "ans": "Equal", "hint": "Same distance per step.", "explanation": "BFS guarantees the shortest path in terms of the number of steps. This is only 'optimal' if every step costs the exact same amount."},
    {"q": "Uninformed search algorithms have domain-specific knowledge about the goal location.", "options": ["True", "False"], "ans": "False", "hint": "They are 'blind'.", "explanation": "Uninformed algorithms are 'blind' and have no heuristic knowledge about how far they are from the goal."},
    {"q": "If the search space is infinite and the goal is at a finite depth, which algorithm will fail?", "options": ["BFS", "DFS", "IDDFS", "None of the above"], "ans": "DFS", "hint": "It will fall down an infinite hole.", "explanation": "DFS will dive down an infinite path and get stuck forever, failing to find the goal. BFS and IDDFS will eventually find it."},

    # --- Section F: Hill Climbing & Heuristics (39-44) ---
    {"q": "A state in Hill Climbing that is better than all its neighbors but not the global best is called:", "options": ["Plateau", "Ridge", "Local Maximum", "Global Minimum"], "ans": "Local Maximum", "hint": "A smaller peak.", "explanation": "A local maximum looks like the best solution locally, tricking the algorithm into stopping before finding the true global maximum."},
    {"q": "A flat area of the search space in Hill Climbing where all neighboring states have the same value is a:", "options": ["Local Maximum", "Plateau", "Ridge", "Global Maximum"], "ans": "Plateau", "hint": "A flat geographical feature.", "explanation": "A plateau provides no upward slope, making it impossible for standard hill climbing to determine which direction to move."},
    {"q": "Which variation of Hill Climbing evaluates all neighbors and chooses the best one?", "options": ["Simple Hill Climbing", "Steepest-Ascent Hill Climbing", "Stochastic Hill Climbing", "Simulated Annealing"], "ans": "Steepest-Ascent Hill Climbing", "hint": "Looks for the steepest path up.", "explanation": "Steepest-Ascent examines all possible next moves and picks the absolute highest-valued one, unlike Simple Hill Climbing which picks the first better one it sees."},
    {"q": "A heuristic function h(n) estimates the ________ from node n to the goal.", "options": ["Cost/Distance", "Branching Factor", "Depth", "State Space"], "ans": "Cost/Distance", "hint": "How far is it?", "explanation": "The heuristic estimates the cheapest cost (or distance) to reach the goal from the current state."},
    {"q": "Best First Search combines advantages of BFS and DFS by using a priority queue guided by an evaluation function.", "options": ["True", "False"], "ans": "True", "hint": "It prioritizes the 'best' looking node.", "explanation": "Best First Search algorithms (like Greedy and A*) use priority queues ordered by heuristic evaluation functions."},
    {"q": "Assertion: Pure Hill Climbing algorithm can get stuck easily.\nReason: It does not maintain a search tree or history.", "options": ["Both True and Reason is correct", "Both True but Reason is incorrect", "Assertion True, Reason False", "Both False"], "ans": "Both True and Reason is correct", "hint": "It only looks at the present.", "explanation": "Hill climbing is a 'local search' algorithm. Because it keeps no memory of past states, it cannot backtrack when it hits a dead end or local maximum."},

    # --- Section G: CSP & Means-End Analysis (45-50) ---
    {"q": "In a Constraint Satisfaction Problem (CSP), state is defined by:", "options": ["Nodes and edges", "Variables and values from domains", "Initial and goal states only", "Heuristics"], "ans": "Variables and values from domains", "hint": "X, D, C.", "explanation": "A CSP is defined by a set of Variables, a set of Domains (values for the variables), and a set of Constraints."},
    {"q": "Map Coloring and Sudoku are classic examples of:", "options": ["Means-End Analysis", "Uninformed Search", "Constraint Satisfaction Problems", "Production Systems"], "ans": "Constraint Satisfaction Problems", "hint": "They have strict rules.", "explanation": "These problems require assigning values to variables (colors to regions, numbers to grid squares) without violating specific rules (constraints)."},
    {"q": "Means-End Analysis works by detecting the difference between the current state and the goal state, and selecting an operator to reduce that difference.", "options": ["True", "False"], "ans": "True", "hint": "It analyzes the means to the end.", "explanation": "MEA constantly compares the current state to the goal state and applies operators specifically designed to reduce the observed difference."},
    {"q": "In CSP, if assigning a value to a variable violates a constraint, the algorithm performs ________.", "options": ["Hill Climbing", "Backtracking", "Breadth-First Search", "Simulated Annealing"], "ans": "Backtracking", "hint": "Goes back a step.", "explanation": "When a constraint is violated, the algorithm backtracks to a previous variable and tries a different value."},
    {"q": "[Scenario] Scheduling classes for a university without overlapping professors or rooms is best formulated as a:", "options": ["CSP", "BFS", "Turing Test", "Hill Climbing"], "ans": "CSP", "hint": "Strict scheduling rules = constraints.", "explanation": "Time, rooms, and professors are variables with strict overlap rules, perfectly fitting a Constraint Satisfaction Problem."},
    {"q": "Means-End Analysis uses a table called ________ to match differences to operators.", "options": ["Difference table", "Truth table", "Connection table", "Heuristic table"], "ans": "Difference table", "hint": "Table of differences.", "explanation": "A Difference Table maps specific state differences to the operators capable of reducing those differences."}
]

# ==========================================
# 2. SESSION STATE INITIALIZATION
# ==========================================
st.set_page_config(page_title="AI Learning Portal", page_icon="🧠", layout="wide")

if "app_mode" not in st.session_state:
    st.session_state.app_mode = "home" 

def init_game():
    st.session_state.quiz_questions = random.sample(QUESTIONS, 10)
    st.session_state.current_index = 0
    st.session_state.user_answers = {i: None for i in range(10)} 
    st.session_state.reduced_options = {} 
    st.session_state.quiz_submitted = False
    st.session_state.start_time = time.time()
    st.session_state.used_5050_global = False 

# ==========================================
# 3. HOME MENU (LANDING PAGE)
# ==========================================
if st.session_state.app_mode == "home":
    st.title("🧠 AI Interactive Learning Portal")
    st.markdown("### Units I & II: Artificial Intelligence")
    st.write("Welcome! Please select an option below to proceed.")
    
    st.divider()
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.info("### 🚀 Take the Quiz\nTest your knowledge with a 10-question timed exam simulator. Features include lifelines, a navigation grid, and detailed performance evaluation.")
        if st.button("Start Exam Simulator", type="primary", use_container_width=True):
            init_game()
            st.session_state.app_mode = "quiz"
            st.rerun()
            
    with col2:
        st.success(f"### 📚 Question Bank\nStudy and review the complete database of all {len(QUESTIONS)} questions, including correct answers and detailed explanations.")
        if st.button("Browse Question Bank", type="secondary", use_container_width=True):
            st.session_state.app_mode = "qbank"
            st.rerun()

# ==========================================
# 4. QUESTION BANK PAGE
# ==========================================
elif st.session_state.app_mode == "qbank":
    st.title("📚 Complete Question Bank")
    
    if st.button("🔙 Back to Main Menu"):
        st.session_state.app_mode = "home"
        st.rerun()
        
    st.divider()
    st.write(f"Showing all {len(QUESTIONS)} questions in the database.")
    
    for i, q_dict in enumerate(QUESTIONS):
        with st.expander(f"Q{i+1}: {q_dict['q'][:70]}..."):
            st.markdown(f"**Question:** {q_dict['q']}")
            st.markdown("**Options:**")
            for opt in q_dict['options']:
                st.markdown(f"- {opt}")
            st.markdown(f"**Correct Answer:** ✅ `{q_dict['ans']}`")
            st.info(f"**Explanation:** 📖 {q_dict['explanation']}")

# ==========================================
# 5. QUIZ EXAM SIMULATOR
# ==========================================
elif st.session_state.app_mode == "quiz":
    
    # --- Sidebar Navigation Grid ---
    with st.sidebar:
        st.header("🗺️ Quiz Navigation")
        st.write("Click a square to jump to that question.")
        
        cols = st.columns(4)
        for i in range(10):
            col = cols[i % 4]
            if st.session_state.user_answers[i] is not None:
                btn_label = f"{i+1} ✓"
            else:
                btn_label = f"{i+1}"
                
            btn_type = "primary" if i == st.session_state.current_index else "secondary"
            
            if col.button(btn_label, key=f"nav_{i}", type=btn_type, use_container_width=True):
                st.session_state.current_index = i
                st.rerun()
                
        st.divider()
        st.write("**✓ = Answered**")
        st.divider()
        
        if not st.session_state.quiz_submitted:
            unanswered = sum(1 for v in st.session_state.user_answers.values() if v is None)
            if unanswered > 0:
                st.warning(f"You have {unanswered} unanswered questions.")
            if st.button("🏁 Submit Final Quiz", type="primary", use_container_width=True):
                st.session_state.quiz_submitted = True
                st.rerun()
                
        st.divider()
        if st.button("🚪 Quit to Main Menu", use_container_width=True):
            st.session_state.app_mode = "home"
            st.rerun()

    # --- Ongoing Exam ---
    if not st.session_state.quiz_submitted:
        idx = st.session_state.current_index
        q_data = st.session_state.quiz_questions[idx]

        st.title("🧠 AI Exam Simulator")
        
        elapsed = int(time.time() - st.session_state.start_time)
        st.markdown(f"**Question {idx + 1} of 10** | ⏱️ Time Elapsed: {elapsed // 60}m {elapsed % 60}s")
        st.divider()

        st.subheader(q_data["q"])

        if idx in st.session_state.reduced_options:
            active_options = st.session_state.reduced_options[idx]
        else:
            active_options = q_data["options"]

        c1, c2 = st.columns(2)
        with c1:
            if st.button("💡 Show Hint", key=f"hint_{idx}"):
                st.info(f"**Hint:** {q_data['hint']}")
        with c2:
            if not st.session_state.used_5050_global and idx not in st.session_state.reduced_options:
                if st.button("🌗 Use 50/50 (Once per game)", key=f"5050_{idx}"):
                    st.session_state.used_5050_global = True
                    wrong_options = [opt for opt in q_data["options"] if opt != q_data["ans"]]
                    survivor_wrong = random.choice(wrong_options)
                    new_options = [q_data["ans"], survivor_wrong]
                    random.shuffle(new_options)
                    st.session_state.reduced_options[idx] = new_options
                    
                    if st.session_state.user_answers[idx] not in new_options:
                        st.session_state.user_answers[idx] = None
                    st.rerun()

        with st.form(key=f"form_{idx}"):
            default_index = None
            if st.session_state.user_answers[idx] in active_options:
                default_index = active_options.index(st.session_state.user_answers[idx])

            user_choice = st.radio("Select your answer:", active_options, index=default_index)
            
            btn_col1, btn_col2 = st.columns(2)
            with btn_col1:
                save_btn = st.form_submit_button("Save Answer & Next ➡️")
            with btn_col2:
                skip_btn = st.form_submit_button("Skip Question ⏭️")
            
            if save_btn:
                if user_choice is not None:
                    st.session_state.user_answers[idx] = user_choice
                    if idx < 9:
                        st.session_state.current_index += 1
                    st.rerun()
                else:
                    st.warning("⚠️ Please select an answer before saving! Or use the 'Skip Question' button.")
                    
            if skip_btn:
                if idx < 9:
                    st.session_state.current_index += 1
                st.rerun()

    # --- Game Over / Result Screen ---
    else:
        st.balloons()
        st.title("📊 Final Results")
        
        correct = 0
        skipped = 0
        incorrect = 0
        
        for i in range(10):
            user_ans = st.session_state.user_answers[i]
            real_ans = st.session_state.quiz_questions[i]["ans"]
            if user_ans is None:
                skipped += 1
            elif user_ans == real_ans:
                correct += 1
            else:
                incorrect += 1
                
        attended = 10 - skipped
        total_time = int(time.time() - st.session_state.start_time)
        
        st.header(f"Final Score: {correct} / 10")
        st.write(f"⏱️ **Total Time Taken:** {total_time // 60} minutes and {total_time % 60} seconds.")
        
        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Attended", attended)
        col2.metric("Correct ✅", correct)
        col3.metric("Incorrect ❌", incorrect)
        col4.metric("Skipped ⏭️", skipped)
        
        st.divider()
        
        st.subheader("📝 Detailed Question Review")
        for i in range(10):
            q_data = st.session_state.quiz_questions[i]
            user_ans = st.session_state.user_answers[i]
            real_ans = q_data["ans"]
            
            if user_ans is None:
                status = "⏭️ Skipped"
            elif user_ans == real_ans:
                status = "✅ Correct"
            else:
                status = "❌ Incorrect"
                
            with st.expander(f"Q{i+1}: {status} | {q_data['q'][:50]}..."):
                st.markdown(f"**Question:** {q_data['q']}")
                st.write(f"**Your Answer:** {user_ans if user_ans else 'No answer provided'}")
                st.write(f"**Correct Answer:** {real_ans}")
                st.info(f"📖 **Explanation:** {q_data['explanation']}")
                
        st.divider()
        c1, c2 = st.columns(2)
        with c1:
            st.button("🔄 Retake Quiz", on_click=init_game, type="primary", use_container_width=True)
        with c2:
            if st.button("🔙 Return to Main Menu", use_container_width=True):
                st.session_state.app_mode = "home"
                st.rerun()