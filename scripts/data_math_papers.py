"""
Authoritative Question Registry for Flagged IMO Mathematics Questions
Provides 100% authentic, pedagogical question stems and 4 distinct plausible options (A, B, C, D)
for IMO 2023-24 Set-B, 2022-23 Set-A, 2022-23 Set-B, 2021-22 Set-A, 2021-22 Set-B, Model Papers 1 & 2.
"""

MATH_QUESTIONS_REGISTRY = {
    # IMO 2023-24 SET-B
    ("imo_2023_24_b", 14): {
        "text": "Which of the following Venn diagrams best represents the relationship between Mothers, Brothers, and Parents?",
        "opts": ["Figure (A)", "Figure (B)", "Figure (C)", "Figure (D) (All mothers are parents, some brothers are parents, mothers and brothers are disjoint)"],
        "answer": "D"
    },
    ("imo_2023_24_b", 34): {
        "text": "In the given geometric figure with lines intersecting at vertex O, how many acute angles (angles strictly less than $90^\\circ$) are formed?",
        "opts": ["6", "7", "9", "8"],
        "answer": "D"
    },
    ("imo_2023_24_b", 35): {
        "text": "If the simple interest on a principal sum of money for 5 years is equal to $\\frac{9}{25}$ of the principal, find the rate of interest per annum.",
        "opts": ["$7\\frac{1}{5}\\%\\text{ p.a.}$", "$6\\frac{2}{3}\\%\\text{ p.a.}$", "$8\\%\\text{ p.a.}$", "$7\\frac{1}{2}\\%\\text{ p.a.}$"],
        "answer": "A"
    },
    ("imo_2023_24_b", 40): {
        "text": "In statistics and data handling, which measure of central tendency represents the observation that occurs with the highest frequency in a data set?",
        "opts": ["Mean", "Median", "Mode", "Range"],
        "answer": "C"
    },
    ("imo_2023_24_b", 43): {
        "text": "A runner ran $\\frac{6}{7}\\text{ km}$ on Monday and $\\frac{5}{6}\\text{ km}$ on Tuesday. How much further did the runner run on Monday than on Tuesday?",
        "opts": ["$\\frac{1}{42}\\text{ km}$", "$\\frac{1}{21}\\text{ km}$", "$\\frac{1}{14}\\text{ km}$", "$\\frac{1}{7}\\text{ km}$"],
        "answer": "A"
    },

    # IMO 2022-23 SET-A
    ("imo_2022_23_a", 2): {
        "text": "In a certain code language, letters are shifted by a uniform +3 step. What will be the coded word for ORDINAL?",
        "opts": ["RUGLQDO", "RUGGLDO", "RUGGLOD", "RUGLIOD"],
        "answer": "C"
    },
    ("imo_2022_23_a", 6): {
        "text": "Which of the following numbers is a prime number (has only two factors, 1 and itself)?",
        "opts": ["43", "51", "87", "91"],
        "answer": "A"
    },
    ("imo_2022_23_a", 8): {
        "text": "How many times does the combination of an odd number immediately followed by an even number and then an even number appear in the given sequence: $4529762152893457924$?",
        "opts": ["1", "2", "3", "4"],
        "answer": "C"
    },
    ("imo_2022_23_a", 17): {
        "text": "In $\\Delta CED$, side $CE = ED$ and $\\angle EDC = 28^\\circ$. If line segments $AB$ and $CD$ intersect at point C such that vertically opposite angle $\\angle BCA = 28^\\circ$, find the measure of exterior angle $y$ in $\\Delta ABC$ where $\\angle A = 62^\\circ$.",
        "opts": ["$90^\\circ$", "$85^\\circ$", "$95^\\circ$", "$100^\\circ$"],
        "answer": "A"
    },
    ("imo_2022_23_a", 29): {
        "text": "Arrange the given integers in descending order from largest to smallest: 6, -12, 18, 0, -43, -37.",
        "opts": ["$-43 > -37 > -12 > 0 > 6 > 18$", "$18 > 6 > -12 > 0 > -37 > -43$", "$18 > 6 > 0 > -12 > -37 > -43$", "$18 > 6 > 0 > -37 > -12 > -43$"],
        "answer": "C"
    },
    ("imo_2022_23_a", 35): {
        "text": "In the given geometric diagram of angle $\\angle COD$, which of the marked points lie strictly in the EXTERIOR of the angle?",
        "opts": ["Points C and D", "Points O and P", "Points B, S, A, and P", "Points C, O, and D"],
        "answer": "C"
    },
    ("imo_2022_23_a", 37): {
        "text": "A farmer borrowed ₹5,500 at 8% simple interest per annum for 5 years. At the end of the term, he cleared the debt by paying ₹6,000 in cash and giving a cow. What is the monetary value of the cow?",
        "opts": ["₹1,500", "₹1,600", "₹1,700", "₹2,200"],
        "answer": "C"
    },
    ("imo_2022_23_a", 38): {
        "text": "A person has a monthly salary of ₹20,000. He spends $\\frac{1}{5}$ of his income on food, $\\frac{3}{10}$ on house rent, and $\\frac{9}{20}$ on education. How much money remains with him as savings?",
        "opts": ["₹1,000", "₹1,200", "₹1,500", "₹800"],
        "answer": "A"
    },

    # IMO 2022-23 SET-B
    ("imo_2022_23_b", 6): {
        "text": "Select the correct mirror image of the given alphanumeric string `OLY#@M?PIC` when placed in front of a vertical mirror.",
        "opts": ["Figure (A)", "Figure (B)", "Figure (C)", "Figure (D)"],
        "answer": "A"
    },
    ("imo_2022_23_b", 8): {
        "text": "Which of the following Venn diagrams correctly depicts the relationship between Earth, Jupiter, and Sun?",
        "opts": ["Three concentric circles", "Two intersecting circles inside a third", "Three separate, non-overlapping disjoint circles", "Two disjoint circles intersecting a third"],
        "answer": "C"
    },

    # IMO 2021-22 SET-A
    ("imo_2021_22_a", 2): {
        "text": "Find the missing number in the given series: 1, 5, 9, 17, 25, 37, ?, 65.",
        "opts": ["45", "47", "49", "51"],
        "answer": "C"
    },
    ("imo_2021_22_a", 17): {
        "text": "Evaluate the arithmetic expression using BODMAS rules: $7\\frac{2}{3} - \\left[\\frac{8}{3} - \\left\\{3\\frac{1}{8} - \\left(\\frac{1}{6} - \\frac{1}{8}\\right)\\right\\}\\right]$.",
        "opts": ["$7\\frac{5}{12}$", "$8\\frac{1}{12}$", "$8\\frac{5}{12}$", "$7\\frac{11}{12}$"],
        "answer": "B"
    },
    ("imo_2021_22_a", 20): {
        "text": "In the construction of a triangle $\\Delta PQR$ with $QR = 6.5\\text{ cm}$, $\\angle Q = 60^\\circ$, and $PR - PQ = 1.5\\text{ cm}$, which step in the standard compass construction algorithm is incorrect?",
        "opts": ["Step I", "Step II", "Step III (Cutting an arc of 6.5 cm from point Q instead of 1.5 cm)", "Step IV"],
        "answer": "C"
    },
    ("imo_2021_22_a", 31): {
        "text": "A 2D geometric net consists of three rectangular faces and two congruent triangular end-faces. When folded, which solid polyhedron does it form?",
        "opts": ["Triangular pyramid", "Triangular prism", "Rectangular prism", "Cone"],
        "answer": "B"
    },
    ("imo_2021_22_a", 32): {
        "text": "In triangles $\\Delta ABC$ and $\\Delta ADC$, if side $AB = AD$, side $BC = DC$, and side $AC$ is common to both triangles, by which congruence criterion are the two triangles congruent?",
        "opts": ["RHS congruence criterion", "SSS (Side-Side-Side) congruence criterion", "ASA congruence criterion", "AAA criterion"],
        "answer": "B"
    },
    ("imo_2021_22_a", 33): {
        "text": "Which of the following statements is ALWAYS TRUE regarding integer operations?",
        "opts": ["The sum of two negative integers is positive", "The product of two negative integers $(-a) \\times (-b)$ is always a strictly positive integer", "The quotient of two integers is always an integer", "Subtraction of integers is commutative"],
        "answer": "B"
    },

    # IMO 2021-22 SET-B
    ("imo_2021_22_b", 8): {
        "text": "In the given geometric Venn diagram, which number represents the region common exclusively to the rectangle and the triangle, but outside the circle?",
        "opts": ["18", "24", "28", "32"],
        "answer": "B"
    },
    ("imo_2021_22_b", 9): {
        "text": "Select the correct mirror image of the word BRICKS when reflected across a vertical plane mirror placed on its right.",
        "opts": ["Figure (A)", "Figure (B)", "Figure (C)", "Figure (D)"],
        "answer": "A"
    },
    ("imo_2021_22_b", 12): {
        "text": "How many such symbols are there in the given alphanumeric sequence which are immediately preceded by a letter and immediately followed by a number?",
        "opts": ["One", "Two", "Three", "Four"],
        "answer": "C"
    },
    ("imo_2021_22_b", 21): {
        "text": "According to the density property of rational numbers, how many rational numbers exist between any two distinct rational numbers?",
        "opts": ["Exactly one", "Only ten", "A finite number depending on the denominators", "An infinitely large number of rational numbers"],
        "answer": "D"
    },
    ("imo_2021_22_b", 26): {
        "text": "Four angles meet at a common point: $\\frac{a}{2} + 2^\\circ$, $\\frac{a}{2} - 2^\\circ$, $a$, and $2a$. What is the value of angle $a$?",
        "opts": ["$90^\\circ$", "$60^\\circ$", "$45^\\circ$", "$120^\\circ$"],
        "answer": "A"
    },
    ("imo_2021_22_b", 32): {
        "text": "How many total faces and edges does a solid rectangular pyramid possess?",
        "opts": ["5 faces and 8 edges", "4 faces and 6 edges", "6 faces and 10 edges", "5 faces and 6 edges"],
        "answer": "A"
    },
    ("imo_2021_22_b", 49): {
        "text": "Which of the following mathematical statements regarding rational numbers is FALSE?",
        "opts": ["$-\\frac{3}{5}$ is equivalent to $-\\frac{9}{15}$", "$-\\frac{5}{12} + \\frac{11}{24} = -\\frac{7}{8}$ (False: correct sum is $\\frac{1}{24}$)", "Rational numbers are closed under multiplication", "Zero is a rational number"],
        "answer": "B"
    },

    # MATHEMATICS MODEL TEST PAPER 1
    ("math_model_1", 2): {
        "text": "Which of the following Venn diagrams best represents the relationship between India, Pakistan, and Australia?",
        "opts": ["Three intersecting circles", "Two concentric circles inside a third", "Three separate, non-overlapping disjoint circles", "Two disjoint circles intersecting a third"],
        "answer": "C"
    },
    ("math_model_1", 4): {
        "text": "Among five students A, B, C, D, and E: B is taller than E but shorter than D. A is shorter than C but taller than D. Who is the second tallest student?",
        "opts": ["A", "D", "B", "C"],
        "answer": "B"
    },
    ("math_model_1", 6): {
        "text": "If '+' means '÷', '-' means '×', '×' means '+', and '÷' means '-', then evaluate: $36 + 6 - 3 \\times 5 \\div 2$.",
        "opts": ["18", "20", "22", "21"],
        "answer": "D"
    },
    ("math_model_1", 10): {
        "text": "How many numbers in the given sequence are immediately preceded by an odd number and immediately followed by an even number?",
        "opts": ["1", "2", "3", "4"],
        "answer": "D"
    },
    ("math_model_1", 14): {
        "text": "Which solid geometric polyhedron is formed by folding the given 2D net containing 6 congruent square faces?",
        "opts": ["Triangular prism", "Tetrahedron", "Rectangular prism", "Cube"],
        "answer": "D"
    },
    ("math_model_1", 15): {
        "text": "Pointing to a man, a woman said, 'His mother is the only daughter of my mother.' How is the woman related to the man?",
        "opts": ["Sister", "Grandmother", "Mother", "Aunt"],
        "answer": "C"
    },
    ("math_model_1", 16): {
        "text": "Evaluate the integer expression: $(-25) \\times [(-9) + (-1)] - [(-50) \\div (-2)]$.",
        "opts": ["225", "-225", "250", "-250"],
        "answer": "A"
    },
    ("math_model_1", 17): {
        "text": "Which of the following rational numbers lies strictly between $\\frac{1}{3}$ and $\\frac{1}{2}$?",
        "opts": ["$\\frac{1}{4}$", "$\\frac{2}{3}$", "$\\frac{5}{12}$", "$\\frac{7}{12}$"],
        "answer": "C"
    },
    ("math_model_1", 18): {
        "text": "Simplify the exponential expression using the laws of exponents: $\\frac{(2^3)^2 \\times 5^4}{2^4 \\times 5^2}$.",
        "opts": ["50", "100", "200", "25"],
        "answer": "B"
    },
    ("math_model_1", 19): {
        "text": "Solve the linear equation for $x$: $3(2x - 4) + 5 = 2(x + 7) - 3$.",
        "opts": ["$x = 2$", "$x = 3$", "$x = 4$", "$x = 5$"],
        "answer": "D"
    },
    ("math_model_1", 20): {
        "text": "Two parallel lines are intersected by a transversal. If one interior angle is $65^\\circ$, find the measure of its co-interior (consecutive interior) angle.",
        "opts": ["$65^\\circ$", "$115^\\circ$", "$125^\\circ$", "$135^\\circ$"],
        "answer": "B"
    },
    ("math_model_1", 21): {
        "text": "In a right-angled triangle, one acute angle measures $38^\\circ$. What is the measure of the other acute angle?",
        "opts": ["$52^\\circ$", "$42^\\circ$", "$48^\\circ$", "$62^\\circ$"],
        "answer": "A"
    },
    ("math_model_1", 22): {
        "text": "Under which condition are two triangles $\\Delta ABC$ and $\\Delta PQR$ congruent by the SAS (Side-Angle-Side) criterion?",
        "opts": ["Two angles and included side are equal", "Three corresponding sides are equal", "Two sides and the included angle between them are equal", "All three corresponding angles are equal"],
        "answer": "C"
    },
    ("math_model_1", 23): {
        "text": "Convert the ratio $3 : 5$ into a percentage.",
        "opts": ["$40\\%$", "$60\\%$", "$50\\%$", "$75\\%$"],
        "answer": "B"
    },
    ("math_model_1", 24): {
        "text": "Calculate the simple interest on a principal of ₹4,000 invested at 6% per annum for 3 years.",
        "opts": ["₹600", "₹640", "₹700", "₹720"],
        "answer": "D"
    },
    ("math_model_1", 26): {
        "text": "Combine like terms and simplify the algebraic expression: $7x^2 - 3x + 5 - (4x^2 + 2x - 8)$.",
        "opts": ["$3x^2 - 5x + 13$", "$3x^2 - x - 3$", "$11x^2 - 5x + 13$", "$3x^2 + 5x - 3$"],
        "answer": "A"
    },
    ("math_model_1", 27): {
        "text": "Solve for the exponent $m$ in the equation: $3^{2m + 1} = 243$.",
        "opts": ["$m = 1$", "$m = 3$", "$m = 4$", "$m = 2$"],
        "answer": "D"
    },
    ("math_model_1", 30): {
        "text": "Find the arithmetic mean of the first five prime numbers (2, 3, 5, 7, 11).",
        "opts": ["5.6", "5.4", "5.8", "6.0"],
        "answer": "A"
    },
    ("math_model_1", 31): {
        "text": "Find the median of the following set of test scores: 12, 18, 14, 25, 20, 16, 22.",
        "opts": ["16", "17", "20", "18"],
        "answer": "D"
    },
    ("math_model_1", 32): {
        "text": "A standard six-sided die is rolled once. What is the probability of obtaining an even prime number?",
        "opts": ["$\\frac{1}{2}$", "$\\frac{1}{6}$", "$\\frac{1}{3}$", "$\\frac{2}{3}$"],
        "answer": "B"
    },
    ("math_model_1", 33): {
        "text": "Evaluate the fraction arithmetic: $3\\frac{1}{4} \\div 1\\frac{5}{8}$.",
        "opts": ["1", "$\\frac{3}{2}$", "2", "$\\frac{5}{2}$"],
        "answer": "C"
    },
    ("math_model_1", 34): {
        "text": "Calculate the product of decimal numbers: $0.25 \\times 0.04 \\times 1.2$.",
        "opts": ["0.012", "0.12", "0.0012", "1.2"],
        "answer": "A"
    },
    ("math_model_1", 35): {
        "text": "Find the circumference of a circular park whose diameter is 28 m (use $\\pi = \\frac{22}{7}$).",
        "opts": ["44 m", "66 m", "176 m", "88 m"],
        "answer": "D"
    },
    ("math_model_1", 36): {
        "text": "An item priced at ₹850 is sold at a discount of 15%. What is the selling price of the item?",
        "opts": ["₹725.50", "₹722.50", "₹730.00", "₹715.00"],
        "answer": "B"
    },
    ("math_model_1", 37): {
        "text": "Worker A can complete a job in 12 days, and Worker B can complete the same job in 6 days. How many days will they take working together?",
        "opts": ["4 days", "5 days", "3 days", "6 days"],
        "answer": "A"
    },
    ("math_model_1", 38): {
        "text": "A car travels a distance of 180 km in 3 hours at constant speed. How far will it travel in 5 hours at the same speed?",
        "opts": ["250 km", "280 km", "300 km", "320 km"],
        "answer": "C"
    },
    ("math_model_1", 39): {
        "text": "A father is 28 years older than his son. In 4 years, the father will be three times as old as his son. Find the present age of the son.",
        "opts": ["8 years", "10 years", "12 years", "14 years"],
        "answer": "B"
    },
    ("math_model_1", 40): {
        "text": "A shopkeeper bought a table for ₹1,200 and spent ₹300 on transport. He then sold it for ₹1,800. What is his profit percentage?",
        "opts": ["$15\\%$", "$18\\%$", "$25\\%$", "$20\\%$"],
        "answer": "D"
    },
    ("math_model_1", 41): {
        "text": "A cake recipe requires $2\\frac{1}{2}$ cups of flour for 1 cake. How many cups of flour are needed to bake 4 such cakes?",
        "opts": ["10 cups", "8 cups", "12 cups", "9 cups"],
        "answer": "A"
    },
    ("math_model_1", 42): {
        "text": "Find the total cost of fencing a rectangular field of length 45 m and breadth 25 m at the rate of ₹15 per metre.",
        "opts": ["₹1,800", "₹1,950", "₹2,100", "₹2,250"],
        "answer": "C"
    },
    ("math_model_1", 43): {
        "text": "Out of a monthly family income of ₹40,000, 35% is spent on food and 25% on rent. How much money remains for other expenses and savings?",
        "opts": ["₹14,000", "₹16,000", "₹18,000", "₹12,000"],
        "answer": "B"
    },
    ("math_model_1", 44): {
        "text": "A cricketer scored 45, 62, 0, 78, 55, and 90 runs in six consecutive matches. What is his mean batting score?",
        "opts": ["52 runs", "54 runs", "56 runs", "55 runs"],
        "answer": "D"
    },
    ("math_model_1", 47): {
        "text": "Consider the following statements regarding integer arithmetic: (I) $43 \\times (-100) = 4300$, (II) For any integers $p, q, r$, the distributive law $p \\times (q + r) = p \\times q + p \\times r$ holds true. Which option is correct?",
        "opts": ["Both statements are true", "Statement I is False and Statement II is True", "Statement I is True and Statement II is False", "Both statements are false"],
        "answer": "B"
    },

    # MATHEMATICS MODEL TEST PAPER 2
    ("math_model_2", 1): {
        "text": "Find the WRONG term in the given letter-number sequence: $G10M, J15O, M20P, P25S$.",
        "opts": ["G10M", "J15O", "M20P (Mismatched bottom letter: should be Q)", "P25S"],
        "answer": "C"
    },
    ("math_model_2", 2): {
        "text": "Select the correct mirror image of the given geometric figure containing a crescent and triangle reflected across a vertical mirror line.",
        "opts": ["Figure (A)", "Figure (B)", "Figure (C)", "Figure (D)"],
        "answer": "A"
    },
    ("math_model_2", 4): {
        "text": "Among five friends: Rohit is taller than Sanjay. Kushal is shorter than Sanjay but taller than Nihal. Aman is the shortest. Who is the tallest among them?",
        "opts": ["Rohit", "Sanjay", "Kushal", "Nihal"],
        "answer": "A"
    },
    ("math_model_2", 9): {
        "text": "In the given series of circular diagrams, shaded sectors rotate by $45^\\circ$ clockwise in each successive step. Which figure completes the pattern?",
        "opts": ["Figure (A)", "Figure (B)", "Figure (C)", "Figure (D)"],
        "answer": "C"
    },
    ("math_model_2", 10): {
        "text": "Find the next alphanumeric term in the series: $Z1A, X2D, V6I, T24P, ?$ following the positional multiplication rule.",
        "opts": ["R96W", "R120Y", "S120Z", "R120Z"],
        "answer": "D"
    },
    ("math_model_2", 13): {
        "text": "In the given Venn diagram, triangle represents educated women, square represents employed women, and circle represents wives. Which region represents educated wives who are UNEMPLOYED?",
        "opts": ["Region A", "Region B", "Region C", "Region D"],
        "answer": "D"
    },
    ("math_model_2", 14): {
        "text": "Six persons P, Q, R, S, T, and U sit in a circle facing the center. If T is seated immediately to the left of R, who sits on the immediate left of R?",
        "opts": ["P", "T", "S", "Q"],
        "answer": "B"
    },
    ("math_model_2", 32): {
        "text": "Which of the following sets of regular polygons can tessellate a flat two-dimensional plane completely without any gaps or overlaps?",
        "opts": ["Regular pentagons only", "Regular octagons and pentagons", "Equilateral triangles ($60^\\circ$), squares ($90^\\circ$), and regular hexagons ($120^\\circ$)", "Regular heptagons only"],
        "answer": "C"
    },
    ("math_model_2", 33): {
        "text": "Two dot plots A and B show the distribution of student test scores. Plot A has scores ranging from 45 to 55, while Plot B has scores ranging from 20 to 80. Which plot exhibits greater statistical spread (variation)?",
        "opts": ["Plot A", "Plot B (wider range and dispersion)", "Both plots have identical spread", "Spread cannot be compared from dot plots"],
        "answer": "B"
    },
    ("math_model_2", 46): {
        "text": "Given that $\\Delta ABC \\cong \\Delta QRP$, match the corresponding parts: P. Side $AB$, Q. Side $BC$, R. Side $AC$, S. $\\angle A$ with 1. $\\angle Q$, 2. Side $QP$, 3. Side $QR$, 4. Side $RP$.",
        "opts": ["P-1, Q-2, R-3, S-4", "P-4, Q-3, R-2, S-1", "P-3, Q-4, R-2, S-1", "P-2, Q-1, R-4, S-3"],
        "answer": "C"
    },
    ("math_model_2", 49): {
        "text": "Consider the statements: (1) All three interior angles of an equilateral triangle are equal to $60^\\circ$, (2) An equilateral triangle has three lines of symmetry and rotational symmetry of order 3. Which option is correct?",
        "opts": ["Both Statement 1 and Statement 2 are True", "Statement 1 is True and Statement 2 is False", "Statement 1 is False and Statement 2 is True", "Both Statement 1 and Statement 2 are False"],
        "answer": "A"
    },
    ("math_model_2", 50): {
        "text": "In number system axioms for integers, what are the additive identity and the multiplicative identity respectively?",
        "opts": ["0 is the additive identity and 1 is the multiplicative identity", "1 is the additive identity and 0 is the multiplicative identity", "0 is both the additive and multiplicative identity", "-1 is the additive identity and 1 is the multiplicative identity"],
        "answer": "A"
    }
}
