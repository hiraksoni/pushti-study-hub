# CHAPTER KNOWLEDGE BASE: LISTS AND IMAGES IN HTML
**Subject**: ICT | **Chapter**: 5 | **Standard**: Class 7 CBSE

## 1. Executive Summary
Covers semantic list creation in HTML (Unordered, Ordered, Definition Lists, Nested Lists), list attributes (type, start, reversed), CSS list styling, inserting images (<img> tag, attributes: src, alt, width, height, common formats), and the scrolling marquee effect (<marquee> tag and attributes).

## 2. Core Conceptual Theory & Notes
### [chapter_notes] Significance of Lists in HTML
Lists structure related information into readable, organized formats. All list items are encapsulated within the <li> (List Item) container tag inside a parent list tag.

### [chapter_notes] Three Types of Lists
1. Unordered List (<ul>): Bulleted list without numerical order. Default bullet is 'disc'. Other valid types: 'circle', 'square' (Note: 'rectangle' is NOT a valid bullet type). 2. Ordered List (<ol>): Numbered sequential list. Default type is Arabic numerals '1'. Other types: 'A', 'a', 'I', 'i'. Attributes include start (starting number) and reversed (counts downward). 3. Definition List (<dl>): Formats terms and explanations using <dt> (Definition Term) and <dd> (Definition Data/Description). Nested lists occur when one list is placed inside another list item.

### [chapter_notes] CSS List Properties
CSS replaces HTML list attributes with properties: list-style-type (sets bullet/numbering marker), list-style-image (replaces bullets with custom icons), list-style-position (inside or outside the text block).

### [chapter_notes] Inserting Images (<img> Tag)
Images enhance visual presentation. The <img> tag is an empty tag. Key attributes: src (source file path/URL), alt (alternative descriptive text shown if image fails to load or for screen readers), width and height (dimensions in pixels or percentage). Supported formats include .jpg (photos), .gif (animated/simple graphics), and .png (transparent backgrounds).

### [chapter_notes] The Marquee Tag
<marquee> creates scrolling text or images across the screen. Key attributes: direction (left, right, up, down; default is left), behavior (scroll, slide, alternate), scrollamount (speed of movement), bgcolor (background color of ticker strip).

### [researched_enrichment] Modern Web Evolution: Semantic Menus & Marquee Obsolescence
In professional modern web development: 1. Navigation bars (navbars) on Google, YouTube, and Amazon are built using semantic <ul> and <li> tags, stripped of bullets and arranged horizontally with CSS Flexbox. 2. The <marquee> tag was deprecated in HTML5 because it causes accessibility problems for readers; smooth animations are now created with CSS keyframe animations.

## 3. Tagged Question & Assessment Bank
### Q1. [ict_ch5_tb_mcq1] | Unordered List Default Bullet
* **Source**: `textbook_exercise` | **Type**: `mcq` | **Difficulty**: `easy` | **Marks**: 1M
* **Question**: Which is the default bullet style in an unordered list (<ul>) in HTML?
* **Options**:
  - (a) Circle
  - (b) Square
  - (c) Disc
  - (d) Rectangle
* **Answer**: (c) Disc
* **Explanation**: In HTML, the default bullet style for an unordered list is 'Disc' (a filled black circle). Other valid styles are 'Circle' and 'Square'.

### Q2. [ict_ch5_tb_mcq2] | List Tags
* **Source**: `textbook_exercise` | **Type**: `mcq` | **Difficulty**: `easy` | **Marks**: 1M
* **Question**: Which tag is used to create an Ordered (numbered) list in HTML?
* **Options**:
  - (a) <UL>
  - (b) <OL>
  - (c) <DL>
  - (d) <LI>
* **Answer**: (b) <OL>
* **Explanation**: <OL> creates an Ordered List, <UL> creates an Unordered List, and <DL> creates a Definition List.

### Q3. [ict_ch5_tb_mcq3] | Invalid List Attributes
* **Source**: `textbook_exercise` | **Type**: `mcq` | **Difficulty**: `easy` | **Marks**: 1M
* **Question**: Which of the following CANNOT be a valid value for the TYPE attribute in a <UL> tag?
* **Options**:
  - (a) Square
  - (b) Circle
  - (c) Disc
  - (d) Rectangle
* **Answer**: (d) Rectangle
* **Explanation**: Valid bullet values for <UL> are disc, circle, and square. 'Rectangle' is not supported in HTML.

### Q4. [ict_ch5_tb_mcq4] | Image Tag Attributes
* **Source**: `textbook_exercise` | **Type**: `mcq` | **Difficulty**: `easy` | **Marks**: 1M
* **Question**: Which attribute of the <IMG> tag is used to specify alternate text if the image fails to load?
* **Options**:
  - (a) SRC
  - (b) ALT
  - (c) TITLE
  - (d) NAME
* **Answer**: (b) ALT
* **Explanation**: The ALT (Alternate text) attribute displays descriptive text if the image file cannot be found or loaded, and helps screen reader accessibility.

### Q5. [ict_ch5_tb_mcq5] | Ordered List Attributes
* **Source**: `textbook_exercise` | **Type**: `mcq` | **Difficulty**: `medium` | **Marks**: 1M
* **Question**: Which attribute allows an ordered list to count in reverse order (e.g. 5, 4, 3, 2, 1)?
* **Options**:
  - (a) BACKWARD
  - (b) DOWN
  - (c) REVERSED
  - (d) INVERSE
* **Answer**: (c) REVERSED
* **Explanation**: The 'reversed' attribute in <ol reversed> instructs the browser to number list items in descending/reverse order.

### Q6. [ict_ch5_tb_tf1] | Image Tag Nature
* **Source**: `textbook_exercise` | **Type**: `true_false` | **Difficulty**: `easy` | **Marks**: 1M
* **Question**: True or False: The <IMG> tag is a container tag that requires a closing </IMG> tag.
* **Options**:
  - (a) True
  - (b) False
* **Answer**: (b) False
* **Explanation**: The <IMG> tag is an empty (void) tag. It takes attributes like src and alt but has no closing tag.

### Q7. [ict_ch5_tb_tf2] | Ordered List Default Type
* **Source**: `textbook_exercise` | **Type**: `true_false` | **Difficulty**: `easy` | **Marks**: 1M
* **Question**: True or False: By default, an Ordered List numbers items using Arabic numbers (1, 2, 3...).
* **Options**:
  - (a) True
  - (b) False
* **Answer**: (a) True
* **Explanation**: If no TYPE attribute is specified in <ol>, the browser defaults to Arabic numerals starting at 1.

### Q8. [ict_ch5_tb_fib1] | List Items
* **Source**: `textbook_exercise` | **Type**: `fib` | **Difficulty**: `easy` | **Marks**: 1M
* **Question**: Individual items inside both ordered and unordered lists are marked using the ________ tag.
* **Answer**: <li> or <LI>
* **Explanation**: <li> stands for List Item and encloses every entry in ordered and unordered lists.

### Q9. [ict_ch5_tb_fib2] | Marquee Default Direction
* **Source**: `textbook_exercise` | **Type**: `fib` | **Difficulty**: `medium` | **Marks**: 1M
* **Question**: By default, text inside a <marquee> tag scrolls towards the ________.
* **Answer**: Left
* **Explanation**: The default scrolling direction of a <marquee> is from right to left (direction='left').

### Q10. [ict_ch5_tb_sa1] | Definition List Tags
* **Source**: `textbook_exercise` | **Type**: `short_answer` | **Difficulty**: `medium` | **Marks**: 2M
* **Question**: Name the three tags used to build a Definition List in HTML and state their roles.
* **Answer**: 1. <DL>: Defines the start and end of the Definition List. 2. <DT>: Defines the Definition Term. 3. <DD>: Defines the Data/Definition Description of that term.
* **Explanation**: Full 2 marks: 1M for listing <dl>, <dt>, and <dd>, 1M for accurate explanation of their individual functions.

### Q11. [ict_ch5_tb_sa2] | Ordered List Attributes
* **Source**: `textbook_exercise` | **Type**: `short_answer` | **Difficulty**: `medium` | **Marks**: 2M
* **Question**: Write the HTML code to create an ordered list of 3 subjects that starts numbering from the Roman numeral V (5).
* **Answer**: <ol type="I" start="5">
  <li>English</li>
  <li>Science</li>
  <li>Mathematics</li>
</ol>
* **Explanation**: Full 2 marks: 1M for type='I' and start='5' (start always takes integer 5, not 'V'), 1M for valid <li> entries.

### Q12. [ict_ch5_tb_sa3] | Image Tag Attributes
* **Source**: `textbook_exercise` | **Type**: `short_answer` | **Difficulty**: `medium` | **Marks**: 2M
* **Question**: Explain the significance of the SRC and ALT attributes of the <IMG> tag.
* **Answer**: 'SRC' specifies the source address/path of the image file so the browser knows where to load it from. 'ALT' provides alternate text displayed if the image fails to load and is read aloud by screen readers for accessibility.
* **Explanation**: Full 2 marks: 1M for SRC explanation, 1M for ALT explanation.

### Q13. [ict_ch5_tb_la1] | Marquee Attributes
* **Source**: `textbook_exercise` | **Type**: `long_answer` | **Difficulty**: `medium` | **Marks**: 3M
* **Question**: What is a marquee? Explain any three attributes supported by the <marquee> tag.
* **Answer**: A marquee is a scrolling piece of text or image that moves horizontally or vertically across a webpage. Three attributes: 1. direction: Specifies the movement direction (left, right, up, down). 2. behavior: Controls movement style (scroll = continuous wrap, slide = scrolls once and stops, alternate = bounces back and forth). 3. scrollamount: Sets the speed of scrolling in pixels per tick.
* **Explanation**: Full 3 marks: 1M for marquee definition, 2M for accurately defining 3 attributes with valid options.

### Q14. [ict_ch5_hots1] | Semantic Web & Navigation Menus
* **Source**: `researched_enrichment` | **Type**: `hots` | **Difficulty**: `hard_hots` | **Marks**: 3M
* **Question**: Why do professional web developers use unordered lists (<ul> and <li>) to build website navigation menus instead of simply using separate paragraph tags (<p>)?
* **Answer**: 1. Semantic Structure: Search engines (Google) and screen readers recognize a <ul> as a structured group of navigation links. 2. Accessibility: Assistive screen readers announce the number of menu items in advance (e.g. 'List of 5 items'), helping visually impaired users. 3. Clean CSS Styling: CSS can easily target the list items with flexbox or inline-block to create responsive horizontal headers and dropdown menus.
* **Explanation**: Full 3 marks: 1M for semantic structure, 1M for accessibility/screen readers, 1M for CSS styling efficiency.

### Q15. [ict_ch5_trap1] | Ordered List Start Trap
* **Source**: `exam_trap` | **Type**: `short_answer` | **Difficulty**: `medium` | **Marks**: 2M
* **Question**: A student wrote <ol type="A" start="C"> to begin a list at letter C. Why does this result in an error or unexpected behavior in HTML?
* **Answer**: In HTML, the 'start' attribute MUST always be specified as an integer number, regardless of the list 'type'. To start from 'C', the student must write <ol type="A" start="3">. The browser automatically translates integer 3 to 'C'.
* **Explanation**: Full 2 marks: 1M for identifying that 'start' must be numeric, 1M for providing the corrected code <ol type='A' start='3'>.
