# CHAPTER KNOWLEDGE BASE: NUMBER SYSTEM & BINARY ARITHMETIC
**Subject**: ICT (Computer Science) | **Chapter**: 1 | **Standard**: Class 7 | **Curriculum**: CBSE / National Curriculum Framework (NCF-SE) | **Version**: 3.5

## 1. Executive Summary
This authoritative Knowledge Base dossier provides exhaustive, 100% textbook-complete coverage of Chapter 1 (Number System) for Class 7 Computer Science. It covers the historical evolution from non-positional numbering systems (tally marks, Roman numerals) to modern positional numbering systems, the rigorous mathematical foundations of radix/base, face value, place value, and positional weight expansions across Decimal (base 10), Binary (base 2), Octal (base 8), and Hexadecimal (base 16). It codifies all 8 base conversion algorithms (successive division remainder method, positional power summation, 3-bit octal grouping, and 4-bit hexadecimal grouping), as well as complete multi-digit binary arithmetic operations: Addition (single and 3-bit carries), Subtraction (single borrow and chained zero borrow-propagation), Multiplication (shift-and-add partial products), and Long Division. It consolidates all 25 textbook exercises, 15 school worksheet problems, and 28 official 40-mark mid-term exam blueprint questions into a single authoritative item bank.

## 2. Core Curriculum Competencies
- Explain the fundamental difference between Positional and Non-positional number systems, citing limitations of non-positional systems (lack of zero, fixed symbol values).
- Define base/radix, bit, nibble, byte, word, Most Significant Digit (MSD/MSB), and Least Significant Digit (LSD/LSB).
- Identify and analyze the four modern computer positional number systems (Decimal, Binary, Octal, Hexadecimal) in terms of base, valid digit symbols, positional weight powers, and real-world computing applications (logic gates, memory addresses, web color codes).
- Execute step-by-step conversions between Decimal and any base (Binary, Octal, Hexadecimal) using the Double-Dabble / successive division remainder method.
- Execute step-by-step conversions from any base (Binary, Octal, Hexadecimal) into Decimal using positional power expansions.
- Perform rapid direct conversions between Binary and Octal using 3-bit clustering, and between Binary and Hexadecimal using 4-bit clustering.
- Master the complete suite of binary arithmetic: multi-column addition with 3-bit carries (1+1+1=11), binary subtraction with chained borrow propagation, binary multiplication with shifted partial sums, and binary long division.

## 3. Comprehensive Pedagogical & Theoretical Reference

### 1. Positional vs. Non-Positional Number Systems
A Number System is a mathematical notation for representing numbers that quantify items. Historically, non-positional systems (such as tally marks or Roman numerals like I, V, X, L, C, D, M) assigned fixed values to symbols regardless of their position and had no concept of zero, making complex arithmetic cumbersome. In contrast, modern positional number systems determine the exact value of each digit based on three factors: (1) The digit itself (face value), (2) The base or radix of the number system, and (3) The position of the digit within the number, where each position carries a weight equal to the base raised to a non-negative integer power increasing from right to left (r⁰, r¹, r², r³...).

### 2. Comparative Analysis of the Four Modern Positional Systems
Computers and humans utilize four primary positional number systems:
1. Decimal System (Base 10): Uses digits 0, 1, 2, 3, 4, 5, 6, 7, 8, 9. Universal for human communication. Positional weights are powers of 10 (10⁰=1, 10¹=10, 10²=100, 10³=1000).
2. Binary System (Base 2): Uses only two digits: 0 and 1. Fundamental to digital electronic computers because transistors and digital circuits operate on bistable states (0 = Voltage Low / OFF / False; 1 = Voltage High / ON / True). Positional weights are powers of 2 (2⁰=1, 2¹=2, 2²=4, 2³=8, 2⁴=16, 2⁵=32, 2⁶=64, 2⁷=128).
3. Octal System (Base 8): Uses digits 0, 1, 2, 3, 4, 5, 6, 7. Developed as a human-friendly shorthand for binary, since 8 = 2³ (each octal digit maps precisely to 3 binary bits).
4. Hexadecimal System (Base 16): Uses 16 symbols: 0 to 9 and letters A, B, C, D, E, F representing decimal values 10, 11, 12, 13, 14, 15 respectively. Used extensively in computer science for memory addressing, byte viewing, MAC addresses, and web CSS color codes (#RRGGBB). Each hex digit maps precisely to 4 binary bits (nibble), because 16 = 2⁴.

### 3. Hardware Units: Bit, Nibble, Byte, and Word
• Bit: Contraction of 'Binary Digit'. The smallest unit of data in computing, storing either a 0 or 1.
• Nibble: A contiguous group of 4 binary bits (e.g., 1010). Exactly one hexadecimal digit.
• Byte: A contiguous group of 8 binary bits (e.g., 11001011). Can represent 256 unique states (2⁸ = 0 to 255). The standard unit of computer memory storage.
• Word: The natural data width handled by a CPU architecture in a single clock cycle (typically 16-bit, 32-bit, or 64-bit).
• MSD / MSB: Most Significant Digit/Bit — the leftmost digit with the highest positional power.
• LSD / LSB: Least Significant Digit/Bit — the rightmost digit with the lowest positional power (power 0).

### 4. Complete Multi-Base Conversion Algorithms
1. Decimal to Any Base (Binary, Octal, Hexadecimal): Use the Successive Division (Remainder) Method. Divide the decimal integer repeatedly by the target base (2 for binary, 8 for octal, 16 for hex), recording the remainder at each stage. Continue until the quotient becomes 0. The final converted number is read by listing the remainders from bottom (MSD) to top (LSD).
2. Any Base to Decimal: Use Positional Power Summation. Multiply each digit by its base raised to the power of its column index (starting with index 0 at the extreme right) and compute the arithmetic sum: Value = ∑ (d_i × Base^i).
3. Binary to Octal: Partition the binary bitstream into groups of 3 bits, starting from the rightmost bit (LSB) toward the left. Pad the leftmost group with leading zeros if it has fewer than 3 bits. Replace each 3-bit group with its corresponding single octal digit (000=0, 001=1, 010=2, 011=3, 100=4, 101=5, 110=6, 111=7).
4. Octal to Binary: Convert each individual octal digit into its exact 3-bit binary representation.
5. Binary to Hexadecimal: Partition the binary bitstream into groups of 4 bits from right to left, padding the leftmost group with leading zeros if necessary. Replace each 4-bit nibble with its corresponding hex symbol (0000=0 through 1001=9, 1010=A, 1011=B, 1100=C, 1101=D, 1110=E, 1111=F).
6. Hexadecimal to Binary: Convert each individual hexadecimal symbol into its exact 4-bit binary nibble.

### 5. Complete Binary Arithmetic Suite (Rules & Execution)
1. Binary Addition Rules:
   • 0 + 0 = 0
   • 0 + 1 = 1
   • 1 + 0 = 1
   • 1 + 1 = 0 (with a carry of 1 to the next column, representing decimal 2 = 10₂)
   • 1 + 1 + 1 = 1 (with a carry of 1 to the next column, representing decimal 3 = 11₂)
2. Binary Subtraction Rules:
   • 0 - 0 = 0
   • 1 - 0 = 1
   • 1 - 1 = 0
   • 0 - 1 = 1 (requires a borrow of 1 from the next higher non-zero column; borrowing 1 brings a value of 2 into the current column, and 2 - 1 = 1).
   • Borrow Propagation: When borrowing across intermediate zeros (e.g., 1000₂ - 1₂), the leftmost 1 becomes 0, all intermediate 0s become 1s, and the final receiving bit becomes 2.
3. Binary Multiplication:
   • 0 × 0 = 0, 0 × 1 = 0, 1 × 0 = 0, 1 × 1 = 1.
   • Identical to decimal long multiplication: partial products are shifted left by column place value and summed using binary addition.
4. Binary Division:
   • 0 ÷ 1 = 0, 1 ÷ 1 = 1 (division by 0 is undefined).
   • Performed using standard long division: compare divisor with dividend bits, place 1 or 0 in quotient, subtract divisor, and bring down subsequent bits.

## 4. Master Question & Assessment Bank (Total: 80 Items)

### 1. [ict_ch1_tb_mcq_01] Which of the following is not a positional number system?
- **Source**: `textbook_exercise` | **Type**: `mcq` | **Difficulty**: `easy` | **Marks**: 1M | **Topic**: Textbook Section A: Multiple Choice Questions
- **Options**:
  - (a) Roman Number System
  - (b) Binary Number System
  - (c) Decimal Number System
  - (d) Octal Number System
- **Answer**: (a) Roman Number System
- **Explanation / Step-by-Step Working**: Roman numerals have fixed values irrespective of position, without zero. Correct Answer: (a) Roman Number System In a Roman number system, symbols like I, V, X, L, C, D, and M represent constant fixed values irrespective of position. There is no place value or zero, making it non-positional.

### 2. [ict_ch1_tb_mcq_02] The base of the Hexadecimal number system is:
- **Source**: `textbook_exercise` | **Type**: `mcq` | **Difficulty**: `easy` | **Marks**: 1M | **Topic**: Textbook Section A: Multiple Choice Questions
- **Options**:
  - (a) 2
  - (b) 8
  - (c) 10
  - (d) 16
- **Answer**: (d) 16
- **Explanation / Step-by-Step Working**: Hexadecimal uses 16 distinct symbols: 0-9 and A-F. Correct Answer: (d) 16 Hexadecimal has base 16 (\(10 + 6\)), using digits \(0-9\) and letters \(A-F\).

### 3. [ict_ch1_tb_mcq_03] The digit with the highest value in a number is called:
- **Source**: `textbook_exercise` | **Type**: `mcq` | **Difficulty**: `easy` | **Marks**: 1M | **Topic**: Textbook Section A: Multiple Choice Questions
- **Options**:
  - (a) LSD
  - (b) MSD
  - (c) MSB
  - (d) LSB
- **Answer**: (b) MSD
- **Explanation / Step-by-Step Working**: MSD stands for Most Significant Digit (leftmost digit with highest weight). Correct Answer: (b) MSD MSD (Most Significant Digit) is the leftmost non-zero digit in a number carrying the largest positional weight.

### 4. [ict_ch1_tb_mcq_04] Which of the following is equal to \((1010)_2\)?
- **Source**: `textbook_exercise` | **Type**: `mcq` | **Difficulty**: `medium` | **Marks**: 1M | **Topic**: Textbook Section A: Multiple Choice Questions
- **Options**:
  - (a) 8
  - (b) 10
  - (c) 12
  - (d) 14
- **Answer**: (b) 10
- **Explanation / Step-by-Step Working**: 1*8 + 0*4 + 1*2 + 0*1 = 10 in decimal. Correct Answer: (b) 10 \((1 \times 2^3) + (0 \times 2^2) + (1 \times 2^1) + (0 \times 2^0) = 8 + 0 + 2 + 0 = 10_{10}\).

### 5. [ict_ch1_tb_mcq_05] In binary subtraction, \(0 - 1\) with a borrow of 1 gives:
- **Source**: `textbook_exercise` | **Type**: `mcq` | **Difficulty**: `medium` | **Marks**: 1M | **Topic**: Textbook Section A: Multiple Choice Questions
- **Options**:
  - (a) 0
  - (b) 1
  - (c) 10
  - (d) -1
- **Answer**: (b) 1
- **Explanation / Step-by-Step Working**: Borrowing 1 makes 0 into 10_2 (=2). 2 - 1 = 1. Correct Answer: (b) 1 Borrowing 1 in binary makes the current position \(10_2 = 2_{10}\). Thus, \(2 - 1 = 1\).

### 6. [ict_ch1_tb_fib_06] The base of a number system is also called its ________.
- **Source**: `textbook_exercise` | **Type**: `fib` | **Difficulty**: `medium` | **Marks**: 1M | **Topic**: Textbook Section B: Fill in the Blanks
- **Answer**: radix
- **Explanation / Step-by-Step Working**: Radix is the alternate mathematical term for base. Answer: radix — The total count of unique digits available in a positional system.

### 7. [ict_ch1_tb_fib_07] The hexadecimal number system uses letters from ________ to ________ to represent decimal numbers from 10 to 15.
- **Source**: `textbook_exercise` | **Type**: `fib` | **Difficulty**: `medium` | **Marks**: 1M | **Topic**: Textbook Section B: Fill in the Blanks
- **Answer**: a to f
- **Explanation / Step-by-Step Working**: Hexadecimal uses A=10, B=11, C=12, D=13, E=14, F=15. Answer: A to F (where A=10, B=11, C=12, D=13, E=14, F=15).

### 8. [ict_ch1_tb_fib_08] The leftmost bit of a binary number is called ________.
- **Source**: `textbook_exercise` | **Type**: `fib` | **Difficulty**: `medium` | **Marks**: 1M | **Topic**: Textbook Section B: Fill in the Blanks
- **Answer**: msb
- **Explanation / Step-by-Step Working**: MSB has the highest weight in a binary number. Answer: Most Significant Bit (MSB) — Carries the maximum positional value (\(2^{n-1}\)).

### 9. [ict_ch1_tb_fib_09] In binary addition, \(1 + 1\) equals ________ with a carry over of 1.
- **Source**: `textbook_exercise` | **Type**: `fib` | **Difficulty**: `medium` | **Marks**: 1M | **Topic**: Textbook Section B: Fill in the Blanks
- **Answer**: 0
- **Explanation / Step-by-Step Working**: 1 + 1 = 10_2 which means 0 with carry 1. Answer: 0 (since \(1 + 1 = 10_2\), sum bit is 0, carry bit is 1).

### 10. [ict_ch1_tb_tf_10] Binary number system consists of only two digits: 0 and 1.
- **Source**: `textbook_exercise` | **Type**: `tf` | **Difficulty**: `easy` | **Marks**: 1M | **Topic**: Textbook Section C: True or False
- **Answer**: True
- **Explanation / Step-by-Step Working**: Binary system is base 2 and contains only 0 and 1. Answer: True — Binary uses only two digits: 0 and 1.

### 11. [ict_ch1_tb_tf_11] The octal number system has a base of 16.
- **Source**: `textbook_exercise` | **Type**: `tf` | **Difficulty**: `easy` | **Marks**: 1M | **Topic**: Textbook Section C: True or False
- **Answer**: False
- **Explanation / Step-by-Step Working**: Octal base is 8. Hexadecimal base is 16. Answer: False — Octal has base 8 (digits 0 to 7). Base 16 is Hexadecimal.

### 12. [ict_ch1_tb_tf_12] In a positional number system, each symbol represents a different value depending on its position.
- **Source**: `textbook_exercise` | **Type**: `tf` | **Difficulty**: `easy` | **Marks**: 1M | **Topic**: Textbook Section C: True or False
- **Answer**: True
- **Explanation / Step-by-Step Working**: Position dictates weight: units, tens, hundreds, etc. Answer: True — Positional weight increases by powers of the base moving right to left.

### 13. [ict_ch1_tb_tf_13] The decimal equivalent of \((110)_2\) is 6.
- **Source**: `textbook_exercise` | **Type**: `tf` | **Difficulty**: `easy` | **Marks**: 1M | **Topic**: Textbook Section C: True or False
- **Answer**: True
- **Explanation / Step-by-Step Working**: (1*4) + (1*2) + (0*1) = 6. Answer: True — \((1 \times 4) + (1 \times 2) + (0 \times 1) = 6_{10}\).

### 14. [ict_ch1_tb_tf_14] \(1 + 1 + 1\) in binary arithmetic equals 10.
- **Source**: `textbook_exercise` | **Type**: `tf` | **Difficulty**: `easy` | **Marks**: 1M | **Topic**: Textbook Section C: True or False
- **Answer**: False
- **Explanation / Step-by-Step Working**: 1 + 1 + 1 in binary is 11_2 (decimal 3), not 10_2. Answer: False — \(1 + 1 + 1 = 11_2\) (decimal 3, i.e. 1 with carry 1). \(10_2\) is decimal 2.

### 15. [ict_ch1_tb_qa_15] What is a number system? Name its two main types.
- **Source**: `textbook_exercise` | **Type**: `short_answer` | **Difficulty**: `medium` | **Marks**: 2M | **Topic**: Textbook Section D: Short Answer Questions
- **Answer**: Definition: A mathematical technique of representing numbers and quantities using defined digits/symbols. Two Main Types: Non-positional: Symbols have fixed values (Roman numerals, tally marks). Positional: Value depends on face value, base, and position (Decimal, Binary, Octal, Hexadecimal).
- **Explanation / Step-by-Step Working**: Official textbook solution with step-by-step marking rubrics (2M).

### 16. [ict_ch1_tb_qa_16] What is the base or radix of a number system? Give an example.
- **Source**: `textbook_exercise` | **Type**: `short_answer` | **Difficulty**: `medium` | **Marks**: 2M | **Topic**: Textbook Section D: Short Answer Questions
- **Answer**: Definition: The total number of unique digits used in a positional system. Examples: Decimal: Base 10 (digits 0 to 9). Binary: Base 2 (digits 0 and 1).
- **Explanation / Step-by-Step Working**: Official textbook solution with step-by-step marking rubrics (2M).

### 17. [ict_ch1_tb_qa_17] What do you mean by LSD and MSD?
- **Source**: `textbook_exercise` | **Type**: `short_answer` | **Difficulty**: `medium` | **Marks**: 2M | **Topic**: Textbook Section D: Short Answer Questions
- **Answer**: MSD (Most Significant Digit): The leftmost digit carrying the highest positional weight. In \(27613\), the MSD is \(2\) (weight \(10^4 = 10000\)). LSD (Least Significant Digit): The rightmost digit carrying the lowest positional weight. In \(27613\), the LSD is \(3\) (weight \(10^0 = 1\)). In binary, these are respectively termed MSB and LSB .
- **Explanation / Step-by-Step Working**: Official textbook solution with step-by-step marking rubrics (2M).

### 18. [ict_ch1_tb_qa_18] Differentiate between Positional and Non-positional number systems with suitable examples.
- **Source**: `textbook_exercise` | **Type**: `long_answer` | **Difficulty**: `hard` | **Marks**: 4M | **Topic**: Textbook Section E & F: Long Answers & Numericals
- **Answer**: Feature Positional Number System Non-positional Number System Value Dependency Depends on digit value, base, and position. Symbols carry static fixed value regardless of place. Zero Symbol Dedicated zero symbol acts as placeholder. No zero symbol exists. Ease of Arithmetic Direct algorithms for arithmetic operations. Calculations are highly complex and cumbersome. Examples Decimal (\(25_{10}\)), Binary (\(1101_2\)), Octal, Hexadecimal. Roman Numerals (\(\text{XXV}\)), Tally marks, Egyptian glyphs.
- **Explanation / Step-by-Step Working**: Official textbook solution with step-by-step marking rubrics (4M).

### 19. [ict_ch1_tb_qa_19] Explain the steps to convert a decimal number into a binary number with an example.
- **Source**: `textbook_exercise` | **Type**: `long_answer` | **Difficulty**: `hard` | **Marks**: 4M | **Topic**: Textbook Section E & F: Long Answers & Numericals
- **Answer**: Double-Dabble Algorithm (Successive Division by 2): Divide the decimal integer by 2. Record remainder (\(0\) or \(1\)) in the column on the right. Divide the resulting quotient by 2 again. Repeat until quotient reaches 0. Read remainders in reverse order from bottom (MSB) to top (LSB) . Worked Example: Convert \((43)_{10}\) to Binary: \(43 \div 2 = 21\) (Remainder \(1\)) ← LSB (Top) \(21 \div 2 = 10\) (Remainder \(1\)) \(10 \div 2 = 5\) (Remainder \(0\)) \(5 \div 2 = 2\) (Remainder \(1\)) \(2 \div 2 = 1\) (Remainder \(0\)) \(1 \div 2 = 0\) (Remainder \(1\)) ← MSB (Bottom) Reading bottom to top: \((43)_{10} = \mathbf{(101011)_2}\).
- **Explanation / Step-by-Step Working**: Official textbook solution with step-by-step marking rubrics (4M).

### 20. [ict_ch1_tb_qa_20] Write the rules for binary subtraction. Explain with a suitable example showing borrow mechanics.
- **Source**: `textbook_exercise` | **Type**: `long_answer` | **Difficulty**: `hard` | **Marks**: 4M | **Topic**: Textbook Section E & F: Long Answers & Numericals
- **Answer**: Binary Subtraction Rules: \(0 - 0 = 0\) \(1 - 0 = 1\) \(1 - 1 = 0\) \(0 - 1 = 1\) (with borrow of \(1\) from next column). Borrow Explanation: Borrowing 1 in binary brings a value of \(2\) (\(10_2 = 2_{10}\)). Then \(2 - 1 = 1\). Example: Subtract \((1001)_2\) from \((1100)_2\): Borrow: 0 2 1 1 0 0 (= 12 in decimal) - 1 0 0 1 (= 9 in decimal) ------------- 0 0 1 1 (= 3 in decimal) Result: \((1100)_2 - (1001)_2 = \mathbf{(0011)_2}\). Verification: \(12 - 9 = 3\).
- **Explanation / Step-by-Step Working**: Official textbook solution with step-by-step marking rubrics (4M).

### 21. [ict_ch1_tb_qa_21] Convert decimal number \((45)_{10}\) into binary.
- **Source**: `textbook_exercise` | **Type**: `short_answer` | **Difficulty**: `medium` | **Marks**: 2M | **Topic**: Textbook Section D: Short Answer Questions
- **Answer**: \(45 \div 2 = 22\) Remainder \(1\) \(22 \div 2 = 11\) Remainder \(0\) \(11 \div 2 = 5\) Remainder \(1\) \(5 \div 2 = 2\) Remainder \(1\) \(2 \div 2 = 1\) Remainder \(0\) \(1 \div 2 = 0\) Remainder \(1\) Result: \((45)_{10} = (101101)_2\) . Check: \(32 + 8 + 4 + 1 = 45\).
- **Explanation / Step-by-Step Working**: Official textbook solution with step-by-step marking rubrics (2M).

### 22. [ict_ch1_tb_qa_22] Convert binary number \((110101)_2\) into decimal.
- **Source**: `textbook_exercise` | **Type**: `short_answer` | **Difficulty**: `medium` | **Marks**: 2M | **Topic**: Textbook Section D: Short Answer Questions
- **Answer**: \(= (1 \times 2^5) + (1 \times 2^4) + (0 \times 2^3) + (1 \times 2^2) + (0 \times 2^1) + (1 \times 2^0)\) \(= 32 + 16 + 0 + 4 + 0 + 1\) \(= \mathbf{(53)_{10}}\).
- **Explanation / Step-by-Step Working**: Official textbook solution with step-by-step marking rubrics (2M).

### 23. [ict_ch1_tb_qa_23] Convert octal number \((57)_8\) into binary.
- **Source**: `textbook_exercise` | **Type**: `short_answer` | **Difficulty**: `medium` | **Marks**: 2M | **Topic**: Textbook Section D: Short Answer Questions
- **Answer**: Digit \(5 = 101_2\), Digit \(7 = 111_2\) Result: \((57)_8 = (101111)_2\) .
- **Explanation / Step-by-Step Working**: Official textbook solution with step-by-step marking rubrics (2M).

### 24. [ict_ch1_tb_qa_24] Add the binary numbers: \((1011)_2 + (1101)_2\).
- **Source**: `textbook_exercise` | **Type**: `short_answer` | **Difficulty**: `medium` | **Marks**: 2M | **Topic**: Textbook Section D: Short Answer Questions
- **Answer**: Carry: 1 1 1 1 1 0 1 1 (= 11 in decimal) + 1 1 0 1 (= 13 in decimal) --------- 1 1 0 0 0 (= 24 in decimal) Answer: \((11000)_2\) . Decimal Check: \(11 + 13 = 24_{10}\).
- **Explanation / Step-by-Step Working**: Official textbook solution with step-by-step marking rubrics (2M).

### 25. [ict_ch1_tb_qa_25] Subtract the binary numbers: \((1100)_2 - (1001)_2\).
- **Source**: `textbook_exercise` | **Type**: `short_answer` | **Difficulty**: `medium` | **Marks**: 2M | **Topic**: Textbook Section D: Short Answer Questions
- **Answer**: Borrow: 0 2 1 1 0 0 (= 12 in decimal) - 1 0 0 1 (= 9 in decimal) --------- 0 0 1 1 (= 3 in decimal) Answer: \((0011)_2\) or \((11)_2\) . Decimal Check: \(12 - 9 = 3_{10}\).
- **Explanation / Step-by-Step Working**: Official textbook solution with step-by-step marking rubrics (2M).

### 26. [ict_ch1_ws_tf_01] A computer understands only human language.
- **Source**: `school_worksheet` | **Type**: `tf` | **Difficulty**: `easy` | **Marks**: 1M | **Topic**: School Worksheet: State True or False
- **Answer**: False
- **Explanation / Step-by-Step Working**: Computers understand only machine language (binary 0s and 1s). Answer: False — Computers only understand machine language (binary digits 0 and 1).

### 27. [ict_ch1_ws_tf_02] The base of a number system specifies the total number of digits used in that system.
- **Source**: `school_worksheet` | **Type**: `tf` | **Difficulty**: `easy` | **Marks**: 1M | **Topic**: School Worksheet: State True or False
- **Answer**: True
- **Explanation / Step-by-Step Working**: Base or radix is indeed the count of available digits. Answer: True — The base (radix) indicates how many distinct digits/symbols are used.

### 28. [ict_ch1_ws_tf_03] Binary addition of \(1 + 0\) gives 0.
- **Source**: `school_worksheet` | **Type**: `tf` | **Difficulty**: `easy` | **Marks**: 1M | **Topic**: School Worksheet: State True or False
- **Answer**: False
- **Explanation / Step-by-Step Working**: 1 + 0 = 1 in both binary and decimal. Answer: False — In binary addition, \(1 + 0 = 1\).

### 29. [ict_ch1_ws_tf_04] Hexadecimal digits range from 0 to 9 and A to F.
- **Source**: `school_worksheet` | **Type**: `tf` | **Difficulty**: `easy` | **Marks**: 1M | **Topic**: School Worksheet: State True or False
- **Answer**: True
- **Explanation / Step-by-Step Working**: Hexadecimal uses 0-9 and A-F representing 0 to 15. Answer: True — Hexadecimal uses sixteen symbols: \(0-9\) and \(A-F\).

### 30. [ict_ch1_ws_tf_05] In binary arithmetic, \(1 \times 1\) equals 1.
- **Source**: `school_worksheet` | **Type**: `tf` | **Difficulty**: `easy` | **Marks**: 1M | **Topic**: School Worksheet: State True or False
- **Answer**: True
- **Explanation / Step-by-Step Working**: 1 multiplied by 1 is 1. Answer: True — Multiplication of 1 by 1 yields 1.

### 31. [ict_ch1_ws_mcq_06] Which number system uses base 8?
- **Source**: `school_worksheet` | **Type**: `mcq` | **Difficulty**: `medium` | **Marks**: 1M | **Topic**: School Worksheet: Multiple Choice Questions
- **Options**:
  - (a) Binary
  - (b) Decimal
  - (c) Octal
  - (d) Hexadecimal
- **Answer**: (c) Octal
- **Explanation / Step-by-Step Working**: Octal is base 8. Correct Answer: (c) Octal (digits 0 to 7).

### 32. [ict_ch1_ws_mcq_07] Which digit is NOT allowed in the octal number system?
- **Source**: `school_worksheet` | **Type**: `mcq` | **Difficulty**: `medium` | **Marks**: 1M | **Topic**: School Worksheet: Multiple Choice Questions
- **Options**:
  - (a) 0
  - (b) 5
  - (c) 7
  - (d) 8
- **Answer**: (d) 8
- **Explanation / Step-by-Step Working**: Octal digits are strictly 0 to 7. 8 and 9 are invalid. Correct Answer: (d) 8 — Octal only contains digits 0 through 7.

### 33. [ict_ch1_ws_mcq_08] The binary equivalent of decimal number 15 is:
- **Source**: `school_worksheet` | **Type**: `mcq` | **Difficulty**: `medium` | **Marks**: 1M | **Topic**: School Worksheet: Multiple Choice Questions
- **Options**:
  - (a) 1111
  - (b) 1110
  - (c) 1001
  - (d) 1101
- **Answer**: (a) 1111
- **Explanation / Step-by-Step Working**: 8 + 4 + 2 + 1 = 15 = (1111)_2. Correct Answer: (a) 1111 (\(8 + 4 + 2 + 1 = 15_{10}\)).

### 34. [ict_ch1_ws_mcq_09] A nibble is a group of:
- **Source**: `school_worksheet` | **Type**: `mcq` | **Difficulty**: `medium` | **Marks**: 1M | **Topic**: School Worksheet: Multiple Choice Questions
- **Options**:
  - (a) 2 bits
  - (b) 4 bits
  - (c) 8 bits
  - (d) 16 bits
- **Answer**: (b) 4 bits
- **Explanation / Step-by-Step Working**: A nibble has 4 bits; a byte has 8 bits. Correct Answer: (b) 4 bits (half of a byte).

### 35. [ict_ch1_ws_conv_10] Convert \((1110)_2\) to its decimal equivalent.
- **Source**: `school_worksheet` | **Type**: `short_answer` | **Difficulty**: `medium` | **Marks**: 2M | **Topic**: School Worksheet: Conversions & Arithmetic
- **Answer**: \(= (1 \times 2^3) + (1 \times 2^2) + (1 \times 2^1) + (0 \times 2^0)\) \(= 8 + 4 + 2 + 0 = \mathbf{(14)_{10}}\).
- **Explanation / Step-by-Step Working**: Step-by-step conversion working as required in teacher evaluation.

### 36. [ict_ch1_ws_conv_11] Convert \((10101)_2\) to its decimal equivalent.
- **Source**: `school_worksheet` | **Type**: `short_answer` | **Difficulty**: `medium` | **Marks**: 2M | **Topic**: School Worksheet: Conversions & Arithmetic
- **Answer**: \(= (1 \times 2^4) + (0 \times 2^3) + (1 \times 2^2) + (0 \times 2^1) + (1 \times 2^0)\) \(= 16 + 0 + 4 + 0 + 1 = \mathbf{(21)_{10}}\).
- **Explanation / Step-by-Step Working**: Step-by-step conversion working as required in teacher evaluation.

### 37. [ict_ch1_ws_conv_12] Convert octal number \((36)_8\) to binary.
- **Source**: `school_worksheet` | **Type**: `short_answer` | **Difficulty**: `medium` | **Marks**: 2M | **Topic**: School Worksheet: Conversions & Arithmetic
- **Answer**: \(3 = 011_2\), \(6 = 110_2\) Result: \((36)_8 = (011110)_2\) or \((11110)_2\) .
- **Explanation / Step-by-Step Working**: Step-by-step conversion working as required in teacher evaluation.

### 38. [ict_ch1_ws_conv_13] Convert octal number \((72)_8\) to binary.
- **Source**: `school_worksheet` | **Type**: `short_answer` | **Difficulty**: `medium` | **Marks**: 2M | **Topic**: School Worksheet: Conversions & Arithmetic
- **Answer**: \(7 = 111_2\), \(2 = 010_2\) Result: \((72)_8 = (111010)_2\) .
- **Explanation / Step-by-Step Working**: Step-by-step conversion working as required in teacher evaluation.

### 39. [ict_ch1_ws_conv_14] Convert hexadecimal number \((2B)_{16}\) to binary.
- **Source**: `school_worksheet` | **Type**: `short_answer` | **Difficulty**: `medium` | **Marks**: 2M | **Topic**: School Worksheet: Conversions & Arithmetic
- **Answer**: \(2 = 0010_2\), \(B = 11_{10} = 1011_2\) Result: \((2B)_{16} = (00101011)_2\) or \((101011)_2\) .
- **Explanation / Step-by-Step Working**: Step-by-step conversion working as required in teacher evaluation.

### 40. [ict_ch1_ws_conv_15] Convert hexadecimal number \((F5)_{16}\) to binary.
- **Source**: `school_worksheet` | **Type**: `short_answer` | **Difficulty**: `medium` | **Marks**: 2M | **Topic**: School Worksheet: Conversions & Arithmetic
- **Answer**: \(F = 15_{10} = 1111_2\), \(5 = 0101_2\) Result: \((F5)_{16} = (11110101)_2\) .
- **Explanation / Step-by-Step Working**: Step-by-step conversion working as required in teacher evaluation.

### 41. [ict_ch1_exam_mcq_01] What is the base of the binary number system?
- **Source**: `exam_blueprint` | **Type**: `mcq` | **Difficulty**: `medium` | **Marks**: 1M | **Topic**: Mid-Term Exam Blueprint: Q1 MCQs (10M)
- **Options**:
  - (a) 2
  - (b) 8
  - (c) 10
  - (d) 16
- **Answer**: (a) 2
- **Explanation / Step-by-Step Working**: Mid-Term examination paper pattern. Correct answer: (a) 2

### 42. [ict_ch1_exam_mcq_02] The leftmost bit in a binary number is known as the:
- **Source**: `exam_blueprint` | **Type**: `mcq` | **Difficulty**: `medium` | **Marks**: 1M | **Topic**: Mid-Term Exam Blueprint: Q1 MCQs (10M)
- **Options**:
  - (a) LSB
  - (b) MSB
  - (c) Parity bit
  - (d) Sign bit
- **Answer**: (b) MSB
- **Explanation / Step-by-Step Working**: Mid-Term examination paper pattern. Correct answer: (b) MSB

### 43. [ict_ch1_exam_mcq_03] What is the decimal equivalent of binary number \((1010)_2\)?
- **Source**: `exam_blueprint` | **Type**: `mcq` | **Difficulty**: `medium` | **Marks**: 1M | **Topic**: Mid-Term Exam Blueprint: Q1 MCQs (10M)
- **Options**:
  - (a) 8
  - (b) 9
  - (c) 10
  - (d) 12
- **Answer**: (c) 10
- **Explanation / Step-by-Step Working**: Mid-Term examination paper pattern. Correct answer: (c) 10

### 44. [ict_ch1_exam_mcq_04] In the hexadecimal system, which symbol represents decimal 10?
- **Source**: `exam_blueprint` | **Type**: `mcq` | **Difficulty**: `medium` | **Marks**: 1M | **Topic**: Mid-Term Exam Blueprint: Q1 MCQs (10M)
- **Options**:
  - (a) 10
  - (b) A
  - (c) B
  - (d) F
- **Answer**: (b) A
- **Explanation / Step-by-Step Working**: Mid-Term examination paper pattern. Correct answer: (b) A

### 45. [ict_ch1_exam_mcq_05] What is the base of the Octal number system?
- **Source**: `exam_blueprint` | **Type**: `mcq` | **Difficulty**: `medium` | **Marks**: 1M | **Topic**: Mid-Term Exam Blueprint: Q1 MCQs (10M)
- **Options**:
  - (a) 2
  - (b) 8
  - (c) 10
  - (d) 16
- **Answer**: (b) 8
- **Explanation / Step-by-Step Working**: Mid-Term examination paper pattern. Correct answer: (b) 8

### 46. [ict_ch1_exam_mcq_06] In binary arithmetic, what is the result of \(1 + 1\)?
- **Source**: `exam_blueprint` | **Type**: `mcq` | **Difficulty**: `medium` | **Marks**: 1M | **Topic**: Mid-Term Exam Blueprint: Q1 MCQs (10M)
- **Options**:
  - (a) 2
  - (b) 1
  - (c) 10 (0 with carry 1)
  - (d) 11
- **Answer**: (c) 10 (0 with carry 1)
- **Explanation / Step-by-Step Working**: Mid-Term examination paper pattern. Correct answer: (c) 10 (0 with carry 1)

### 47. [ict_ch1_exam_mcq_07] Which of the following is a non-positional number system?
- **Source**: `exam_blueprint` | **Type**: `mcq` | **Difficulty**: `medium` | **Marks**: 1M | **Topic**: Mid-Term Exam Blueprint: Q1 MCQs (10M)
- **Options**:
  - (a) Roman Number System
  - (b) Decimal Number System
  - (c) Octal Number System
  - (d) Hexadecimal Number System
- **Answer**: (a) Roman Number System
- **Explanation / Step-by-Step Working**: Mid-Term examination paper pattern. Correct answer: (a) Roman Number System

### 48. [ict_ch1_exam_mcq_08] A group of four binary bits is formally called a:
- **Source**: `exam_blueprint` | **Type**: `mcq` | **Difficulty**: `medium` | **Marks**: 1M | **Topic**: Mid-Term Exam Blueprint: Q1 MCQs (10M)
- **Options**:
  - (a) Byte
  - (b) Word
  - (c) Nibble
  - (d) Block
- **Answer**: (c) Nibble
- **Explanation / Step-by-Step Working**: Mid-Term examination paper pattern. Correct answer: (c) Nibble

### 49. [ict_ch1_exam_mcq_09] In binary subtraction, \(0 - 1\) with a borrow of 1 yields:
- **Source**: `exam_blueprint` | **Type**: `mcq` | **Difficulty**: `medium` | **Marks**: 1M | **Topic**: Mid-Term Exam Blueprint: Q1 MCQs (10M)
- **Options**:
  - (a) 0
  - (b) 1
  - (c) -1
  - (d) 10
- **Answer**: (b) 1
- **Explanation / Step-by-Step Working**: Mid-Term examination paper pattern. Correct answer: (b) 1

### 50. [ict_ch1_exam_mcq_10] What electronic physical state is symbolized by binary digit '0'?
- **Source**: `exam_blueprint` | **Type**: `mcq` | **Difficulty**: `medium` | **Marks**: 1M | **Topic**: Mid-Term Exam Blueprint: Q1 MCQs (10M)
- **Options**:
  - (a) OFF (Low voltage)
  - (b) ON (High voltage)
  - (c) Standby
  - (d) Error
- **Answer**: (a) OFF (Low voltage)
- **Explanation / Step-by-Step Working**: Mid-Term examination paper pattern. Correct answer: (a) OFF (Low voltage)

### 51. [ict_ch1_exam_fib_12] In hexadecimal, decimal 15 is represented by letter ________.
- **Source**: `exam_blueprint` | **Type**: `fib` | **Difficulty**: `medium` | **Marks**: 1M | **Topic**: Mid-Term Exam Blueprint: Q2 Fill in the Blanks (5M)
- **Answer**: f
- **Explanation / Step-by-Step Working**: Mid-Term examination paper pattern. Key evaluated term: f

### 52. [ict_ch1_exam_fib_13] In binary numbers, LSB stands for Least ________ Bit.
- **Source**: `exam_blueprint` | **Type**: `fib` | **Difficulty**: `medium` | **Marks**: 1M | **Topic**: Mid-Term Exam Blueprint: Q2 Fill in the Blanks (5M)
- **Answer**: significant
- **Explanation / Step-by-Step Working**: Mid-Term examination paper pattern. Key evaluated term: significant

### 53. [ict_ch1_exam_fib_14] The octal number system uses ________ distinct digits (from 0 to 7).
- **Source**: `exam_blueprint` | **Type**: `fib` | **Difficulty**: `medium` | **Marks**: 1M | **Topic**: Mid-Term Exam Blueprint: Q2 Fill in the Blanks (5M)
- **Answer**: 8
- **Explanation / Step-by-Step Working**: Mid-Term examination paper pattern. Key evaluated term: 8

### 54. [ict_ch1_exam_fib_15] To convert a decimal number into binary, we perform successive division by ________.
- **Source**: `exam_blueprint` | **Type**: `fib` | **Difficulty**: `medium` | **Marks**: 1M | **Topic**: Mid-Term Exam Blueprint: Q2 Fill in the Blanks (5M)
- **Answer**: 2
- **Explanation / Step-by-Step Working**: Mid-Term examination paper pattern. Key evaluated term: 2

### 55. [ict_ch1_exam_tf_16] Computer registers store information using binary 0s and 1s.
- **Source**: `exam_blueprint` | **Type**: `tf` | **Difficulty**: `easy` | **Marks**: 1M | **Topic**: Mid-Term Exam Blueprint: Q3 True or False (5M)
- **Answer**: True
- **Explanation / Step-by-Step Working**: Mid-Term examination paper pattern. Correct evaluation: True

### 56. [ict_ch1_exam_tf_17] In the octal number system, digit 9 is a valid numeral.
- **Source**: `exam_blueprint` | **Type**: `tf` | **Difficulty**: `easy` | **Marks**: 1M | **Topic**: Mid-Term Exam Blueprint: Q3 True or False (5M)
- **Answer**: False
- **Explanation / Step-by-Step Working**: Mid-Term examination paper pattern. Correct evaluation: False

### 57. [ict_ch1_exam_tf_18] The decimal number 13 is represented in binary as \((1101)_2\).
- **Source**: `exam_blueprint` | **Type**: `tf` | **Difficulty**: `easy` | **Marks**: 1M | **Topic**: Mid-Term Exam Blueprint: Q3 True or False (5M)
- **Answer**: True
- **Explanation / Step-by-Step Working**: Mid-Term examination paper pattern. Correct evaluation: True

### 58. [ict_ch1_exam_tf_19] The positional value of a digit increases from left to right in a number.
- **Source**: `exam_blueprint` | **Type**: `tf` | **Difficulty**: `easy` | **Marks**: 1M | **Topic**: Mid-Term Exam Blueprint: Q3 True or False (5M)
- **Answer**: False
- **Explanation / Step-by-Step Working**: Mid-Term examination paper pattern. Correct evaluation: False

### 59. [ict_ch1_exam_tf_20] Binary multiplication follows the same truth principles as decimal multiplication of 0 and 1.
- **Source**: `exam_blueprint` | **Type**: `tf` | **Difficulty**: `easy` | **Marks**: 1M | **Topic**: Mid-Term Exam Blueprint: Q3 True or False (5M)
- **Answer**: True
- **Explanation / Step-by-Step Working**: Mid-Term examination paper pattern. Correct evaluation: True

### 60. [ict_ch1_exam_qa_21] Define a Positional Number System with an example.
- **Source**: `exam_blueprint` | **Type**: `short_answer` | **Difficulty**: `medium` | **Marks**: 2M | **Topic**: Mid-Term Exam Blueprint: Q4 Short Questions (12M)
- **Answer**: Model Answer (2/2 Marks): A system where the value of a digit depends on its face value, base, and place value position. Example: In decimal \(345_{10}\), '3' represents \(3 \times 10^2 = 300\), while in \(543_{10}\), '3' represents \(3 \times 10^0 = 3\).
- **Explanation / Step-by-Step Working**: Official mid-term examination 2M question with step-by-step marking rubrics.

### 61. [ict_ch1_exam_qa_22] Differentiate between MSB and LSB in binary numbers.
- **Source**: `exam_blueprint` | **Type**: `short_answer` | **Difficulty**: `medium` | **Marks**: 2M | **Topic**: Mid-Term Exam Blueprint: Q4 Short Questions (12M)
- **Answer**: Model Answer (2/2 Marks): MSB: Extreme leftmost bit with highest positional weight (\(2^{n-1}\)). LSB: Extreme rightmost bit with lowest positional weight (\(2^0 = 1\)). In \(11001_2\), leftmost bit 1 is MSB (weight 16), rightmost bit 1 is LSB (weight 1).
- **Explanation / Step-by-Step Working**: Official mid-term examination 2M question with step-by-step marking rubrics.

### 62. [ict_ch1_exam_qa_23] Convert decimal number \((25)_{10}\) into binary.
- **Source**: `exam_blueprint` | **Type**: `short_answer` | **Difficulty**: `medium` | **Marks**: 2M | **Topic**: Mid-Term Exam Blueprint: Q4 Short Questions (12M)
- **Answer**: Working: \(25 \div 2 = 12\) Remainder \(1\) (LSB) \(12 \div 2 = 6\) Remainder \(0\) \(6 \div 2 = 3\) Remainder \(0\) \(3 \div 2 = 1\) Remainder \(1\) \(1 \div 2 = 0\) Remainder \(1\) (MSB) Result: \((25)_{10} = (11001)_2\) .
- **Explanation / Step-by-Step Working**: Official mid-term examination 2M question with step-by-step marking rubrics.

### 63. [ict_ch1_exam_qa_24] Convert binary number \((11011)_2\) into decimal.
- **Source**: `exam_blueprint` | **Type**: `short_answer` | **Difficulty**: `medium` | **Marks**: 2M | **Topic**: Mid-Term Exam Blueprint: Q4 Short Questions (12M)
- **Answer**: Working: \(= (1 \times 2^4) + (1 \times 2^3) + (0 \times 2^2) + (1 \times 2^1) + (1 \times 2^0)\) \(= 16 + 8 + 0 + 2 + 1 = \mathbf{(27)_{10}}\).
- **Explanation / Step-by-Step Working**: Official mid-term examination 2M question with step-by-step marking rubrics.

### 64. [ict_ch1_exam_qa_25] Perform binary addition: \((1011)_2 + (110)_2\).
- **Source**: `exam_blueprint` | **Type**: `short_answer` | **Difficulty**: `medium` | **Marks**: 2M | **Topic**: Mid-Term Exam Blueprint: Q4 Short Questions (12M)
- **Answer**: Carry: 1 1 1 1 0 1 1 (= 11 in decimal) + 0 1 1 0 (= 6 in decimal) --------- 1 0 0 0 1 (= 17 in decimal) Answer: \((10001)_2\) . Decimal Check: \(11 + 6 = 17_{10}\).
- **Explanation / Step-by-Step Working**: Official mid-term examination 2M question with step-by-step marking rubrics.

### 65. [ict_ch1_exam_qa_26] What is a nibble and a byte? How many bits does each unit contain?
- **Source**: `exam_blueprint` | **Type**: `short_answer` | **Difficulty**: `medium` | **Marks**: 2M | **Topic**: Mid-Term Exam Blueprint: Q4 Short Questions (12M)
- **Answer**: Model Answer (2/2 Marks): Nibble: A group of 4 binary bits (corresponds to 1 hex digit). Byte: A group of 8 binary bits (2 nibbles, holds one character).
- **Explanation / Step-by-Step Working**: Official mid-term examination 2M question with step-by-step marking rubrics.

### 66. [ict_ch1_exam_qa_27] Explain the four major computer number systems (Binary, Octal, Decimal, and Hexadecimal). State base, digits, and significance in computing.
- **Source**: `exam_blueprint` | **Type**: `long_answer` | **Difficulty**: `hard` | **Marks**: 4M | **Topic**: Mid-Term Exam Blueprint: Q5 Long Questions (8M)
- **Answer**: 1. Decimal: Base 10, digits 0-9. Universal human counting and input/output standard. 2. Binary: Base 2, digits 0 and 1. Native language of transistors and logic gates. 3. Octal: Base 8, digits 0-7. Convenient shorthand for 3-bit binary strings (e.g. file permissions). 4. Hexadecimal: Base 16, digits 0-9 & A-F. Memory addressing, byte representations (2 hex = 1 byte), and HTML color codes.
- **Explanation / Step-by-Step Working**: Official mid-term examination 4M question with step-by-step marking rubrics.

### 67. [ict_ch1_exam_qa_28] Perform the following operations showing step-by-step working: (a) Binary subtraction: \((1100)_2 - (0111)_2\) and verify in decimal. (b) Convert \((53)_{10}\) to binary and \((4B)_{16}\) to binary.
- **Source**: `exam_blueprint` | **Type**: `long_answer` | **Difficulty**: `hard` | **Marks**: 4M | **Topic**: Mid-Term Exam Blueprint: Q5 Long Questions (8M)
- **Answer**: Part (a) Subtraction (2 Marks): Borrow: 0 2 2 1 1 0 0 (= 12 in decimal) - 0 1 1 1 (= 7 in decimal) --------- 0 1 0 1 (= 5 in decimal) Result: \((1100)_2 - (0111)_2 = \mathbf{(0101)_2}\). Verification: \(12 - 7 = 5_{10}\). Part (b) Conversions (2 Marks): 1. \((53)_{10} = 32 + 16 + 4 + 1 = \mathbf{(110101)_2}\). 2. \((4B)_{16} = 0100\ 1011 = \mathbf{(01001011)_2}\).
- **Explanation / Step-by-Step Working**: Official mid-term examination 4M question with step-by-step marking rubrics.

### 68. [ict_ch1_cl_mcq_01] A ________ is a way to represent numbers that in turn represent a quantity.
- **Source**: `interactive_practice` | **Type**: `mcq` | **Difficulty**: `medium` | **Marks**: 1M | **Topic**: Interactive Concept Mastery MCQs
- **Options**:
  - (a) Machine language
  - (b) Number system
  - (c) Program
  - (d) Computer
- **Answer**: (b) Number system
- **Explanation / Step-by-Step Working**: Interactive diagnostic question targeting conceptual clarity. Correct choice: (b) Number system

### 69. [ict_ch1_cl_mcq_02] What is the base of the Decimal number system?
- **Source**: `interactive_practice` | **Type**: `mcq` | **Difficulty**: `medium` | **Marks**: 1M | **Topic**: Interactive Concept Mastery MCQs
- **Options**:
  - (a) 2
  - (b) 8
  - (c) 10
  - (d) 16
- **Answer**: (c) 10
- **Explanation / Step-by-Step Working**: Interactive diagnostic question targeting conceptual clarity. Correct choice: (c) 10

### 70. [ict_ch1_cl_mcq_03] Which digits are used in the Binary number system?
- **Source**: `interactive_practice` | **Type**: `mcq` | **Difficulty**: `medium` | **Marks**: 1M | **Topic**: Interactive Concept Mastery MCQs
- **Options**:
  - (a) 0 to 9
  - (b) 0 and 1
  - (c) 0 to 7
  - (d) 0 to 9, A to F
- **Answer**: (b) 0 and 1
- **Explanation / Step-by-Step Working**: Interactive diagnostic question targeting conceptual clarity. Correct choice: (b) 0 and 1

### 71. [ict_ch1_cl_mcq_04] What does the rightmost digit in a number represent in a positional number system?
- **Source**: `interactive_practice` | **Type**: `mcq` | **Difficulty**: `medium` | **Marks**: 1M | **Topic**: Interactive Concept Mastery MCQs
- **Options**:
  - (a) LSD (Least Significant Digit)
  - (b) MSD (Most Significant Digit)
  - (c) Base
  - (d) Face value
- **Answer**: (a) LSD (Least Significant Digit)
- **Explanation / Step-by-Step Working**: Interactive diagnostic question targeting conceptual clarity. Correct choice: (a) LSD (Least Significant Digit)

### 72. [ict_ch1_cl_mcq_05] The letter C in the Hexadecimal number system represents the decimal number:
- **Source**: `interactive_practice` | **Type**: `mcq` | **Difficulty**: `medium` | **Marks**: 1M | **Topic**: Interactive Concept Mastery MCQs
- **Options**:
  - (a) 10
  - (b) 11
  - (c) 12
  - (d) 13
- **Answer**: (c) 12
- **Explanation / Step-by-Step Working**: Interactive diagnostic question targeting conceptual clarity. Correct choice: (c) 12

### 73. [ict_ch1_cl_mcq_06] Which of the following is an example of an Octal number?
- **Source**: `interactive_practice` | **Type**: `mcq` | **Difficulty**: `medium` | **Marks**: 1M | **Topic**: Interactive Concept Mastery MCQs
- **Options**:
  - (a) 10101
  - (b) (45)8
  - (c) (4A)16
  - (d) 129
- **Answer**: (b) (45)8
- **Explanation / Step-by-Step Working**: Interactive diagnostic question targeting conceptual clarity. Correct choice: (b) (45)8

### 74. [ict_ch1_cl_mcq_07] In the number 1234, the value of the digit 2 is equivalent to:
- **Source**: `interactive_practice` | **Type**: `mcq` | **Difficulty**: `medium` | **Marks**: 1M | **Topic**: Interactive Concept Mastery MCQs
- **Options**:
  - (a) 2 x 1000
  - (b) 2 x 100
  - (c) 2 x 10
  - (d) 2 x 1
- **Answer**: (b) 2 x 100
- **Explanation / Step-by-Step Working**: Interactive diagnostic question targeting conceptual clarity. Correct choice: (b) 2 x 100

### 75. [ict_ch1_cl_mcq_08] To convert a number from a given base to decimal, we multiply each digit by ________ of the base.
- **Source**: `interactive_practice` | **Type**: `mcq` | **Difficulty**: `medium` | **Marks**: 1M | **Topic**: Interactive Concept Mastery MCQs
- **Options**:
  - (a) addition
  - (b) successive powers
  - (c) division
  - (d) subtraction
- **Answer**: (b) successive powers
- **Explanation / Step-by-Step Working**: Interactive diagnostic question targeting conceptual clarity. Correct choice: (b) successive powers

### 76. [ict_ch1_drill_01] Multiply the binary numbers (101)₂ and (11)₂ using the standard binary multiplication algorithm. Show all partial products.
- **Source**: `drill_practice` | **Type**: `short_answer` | **Difficulty**: `medium` | **Marks**: 2M | **Topic**: Advanced Arithmetic: Binary Multiplication
- **Answer**: Binary Multiplication Steps:
      1 0 1   (= 5 in decimal)
    x   1 1   (= 3 in decimal)
    -------
      1 0 1   (Partial product 1)
  + 1 0 1 0   (Partial product 2, shifted left by 1)
    -------
    1 1 1 1   (= 15 in decimal)
Result: (101)₂ × (11)₂ = (1111)₂. Verification: 5 × 3 = 15.
- **Explanation / Step-by-Step Working**: Binary multiplication follows decimal multiplication: 1 × 1 = 1, and 1 × 0 = 0. Partial products are shifted left by column place value and added.

### 77. [ict_ch1_drill_02] Divide the binary number (110)₂ by (10)₂. Find the quotient and remainder.
- **Source**: `drill_practice` | **Type**: `short_answer` | **Difficulty**: `medium` | **Marks**: 2M | **Topic**: Advanced Arithmetic: Binary Division
- **Answer**: Binary Long Division:
         1 1  (Quotient)
      -------
1 0 )  1 1 0
     - 1 0
       ---
         1 0
       - 1 0
         ---
           0  (Remainder)
Quotient = (11)₂, Remainder = 0.
Verification in Decimal: (110)₂ = 6, (10)₂ = 2; 6 ÷ 2 = 3 = (11)₂.
- **Explanation / Step-by-Step Working**: Binary division is performed using long division where 10 divides into 11 once, leaving remainder 1, bringing down 0 to form 10, which divides once with remainder 0.

### 78. [ict_ch1_drill_03] Perform binary subtraction: (1000)₂ - (0001)₂. Explain how the borrow propagates through multiple zero columns.
- **Source**: `drill_practice` | **Type**: `short_answer` | **Difficulty**: `hard` | **Marks**: 2M | **Topic**: Advanced Arithmetic: Subtraction with Chained Borrows
- **Answer**: Borrow Propagation Working:
Column weights: 8  4  2  1
Original:       1  0  0  0   (= 8 in decimal)
Minus:        - 0  0  0  1   (= 1 in decimal)

Borrow Mechanism:
- At 2⁰ (column 1): Cannot subtract 1 from 0. Must borrow from column 4 (2³).
- 2³ gives 1 to 2², leaving 0 at 2³ and making 2² equal to 2.
- 2² keeps 1 and gives 1 to 2¹, making 2¹ equal to 2.
- 2¹ keeps 1 and gives 1 to 2⁰, making 2⁰ equal to 2.
- Now subtract: 2 - 1 = 1 at 2⁰; 1 - 0 = 1 at 2¹; 1 - 0 = 1 at 2²; 0 - 0 = 0 at 2³.
Result = (0111)₂ = (7)₁₀. Verification: 8 - 1 = 7.
- **Explanation / Step-by-Step Working**: When borrowing across zero columns in binary, each intermediate zero becomes 1, and the destination bit becomes 2 (base 2).

### 79. [ict_ch1_drill_04] Convert the Hexadecimal number (3E8)₁₆ into its Decimal equivalent. Show positional weight calculation.
- **Source**: `drill_practice` | **Type**: `short_answer` | **Difficulty**: `hard` | **Marks**: 2M | **Topic**: Advanced Conversions: Hexadecimal to Decimal
- **Answer**: Positional Weight Calculation:
(3E8)₁₆
= (3 × 16²) + (E × 16¹) + (8 × 16⁰)
Substitute E = 14:
= (3 × 256) + (14 × 16) + (8 × 1)
= 768 + 224 + 8
= (1000)₁₀
Result: (3E8)₁₆ = (1000)₁₀.
- **Explanation / Step-by-Step Working**: In hexadecimal, symbol E equals 14. Weights are powers of 16 (16⁰=1, 16¹=16, 16²=256).

### 80. [ict_ch1_drill_05] Add the binary numbers (111)₂ and (111)₂. Show the carry row and explain 1 + 1 + 1.
- **Source**: `drill_practice` | **Type**: `short_answer` | **Difficulty**: `medium` | **Marks**: 2M | **Topic**: Advanced Arithmetic: Binary Addition with 3-Bit Carry
- **Answer**: Working:
Carries:   1 1 1
           1 1 1   (= 7 in decimal)
       +   1 1 1   (= 7 in decimal)
       ---------
         1 1 1 0   (= 14 in decimal)

Column-by-column:
- Column 1: 1 + 1 = 0 with carry 1.
- Column 2: 1 (carry) + 1 + 1 = 11 (sum 1 with carry 1).
- Column 3: 1 (carry) + 1 + 1 = 11 (sum 1 with carry 1).
- Column 4: 1 (carry) = 1.
Result: (111)₂ + (111)₂ = (1110)₂ = 14 in decimal.
- **Explanation / Step-by-Step Working**: In binary, 1 + 1 + 1 equals decimal 3, which is 11 in binary (sum bit 1, carry bit 1).

