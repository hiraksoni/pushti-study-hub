# CHAPTER KNOWLEDGE BASE: WORKING WITH HTML TAGS AND CSS
**Subject**: ICT | **Chapter**: 4 | **Standard**: Class 7 CBSE

## 1. Executive Summary
Covers HTML document structure, body tag attributes (bgcolor, text, background, link, alink, vlink), text formatting tags (paragraph, break, font, sub, sup), HTML comments, CSS definition and syntax, 3 ways of linking CSS (inline, internal, external), and foundational CSS properties.

## 2. Core Conceptual Theory & Notes
### [chapter_notes] Body Tag Attributes
The <body> tag defines the main visible canvas of a webpage. Key attributes include: bgcolor (page background color), text (default font color for all body text), background (image file path for background wallpaper), link (unvisited hyperlink color, default blue), alink (active link color during click, default red), and vlink (visited link color, default purple).

### [chapter_notes] Text Formatting Tags & Container vs Empty
Container tags have both opening and closing tags (e.g. <p>...</p>, <u>...</u>, <font>...</font>). Empty tags (void elements) do not require a closing tag (e.g. <br> for line break, <hr> for horizontal rule). <p> supports the align attribute (left, right, center, justify). The <font> tag supports face (font family), size (1 to 7), and color. <sub> creates subscript (e.g. H2O) and <sup> creates superscript (e.g. X2).

### [chapter_notes] HTML Comments
Comments are developer annotations ignored by the web browser rendering engine. Standard HTML comments use the syntax <!-- comment text -->. The older, obsolete <comment> tag is deprecated and should not be used in modern HTML.

### [chapter_notes] CSS Definition, Syntax & Linking
Cascading Style Sheets (CSS) format webpage presentation and layout. Syntax consists of a Selector and a Declaration Block: selector { property: value; }. CSS can be integrated in 3 ways: 1. Inline (style attribute inside HTML tag; inefficient for repeated elements). 2. Internal (<style> tag in <head>; styles entire single page). 3. External (.css file linked via <link>; maintains consistent styling across multiple web pages).

### [chapter_notes] CSS Styling Properties
Core CSS properties: color (text color), background-color (element background), font-family (typeface name), font-size (text height in px or pt), text-align (left, right, center, justify).

### [researched_enrichment] Real-World Web Standards & Separation of Concerns
Modern web development follows the principle of 'Separation of Concerns': HTML provides the semantic structure, CSS governs visual presentation, and JavaScript handles dynamic interactivity. Deprecated HTML formatting tags like <font> and body attributes like bgcolor are now replaced by clean CSS rules (e.g., body { background-color: #f8fafc; color: #1e293b; }).

## 3. Tagged Question & Assessment Bank
### Q1. [ict_ch4_tb_mcq1] | Line Break Tag
* **Source**: `textbook_exercise` | **Type**: `mcq` | **Difficulty**: `easy` | **Marks**: 1M
* **Question**: In HTML, the <br> tag is used to ________.
* **Options**:
  - (a) Insert a line break
  - (b) Insert a symbol
  - (c) Insert a paragraph
  - (d) Insert a bold word
* **Answer**: (a) Insert a line break
* **Explanation**: The <br> (break) tag is an empty tag used to end the current line and jump to the next line without leaving blank space between lines like a paragraph tag does.

### Q2. [ict_ch4_tb_mcq2] | HTML Comments
* **Source**: `textbook_exercise` | **Type**: `mcq` | **Difficulty**: `easy` | **Marks**: 1M
* **Question**: Which of the following is the standard syntax to insert a comment in an HTML document?
* **Options**:
  - (a) <comment> This is a comment </comment>
  - (b) <!-- This is a comment -->
  - (c) // This is a comment
  - (d) /* This is a comment */
* **Answer**: (b) <!-- This is a comment -->
* **Explanation**: Standard HTML comments begin with '<!--' and end with '-->'. They are ignored by the web browser and assist developers in reading code.

### Q3. [ict_ch4_tb_mcq3] | Body Tag Attributes
* **Source**: `textbook_exercise` | **Type**: `mcq` | **Difficulty**: `easy` | **Marks**: 1M
* **Question**: Which attribute of the <body> tag is used to set the background color of a web page?
* **Options**:
  - (a) COLOR
  - (b) BGCOLOR
  - (c) BACKGROUND
  - (d) TEXT
* **Answer**: (b) BGCOLOR
* **Explanation**: BGCOLOR sets the solid background color of the web page. The BACKGROUND attribute is used when setting an image file as wallpaper.

### Q4. [ict_ch4_tb_mcq4] | Body Text Attribute
* **Source**: `textbook_exercise` | **Type**: `mcq` | **Difficulty**: `easy` | **Marks**: 1M
* **Question**: Which attribute of the <body> tag is used to define the default color of all text on a web page?
* **Options**:
  - (a) COLOR
  - (b) FONTCOLOR
  - (c) TEXT
  - (d) TEXTCOLOR
* **Answer**: (c) TEXT
* **Explanation**: The TEXT attribute of the <body> tag specifies the global text color for the entire page (e.g. <body text='navy'>).

### Q5. [ict_ch4_tb_mcq5] | Hyperlink Colors
* **Source**: `textbook_exercise` | **Type**: `mcq` | **Difficulty**: `medium` | **Marks**: 1M
* **Question**: What is the default color of an Active Link (ALINK) in HTML when clicked?
* **Options**:
  - (a) Blue
  - (b) Red
  - (c) Purple
  - (d) Green
* **Answer**: (b) Red
* **Explanation**: By default in HTML: unvisited link (LINK) is Blue, active link during click (ALINK) is Red, and visited link (VLINK) is Purple.

### Q6. [ict_ch4_tb_tf1] | HTML Attributes
* **Source**: `textbook_exercise` | **Type**: `true_false` | **Difficulty**: `easy` | **Marks**: 1M
* **Question**: True or False: An attribute is used inside an HTML tag to define additional characteristics or properties of that element.
* **Options**:
  - (a) True
  - (b) False
* **Answer**: (a) True
* **Explanation**: Attributes provide extra configuration options inside the opening tag (e.g. align='center', bgcolor='yellow').

### Q7. [ict_ch4_tb_tf2] | Container Tags
* **Source**: `textbook_exercise` | **Type**: `true_false` | **Difficulty**: `medium` | **Marks**: 1M
* **Question**: True or False: The <U> tag is an empty tag because it does not require closing.
* **Options**:
  - (a) True
  - (b) False
* **Answer**: (b) False
* **Explanation**: The <U> (underline) tag is a container tag that requires both opening <U> and closing </U> tags around the underlined text.

### Q8. [ict_ch4_trap_tf1] | CSS Acronym Trap
* **Source**: `exam_trap` | **Type**: `true_false` | **Difficulty**: `medium` | **Marks**: 1M
* **Question**: True or False: CSS stands for 'Collective Style Sheets'.
* **Options**:
  - (a) True
  - (b) False
* **Answer**: (b) False
* **Explanation**: CSS stands for 'Cascading Style Sheets'. The term 'Cascading' signifies that styles can trickle down or override based on priority.

### Q9. [ict_ch4_tb_fib1] | Superscript & Subscript
* **Source**: `textbook_exercise` | **Type**: `fib` | **Difficulty**: `easy` | **Marks**: 1M
* **Question**: To write the chemical formula of Water as H₂O in HTML, the number '2' must be enclosed inside the ________ tag.
* **Answer**: <sub> or <SUB>
* **Explanation**: <sub> stands for subscript, which places text slightly below the baseline (e.g., H<sub>2</sub>O).

### Q10. [ict_ch4_tb_fib2] | Mathematical Powers
* **Source**: `textbook_exercise` | **Type**: `fib` | **Difficulty**: `easy` | **Marks**: 1M
* **Question**: To write mathematical expressions like X², the power '2' is placed inside the ________ tag.
* **Answer**: <sup> or <SUP>
* **Explanation**: <sup> stands for superscript, which places text slightly above the baseline (e.g., X<sup>2</sup>).

### Q11. [ict_ch4_tb_sa1] | Container vs Empty Tags
* **Source**: `textbook_exercise` | **Type**: `short_answer` | **Difficulty**: `medium` | **Marks**: 2M
* **Question**: Distinguish between Container Tags and Empty Tags in HTML with one example of each.
* **Answer**: Container tags require both an opening and a closing tag and enclose content between them (e.g., <p>...</p>, <b>...</b>). Empty tags (void elements) do not contain text and have no closing tag (e.g., <br>, <hr>).
* **Explanation**: Full 2 marks: 1M for defining both tag categories clearly, 1M for providing accurate syntax examples.

### Q12. [ict_ch4_tb_sa2] | CSS Syntax
* **Source**: `textbook_exercise` | **Type**: `short_answer` | **Difficulty**: `medium` | **Marks**: 2M
* **Question**: Explain the general syntax of a CSS rule with an illustrative example.
* **Answer**: A CSS rule consists of a Selector and a Declaration Block: selector { property: value; }. For example: h1 { color: red; font-size: 24px; } where 'h1' is the selector, 'color' is the property, and 'red' is the value.
* **Explanation**: Full 2 marks: 1M for identifying Selector and Declaration block enclosed in curly braces, 1M for valid code example.

### Q13. [ict_ch4_notes_sa1] | Inline vs Internal CSS
* **Source**: `chapter_notes` | **Type**: `short_answer` | **Difficulty**: `medium` | **Marks**: 2M
* **Question**: State the primary difference between Inline CSS and Internal CSS.
* **Answer**: Inline CSS is applied directly inside a specific HTML tag using the 'style' attribute and affects only that single element. Internal CSS is written inside the <style> tag in the <head> section and applies to all matching elements across that entire webpage.
* **Explanation**: Full 2 marks: 1M for inline explanation with style attribute, 1M for internal explanation with <style> in <head>.

### Q14. [ict_ch4_tb_la1] | Three Types of CSS
* **Source**: `textbook_exercise` | **Type**: `long_answer` | **Difficulty**: `medium` | **Marks**: 3M
* **Question**: Explain the three ways of linking CSS to an HTML document. Which one is best for styling a multi-page website?
* **Answer**: 1. Inline Style Sheet: Specified inside an HTML tag using the style attribute. Only affects that element. 2. Internal Style Sheet: Declared within <style> tags in the <head> section. Styles all elements on a single page. 3. External Style Sheet: Written in a separate file with a .css extension and linked using the <link> tag. Best Method for Websites: External CSS is the best because one single .css file controls the visual appearance of multiple web pages, saving time and ensuring consistency.
* **Explanation**: Full 3 marks: 0.5M for each of the 3 CSS types defined, 1M for naming External CSS as best for multi-page sites with valid justification.

### Q15. [ict_ch4_hots1] | CSS Separation of Concerns & Debugging
* **Source**: `researched_enrichment` | **Type**: `hots` | **Difficulty**: `hard_hots` | **Marks**: 3M
* **Question**: A student wrote <body bgcolor='cyan' text='navy'> in HTML, and also linked an internal CSS rule: body { background-color: yellow; color: darkred; }. Which background color will the browser display, and why?
* **Answer**: The browser will display a Yellow background with Dark Red text. Explanation: Modern browsers give higher cascading precedence to CSS style rules over legacy deprecated HTML presentation attributes like 'bgcolor' and 'text'. The CSS declaration overrides the inline HTML tag attributes.
* **Explanation**: Full 3 marks: 1M for identifying Yellow/Dark Red, 2M for explaining the cascading priority of CSS over obsolete HTML attributes.

### Q16. [ict_ch4_enrich_sa1] | Web Color Codes
* **Source**: `researched_enrichment` | **Type**: `short_answer` | **Difficulty**: `hard_hots` | **Marks**: 2M
* **Question**: How are colors specified in CSS beyond simple color names? Write the CSS declaration to set a page background to pure white using Hexadecimal notation.
* **Answer**: Colors in CSS can be specified using Hexadecimal RGB color codes (#RRGGBB) or RGB functions rgb(r, g, b). CSS declaration: body { background-color: #FFFFFF; }
* **Explanation**: Full 2 marks: 1M for hex/rgb explanation, 1M for correct #FFFFFF syntax.
