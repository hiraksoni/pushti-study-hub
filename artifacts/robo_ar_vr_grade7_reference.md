# Ignite with Robotics & Augmented/Virtual Reality (AI & Robotics)
## Class 7 Comprehensive Curriculum Reference Handbook
**Textbook**: *Ignite with Robotics & Augmented/Virtual Reality*  
**Curriculum Focus**: CBSE Grade 7 AI & Robotics (Vocational / Practical Lab)  
**Subject in Timetable**: AI / Robo (SBPS) • Thursday Period 7 & Friday Period 4 (Teacher: VJ Sir)  
**Examination Status**: Non-Exam Practical Subject (Project-based assessment & hands-on lab learning)  
**Associated Hardware/Software**: QtPi QBrik, Qbits Mechanical Kits, Code 2 Play (MIT App Inventor environment), Tinkercad (Autodesk), Sketchfab (WebAR/VR), Median.co (App Builder)

---

## Quick Reference Table of Contents
1. [General Setup: 5-Step Code 2 Play & QBrik Hardware Architecture](#1-general-setup-code-2-play--qbrik-hardware-architecture)
2. [Chapter 1: What are Robots? Understanding the Basics](#2-chapter-1-what-are-robots-understanding-the-basics)
   - *Practical Project 1: Voice Controlled Smart Door Automation*
3. [Chapter 2: How Robots Move: Sensors and Processors Working Together](#3-chapter-2-how-robots-move-sensors-and-processors-working-together)
   - *Practical Project 2: Rishi's RC Car with Turn Indicators*
4. [Chapter 3: How Does Extended Reality (XR) Work?](#4-chapter-3-how-does-extended-reality-xr-work)
   - *AR vs VR vs MR Comparative Matrix & Virtual Reality Expedition*
5. [Chapter 4: Intro to 3D Block-Based Coding & XR Publishing](#5-chapter-4-intro-to-3d-block-based-coding--xr-publishing)
   - *Tinkercad 3D Pond -> Sketchfab AR/VR -> Median.co Mobile App*
6. [Chapter 5: Brain & Logic Lab Worksheets](#6-chapter-5-brain--logic-lab-worksheets)
   - *Rebus Puzzles, Linked Loops, Braille Tactile Code, and Sudoku*
7. [Chapter 6: Artificial Intelligence (AI) Foundations](#7-chapter-6-artificial-intelligence-ai-foundations)
   - *Reserved Branch for Upcoming AI Textbook*

---

## 1. General Setup: Code 2 Play & QBrik Hardware Architecture

### 1.1 Five-Step Guide to Kickstart Code 2 Play (Section A)
Code 2 Play is a block-based visual mobile app development platform built on MIT App Inventor architecture. Every robotic smartphone controller project follows these five initial steps:

1. **Add ListPicker (User Interface)**:
   - In the **Designer** tab, open the **Palette** -> **User Interface**.
   - Drag and drop the `ListPicker` component onto the phone viewer screen.
   - Rename it to `Connect` or `Pick Car` in the Components column.
2. **Add Notifier (User Interface)**:
   - Drag and drop the `Notifier` component onto the viewer screen (this is a non-visible component appearing below the screen).
3. **Add BluetoothClient (Connectivity)**:
   - In the Palette, open **Connectivity**.
   - Drag and drop `BluetoothClient` onto the viewer (non-visible component).
4. **Assign Ports from QtPi Mega Blocks**:
   - Open **QtPi Mega Blocks** drawer.
   - Drag the required hardware blocks for your project (e.g., `LeftMotor`, `RightMotor`, `Buzzer`, `RGB_LED`, `ServoMotor`).
   - In the **Properties** panel on the right, set the `PortNumber` (matching Section B) and associate `BluetoothClient1`.
5. **Rename Components and Properties**:
   - For all visible and non-visible components, rename them intuitively in the Components hierarchy to ensure clean and readable code blocks.

---

### 1.2 Instructions for QBrik Port Connections (Section B)
The **QBrik** is the central robotic controller (brain) designed by QtPi. It features:
- **6 Sensor and Actuator Ports**: `P1`, `P2`, `P3`, `P4`, `P5`, and `P6`.
- **3 Motor Ports**:
  - `M1`: Programmable DC Motor Port (e.g., Left Drive Motor)
  - `M2`: Programmable DC Motor Port (e.g., Right Drive Motor)
  - `M3`: Non-programmable / Constant Testing Port (powers motor directly for hardware testing)

#### Master Port Accessibility Matrix:
| Component | Type | Compatible Ports on QBrik | Key Function / Application |
| :--- | :--- | :--- | :--- |
| **IR Sensor** | Input / Sensor | `P1, P2, P3, P4, P5, P6` (All 6 ports) | Obstacle detection, line tracking, proximity |
| **LDR Sensor** | Input / Sensor | `P1, P2, P3, P4` (Analog/Digital) | Light intensity measurement, automatic lights |
| **Ultrasonic Sensor** | Input / Sensor | `P1, P2, P3, P4, P5, P6` (All 6 ports) | Precision distance measurement (sonar echo) |
| **Temperature Sensor** | Input / Sensor | `P1, P2, P3, P4` | Ambient thermal monitoring, climate control |
| **Gas / Smoke Sensor** | Input / Sensor | `P1, P2, P3, P4` | Hazardous gas / fire alarm systems |
| **Limit Switch** | Input / Sensor | `P1, P2, P3, P4, P5, P6` (All 6 ports) | Physical contact, limit stop, tactile feedback |
| **Buzzer** | Output / Actuator | `P1, P2, P3, P4, P5, P6` (All 6 ports) | Audio warning beeps, sirens, acoustic alerts |
| **LED (Single Color)** | Output / Actuator | `P1, P2, P3, P4, P5, P6` (All 6 ports) | Visual status indicators, headlights |
| **RGB LED** | Output / Actuator | `P1, P2, P3, P4` | Multi-color status indication (turn signals) |
| **Servo Motor** | Output / Actuator | `P1, P2, P3, P4` | Precision angular positioning (0° to 180°) |
| **DC Motor** | Output / Actuator | `M1, M2, M3` | Continuous rotational drive for wheels |
| **Pump Motor** | Output / Actuator | `M1, M2, M3` | Liquid transfer (plant watering, fluid lab) |

---

### 1.3 Bluetooth Pairing Logic in Code 2 Play (Blocks)
To establish two-way communication between the smartphone app and the QBrik:

```text
// Step 1: Populating Available Bluetooth Devices Before Picking
when ListPicker1.BeforePicking do
    set ListPicker1.Elements to BluetoothClient1.AddressesAndNames

// Step 2: Connecting to Selected Device After Picking
when ListPicker1.AfterPicking do
    evaluate:
        if BluetoothClient1.Connect (address: ListPicker1.Selection) then
            set ListPicker1.Text to "Connected!"
            set ListPicker1.BackgroundColor to Green
            call Notifier1.ShowAlert (notice: "Successfully connected to QBrik!")
        else
            set ListPicker1.Text to "Connection Failed"
            set ListPicker1.BackgroundColor to Red
            call Notifier1.ShowAlert (notice: "Could not connect. Turn on Bluetooth & retry.")
```

---

## 2. Chapter 1: What are Robots? Understanding the Basics

### 2.1 Core Definition
> **What is a Robot?**  
> A robot is a programmable electromechanical machine capable of carrying out a complex series of actions automatically. It follows the fundamental tri-part principle: **Sense, Think, and Act**.

### 2.2 Five Essential Subsystems of a Robot
Every functional robot consists of 5 core subsystems:
1. **Sensors (The Input System / Eyes & Ears)**:
   - Collect raw information and physical stimuli from the environment.
   - *Examples*: Ultrasonic distance sensors, Infrared (IR) line trackers, Light Dependent Resistors (LDR), Sound sensors, Temperature probes.
2. **Processor / Controller (The Brain)**:
   - Processes data received from sensors, makes logical decisions based on programmed rules, and computes output commands.
   - *Examples*: QBrik microcontroller, Arduino Uno, Raspberry Pi, Micro:bit.
3. **Actuators (The Muscles & Limbs)**:
   - Convert electrical energy from the controller into physical motion, light, or sound.
   - *Types*:
     - *DC Motors*: Fast, continuous 360° rotation for wheeled mobility.
     - *Servo Motors*: Controlled angular precision (0°–180°) for robotic arms, steering, and gripper claws.
     - *Stepper Motors*: Precise fractional step rotations for 3D printers and CNC machines.
     - *Hydraulic & Pneumatic Cylinders*: High-force fluid/air pistons for heavy industrial automation.
4. **Power Supply (The Heart & Energy)**:
   - Supplies regulated electrical energy to the processor, sensors, and actuators.
   - *Examples*: Rechargeable Lithium-ion / LiPo battery packs, 9V alkaline batteries, USB power banks, solar panels.
5. **Body & Structure (The Skeleton & Chassis)**:
   - The mechanical frame that holds all components together in a rigid, functional form.
   - *Examples*: QtPi Qbits modular structural beams, acrylic chassis, 3D printed shells, aluminum brackets.

---

### 2.3 Practical Project 1: Voice-Controlled Smart Door Automation
*Objective*: Build an automated door barrier that opens and closes on spoken voice commands ("Open" / "Close") using speech recognition on a smartphone paired to a QBrik.

#### Hardware Wiring & Port Configuration:
- **Controller**: QBrik
- **Servo Motor**: Connected to **Port P1** (Controls door lever rotation: 0° = Closed, 90° = Open)
- **Status LED / Buzzer**: Connected to **Port P2** (Audible confirmation beep)
- **Power**: 7.4V Li-ion battery pack connected to QBrik DC input
- **Connectivity**: Integrated Bluetooth module paired to Android device running Code 2 Play

#### Designer Components (Code 2 Play):
1. `ListPicker1` (Connect Bluetooth)
2. `SpeechRecognizer1` (User Interface -> Voice Input)
3. `Button_Speak` ("Tap to Give Voice Command")
4. `Label_Status` ("Awaiting Command...")
5. `ServoMotor1` (QtPi Mega Blocks -> Port P1)
6. `BluetoothClient1` (Connectivity)
7. `Notifier1`

#### Event Blocks Logic:
```text
// Event 1: Trigger Speech Recognizer
when Button_Speak.Click do
    call SpeechRecognizer1.GetText

// Event 2: Process Voice Command
when SpeechRecognizer1.AfterGettingText (result) do
    set Label_Status.Text to get result
    
    // Check if user said "open"
    if (call string_contains_text (piece: "open", text: get result.toLowerCase)) then
        call ServoMotor1.SetAngle (angle: 90)
        set Label_Status.Text to "Door OPENED (90°)"
        call Notifier1.ShowAlert (notice: "Door is now Open")
    
    // Check if user said "close"
    else if (call string_contains_text (piece: "close", text: get result.toLowerCase)) then
        call ServoMotor1.SetAngle (angle: 0)
        set Label_Status.Text to "Door CLOSED (0°)"
        call Notifier1.ShowAlert (notice: "Door is now Closed")
    
    else
        call Notifier1.ShowAlert (notice: "Unknown command! Please say OPEN or CLOSE.")
```

---

### 2.4 Exercises & Review (Chapter 1)
#### Match the Following:
| Column A | Column B | Correct Match |
| :--- | :--- | :--- |
| 1. Sensors | A. Converts electrical energy to movement | **1 -> B** (Collects data from environment) |
| 2. Processor | B. Collects data from environment | **2 -> C** (Makes decisions based on data) |
| 3. Actuator | C. Makes decisions based on data | **3 -> A** (Converts electrical energy to movement) |
| 4. Power Supply | D. Physical frame of the robot | **4 -> E** (Provides energy to run the robot) |
| 5. Body/Structure | E. Provides energy to run the robot | **5 -> D** (Physical frame of the robot) |

#### Concept Review Questions:
1. **Name three common actuators used in robotics**: DC Motor, Servo Motor, Buzzer/Solenoid.
2. **What role does a microcontroller play in a robotic system?** It acts as the brain, processing sensory inputs, executing logic algorithms, and sending pulse-width modulated (PWM) or digital control signals to actuators.

---

## 3. Chapter 2: How Robots Move: Sensors and Processors Working Together

### 3.1 The Sense-Think-Act Cycle
The operational loop of every intelligent autonomous robot is continuous:
```text
┌────────────────────────────────────────────────────────┐
│               THE SENSE-THINK-ACT CYCLE                │
│                                                        │
│   ┌───────────────┐     Electrical      ┌────────────┐ │
│   │ 1. SENSE      │ ──────────────────> │ 2. THINK   │ │
│   │ (Sensors read │     Signal          │ (Processor │ │
│   │ environment)  │                     │ evaluates) │ │
│   └───────────────┘                     └────────────┘ │
│           ▲                                    │       │
│           │                                    │ Pulse │
│   Modifies│ Physical                  Output   │ Width/│
│   Reality │ Consequence               Command  │ PWM   │
│           │                                    ▼       │
│   ┌───────────────┐                     ┌────────────┐ │
│   │ Robot Moves/  │ <────────────────── │ 3. ACT     │ │
│   │ Environment   │     Mechanical      │ (Actuators │ │
│   │ Changes       │     Motion          │ execute)   │ │
│   └───────────────┘                     └────────────┘ │
└────────────────────────────────────────────────────────┘
```
1. **Sense**: Ultrasonic sensor measures distance to wall = `15 cm`.
2. **Think**: Microcontroller compares: `Distance < 20 cm` -> True. Action rule: `Stop and Turn Right`.
3. **Act**: Left DC Motor turns Forward, Right DC Motor turns Reverse for 500ms. Robot rotates away from wall.

---

### 3.2 Practical Project 2: Rishi's RC Car with Turn Indicators
*Scenario*: Rishi was fond of playing with his remote-controlled car. What he disliked was that unlike real automobiles on the street, his toy car did not have turn signals (indicators) to signal direction changes to observers.

#### Mechanical & Electrical Architecture:
- **Chassis**: Qbits structural beams and plates.
- **Drive System (Differential Drive)**:
  - Left DC Motor -> **Port M1**
  - Right DC Motor -> **Port M2**
- **Indicator System**:
  - Left RGB LED -> **Port P1** (Signals Green/Amber on Left turn)
  - Right RGB LED -> **Port P2** (Signals Green/Amber on Right turn)
- **Controller**: QBrik powered by Li-ion battery.

#### Code 2 Play User Interface (Touch Remote):
- 4 Directional Buttons: `Button_Forward`, `Button_Reverse`, `Button_Left`, `Button_Right`, plus `Button_Stop`.

#### Complete Event Logic Matrix:
| Button Touched | Left Motor (M1) | Right Motor (M2) | Left RGB LED (P1) | Right RGB LED (P2) | Visual / Motion Effect |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Forward** | Forward (100%) | Forward (100%) | **OFF** | **OFF** | Car advances straight ahead. |
| **Reverse** | Reverse (100%) | Reverse (100%) | **OFF** | **OFF** | Car moves straight backward. |
| **Turn Left** | STOP (or Reverse) | Forward (100%) | **BLINK / GREEN** | **OFF** | Car pivots left; left indicator flashes. |
| **Turn Right** | Forward (100%) | STOP (or Reverse) | **OFF** | **BLINK / GREEN** | Car pivots right; right indicator flashes. |
| **Stop** | STOP (0%) | STOP (0%) | **OFF** | **OFF** | Car remains stationary. |

---

## 4. Chapter 3: How Does Extended Reality (XR) Work?

### 4.1 Definition of Extended Reality (XR)
> **Extended Reality (XR)** is an umbrella term encompassing all immersive technologies that merge physical and digital realities, including **Virtual Reality (VR)**, **Augmented Reality (AR)**, and **Mixed Reality (MR)**.

### 4.2 The Ultimate XR Comparison Matrix
| Characteristic | Augmented Reality (AR) | Virtual Reality (VR) | Mixed Reality (MR) |
| :--- | :--- | :--- | :--- |
| **Immersion Level** | Low to Moderate (User stays grounded in physical room) | Total Immersion (User completely isolated in digital simulation) | High Hybrid (Digital and real objects co-exist and interact) |
| **Display / Hardware** | Smartphone screens, transparent smart glasses (Google Glass) | Opaque Head-Mounted Display (HMD) e.g., Meta Quest, HTC Vive | Advanced HMD with spatial cameras e.g., Microsoft HoloLens, Apple Vision Pro |
| **Surrounding Awareness**| 100% visible real world with digital graphics overlaid | Physical world completely blocked out by OLED/LCD screens | Real world fully visible with dynamic 3D holograms anchored to physical surfaces |
| **Occlusion & Physics** | Simple overlay (digital character floats on screen) | Entire environment obeys virtual engine physics | Digital ball bounces realistically off physical living-room table (Spatial mapping) |
| **Prime Examples** | Pokémon GO, IKEA Place, Google Maps Live View | Beat Saber, Flight Simulators, Virtual Field Trips | Medical holographic surgery planning, NASA Mars rover spatial collaboration |

---

### 4.3 Five Core Hardware & Software Pillars of XR
1. **Head-Mounted Displays (HMDs) & Optics**:
   - High-resolution displays (4K per eye) with specialized Fresnel or Pancake lenses that bend light to focus on the human retina at close range with wide Field of View (FOV > 110°).
2. **Processors & High-Performance GPUs**:
   - Ultra-low latency image rendering (<20 milliseconds "motion-to-photon" latency) to prevent vestibular mismatch and motion sickness.
3. **Tracking & Degrees of Freedom (DoF)**:
   - **3DoF (Rotational)**: Tracks Orientation only (Pitch, Yaw, Roll) — e.g., phone in Google Cardboard.
   - **6DoF (Positional + Rotational)**: Tracks orientation PLUS spatial translational coordinates ($X, Y, Z$) — walk forward, duck down, lean sideways. Enabled by SLAM (Simultaneous Localization and Mapping).
4. **Spatial Audio**:
   - 3D binaural sound processing that alters volume, delay, and frequency response depending on head rotation, making sounds appear to emanate from specific physical coordinates.
5. **Cameras, LiDAR & Depth Sensors**:
   - Time-of-Flight (ToF) and infrared cameras capture real-world geometry for room-scale boundary detection, hand tracking, and digital occlusion.

---

### 4.4 Virtual Reality Expedition: Visit Rio de Janeiro in VR
The curriculum features an immersive VR field trip to **Rio de Janeiro, Brazil**, allowing students to explore the colossal **Christ the Redeemer** statue atop Mount Corcovado using 360° stereoscopic view:
- **Navigation Controls**: Gyroscopic panning (moving phone or dragging touch screen) or HMD head tracking.
- **Educational Value**: Demonstrates how VR democratizes global exploration, allowing students in India to observe world heritage architecture in 1:1 scale without travel costs.

---

## 5. Chapter 4: Intro to 3D Block-Based Coding & XR Publishing

This unit teaches the end-to-end digital pipeline: **Designing in 3D -> Exporting 3D Geometry -> Publishing to WebAR/VR -> Packaging into a Native Mobile App**.

```text
┌─────────────────┐      .OBJ Export      ┌──────────────────┐
│ 1. TINKERCAD    │ ────────────────────> │ 2. SKETCHFAB     │
│ (Build 3D Pond) │                       │ (Config AR & VR) │
└─────────────────┘                       └──────────────────┘
                                                    │
                                           Share URL│ Webview
                                                    ▼
┌─────────────────┐      Scan QR Code     ┌──────────────────┐
│ 4. SMARTPHONE   │ <──────────────────── │ 3. MEDIAN.CO     │
│ (Google VR App) │                       │ (Web to App APK) │
└─────────────────┘                       └──────────────────┘
```

### 5.1 Step 1: 3D Modeling in Tinkercad (The 3D Pond Project)
Tinkercad is Autodesk's free, browser-based 3D modeling tool:
1. **Workplane & Navigation**:
   - Use the **ViewCube** to rotate views (Top, Front, Right, Isometric).
   - Right-click + drag to orbit, scroll wheel to zoom, middle-click + drag to pan.
2. **Constructing the Pond Terrain**:
   - Drag a solid **Cylinder** onto the workplane. Scale to: `Length: 80mm, Width: 60mm, Height: 15mm`.
   - Drag a "Hole" shape cylinder, scale slightly smaller (`70mm x 50mm x 12mm`), elevate by `3mm`.
   - Select both shapes and click **Group (`Ctrl + G`)** to hollow out the pond basin.
   - Drag a translucent blue oval cylinder into the basin to represent water.
3. **Adding Aquatic Creatures & Characters**:
   - In the Shape Panel dropdown, select **Creatures & Characters**.
   - Import fish, frogs, rocks, and water plants. Scale and arrange around the pond perimeter.
4. **Exporting the 3D Asset**:
   - Click **Export** in the top right.
   - Choose **`.OBJ`** format. Tinkercad downloads a `.zip` archive containing the 3D mesh (`.obj`) and material/texture definitions (`.mtl`).

---

### 5.2 Step 2: Hosting & Configuring in Sketchfab (WebAR/WebVR)
Sketchfab is the leading global repository for real-time 3D and immersive WebXR assets:
1. **Account Setup & Upload**:
   - Log into Sketchfab and click **Upload**.
   - Drag and drop the downloaded `.zip` archive containing the Pond `.obj` and `.mtl` files.
2. **3D Settings & Lighting**:
   - Open **3D Settings**. Under the **Lighting** tab, enable realistic environmental HDRI maps (e.g., "Park Sunset" or "Clear Sky").
   - Adjust ground shadows and ambient occlusion.
3. **Configuring AR & VR Properties**:
   - Click the **AR/VR Icon** in the settings toolbar.
   - Set the ground plane orientation so the pond sits flat on real floors.
   - Adjust scale (1 meter in virtual space = 1 unit).
   - Click the **VR Headset Icon** to preview how the pond appears when viewed through virtual goggles.
   - Click **Save & Publish** and copy the public sharing URL.

---

### 5.3 Step 3: Packaging into a Mobile VR App with Median.co
Median.co (formerly GoNative) wraps dynamic web pages into native Android `.apk` and iOS apps:
1. **App Configuration**:
   - Open Median.co and enter the public Sketchfab 3D Pond URL in the **Website URL** field.
   - Assign App Name: `"Pushti's Pond VR Explorer"`.
   - Set organization name and app icon.
2. **Build Generation**:
   - Click **Start Building My App!**.
   - Median's cloud compiler wraps the WebXR Sketchfab viewer inside a high-performance native WebView wrapper with hardware-accelerated WebGL.
3. **Deployment & Mobile Testing**:
   - A unique QR code is generated on screen.
   - Scan the QR code with an Android smartphone to download and install the `.apk`.
   - Insert the smartphone into a Google Cardboard or VR viewer to explore the 3D pond in full stereoscopic immersion!

---

## 6. Chapter 5: Brain & Logic Lab Worksheets

The handbook concludes with 5 rich cognitive enrichment and puzzle worksheets (Pages 32–36).

### 6.1 Page 32: The Rebus Equation Puzzle ("Guess What?")
A visual deduction equation where graphical representations correspond to syllables or phonetic word parts:
- **Equation**: Visual icons representing mathematical operators and numbers leading to word deduction.
- **Key Concepts Learned**: Symbolic thinking, cryptographic intuition, visual-linguistic pattern recognition.

### 6.2 Page 33: Linked Loops (Spatial Topology)
- **Challenge**: Identify 4 specific pairs of interlinked heart loops entangled among 24 (two dozen) overlapping, tangled heart contours.
- **Cognitive Competency**: Visual figure-ground perception, spatial continuity tracing, edge discrimination.

---

### 6.3 Pages 34–35: Braille Tactile Code System
#### Historical Context:
- Invented in **1824** by **Louis Braille** (1809–1852) at the age of **15**.
- Developed at the National Institute for Blind Children in Paris, inspired by Charles Barbier's military "night writing" system.

#### The 6-Dot Cell Architecture:
Braille characters are formed within a uniform **6-dot matrix cell** consisting of two parallel vertical columns of three dots each:
```text
  Dot 1 (Top Left)    ●   ○  Dot 4 (Top Right)
  Dot 2 (Middle Left) ○   ●  Dot 5 (Middle Right)
  Dot 3 (Bottom Left) ●   ○  Dot 6 (Bottom Right)
```

#### The Alphabet Encoding Matrix (A to Z):
- **A**: Dot 1
- **B**: Dots 1, 2
- **C**: Dots 1, 4
- **D**: Dots 1, 4, 5
- **E**: Dots 1, 5
- **F**: Dots 1, 2, 4
- **G**: Dots 1, 2, 4, 5
- **H**: Dots 1, 2, 5
- **I**: Dots 2, 4
- **J**: Dots 2, 4, 5
- **K**: Dots 1, 3
- **L**: Dots 1, 2, 3
- **M**: Dots 1, 3, 4
- **N**: Dots 1, 3, 4, 5
- **O**: Dots 1, 3, 5
- **P**: Dots 1, 2, 3, 4
- **Q**: Dots 1, 2, 3, 4, 5
- **R**: Dots 1, 2, 3, 5
- **S**: Dots 2, 3, 4
- **T**: Dots 2, 3, 4, 5
- **U**: Dots 1, 3, 6
- **V**: Dots 1, 2, 3, 6
- **W**: Dots 2, 4, 5, 6
- **X**: Dots 1, 3, 4, 6
- **Y**: Dots 1, 3, 4, 5, 6
- **Z**: Dots 1, 3, 5, 6

#### Decoding Worksheet Challenge:
- Example: Decoding the secret word:
  - Cell 1: Dots 1, 4 -> **C**
  - Cell 2: Dots 1, 3, 5 -> **O**
  - Cell 3: Dots 1, 4, 5 -> **D**
  - Cell 4: Dots 1, 5 -> **E**
  - Cell 5: Dots 1, 2, 3, 5 -> **R**
  - **Result**: `C - O - D - E - R`
- Exercise Word 2: `R - O - B - O - T`
- Exercise Word 3: `V - I - R - T - U - A - L`

---

### 6.4 Page 36: Classic 9x9 Sudoku
- **Rules**: Fill numbers 1 through 9 such that each digit appears exactly once in every row, every column, and every 3x3 sub-grid.
- **Skills Cultivated**: Deterministic algorithmic logic, elimination heuristics, memory buffer retention.

---

## 7. Chapter 6: Artificial Intelligence (AI) Foundations
*(Reserved Modular Branch)*
- **Status**: Textbook Part 2 (Artificial Intelligence) will be integrated directly into this branch upon arrival.
- **Anticipated Syllabus Topics**: Machine Learning fundamentals, Computer Vision (Teachable Machine), Natural Language Processing, Ethics in AI, Generative AI applications.

---
*Reference Handbook compiled strictly from source document `source_materials/Robo AR VR.pdf` for Pushti Study Hub under CBSE Class 7 AI & Robotics curriculum standards.*
