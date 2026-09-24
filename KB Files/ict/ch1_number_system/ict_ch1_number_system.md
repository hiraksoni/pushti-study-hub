# CHAPTER KNOWLEDGE BASE: NUMBER SYSTEM
**Subject**: ICT | **Chapter**: 1 | **Standard**: Class 7 CBSE

## 1. Executive Summary
Covers positional and non-positional number systems, radix bases (Decimal, Binary, Octal, Hexadecimal), positional weight expansion, number conversions, and binary arithmetic (addition with carry and subtraction with borrow).

## 2. Core Conceptual Theory & Notes
### [chapter_notes] Types of Number Systems
Non-positional (tally marks, Roman numerals) had fixed symbol values and lacked zero. Positional systems (Decimal, Binary, Octal, Hexadecimal) determine value by digit, base (radix), and position (weights increasing right-to-left as powers of base).

### [chapter_notes] Four Modern Positional Systems
Decimal: Base 10, digits 0-9 (human daily usage). Binary: Base 2, digits 0,1 (digital computer circuits, switches ON/OFF). Octal: Base 8, digits 0-7 (compact binary grouping into 3-bit clusters). Hexadecimal: Base 16, symbols 0-9 and A-F where A=10, B=11, C=12, D=13, E=14, F=15 (used in memory addressing, byte representation, web hex color codes).

### [chapter_notes] Binary Addition Rules
0 + 0 = 0; 0 + 1 = 1; 1 + 0 = 1; 1 + 1 = 10 (0 with carry 1 to next higher column); 1 + 1 + 1 = 11 (1 with carry 1).

### [chapter_notes] Binary Subtraction Rules
0 - 0 = 0; 1 - 0 = 1; 1 - 1 = 0; 0 - 1 = 1 with a borrow of 1 from the next higher column (a borrow in binary brings value 2).

### [chapter_notes] Conversion Algorithms
Decimal to Binary: Repeated division by 2, recording remainders from bottom to top (MSB to LSB). Binary to Decimal: Multiply each bit by 2 raised to its position power (2^0, 2^1, 2^2, ...) and sum the products.

## 3. Tagged Question & Assessment Bank
### Q1. [ict_ch1_tb_mcq1] | Radix Definition
* **Source**: `textbook_exercise` | **Type**: `mcq` | **Difficulty**: `easy` | **Marks**: 1M
* **Question**: The base of a number system is also called its ________.
* **Options**:
  - (a) Exponent
  - (b) Radix
  - (c) Mantissa
  - (d) Quotient
* **Answer**: (b) Radix
* **Explanation**: The base of any number system denotes the total number of unique digits or symbols it uses, and is formally termed the 'Radix'.

### Q2. [ict_ch1_tb_mcq2] | Hexadecimal Symbols
* **Source**: `textbook_exercise` | **Type**: `mcq` | **Difficulty**: `easy` | **Marks**: 1M
* **Question**: In the Hexadecimal number system, the letter 'D' represents the decimal value ________.
* **Options**:
  - (a) 11
  - (b) 12
  - (c) 13
  - (d) 14
* **Answer**: (c) 13
* **Explanation**: In Hexadecimal: A=10, B=11, C=12, D=13, E=14, F=15.

### Q3. [ict_ch1_tb_mcq3] | Binary Arithmetic
* **Source**: `textbook_exercise` | **Type**: `mcq` | **Difficulty**: `medium` | **Marks**: 1M
* **Question**: In binary addition, what is 1 + 1?
* **Options**:
  - (a) 2
  - (b) 1
  - (c) 10
  - (d) 11
* **Answer**: (c) 10
* **Explanation**: 1 + 1 equals decimal 2, which is represented in binary as 10 (sum 0 with carry 1).

### Q4. [ict_ch1_tb_mcq4] | Octal System
* **Source**: `textbook_exercise` | **Type**: `mcq` | **Difficulty**: `easy` | **Marks**: 1M
* **Question**: Which of the following digits cannot be part of an Octal number?
* **Options**:
  - (a) 0
  - (b) 5
  - (c) 7
  - (d) 8
* **Answer**: (d) 8
* **Explanation**: Octal (base 8) uses only digits from 0 to 7. The digit 8 is not a valid octal digit.

### Q5. [ict_ch1_tb_fib1] | Binary System
* **Source**: `textbook_exercise` | **Type**: `fib` | **Difficulty**: `easy` | **Marks**: 1M
* **Question**: The binary number system consists of only two digits: ________ and ________.
* **Answer**: 0, 1
* **Explanation**: Binary is base 2 and operates exclusively using the bits 0 and 1.

### Q6. [ict_ch1_tb_fib2] | Decimal System
* **Source**: `textbook_exercise` | **Type**: `fib` | **Difficulty**: `easy` | **Marks**: 1M
* **Question**: The base of the Decimal number system is ________.
* **Answer**: 10
* **Explanation**: Decimal system uses ten symbols (0 through 9), so its base/radix is 10.

### Q7. [ict_ch1_tb_tf1] | Hexadecimal Base
* **Source**: `textbook_exercise` | **Type**: `tf` | **Difficulty**: `easy` | **Marks**: 1M
* **Question**: The Hexadecimal number system has 16 digits/symbols.
* **Answer**: True
* **Explanation**: True. Hexadecimal uses digits 0–9 and letters A–F, totaling 16 symbols.

### Q8. [ict_ch1_tb_tf2] | Binary Subtraction
* **Source**: `textbook_exercise` | **Type**: `tf` | **Difficulty**: `easy` | **Marks**: 1M
* **Question**: In binary subtraction, 1 - 0 = 0.
* **Answer**: False
* **Explanation**: False. 1 - 0 = 1 in binary subtraction.

### Q9. [ict_ch1_tb_short1] | Positional System
* **Source**: `textbook_exercise` | **Type**: `short_answer` | **Difficulty**: `medium` | **Marks**: 2M
* **Question**: State the three factors that determine the value of each digit in a positional number system.
* **Answer**: 1. The digit itself (face value)
2. The base or radix of the number system
3. The position of the digit within the number (place value as powers of base).
* **Explanation**: Formula: Value = Digit × Base^(Position).

### Q10. [ict_ch1_tb_conv1] | Decimal to Binary Conversion
* **Source**: `textbook_exercise` | **Type**: `conversion` | **Difficulty**: `medium` | **Marks**: 2M
* **Question**: Convert the decimal number (45)₁₀ into its binary equivalent.
* **Answer**: (101101)₂
* **Explanation**: 45 ÷ 2 = 22 R 1
22 ÷ 2 = 11 R 0
11 ÷ 2 = 5 R 1
5 ÷ 2 = 2 R 1
2 ÷ 2 = 1 R 0
1 ÷ 2 = 0 R 1
Reading remainders from bottom to top gives: 101101₂.

### Q11. [ict_ch1_tb_conv2] | Binary to Decimal Conversion
* **Source**: `textbook_exercise` | **Type**: `conversion` | **Difficulty**: `medium` | **Marks**: 2M
* **Question**: Convert the binary number (11010)₂ into its decimal equivalent.
* **Answer**: (26)₁₀
* **Explanation**: 1×2⁴ + 1×2³ + 0×2² + 1×2¹ + 0×2⁰ = 16 + 8 + 0 + 2 + 0 = 26₁₀.

### Q12. [ict_ch1_tb_add1] | Binary Addition
* **Source**: `textbook_exercise` | **Type**: `conversion` | **Difficulty**: `medium` | **Marks**: 2M
* **Question**: Add the binary numbers: (1011)₂ + (1101)₂.
* **Answer**: (11000)₂
* **Explanation**: Col 0: 1+1=0 (carry 1)
Col 1: 1+0+1=0 (carry 1)
Col 2: 0+1+1=0 (carry 1)
Col 3: 1+1+1=11 (write 1, carry 1)
Result: 11000₂. (Decimal check: 11 + 13 = 24).

### Q13. [ict_ch1_tb_sub1] | Binary Subtraction with Borrow
* **Source**: `textbook_exercise` | **Type**: `conversion` | **Difficulty**: `hard_hots` | **Marks**: 3M
* **Question**: Perform binary subtraction: (1100)₂ - (1001)₂.
* **Answer**: (0011)₂ or (11)₂
* **Explanation**: Col 0: 0 - 1 needs borrow. Borrows from Col 2 across Col 1. Becomes 2 - 1 = 1.
Col 1: 1 - 0 = 1.
Col 2: 0 - 0 = 0.
Col 3: 1 - 1 = 0.
Result: 0011₂ = 3₁₀. (Decimal check: 12 - 9 = 3).

### Q14. [ict_ch1_notes_short1] | Non-Positional vs Positional
* **Source**: `chapter_notes` | **Type**: `short_answer` | **Difficulty**: `medium` | **Marks**: 3M
* **Question**: Differentiate between non-positional and positional number systems with examples.
* **Answer**: In non-positional systems (e.g. Roman numerals, tally marks), each symbol represents a fixed value regardless of its place, and there is no symbol for zero. In positional systems (e.g. Decimal, Binary), the value of each symbol depends on its position and powers of the base, allowing complex arithmetic.
* **Explanation**: Positional systems enable place-value arithmetic, which revolutionized science and commerce.

### Q15. [ict_ch1_notes_mcq1] | Radix Applications
* **Source**: `chapter_notes` | **Type**: `mcq` | **Difficulty**: `medium` | **Marks**: 1M
* **Question**: Why do computers use the Binary number system internally instead of the Decimal system?
* **Options**:
  - (a) Binary numbers are easier for humans to read
  - (b) Computer electronic circuits operate via two discrete voltage states (ON/OFF)
  - (c) Binary system has 10 digits
  - (d) Decimal numbers cannot be converted
* **Answer**: (b) Computer electronic circuits operate via two discrete voltage states (ON/OFF)
* **Explanation**: Transistors inside microprocessors act as high/low voltage switches, making binary (0/1) the natural, reliable physical representation.

### Q16. [ict_ch1_trap_mcq] | Hexadecimal Alpha Representation
* **Source**: `exam_trap` | **Type**: `mcq` | **Difficulty**: `hard_hots` | **Marks**: 1M
* **Question**: What is the decimal equivalent of the Hexadecimal number (1A)₁₆?
* **Options**:
  - (a) 110
  - (b) 26
  - (c) 16
  - (d) 32
* **Answer**: (b) 26
* **Explanation**: Trap: '1A' is NOT '1 followed by 10' = 110! Calculation: (1 × 16¹) + (A × 16⁰) = 16 + 10 = 26₁₀.

### Q17. [ict_ch1_enrich_mcq1] | Data Units
* **Source**: `researched_enrichment` | **Type**: `mcq` | **Difficulty**: `easy` | **Marks**: 1M
* **Question**: A collection of 4 binary bits is technically known as a ________.
* **Options**:
  - (a) Byte
  - (b) Nibble
  - (c) Word
  - (d) Pixel
* **Answer**: (b) Nibble
* **Explanation**: 1 Bit = single 0 or 1; 1 Nibble = 4 bits (e.g., 1010); 1 Byte = 8 bits (2 nibbles); 1 Word = 16/32/64 bits.

### Q18. [ict_ch1_enrich_short1] | Real-World Hex Codes
* **Source**: `researched_enrichment` | **Type**: `short_answer` | **Difficulty**: `medium` | **Marks**: 2M
* **Question**: Where is the Hexadecimal number system commonly used in real-world computer technology?
* **Answer**: 1. Web Color Codes: HTML/CSS 6-digit hex codes (e.g., #FFFFFF for white, #000000 for black, #FF0000 for red).
2. Hardware MAC Addresses & Memory Dumps: Displaying large binary addresses compactly (each hex digit represents exactly 4 binary bits).
* **Explanation**: Hexadecimal compresses long binary strings (e.g. 11111111 becomes just FF).
