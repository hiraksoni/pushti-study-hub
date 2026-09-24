# CHAPTER KNOWLEDGE BASE: WORKING WITH HTML TAGS AND CSS
**Subject**: ICT | **Chapter**: 4 | **Standard**: Class 7 CBSE
**Textbook Reference Scans**: `IMG20260830222120.jpg` to `IMG20260830222213.jpg` (pp. 55–72)

## 1. Executive Summary & Learning Outcomes
This chapter establishes the core architectural foundations of web page design using HTML tags and Cascading Style Sheets (CSS). It covers:
- HTML structural elements and the `<body>` tag canvas with its complete attribute suite (`BGCOLOR`, `BACKGROUND`, `TEXT`, `LEFTMARGIN`, `TOPMARGIN`, `LINK`, `ALINK`, `VLINK`).
- Text and character formatting tags: `<P>` (with `ALIGN`), `<BR>`, `<CENTER>`, `<B>`, `<I>`, `<U>`, and mathematical/chemical formatting via `<SUB>` and `<SUP>`.
- Implementation of developer annotations and comments (`<!-- ... -->` and legacy `<COMMENT>`).
- Historical origin and architectural purpose of CSS (Håkon Wium Lie 1994, W3C 1996).
- The 4 major advantages of CSS (Saves Time, Easy Maintenance, Fast Webpage Loading, Superior/Printer-Friendly Styles).
- CSS Rule Anatomy (Selector and Declaration Block with Property and Value).
- The 3 methods of linking CSS with HTML: Inline, Internal (Embedded), and External.
- Core CSS Properties: Background properties (`background-color`, `background-image`, `background-position`, `background-repeat`) and Typography properties (`font-family`, `font-style`, `font-variant`, `font-weight`, `font-size`, `font` shorthand).
- Evolution of web standards: HTML5 deprecation of styling elements, Separation of Concerns, and the CSS Cascade hierarchy.

## 2. Core Conceptual Theory & Detailed Textbook Notes

### [textbook_theory] HTML Document Structure & Canvas (<BODY> Tag) (pp. 55-57)
The <body> tag defines the main visible document body and canvas of an HTML webpage. It is a container tag (requires <body> and </body>). It supports key styling and positioning attributes: 1. BGCOLOR: Sets the background color of the web page (e.g., <body bgcolor='yellow'> or hex '#FF0000'). 2. BACKGROUND: Specifies the path to an image file displayed as background wallpaper (e.g., <body background='flower.jpg'>). 3. TEXT: Sets the default foreground text color for the entire page (e.g., <body text='blue'>; default is black). 4. LEFTMARGIN: Specifies the left margin width in pixels from the browser border (e.g., <body leftmargin='50'>). 5. TOPMARGIN: Specifies the top margin height in pixels from the top browser edge (e.g., <body topmargin='40'>). 6. LINK: Sets the display color of unvisited hyperlinks (default is Blue). 7. ALINK: Sets the display color of active hyperlinks during the click action (default is Red). 8. VLINK: Sets the display color of visited hyperlinks already clicked in history (default is Purple/Violet).

### [textbook_theory] Text Structure & Paragraph Formatting Tags (pp. 58-59)
HTML provides structural tags to format text blocks: 1. <P> Tag: Container tag (<p>...</p>) used to define a paragraph. The browser automatically adds an empty line before and after the paragraph. It supports the ALIGN attribute with 4 values: LEFT (default), CENTER, RIGHT, and JUSTIFY (aligns text to both left and right margins). 2. <BR> Tag: Empty/unpaired tag (<br>) used to force a single line break without inserting an empty line. It has no closing tag and no attributes. 3. <CENTER> Tag: Container tag (<center>...</center>) that centers all enclosed text, images, or elements horizontally across the page.

### [textbook_theory] HTML Comments (p. 59)
Comments are non-executable explanatory notes written in the source code to help programmers understand code logic. Comments are completely ignored by the web browser rendering engine and do not appear on the rendered page. Two syntaxes exist in HTML: 1. Standard HTML Comment: <!-- comment text here --> (starts with '<!--' and ends with '-->'). 2. Deprecated <COMMENT> Tag: An older container tag (<comment>...</comment>) from legacy HTML, now obsolete in HTML5.

### [textbook_theory] Character & Font Formatting Tags (pp. 59-61)
Tags for physical character styling: 1. <FONT> Tag: Container tag used to format font appearance. Supports 3 attributes: FACE (specifies typeface/font family, e.g., face='Arial, Courier New'), COLOR (specifies font color by name or hex, e.g., color='red'), and SIZE (sets font size from 1 to 7, default is 3). 2. Physical Style Tags: <B>...</B> (renders text in Bold), <I>...</I> (renders text in Italic), <U>...</U> (renders text with an Underline). 3. Mathematical & Chemical Formatting: <SUB>...</SUB> (Subscript tag: displays text slightly below the baseline in smaller size, used for chemical formulas like H<sub>2</sub>SO<sub>4</sub>) and <SUP>...</SUP> (Superscript tag: displays text slightly above the baseline in smaller size, used for mathematical powers like (a+b)<sup>2</sup>).

### [textbook_theory] Introduction to Cascading Style Sheets (CSS) (pp. 60-61)
Cascading Style Sheets (CSS) is a style sheet language used to format the layout and visual presentation of an HTML document. History: CSS was first proposed by Håkon Wium Lie on October 10, 1994, while working with Tim Berners-Lee at CERN/W3C. In December 1996, the World Wide Web Consortium (W3C) published the CSS1 Recommendation. CSS is actively developed and maintained by the W3C CSS Working Group. Core Concept: CSS separates presentation (fonts, colors, spacing, layouts) from HTML content structure.

### [textbook_theory] Advantages of Using CSS (pp. 61-62)
The textbook highlights four major advantages of CSS: 1. Saves Time: Write CSS once and reuse the same style rules across multiple elements or multiple web pages. 2. Easy Maintenance: Separation of content and presentation enables global design changes by editing a single style sheet, updating all linked web pages automatically. 3. Fast Webpage Loading: External CSS files are downloaded once by the browser and cached locally, reducing network bandwidth, page size, and server requests. 4. Superior Styles & Printer-Friendly: Offers vastly richer typography and visual properties than plain HTML, and allows specifying different stylesheets for screen and print media.

### [textbook_theory] CSS Rule Syntax & Anatomy (pp. 62-63)
A CSS rule consists of two main components: 1. Selector: Indicates which HTML element(s) to style (e.g., 'h1', 'p', 'body', 'table'). 2. Declaration Block: Enclosed in curly braces '{ }', containing one or more declarations separated by semicolons ';'. Each declaration consists of a Property (style attribute, e.g., 'color') and a Value separated by a colon ':'. Syntax: selector { property: value; property: value; }. Example: h1 { color: blue; font-size: 24px; text-align: center; }.

### [textbook_theory] Three Types of CSS (Linking CSS to HTML) (pp. 63-65)
HTML documents can incorporate CSS using three primary methods: 1. Inline Style Sheet: Applied directly to a single HTML element using the 'style' attribute (e.g., <h1 style='color:red; font-size:20px;'>). Scope: Only affects that specific element. Disadvantage: Highly inefficient because declarations must be repeated for every element, mixing content with presentation. 2. Internal / Embedded Style Sheet: Defined within the <style>...</style> container tag inside the <head> section of a webpage (e.g., <head><style> p { color: green; } </style></head>). Scope: Applies to all matching elements on that single page. Disadvantage: Styles cannot be shared across multiple HTML files. 3. External Style Sheet: Written in an independent plain text file saved with a '.css' extension (e.g., 'styles.css') containing only CSS rules (no HTML tags). Linked inside the HTML <head> using the empty <link> tag: <link rel='stylesheet' type='text/css' href='styles.css'>. Advantage: Best for websites because a single file standardizes design across hundreds of pages and enables instant site-wide redesigns.

### [textbook_theory] CSS Background Properties (pp. 65-66)
CSS provides dedicated properties for page and element backgrounds: 1. background-color: Sets the solid background color (e.g., body { background-color: lightblue; }). Supports color names, hexadecimal codes (#RRGGBB), RGB (rgb(r,g,b)), and RGBA with opacity (rgba(r,g,b,alpha) where alpha is 0.0 to 1.0). 2. background-image: Specifies a background image url (e.g., body { background-image: url('paper.gif'); }). 3. background-position: Defines the initial starting position of a background image. Accepts coordinates (x y in px), percentages (x% y%), or keywords (top left, center, bottom right; default is '0 0' or top-left). 4. background-repeat: Controls image tiling/repetition: 'repeat' (default tiles horizontally and vertically), 'repeat-x' (tiles horizontally only), 'repeat-y' (tiles vertically only), 'no-repeat' (displays image only once).

### [textbook_theory] CSS Typography & Font Properties (pp. 66-67)
Typography in CSS is controlled via font properties: 1. font-family: Changes typeface. Divided into 'Family Names' (specific fonts like Arial, Times New Roman, Courier New, Constantia) and 'Generic Families' (fallback font categories: Serif, Sans-serif, Monospace, Cursive, Fantasy). Crucial exam note: 'Constantia' is a specific family-name, NOT a generic family. 2. font-style: Sets font posture ('normal', 'italic', 'oblique'). 3. font-variant: Controls typographic casing ('normal' or 'small-caps' where lowercase letters appear as smaller capital letters). 4. font-weight: Controls boldness ('normal', 'bold', 'bolder', 'lighter', or numeric 100 to 900). 5. font-size: Sets font height using units (pixels 'px', points 'pt', percentages '%') or keywords ('small', 'medium', 'large'). 6. font (Shorthand): Combines all font properties into a single concise declaration (e.g., p { font: italic bold 16px Arial, sans-serif; }).

### [textbook_theory] Evolution of Web Standards, Deprecation & The CSS Cascade (p. 68)
Evolution: Early HTML (1990s) lacked styling capabilities, leading to presentational tags like <font>, <center>, and <body> styling attributes (bgcolor, text). HTML5 strictly deprecates these presentational elements in favor of CSS 'Separation of Concerns'. The Cascade: CSS rules follow a strict precedence hierarchy when multiple conflicting styles apply to the same element: 1. Inline Style (highest priority - overrides all other styles). 2. Internal Style Sheet (in <head>). 3. External Style Sheet. 4. Browser Default Styles (lowest priority). Styles 'cascade' down like water, with closer, more specific definitions taking precedence.

## 3. Tagged Question & Assessment Bank

### --- TEXTBOOK EXERCISE ---

#### Q. [ict_ch4_tb_mcq1] | CSS Acronym
* **Source**: `textbook_exercise` | **Type**: `mcq` | **Difficulty**: `easy` | **Marks**: 1M
* **Question**: CSS stands for ______________
* **Options**:
  - (a) Cascade style sheets
  - (b) Color and style sheets
  - (c) Cascading style sheets
  - (d) None of the above
* **Answer**: (c) Cascading style sheets
* **Explanation**: CSS stands for Cascading Style Sheets. It is used to format the layout and presentation of HTML webpages.

#### Q. [ict_ch4_tb_mcq2] | Embedding CSS Tag
* **Source**: `textbook_exercise` | **Type**: `mcq` | **Difficulty**: `easy` | **Marks**: 1M
* **Question**: In an HTML page, which of these tags is used for embedding CSS?
* **Options**:
  - (a) <!DOCTYPE html>
  - (b) <css>
  - (c) <style>
  - (d) <script>
* **Answer**: (c) <style>
* **Explanation**: Internal CSS is defined inside the <style>...</style> container tag, placed within the <head> section of an HTML document.

#### Q. [ict_ch4_tb_mcq3] | CSS Font Size Property
* **Source**: `textbook_exercise` | **Type**: `mcq` | **Difficulty**: `easy` | **Marks**: 1M
* **Question**: Which one of the following properties is used to define the size of the font in CSS?
* **Options**:
  - (a) Font-size
  - (b) Font-color
  - (c) Size
  - (d) None of these
* **Answer**: (a) Font-size
* **Explanation**: The 'font-size' property defines the text height in units like pixels (px), points (pt), or percentages (%).

#### Q. [ict_ch4_tb_mcq4] | CSS Font Face Property
* **Source**: `textbook_exercise` | **Type**: `mcq` | **Difficulty**: `easy` | **Marks**: 1M
* **Question**: Which of the following properties is used to change the font face of the text in CSS?
* **Options**:
  - (a) Font-size
  - (b) Font-color
  - (c) Font-face
  - (d) None of these
* **Answer**: (c) Font-face
* **Explanation**: In the textbook options, 'Font-face' is designated as the answer (in standard CSS, 'font-family' sets typeface, while @font-face embeds custom fonts).

#### Q. [ict_ch4_tb_mcq5] | Generic Font Families
* **Source**: `textbook_exercise` | **Type**: `mcq` | **Difficulty**: `medium` | **Marks**: 1M
* **Question**: Which one of the following is not a member of the generic font family?
* **Options**:
  - (a) Serif
  - (b) Sans-serif
  - (c) Constantia
  - (d) None of these
* **Answer**: (c) Constantia
* **Explanation**: Serif, Sans-serif, Monospace, Cursive, and Fantasy are generic font families. Constantia is a specific font family name, not a generic family.

#### Q. [ict_ch4_tb_fib1] | HTML Fundamental Elements
* **Source**: `textbook_exercise` | **Type**: `fib` | **Difficulty**: `easy` | **Marks**: 1M
* **Question**: Fill in the blanks: __________________ are the fundamental elements of an HTML document.
* **Answer**: Tags
* **Explanation**: Tags are the fundamental building blocks of an HTML document that tell web browsers how to format and display content.

#### Q. [ict_ch4_tb_fib2] | Background Image Attribute
* **Source**: `textbook_exercise` | **Type**: `fib` | **Difficulty**: `easy` | **Marks**: 1M
* **Question**: Fill in the blanks: __________________ attribute is used to insert an image in the background of a web page.
* **Answer**: background
* **Explanation**: The 'background' attribute of the <body> tag specifies the URL or file path of an image used as background wallpaper.

#### Q. [ict_ch4_tb_fib3] | Inline Style Sheet
* **Source**: `textbook_exercise` | **Type**: `fib` | **Difficulty**: `medium` | **Marks**: 1M
* **Question**: Fill in the blanks: __________________ is used to apply a unique style to a single HTML element.
* **Answer**: The inline style
* **Explanation**: An inline style uses the 'style' attribute directly inside an opening HTML tag to style only that single element.

#### Q. [ict_ch4_tb_fib4] | CSS Purpose
* **Source**: `textbook_exercise` | **Type**: `fib` | **Difficulty**: `easy` | **Marks**: 1M
* **Question**: Fill in the blanks: __________________ are used to format the layout of a webpage.
* **Answer**: Cascading Style Sheets (CSS)
* **Explanation**: Cascading Style Sheets (CSS) control the visual presentation, color scheme, typography, and page layout.

#### Q. [ict_ch4_tb_tf1] | CSS Background Image Property
* **Source**: `textbook_exercise` | **Type**: `true_false` | **Difficulty**: `easy` | **Marks**: 1M
* **Question**: Write 'T' for true or 'F' for false: To add a background image to the webpage, we can use the background-image property.
* **Options**:
  - (a) True
  - (b) False
* **Answer**: (a) True
* **Explanation**: True. In CSS, the 'background-image' property (e.g., body { background-image: url('image.jpg'); }) adds a background image.

#### Q. [ict_ch4_tb_tf2] | Internal Style Sheet Efficiency
* **Source**: `textbook_exercise` | **Type**: `true_false` | **Difficulty**: `medium` | **Marks**: 1M
* **Question**: Write 'T' for true or 'F' for false: The internal style sheet is not an efficient use of a style sheet.
* **Options**:
  - (a) True
  - (b) False
* **Answer**: (b) False
* **Explanation**: False according to textbook context (Internal styles are efficient for single-page styling compared to repeating inline styles; however, external stylesheets are superior across multiple pages).

#### Q. [ict_ch4_tb_tf3] | CSS Layout Function
* **Source**: `textbook_exercise` | **Type**: `true_false` | **Difficulty**: `easy` | **Marks**: 1M
* **Question**: Write 'T' for true or 'F' for false: Cascading Style Sheets (CSS) are used to format the layout of a webpage.
* **Options**:
  - (a) True
  - (b) False
* **Answer**: (a) True
* **Explanation**: True. CSS is specifically designed to format visual layout, color schemes, and presentation.

#### Q. [ict_ch4_tb_tf4] | CSS Rule Components
* **Source**: `textbook_exercise` | **Type**: `true_false` | **Difficulty**: `easy` | **Marks**: 1M
* **Question**: Write 'T' for true or 'F' for false: A CSS rule contains two parts- Selector and Declaration Block.
* **Options**:
  - (a) True
  - (b) False
* **Answer**: (a) True
* **Explanation**: True. A CSS rule consists of a Selector (pointing to the element) and a Declaration Block (enclosed in curly brackets containing properties and values).

#### Q. [ict_ch4_tb_sa1] | CSS Selector
* **Source**: `textbook_exercise` | **Type**: `short_answer` | **Difficulty**: `easy` | **Marks**: 2M
* **Question**: Define CSS Selector.
* **Answer**: A CSS Selector is the part of a CSS rule that points to the HTML element you want to style (e.g., 'h1', 'p', or 'body').
* **Explanation**: Full 2 marks: 1M for defining selector as pointing to HTML elements, 1M for a correct example.

#### Q. [ict_ch4_tb_sa2] | <style> Tag Purpose
* **Source**: `textbook_exercise` | **Type**: `short_answer` | **Difficulty**: `easy` | **Marks**: 2M
* **Question**: What is the use of the <style> tag?
* **Answer**: The <style> tag in HTML helps us to modify text and elements in a page. It allows defining internal CSS rules—including font size, font family, color, and background styling—for an entire single webpage.
* **Explanation**: Full 2 marks: 1M for mentioning it embeds internal CSS, 1M for mentioning styling of elements/fonts/colors.

#### Q. [ict_ch4_tb_sa3] | Linking External CSS Syntax
* **Source**: `textbook_exercise` | **Type**: `short_answer` | **Difficulty**: `medium` | **Marks**: 2M
* **Question**: Write the general format of linking CSS with HTML?
* **Answer**: An external CSS file is linked inside the <head> section using the <link> tag:
<head>
  <link rel="stylesheet" type="text/css" href="filename.css">
</head>
* **Explanation**: Full 2 marks: 1M for mentioning <link> in <head>, 1M for correct attributes (rel='stylesheet' and href).

#### Q. [ict_ch4_tb_sa4] | CSS Comments
* **Source**: `textbook_exercise` | **Type**: `short_answer` | **Difficulty**: `easy` | **Marks**: 2M
* **Question**: How are comments given in CSS?
* **Answer**: Comments in CSS are written inside '/*' and '*/'. Everything between these symbols is ignored by the browser.
Example: /* This is a CSS comment */
* **Explanation**: Full 2 marks: 1M for identifying /* and */ delimiters, 1M for example.

#### Q. [ict_ch4_tb_sa5] | background-image Property Syntax
* **Source**: `textbook_exercise` | **Type**: `short_answer` | **Difficulty**: `medium` | **Marks**: 2M
* **Question**: Write the syntax of background-image property.
* **Answer**: Syntax: selector { background-image: url('image_path_or_URL'); }
Example: body { background-image: url('nature.jpg'); }
* **Explanation**: Full 2 marks: 1M for property name and url() function syntax, 1M for complete example.

#### Q. [ict_ch4_tb_la1] | Advantages of Using CSS
* **Source**: `textbook_exercise` | **Type**: `long_answer` | **Difficulty**: `medium` | **Marks**: 4M
* **Question**: What are the advantages of using CSS?
* **Answer**: 1. Saves Time: Write CSS code once and reuse it across multiple HTML elements and multiple web pages.
2. Easy Maintenance: Separation of content and presentation means you can change the look of an entire website by editing a single style sheet.
3. Fast Webpage Loading: External CSS files are cached by the browser, reducing bandwidth and server request loads.
4. Superior Styles & Printer-Friendly: Allows advanced typographic formatting and allows creating printer-friendly page layouts.
* **Explanation**: Full 4 marks: 1M for each of the 4 key advantages explained with clarity.

#### Q. [ict_ch4_tb_la2] | How CSS Saves Time
* **Source**: `textbook_exercise` | **Type**: `long_answer` | **Difficulty**: `medium` | **Marks**: 3M
* **Question**: Explain how CSS saves time.
* **Answer**: CSS saves time because you can define a style rule once and apply it to multiple elements on a page or across thousands of pages on a website. Instead of repeating formatting attributes (like <font color='red'>) inside every single HTML tag, one CSS rule (p { color: red; }) styles them all instantly. Furthermore, to make a global design update, you only modify the CSS sheet in one place rather than editing each webpage individually.
* **Explanation**: Full 3 marks: 1.5M for single declaration reuse, 1.5M for centralized global updates.

#### Q. [ict_ch4_tb_la3] | Three Types of CSS
* **Source**: `textbook_exercise` | **Type**: `long_answer` | **Difficulty**: `medium` | **Marks**: 4M
* **Question**: Explain the types of CSS.
* **Answer**: 1. Inline Style Sheet: Applied directly inside an individual HTML tag using the 'style' attribute (e.g., <p style='color:blue;'>). Useful for styling a single element, but inefficient for reuse.
2. Internal Style Sheet: Declared within <style> tags inside the <head> section. Styles all matching elements on that single page.
3. External Style Sheet: Written in a separate file with a .css extension and linked via the <link> tag. Best for websites because a single file styles multiple pages consistently.
* **Explanation**: Full 4 marks: 1M each for Inline, Internal, External explanations, and 1M for comparing their scope.

#### Q. [ict_ch4_tb_la4] | HTML Tag Definitions
* **Source**: `textbook_exercise` | **Type**: `long_answer` | **Difficulty**: `medium` | **Marks**: 4M
* **Question**: Define the following tags with examples:
(a) <P>
(b) <Font>
(c) <Body>
(d) <BR>
* **Answer**: (a) <P>: Paragraph tag. A container tag used to define a paragraph. Leaves blank space before and after. Example: <p align='center'>Welcome to my page</p>
(b) <Font>: A container tag used to change the font face, size, and color of text. Example: <font face='Arial' color='red' size='4'>Sample Text</font>
(c) <Body>: A container tag that encloses all visible contents of a webpage. Example: <body bgcolor='yellow' text='black'>...</body>
(d) <BR>: Break tag. An empty tag used to insert a single line break without spacing. Example: First Line<br>Second Line
* **Explanation**: Full 4 marks: 1M for each tag (0.5M definition + 0.5M valid example).

#### Q. [ict_ch4_tb_la5] | HTML Code for Formulas
* **Source**: `textbook_exercise` | **Type**: `long_answer` | **Difficulty**: `medium` | **Marks**: 3M
* **Question**: Write the HTML code of the following output:
(a) H2SO4
(b) (Hypotenus)^2 = (one side)^2 + (other side)^2
* **Answer**: (a) Chemical Formula (Subscript):
H<sub>2</sub>SO<sub>4</sub>

(b) Mathematical Equation (Superscript):
(Hypotenus)<sup>2</sup> = (one side)<sup>2</sup> + (other side)<sup>2</sup>
* **Explanation**: Full 3 marks: 1.5M for correct <sub> usage in H2SO4, 1.5M for correct <sup> usage in equation.

#### Q. [ict_ch4_tb_lab1] | CSS Table Styling Lab Project
* **Source**: `textbook_exercise` | **Type**: `long_answer` | **Difficulty**: `hard_hots` | **Marks**: 4M
* **Question**: Create a CSS page that will hold details about your friends like name, address, date of birth, etc. Follow the details given below to create the table:
1. Background page color: Cyan
2. Table, th, td: border should be 1px solid black
3. Border with collapse property
4. th and td padding should be set to 10px
5. font-face: Courier New
6. font-size: 20
* **Answer**: <!DOCTYPE html>
<html>
<head>
  <title>Friends Details</title>
  <style>
    body {
      background-color: cyan;
      font-family: 'Courier New', Courier, monospace;
      font-size: 20px;
    }
    table, th, td {
      border: 1px solid black;
      border-collapse: collapse;
      padding: 10px;
    }
  </style>
</head>
<body>
  <h2>Friends Information Table</h2>
  <table>
    <tr><th>Name</th><th>Address</th><th>Date of Birth</th></tr>
    <tr><td>Aarav</td><td>123 Park Street</td><td>15/08/2012</td></tr>
    <tr><td>Pushti</td><td>456 Lake View</td><td>22/11/2012</td></tr>
  </table>
</body>
</html>
* **Explanation**: Full 4 marks: 1M for body background-color and font properties, 1M for table border and collapse, 1M for th/td padding, 1M for valid HTML table structure.

#### Q. [ict_ch4_tb_lab2] | HTML Webpage Creation Lab Project
* **Source**: `textbook_exercise` | **Type**: `long_answer` | **Difficulty**: `hard_hots` | **Marks**: 4M
* **Question**: Collect information from the internet and create an HTML page on 'Mobile and Internet Addiction in children'. Make use of the following tags:
(a) Paragraph tag
(b) Line break tag
(c) Font tag
(d) Bold, Italic and Underline tags
(e) Subscript tag
(f) Add comments explaining the use of the tags in the code.
* **Answer**: <!DOCTYPE html>
<html>
<head><title>Internet Addiction in Children</title></head>
<body bgcolor='#F0F8FF'>
  <!-- Comment: Heading Section with Underline and Bold -->
  <center><u><b><font face='Arial' size='6' color='darkblue'>Impact of Mobile Addiction</font></b></u></center>
  <br>
  <!-- Comment: Introductory Paragraph with Italic -->
  <p align='justify'>
    <i>Excessive screen time among young children leads to reduced physical activity and poor sleep habits.</i><br>
    Researchers found that prolonged gaming triggers chemical changes in dopamine<sub>1</sub> receptor pathways.
  </p>
  <!-- Comment: Recommendations Section -->
  <p><b>Tips to overcome addiction:</b><br>
    1. Limit recreational screen time.<br>
    2. Encourage outdoor sports.
  </p>
</body>
</html>
* **Explanation**: Full 4 marks: 0.5M for each required element (<p>, <br>, <font>, <b>/<i>/<u>, <sub>, and HTML comments).

### --- TEXTBOOK WORKSHEET ---

#### Q. [ict_ch4_ws_mcq1] | Line Break Tag (Worksheet)
* **Source**: `textbook_worksheet` | **Type**: `mcq` | **Difficulty**: `easy` | **Marks**: 1M
* **Question**: In HTML, a <br> tag is used to _______.
* **Options**:
  - (i) Insert a line break
  - (ii) Insert a symbol
  - (iii) Insert a paragraph
  - (iv) None of these
* **Answer**: (i) Insert a line break
* **Explanation**: The <br> tag is an empty tag used to insert a single line break in an HTML document.

#### Q. [ict_ch4_ws_mcq2] | Comment Tag (Worksheet)
* **Source**: `textbook_worksheet` | **Type**: `mcq` | **Difficulty**: `easy` | **Marks**: 1M
* **Question**: Which of the following tags is used to insert a comment on a web page?
* **Options**:
  - (i) <hr>
  - (ii) <line>
  - (iii) <comment>
  - (iv) None of these
* **Answer**: (iii) <comment>
* **Explanation**: In older HTML, the <comment> tag was used. In modern HTML, <!-- --> is standard.

#### Q. [ict_ch4_ws_mcq3] | Background Color Attribute (Worksheet)
* **Source**: `textbook_worksheet` | **Type**: `mcq` | **Difficulty**: `easy` | **Marks**: 1M
* **Question**: Which of the following is used to set the background color of a web page?
* **Options**:
  - (i) BGCOLOR
  - (ii) COLOR
  - (iii) Both (a) and (b)
  - (iv) None of these
* **Answer**: (i) BGCOLOR
* **Explanation**: The BGCOLOR attribute of the <body> tag sets the page background color.

#### Q. [ict_ch4_ws_mcq4] | Text Color Attribute (Worksheet)
* **Source**: `textbook_worksheet` | **Type**: `mcq` | **Difficulty**: `easy` | **Marks**: 1M
* **Question**: Which of the following is used to set the text colour in the <body> tag?
* **Options**:
  - (i) Color
  - (ii) Text
  - (iii) Textcolor
  - (iv) None
* **Answer**: (ii) Text
* **Explanation**: The TEXT attribute of the <body> tag sets the default color for all body text.

#### Q. [ict_ch4_ws_tf1] | HTML Attribute Definition (Worksheet)
* **Source**: `textbook_worksheet` | **Type**: `true_false` | **Difficulty**: `easy` | **Marks**: 1M
* **Question**: An attribute is used to define the characteristics of an HTML element.
* **Options**:
  - (a) True
  - (b) False
* **Answer**: (a) True
* **Explanation**: True. Attributes provide additional properties and specifications inside an HTML tag.

#### Q. [ict_ch4_ws_tf2] | ALINK Default Color (Worksheet)
* **Source**: `textbook_worksheet` | **Type**: `true_false` | **Difficulty**: `medium` | **Marks**: 1M
* **Question**: The default colour of ALINK attribute is violet.
* **Options**:
  - (a) True
  - (b) False
* **Answer**: (b) False
* **Explanation**: False. The default color of ALINK (Active Link) is Red. Visited link (VLINK) is purple/violet.

#### Q. [ict_ch4_ws_tf3] | Underline Container Tag (Worksheet)
* **Source**: `textbook_worksheet` | **Type**: `true_false` | **Difficulty**: `easy` | **Marks**: 1M
* **Question**: The <U> is a container tag.
* **Options**:
  - (a) True
  - (b) False
* **Answer**: (a) True
* **Explanation**: True. The <U> tag requires both an opening <U> and closing </U> tag.

#### Q. [ict_ch4_ws_tf4] | CSS Acronym Trap (Worksheet)
* **Source**: `textbook_worksheet` | **Type**: `true_false` | **Difficulty**: `easy` | **Marks**: 1M
* **Question**: CSS stands for Collective Style Sheets.
* **Options**:
  - (a) True
  - (b) False
* **Answer**: (b) False
* **Explanation**: False. CSS stands for Cascading Style Sheets.

#### Q. [ict_ch4_ws_sa1] | Two Container Tags (Worksheet)
* **Source**: `textbook_worksheet` | **Type**: `short_answer` | **Difficulty**: `easy` | **Marks**: 2M
* **Question**: Explain two container tags in HTML with examples.
* **Answer**: Container tags require both an opening and a closing tag. Examples:
1. <P>...</P>: Used to define a paragraph (e.g., <p>Hello World</p>).
2. <B>...</B>: Used to render text in bold (e.g., <b>Important</b>).
* **Explanation**: Full 2 marks: 1M for explaining container tag nature, 1M for two correct examples.

#### Q. [ict_ch4_ws_sa2] | Two Unpaired Tags (Worksheet)
* **Source**: `textbook_worksheet` | **Type**: `short_answer` | **Difficulty**: `easy` | **Marks**: 2M
* **Question**: Explain two unpaired (empty) tags in HTML with examples.
* **Answer**: Unpaired (empty/void) tags do not require a closing tag. Examples:
1. <BR>: Inserts a single line break without space (e.g., Line 1<br>Line 2).
2. <HR>: Inserts a horizontal thematic dividing line across the page.
* **Explanation**: Full 2 marks: 1M for explaining unpaired tag nature, 1M for two correct examples.

#### Q. [ict_ch4_ws_sa3] | Subscript vs Superscript (Worksheet)
* **Source**: `textbook_worksheet` | **Type**: `short_answer` | **Difficulty**: `medium` | **Marks**: 2M
* **Question**: Explain the difference between subscript and superscript tags.
* **Answer**: Subscript (<sub>) displays text slightly below the normal baseline in a smaller font, commonly used for chemical formulas (e.g., H<sub>2</sub>O).
Superscript (<sup>) displays text slightly above the normal baseline in a smaller font, commonly used for mathematical powers (e.g., X<sup>2</sup>).
* **Explanation**: Full 2 marks: 1M for <sub> with example, 1M for <sup> with example.

#### Q. [ict_ch4_ws_sa4] | Paragraph Tag (Worksheet)
* **Source**: `textbook_worksheet` | **Type**: `short_answer` | **Difficulty**: `medium` | **Marks**: 2M
* **Question**: Explain the paragraph tag in HTML with an example.
* **Answer**: The <P> tag is a container tag used to structure text into paragraphs. The browser automatically inserts blank vertical space before and after the paragraph. It supports the ALIGN attribute (left, right, center, justify).
Example: <p align='center'>This is a centered paragraph.</p>
* **Explanation**: Full 2 marks: 1M for paragraph definition and spacing behavior, 1M for ALIGN attribute example.

### --- LEGACY PORTAL ---

#### Q. [ict_ch4_portal_mcq1] | Body Background Attribute
* **Source**: `legacy_portal` | **Type**: `mcq` | **Difficulty**: `easy` | **Marks**: 1M
* **Question**: Which body attribute sets the background colour of a web page?
* **Options**:
  - (a) TEXT
  - (b) BGCOLOR
  - (c) BACKGROUND
  - (d) LINK
* **Answer**: (b) BGCOLOR
* **Explanation**: BGCOLOR sets the canvas color, whereas BACKGROUND sets a graphic image as the wallpaper.

#### Q. [ict_ch4_portal_mcq2] | Line Break Tag
* **Source**: `legacy_portal` | **Type**: `mcq` | **Difficulty**: `easy` | **Marks**: 1M
* **Question**: Which tag is used to insert a new line without starting a new paragraph?
* **Options**:
  - (a) <p>
  - (b) <br>
  - (c) <font>
  - (d) <hr>
* **Answer**: (b) <br>
* **Explanation**: The <br> tag breaks the line immediately without adding paragraph margins.

#### Q. [ict_ch4_portal_mcq3] | Subscript Tag
* **Source**: `legacy_portal` | **Type**: `mcq` | **Difficulty**: `easy` | **Marks**: 1M
* **Question**: Which tag displays text slightly below the normal line?
* **Options**:
  - (a) <sup>
  - (b) <sub>
  - (c) <font>
  - (d) <p>
* **Answer**: (b) <sub>
* **Explanation**: The <sub> tag formats text as subscript (below the baseline).

#### Q. [ict_ch4_portal_mcq4] | Font Face Attribute
* **Source**: `legacy_portal` | **Type**: `mcq` | **Difficulty**: `easy` | **Marks**: 1M
* **Question**: Which attribute of the <font> tag changes the font type?
* **Options**:
  - (a) SIZE
  - (b) COLOR
  - (c) FACE
  - (d) ALIGN
* **Answer**: (c) FACE
* **Explanation**: FACE specifies typeface names like Arial, Times New Roman, or Verdana.

#### Q. [ict_ch4_portal_mcq5] | HTML Comment Syntax
* **Source**: `legacy_portal` | **Type**: `mcq` | **Difficulty**: `easy` | **Marks**: 1M
* **Question**: Which is the standard syntax for an HTML comment?
* **Options**:
  - (a) // comment
  - (b) /* comment */
  - (c) <!-- comment -->
  - (d) # comment
* **Answer**: (c) <!-- comment -->
* **Explanation**: <!-- ... --> is standard HTML comment syntax.

#### Q. [ict_ch4_portal_mcq6] | Internal Style Tag
* **Source**: `legacy_portal` | **Type**: `mcq` | **Difficulty**: `easy` | **Marks**: 1M
* **Question**: Which HTML tag is used to define an internal style sheet?
* **Options**:
  - (a) <css>
  - (b) <script>
  - (c) <style>
  - (d) <link>
* **Answer**: (c) <style>
* **Explanation**: <style> is placed inside <head> to embed internal CSS rules.

#### Q. [ict_ch4_portal_mcq7] | CSS Background Color Property
* **Source**: `legacy_portal` | **Type**: `mcq` | **Difficulty**: `easy` | **Marks**: 1M
* **Question**: Which property is used to change the background color of an element in CSS?
* **Options**:
  - (a) bgcolor
  - (b) color
  - (c) background-color
  - (d) back-color
* **Answer**: (c) background-color
* **Explanation**: In CSS, background-color sets the background color. (bgcolor is an obsolete HTML attribute).

#### Q. [ict_ch4_portal_mcq8] | Inline Style Sheet Definition
* **Source**: `legacy_portal` | **Type**: `mcq` | **Difficulty**: `easy` | **Marks**: 1M
* **Question**: Which type of CSS is written inside the style attribute of an HTML tag?
* **Options**:
  - (a) Inline CSS
  - (b) Internal CSS
  - (c) External CSS
  - (d) Linked CSS
* **Answer**: (a) Inline CSS
* **Explanation**: Inline CSS is declared locally inside the style attribute of an HTML element.

#### Q. [ict_ch4_portal_mcq9] | External Style Sheet File
* **Source**: `legacy_portal` | **Type**: `mcq` | **Difficulty**: `easy` | **Marks**: 1M
* **Question**: Which type of CSS is stored in a separate file with a .css extension?
* **Options**:
  - (a) Inline CSS
  - (b) Internal CSS
  - (c) External CSS
  - (d) Font CSS
* **Answer**: (c) External CSS
* **Explanation**: External style sheets are saved as separate .css files and linked with <link>.

#### Q. [ict_ch4_portal_mcq10] | CSS Font Family Property
* **Source**: `legacy_portal` | **Type**: `mcq` | **Difficulty**: `easy` | **Marks**: 1M
* **Question**: Which CSS property changes the typeface of text?
* **Options**:
  - (a) font-size
  - (b) font-family
  - (c) font-weight
  - (d) font-style
* **Answer**: (b) font-family
* **Explanation**: The font-family property in CSS sets the typeface (e.g. font-family: Arial, sans-serif;).

#### Q. [ict_ch4_portal_mcq11] | CSS Declaration Separator
* **Source**: `legacy_portal` | **Type**: `mcq` | **Difficulty**: `easy` | **Marks**: 1M
* **Question**: In a CSS rule, what separates a property from its value?
* **Options**:
  - (a) Semicolon
  - (b) Colon
  - (c) Comma
  - (d) Full stop
* **Answer**: (b) Colon
* **Explanation**: A colon ':' separates the property from its value; a semicolon ';' separates distinct declarations.

#### Q. [ict_ch4_portal_fib1] | Unvisited Link Attribute
* **Source**: `legacy_portal` | **Type**: `fib` | **Difficulty**: `easy` | **Marks**: 1M
* **Question**: The ____________ attribute sets the colour of unvisited links in the <body> tag.
* **Answer**: LINK
* **Explanation**: LINK sets unvisited link color (default blue).

#### Q. [ict_ch4_portal_fib2] | Font Weight Property
* **Source**: `legacy_portal` | **Type**: `fib` | **Difficulty**: `easy` | **Marks**: 1M
* **Question**: The CSS property used to make text bold or lighter is ____________.
* **Answer**: font-weight
* **Explanation**: The font-weight property accepts values like normal, bold, bolder, lighter, or numeric 100-900.

#### Q. [ict_ch4_portal_tf1] | Superscript Placement
* **Source**: `legacy_portal` | **Type**: `true_false` | **Difficulty**: `easy` | **Marks**: 1M
* **Question**: The <sup> tag displays text below the normal line.
* **Options**:
  - (a) True
  - (b) False
* **Answer**: (b) False
* **Explanation**: False. <sup> displays text above the normal line. <sub> displays text below.

#### Q. [ict_ch4_portal_tf2] | External CSS Sharing
* **Source**: `legacy_portal` | **Type**: `true_false` | **Difficulty**: `easy` | **Marks**: 1M
* **Question**: An external style sheet can be linked to more than one HTML page.
* **Options**:
  - (a) True
  - (b) False
* **Answer**: (a) True
* **Explanation**: True. That is the greatest advantage of external CSS—one stylesheet controls thousands of pages.

#### Q. [ict_ch4_portal_tf3] | Inline CSS Priority
* **Source**: `legacy_portal` | **Type**: `true_false` | **Difficulty**: `medium` | **Marks**: 1M
* **Question**: Inline CSS has lower priority than external CSS.
* **Options**:
  - (a) True
  - (b) False
* **Answer**: (b) False
* **Explanation**: False. Inline CSS has the highest priority and overrides external and internal styles.

#### Q. [ict_ch4_portal_sa1] | <br> vs <p> Tag Difference
* **Source**: `legacy_portal` | **Type**: `short_answer` | **Difficulty**: `medium` | **Marks**: 2M
* **Question**: Differentiate between the <br> tag and the <p> tag.
* **Answer**: The <br> tag inserts a single line break without extra vertical spacing and is an empty tag. The <p> tag creates a paragraph block with automatic blank space before and after, and is a container tag supporting alignment.
* **Explanation**: Full 2 marks: 1M for line break vs paragraph distinction, 1M for empty vs container tag distinction.

#### Q. [ict_ch4_portal_sa2] | Body BGCOLOR, TEXT, BACKGROUND Attributes
* **Source**: `legacy_portal` | **Type**: `short_answer` | **Difficulty**: `medium` | **Marks**: 2M
* **Question**: What are the uses of the BGCOLOR, TEXT and BACKGROUND attributes of the <body> tag?
* **Answer**: BGCOLOR sets the solid background color of the webpage, TEXT sets the default color of all page text, and BACKGROUND specifies an image file path to display as the background wallpaper.
* **Explanation**: Full 2 marks: Accurate explanation for all 3 attributes.

#### Q. [ict_ch4_portal_sa3] | CSS Font Properties Trio
* **Source**: `legacy_portal` | **Type**: `short_answer` | **Difficulty**: `medium` | **Marks**: 2M
* **Question**: What do font-size, font-family and font-style do in CSS?
* **Answer**: font-size defines the height/size of the text (e.g. 16px), font-family sets the typeface/font name (e.g. Arial), and font-style specifies whether the text is normal, italic, or oblique.
* **Explanation**: Full 2 marks: Accurate explanation for each property.

### --- TRIVIA ENRICHMENT ---

#### Q. [ict_ch4_trivia1] | HTML Creator History
* **Source**: `trivia_enrichment` | **Type**: `short_answer` | **Difficulty**: `easy` | **Marks**: 1M
* **Question**: Who created HTML and when?
* **Answer**: HTML was created by Sir Tim Berners-Lee in late 1991 while working at CERN, and was officially released to the public in 1995.
* **Explanation**: 1 mark for Tim Berners-Lee and CERN/1991.

#### Q. [ict_ch4_trivia2] | CSS Inception History
* **Source**: `trivia_enrichment` | **Type**: `short_answer` | **Difficulty**: `easy` | **Marks**: 1M
* **Question**: Who proposed CSS and when was it published by W3C?
* **Answer**: CSS was proposed by Håkon Wium Lie on October 10, 1994, and was officially published as a recommendation by the W3C in December 1996.
* **Explanation**: 1 mark for Håkon Wium Lie (1994) and W3C (1996).

#### Q. [ict_ch4_trivia3] | The Cascade Metaphor
* **Source**: `trivia_enrichment` | **Type**: `short_answer` | **Difficulty**: `medium` | **Marks**: 1M
* **Question**: Why is CSS called 'Cascading'?
* **Answer**: It is called cascading because styles flow down from highest to lowest priority like a waterfall: Inline CSS overrides Internal CSS, which overrides External CSS, which overrides Browser Defaults.
* **Explanation**: 1 mark for explaining style priority inheritance waterfall.
