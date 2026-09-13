# Ignite with Coding & Artificial Intelligence (AI & Robotics - Book 2)
## Class 7 Comprehensive Curriculum Reference Handbook
**Textbook**: *Ignite with Coding & Artificial Intelligence*  
**Curriculum Focus**: CBSE Grade 7 AI & Coding (Vocational / Practical Lab)  
**Subject in Timetable**: AI / Robo (SBPS) • Tuesday Period 7 & Wednesday Period 4 (Teacher: VJ Sir)  
**Examination Status**: Non-Exam Practical Subject (Project-based learning & lab exercises)  
**Associated Platforms**: EduGenius AI Skill Lab (`https://www.edugeniusailab.com/`), Orange Data Mining, Scratch, Breshna AI Game Maker, Google Food Mood AI, IBM SkillsBuild

---

## Master Table of Contents
1. [Platform Access & Teacher/Student Lab Setup](#1-platform-access--edugenius-ai-skill-lab-setup)
2. [Chapter 1: Introduction to Programming](#2-chapter-1-introduction-to-programming)
   - *Sequencing, Flowcharts, Variables, Decision Logic, Loops & Age Gatekeeper Project*
3. [Chapter 2: HTML - From Basics to Advanced](#3-chapter-2-html---from-basics-to-advanced)
   - *Tags, Lists, Images, Links, Tables, Marquee, Forms & Google Clone Project*
4. [Chapter 3: AI and the Future](#4-chapter-3-ai-and-the-future)
   - *What is AI?, Google Engine, Autonomous Vehicles, Gaming NPCs, Healthcare & Sophia Humanoid*
5. [Chapter 4: Layers of Intelligence: AI, ML and Deep Learning](#5-chapter-4-layers-of-intelligence-ai-ml-and-deep-learning)
   - *Concentric Relationship, Object Classification, Digit Recognition, Neural Networks & Rock-Paper-Scissors*
6. [Chapter 5: Understanding the Data Journey](#6-chapter-5-understanding-the-data-journey)
   - *What is Data?, Features & Labels, Training vs Testing Data, Confusion Matrix & Orange Data Mining*
7. [Chapter 6: Exploring the AI Project Cycle](#7-chapter-6-exploring-the-ai-project-cycle)
   - *The 5 Stages, 4Ws Problem Scoping Canvas, Data Acquisition, Modelling (Supervised vs Unsupervised ML), Evaluation & Deployment*
8. [Chapter 7: Ethical Framework of AI](#8-chapter-7-ethical-framework-of-ai)
   - *AI Ethics Pillars (Fairness, Transparency/Black Box, Privacy, Safety), UN SDG 14 (Life Below Water) & Google Food Mood AI*
9. [Chapter 8: AI Tools & Practical Projects](#9-chapter-8-ai-tools--practical-projects)
   - *AI Detective Data Dan, Research Tools, Breshna Game Engine ('Scramble City'), and Career AI Tools*

---

## 1. Platform Access & EduGenius AI Skill Lab Setup

The curriculum is supported by the **EduGenius AI Skill Lab** platform:
- **URL**: `https://www.edugeniusailab.com/`
- **Modules Available**: Online code compilers, flowchart builders, Orange Data Mining simulations, and interactive AI model training environments.
- **Workflow**:
  1. Access the web portal and select Class 7 Grade Track.
  2. Students enroll in the prescribed learning plan containing hands-on coding exercises, datasets, and sandbox environments.

---

## 2. Chapter 1: Introduction to Programming

### 2.1 What is Coding?
> **Coding (Programming)** is the systematic process of writing precise instructions that a computer can understand, process, and execute to perform a task.

#### Key Benefits of Learning to Code:
1. **Logical Problem-Solving**: Breaks big, confusing problems into small, manageable steps.
2. **Computational Creativity**: Transforms passive consumers of digital media into active creators of games, websites, and autonomous systems.
3. **Stepwise Thinking**: Enhances cognitive precision required across mathematics and scientific inquiry.

---

### 2.2 Sequencing: Doing Things in the Right Order
**Sequencing** means arranging instructions in the exact chronological order needed to achieve the intended outcome.
* Every computer program executes sequentially from top to bottom unless redirected by decision branches or loops.
* *Real-Life Analogies*:
  - Baking a cake: Mixing batter *after* baking ruins the recipe.
  - Getting dressed: Putting on shoes *before* socks fails.

---

### 2.3 Algorithms vs. Flowcharts
| Concept | Format | Definition | Key Characteristics |
| :--- | :--- | :--- | :--- |
| **Algorithm** | Textual | A step-by-step written procedure or set of rules to solve a problem in plain language. | Clear, unambiguous, has finite start and end points. |
| **Flowchart** | Graphical | A visual diagram representing the sequence of operations in an algorithm using standard geometric symbols. | Uses standardized ANSI symbols connected by directional arrows. |

#### Standard Flowchart Symbols:
| Geometric Shape | Symbol Name | Function in Flowchart |
| :--- | :--- | :--- |
| **Oval / Rounded Rectangle** | **Terminal (Start / End)** | Marks the beginning and termination of the program. |
| **Parallelogram** | **Input / Output (I/O)** | Represents entering data (e.g., *Read User Age*) or displaying results (*Print "Allowed"*). |
| **Rectangle** | **Process** | Represents computational actions, calculations, or variable assignments (e.g., `Sum = A + B`). |
| **Diamond** | **Decision** | Evaluates a Boolean condition with two or more exiting branches (e.g., *Is Age >= 18? Yes / No*). |
| **Arrows (Flowlines)** | **Flowline** | Connects symbols and indicates the direction of program execution. |
| **Circle** | **Connector** | Connects complex flowchart paths on the same page. |

---

### 2.4 Variables & Memory Boxes
* **Definition**: A **variable** is a named storage container in computer memory that holds a value which can change during program execution.
* *Cabinet Analogy*: Imagine an organizer with labelled compartments. A drawer labelled `score` holds the number `10`. When the player collects a coin, the program replaces `10` with `20`.
* **Rules for Naming Variables**:
  - Must start with a letter or underscore (`_`).
  - Cannot contain spaces (use camelCase `userAge` or snake_case `user_age`).
  - Cannot use reserved programming keywords (e.g., `if`, `while`, `for`).

---

### 2.5 Decision Making (Conditionals) & Loops
1. **Conditionals (`if-then-else`)**:
   - Allows programs to make decisions based on logical truths:
     ```text
     if (condition is True):
         Execute Action A
     else:
         Execute Action B
     ```
2. **Loops (Repetition / Iteration)**:
   - Repeats a block of code multiple times without re-writing instructions.
   - *Count-controlled loop*: Repeat 10 times.
   - *Condition-controlled loop*: Repeat *while* user battery is above 10%.

---

### 2.6 Practical Project: The Age Gatekeeper Program
*Task*: Write an algorithm and program logic to verify user admission based on age:
```python
# Age Gatekeeper Decision Algorithm
age = int(input("Enter your age: "))

if age < 5:
    print("Result: Too young! Entry not permitted.")
elif 5 <= age <= 17:
    print("Result: Allowed with Adult Supervision.")
else:
    print("Result: Full Independent Entry Allowed.")
```

#### Chapter 1 Exercises:
1. *What is an algorithm?* &rarr; **A step-by-step set of instructions to solve a problem.**
2. *Which flowchart symbol is used for asking questions or making decisions?* &rarr; **Diamond.**

---

## 3. Chapter 2: HTML - From Basics to Advanced

### 3.1 What is HTML?
> **HTML** stands for **HyperText Markup Language**. It is the standard markup code used to structure Web pages and their content.
- **HyperText**: Text containing links (hyperlinks) connecting web pages to one another.
- **Markup Language**: Uses pairs of tags (`<tagname>...</tagname>`) to annotate and format plain text for browser rendering.

---

### 3.2 Anatomy of an HTML Document
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>My First Web Page</title>
</head>
<body>
    <h1>Welcome to Web Development!</h1>
    <p>This is a paragraph of formatted text.</p>
</body>
</html>
```
- `<!DOCTYPE html>`: Informs the browser that the document conforms to the HTML5 standard.
- `<html>`: Root element enclosing all webpage content.
- `<head>`: Contains metadata, stylesheets, and browser tab title (invisible on the page canvas).
- `<body>`: Contains all visible webpage content (headings, paragraphs, images, tables).

---

### 3.3 Lists in HTML
1. **Unordered List (`<ul>`)**:
   - Bulleted list. Default marker: solid disc.
   ```html
   <ul>
       <li>Robotics Kit</li>
       <li>USB Cable</li>
   </ul>
   ```
2. **Ordered List (`<ol>`)**:
   - Numbered list (`1, 2, 3...` or `a, b, c...`).
   ```html
   <ol type="1">
       <li>Initialize Microcontroller</li>
       <li>Connect Bluetooth</li>
   </ol>
   ```

---

### 3.4 Media & Hyperlinks
1. **Images (`<img>`)**:
   - An *empty/void tag* (no closing tag required).
   - Attributes: `src` (image URL/path) and `alt` (alternative text for accessibility).
   ```html
   <img src="robot.png" alt="Autonomous Robot Chassis" width="300" height="200">
   ```
2. **Hyperlinks (`<a>`)**:
   - Anchor tag connecting documents.
   - Attributes: `href` (destination URL), `target="_blank"` (opens in new tab), and `mailto:` (opens email client).
   ```html
   <a href="https://www.edugeniusailab.com/" target="_blank">Visit AI Lab</a>
   <a href="mailto:support@school.com">Send Email</a>
   ```

---

### 3.5 Tables & Marquee
1. **Tables (`<table>`)**:
   - Structured in rows (`<tr>`) and cells (`<td>` for data, `<th>` for bold centered headers).
   ```html
   <table border="1">
       <tr>
           <th>Component</th>
           <th>Type</th>
       </tr>
       <tr>
           <td>Ultrasonic Sensor</td>
           <td>Input</td>
       </tr>
   </table>
   ```
2. **Marquee (`<marquee>`)**:
   - Creates animated scrolling ticker text across the screen.
   ```html
   <marquee direction="left" scrollamount="5">Class 7 AI Lab Schedule Updated!</marquee>
   ```

---

### 3.6 HTML Forms & Interactive Inputs
The `<form>` element captures user data for processing:
| Input Element | Code Snippet | Use Case |
| :--- | :--- | :--- |
| **Text Field** | `<input type="text" placeholder="Your Name">` | Single-line text input |
| **Password** | `<input type="password">` | Masks characters with dots for privacy |
| **Radio Button** | `<input type="radio" name="gender" value="m">` | Choose **ONE** option among a mutually exclusive group |
| **Checkbox** | `<input type="checkbox" name="skill" value="py">` | Choose **MULTIPLE** options independently |
| **Dropdown Select** | `<select><option>Robotics</option></select>` | Compact selectable dropdown menu |
| **Submit Button** | `<input type="submit" value="Register">` | Sends form payload to server |

---

### 3.7 Hands-on Project: Google Homepage Web Clone
Students write semantic HTML replicating the classic Google search engine layout: centered logo (`<img>`), search input box (`<input type="text">`), and action buttons (`Google Search` and `I'm Feeling Lucky`).

---

## 4. Chapter 3: AI and the Future

### 4.1 What is Artificial Intelligence?
> **Artificial Intelligence (AI)** is the branch of computer science dedicated to creating machines capable of performing tasks that typically require human intelligence—such as visual perception, speech recognition, decision-making, and language translation.

---

### 4.2 Four Major Domains of Real-World AI
1. **Search Engines (Google Search)**:
   - RankBrain & BERT algorithms understand the conversational intent of user queries, autocorrect typos, and index billions of websites in milliseconds.
2. **Autonomous Transportation (Tesla Autopilot & Waymo)**:
   - Computer vision neural networks process real-time feeds from 8 external cameras, detecting lane boundaries, pedestrians, traffic lights, and calculating braking distances.
3. **Gaming Industry & Intelligent NPCs**:
   - Non-Player Characters (NPCs) in games act intelligently, strategize cover, adapt to player attack tactics, and generate dynamic game worlds.
4. **Healthcare & Humanoid Robotics**:
   - **Sophia the Humanoid Robot**: Developed by Hanson Robotics (unveiled in 2016). Uses AI facial recognition, natural language conversational models, and 60+ motorized facial expressions to interact with humans.
   - Diagnostic AI detects retinal diseases and pneumonia in X-rays with greater accuracy than human general practitioners.

---

## 5. Chapter 4: Layers of Intelligence: AI, ML and Deep Learning

### 5.1 The Concentric Relationship of AI
AI, Machine Learning, and Deep Learning are not separate entities; they are nested subsets:
```text
┌────────────────────────────────────────────────────────┐
│ 1. ARTIFICIAL INTELLIGENCE (Broadest Domain)           │
│    Any technique that enables machines to mimic human  │
│    behavior and logic.                                 │
│                                                        │
│   ┌────────────────────────────────────────────────┐   │
│   │ 2. MACHINE LEARNING (Subset of AI)             │   │
│   │    Algorithms that learn patterns directly     │   │
│   │    from data without explicit step-by-step     │   │
│   │    programming.                                │   │
│   │                                                │   │
│   │   ┌────────────────────────────────────────┐   │   │
│   │   │ 3. DEEP LEARNING (Subset of ML)        │   │   │
│   │   │    Multi-layered Artificial Neural     │   │   │
│   │   │    Networks inspired by human brain    │   │   │
│   │   │    neurons to process massive data.    │   │   │
│   │   └────────────────────────────────────────┘   │   │
│   └────────────────────────────────────────────────┘   │
└────────────────────────────────────────────────────────┘
```

---

### 5.2 Real-World Machine Learning Workflows
1. **Object Classification**:
   - Training computers to differentiate between groceries, vehicles, or animals by extracting visual edge and color features.
2. **Digit Recognition (MNIST Dataset)**:
   - Recognizes handwritten digits (0 through 9) written by different people with varied handwriting styles by calculating pixel intensity probability distributions.
3. **Rock-Paper-Scissors AI Game**:
   - The AI algorithm records the human opponent's past move sequences, identifies psychological patterns (e.g., humans often switch to Paper after losing with Rock), and predicts the winning counter-move.

---

## 6. Chapter 5: Understanding the Data Journey

### 6.1 What is Data?
> **Data** is any collection of facts, statistics, measurements, or raw information that can be gathered, processed, and analyzed to train AI models.
- Data is the **fuel** of Artificial Intelligence. Without quality data, machine learning algorithms cannot learn.

---

### 6.2 Features vs. Labels (The Core ML Vocabulary)
| Term | Definition | Fruit Identification Example |
| :--- | :--- | :--- |
| **Feature** | An individual measurable property, characteristic, or attribute used as input for the model. | `Color = Yellow`, `Shape = Curved`, `Taste = Sweet` |
| **Label** | The final target class, outcome, or correct answer the AI is being trained to predict. | **"Banana"** |

---

### 6.3 Training Data vs. Testing Data
To evaluate an AI system fairly, dataset splitting is mandatory:
1. **Training Data (80%)**: The textbook given to the student. Used by the machine learning algorithm to discover patterns and adjust internal weights.
2. **Testing Data (20%)**: The unseen exam paper given to the student. The AI has never seen these specific data samples during training; its performance on testing data measures its true generalization capability.

---

### 6.4 Practical Lab: Orange Data Mining Software
**Orange** is an open-source, component-based visual programming software suite for data mining and machine learning:
1. **Data Ingestion**: Drag the **File Widget** to load the fruit dataset (`Fruit.tab`).
2. **Data Inspection**: Connect to the **Data Table Widget** to inspect numerical distributions of sweetness and acidity.
3. **Machine Learning Model**: Connect dataset to the **Linear Regression Widget** to model how physical features correlate with fruit sweetness.
4. **Evaluation**: Drag the **Test and Score Widget** to compute prediction accuracy, Mean Absolute Error (MAE), and Confusion Matrix.

---

## 7. Chapter 6: Exploring the AI Project Cycle

### 7.1 The Five Stages of the AI Project Cycle
The structured engineering framework for designing AI applications:
```text
┌─────────────────┐      ┌─────────────────┐      ┌─────────────────┐
│ 1. PROBLEM      │ ---> │ 2. DATA         │ ---> │ 3. DATA         │
│    SCOPING      │      │    ACQUISITION  │      │    EXPLORATION  │
└─────────────────┘      └─────────────────┘      └─────────────────┘
                                                           │
                                                           ▼
┌─────────────────┐      ┌─────────────────┐      ┌─────────────────┐
│ 6. DEPLOYMENT   │ <--- │ 5. EVALUATION   │ <--- │ 4. MODELLING    │
│    & MONITORING │      │    & TESTING    │      │    & TRAINING   │
└─────────────────┘      └─────────────────┘      └─────────────────┘
```

---

### 7.2 Stage 1: Problem Scoping & The 4Ws Canvas
Before writing a single line of code, developers must validate the problem using the **4Ws Problem Canvas**:
1. **Who? (Stakeholders)**: Who is affected by this problem? Who are the end-users?
2. **What? (The Problem Statement)**: What is the exact nature of the problem? What evidence exists that it is a genuine issue?
3. **Where? (Context / Location)**: In what physical environment or operational setting does this problem occur?
4. **Why? (Value Proposition)**: Why will solving this problem benefit stakeholders? What value does an AI solution provide over traditional methods?

---

### 7.3 Stage 4: Modelling Paradigms: Rule-Based vs. Learning-Based
1. **Rule-Based AI**:
   - Programmer hard-codes all logic manually: `IF Temperature > 30 THEN Turn ON Fan`.
   - The machine *does not learn*—it strictly executes developer-written instructions.
2. **Learning-Based AI (Machine Learning)**:
   - Algorithm figures out the rules automatically by examining thousands of input-output pairs.

---

### 7.4 Machine Learning Taxonomy: Supervised vs. Unsupervised
```text
                           MACHINE LEARNING
                                  │
          ┌───────────────────────┴───────────────────────┐
          ▼                                               ▼
  SUPERVISED LEARNING                            UNSUPERVISED LEARNING
  (Trained on Labelled Data)                     (Finds Patterns in Raw Data)
          │                                               │
    ┌─────┴─────┐                                   ┌─────┴─────┐
    ▼           ▼                                   ▼           ▼
CLASSIFICATION REGRESSION                      CLUSTERING   ASSOCIATION RULES
Discrete labels Continuous numbers              Grouping by  "If Bread ->
(Dog vs Cat,   (House Prices,                  similarity   Then Butter"
Pass vs Fail)   Temperature)                   (Segments)   (Market Basket)
```

1. **Supervised Learning**:
   - Machine is guided by known labels (teacher-guided learning).
   - *Classification*: Predicts discrete categories (e.g., Spam vs Not Spam; Malignant vs Benign).
   - *Regression*: Predicts continuous numeric quantities (e.g., predicting exact marks based on study hours).
2. **Unsupervised Learning**:
   - Machine explores unlabelled raw data without teacher answers.
   - *Clustering*: Groups items naturally based on geometric proximity (e.g., grouping Spotify listeners by music genre tastes).
   - *Association Rules*: Uncovers co-occurrence affinities in consumer transactions (e.g., Market Basket Analysis: Customers buying bread also buy butter 85% of the time).

---

## 8. Chapter 7: Ethical Framework of AI

### 8.1 The Four Ethical Pillars of Responsible AI
As AI systems make decisions impacting human lives, they must satisfy ethical standards:
1. **Fairness & Non-Bias**:
   - AI algorithms trained on biased historical data will amplify human prejudices (e.g., facial recognition models failing on darker skin tones due to non-diverse training sets).
2. **Transparency (The "Black Box" Problem)**:
   - Deep neural networks must not be impenetrable black boxes. High-stakes AI (medical diagnosis, court bail decisions) must provide interpretable explanations for their decisions.
3. **Privacy & Data Security**:
   - User facial scans, voice recordings, and personal telemetry must be encrypted and handled strictly with informed consent.
4. **Safety & Accountability**:
   - If an autonomous vehicle crashes or an AI misdiagnoses a patient, clear legal and moral chains of accountability must exist.

---

### 8.2 AI & The United Nations Sustainable Development Goals (SDGs)
The handbook highlights **SDG 14: Life Below Water**:
- AI-powered computer vision drones and subsea robotic cameras patrol coral reefs, monitor illegal fishing trawlers, and detect microplastic pollution plumes in oceans automatically.
- **Google Food Mood AI Project**:
  - Creative culinary exploration AI combining recipes from varied cultural cuisines to minimize food waste and promote sustainable culinary habits.

---

## 9. Chapter 8: AI Tools & Practical Projects

### 9.1 Meet AI Detective Data Dan!
An interactive gamified case study guiding Class 7 students through real-world AI investigative workflows:
- Formulating queries, validating source data integrity, detecting deepfakes, and cross-referencing AI outputs with reputable scientific literature.

---

### 9.2 Project: Creating Video Games with Breshna AI Game Maker
**Breshna** is a no-code, AI-powered interactive game creation tool:
- Students build *"Scramble City"*: A 2D educational platformer where characters collect correct AI terms (Sensors, Actuators, Labels) while avoiding "Data Bias" obstacles.
- Teaches sprite collision logic, game loops, and experiential computing.

---

### 9.3 Real-World Career AI Tools
The curriculum introduces professional AI tools tailored across career sectors:
- **Software Development**: GitHub Copilot, ChatGPT Code Interpreter (automates boilerplate code and debugging).
- **Digital Marketing**: Midjourney, Canva Magic Studio (generates localized promotional assets).
- **Biomedical Engineering**: AlphaFold, DeepMind health diagnostics (predicts protein folding structures).

---
*Reference Handbook compiled strictly from source document `source_materials/coding and ai_20260912.pdf` for Pushti Study Hub under CBSE Class 7 AI & Robotics curriculum standards.*
