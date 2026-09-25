# CHAPTER KNOWLEDGE BASE: LISTS AND IMAGES IN HTML
**Subject**: ICT | **Chapter**: 5 | **Standard**: Class 7 CBSE
**Curricular Scope**: Pages 73-86 | Let's Exercise (pp. 79-81) | Worksheet 5 (p. 82) | Test Paper 1 (pp. 83-86)

## 1. Executive Summary & Learning Outcomes
This chapter provides an exhaustive curriculum on structuring and presenting rich multimedia content in HTML5. Key learning objectives include:
- Mastering the three list formats: Unordered (<ul>), Ordered (<ol>), and Definition / Description (<dl>).
- Configuring list attributes: 'type', 'start', and the modern HTML5 'reversed' attribute.
- Designing multi-level nested list hierarchies for categorization and navigation menus.
- Styling list markers with CSS: list-style-type, list-style-image, and list-style-position.
- Embedding graphics with the <img> tag: attributes (src, alt, width, height, title) and format characteristics (.jpg, .png, .gif, .webp).
- Constructing animated banners with <marquee> and understanding its modern CSS replacement.
- Structuring tabular data using <table>, <tr>, <th>, <td>, along with 'colspan', 'rowspan', and 'border-collapse'.

---

## 2. Core Conceptual Theory & Detailed Textbook Notes

### 1. Significance of Lists in Web Design & The List Architecture

In HTML, lists are essential structural elements used to group, associate, and format related pieces of information into clean, organized, and easily readable presentations. Rather than presenting dense paragraphs of unstructured text, lists allow users and search engines to scan content rapidly.

Key Architectural Principles:
• List Container Tags: Every list is enclosed within an opening and closing list tag (<ul>...</ul>, <ol>...</ol>, or <dl>...</dl>).
• List Item Tag (<li>): Represents an individual entry within an ordered or unordered list. It is a container element placed inside <ul> or <ol> tags.
• Nested Lists: A list can be embedded inside another list item. For instance, placing a bulleted <ul> inside an <ol> item creates hierarchical sub-categories (outlines, navigation submenus, multi-level recipe steps).

### 2. Comprehensive Taxonomy of HTML Lists (Unordered, Ordered, Definition)

HTML natively supports three distinct types of lists:

1. Unordered List (<ul>...</ul>):
   • Used for collections of items where the sequence or numerical priority does not matter (e.g., shopping list, ingredients, features).
   • Items are displayed with bullet markers.
   • Default bullet style is 'disc' (a filled solid black circle).
   • Supported bullet shapes via the 'type' attribute: 'disc', 'circle' (hollow circle), and 'square' (filled square). Note: 'rectangle' or 'triangle' are INVALID values.

2. Ordered List (<ol>...</ol>):
   • Used for sequential, step-by-step, or prioritized procedures (e.g., recipes, top 10 rankings, instructional guides).
   • Items are preceded by numerical or alphabetical markers.
   • Default numbering style is Arabic numerals ('1').
   • Key Attributes of <ol>:
     - type: Specifies the numbering system: '1' (Arabic: 1, 2, 3), 'A' (Uppercase letters: A, B, C), 'a' (Lowercase letters: a, b, c), 'I' (Uppercase Roman: I, II, III), 'i' (Lowercase Roman: i, ii, iii).
     - start: Specifies the numeric starting offset for the list, regardless of the marker style (e.g., <ol type='A' start='4'> starts at 'D').
     - reversed: A boolean attribute introduced in HTML5 that causes the list numbering to count downwards in descending order (e.g., 5, 4, 3, 2, 1).

3. Definition / Description List (<dl>...</dl>):
   • Designed specifically for glossaries, term-and-definition dictionaries, FAQ lists, or product specifications.
   • Utilizes three interdependent tags:
     - <dl>: Delimits the entire definition list container.
     - <dt>: (Definition Term) Specifies the word, phrase, or question being defined (flush with left margin).
     - <dd>: (Definition Description / Data) Contains the explanation or answer, indented underneath the <dt>.

### 3. Advanced CSS List Properties & Marker Customization

While HTML supports the 'type' attribute, modern web standards recommend Cascading Style Sheets (CSS) for all list presentations:

1. list-style-type: Specifies the visual marker for list items.
   • Values for Unordered: 'disc', 'circle', 'square', 'none'.
   • Values for Ordered: 'decimal', 'lower-alpha', 'upper-alpha', 'lower-roman', 'upper-roman', 'decimal-leading-zero'.
2. list-style-image: Replaces standard geometric bullets with custom graphical icon files.
   • Syntax: list-style-image: url('star_bullet.png');
3. list-style-position: Controls whether bullet markers appear inside or outside the text content block flow.
   • 'outside' (default): Bullets sit to the left of the text block; wrapped text lines do not indent under the bullet.
   • 'inside': Bullets sit inside the text block margin; wrapped text lines wrap directly underneath the bullet.
4. list-style (Shorthand): Combines all three properties into one concise declaration.
   • Syntax: ul { list-style: square inside url('icon.png'); }

### 4. Inserting Images in HTML (<img> Tag & Graphic Formats)

Images provide visual appeal, clarify complex instructions, and enhance emotional engagement on web pages.

The <img> Tag Characteristics:
• It is an EMPTY tag (void element), meaning it has no closing tag (no </img>).
• Attributes of <img>:
  1. src (Source): Mandatory attribute specifying the URL or relative directory file path of the image (e.g., src='images/tiger.jpg').
  2. alt (Alternate Text): Crucial accessibility attribute providing descriptive text if the image fails to load (broken link, slow connection) and for blind users using screen readers.
  3. width & height: Specifies dimensional scaling in pixels (px) or viewport percentage (%) (e.g., width='300' height='200').
  4. title: Displays a floating advisory tooltip when the user hovers the cursor over the image.

Standard Web Image Formats:
• JPEG / JPG (Joint Photographic Experts Group): Lossy compression supporting 16.7 million colors (24-bit). Ideal for natural photographs and realistic scenery.
• GIF (Graphics Interchange Format): 8-bit index color format (max 256 colors). Supports frame animation and single-color binary transparency. Ideal for logos and simple animated graphics.
• PNG (Portable Network Graphics): Lossless format supporting 24-bit color and alpha-channel transparency (smooth gradients against any background). Best for diagrams, icons, and transparent logos.

### 5. Animated Marquees (<marquee> Tag & Dynamic Attributes)

The <marquee> tag is used in legacy HTML to create continuous scrolling text tickers, banner alerts, or animated images across the browser viewport.

Key Attributes of <marquee>:
• direction: Specifies the scrolling vector: 'left' (default), 'right', 'up', or 'down'.
• behavior: Determines the motion pattern:
  - 'scroll' (default): Text scrolls in from one side, moves across, exits completely, and repeats.
  - 'slide': Text scrolls in from one side and permanently stops once it hits the opposing margin.
  - 'alternate': Text continuously bounces back and forth between opposing margins like a ping-pong ball.
• scrollamount: Sets the displacement speed in pixels per animation frame (higher value = faster movement).
• scrolldelay: Specifies the interval delay between movements in milliseconds (higher value = slower stutter).
• loop: Specifies the total number of repetitions before stopping (default is infinite or -1).
• bgcolor: Sets the background highlight strip color of the marquee track.
• height & width: Sets the bounding frame dimensions.

Modern Web Standard Note: The <marquee> tag is deprecated in HTML5 because motion tickers distract neurodivergent readers and fail Web Content Accessibility Guidelines (WCAG). Professional developers now use CSS @keyframes animations.

### 6. Structuring Data with HTML Tables (<table> Tag & Cell Spanning)

Tables organize complex tabular data (timetables, marksheets, schedules, pricing matrices) into rows and columns.

Core Table Architecture:
• <table>: Container element defining the table grid.
• <caption>: Displays an optional title directly above the table.
• <tr> (Table Row): Encapsulates a horizontal row of cells.
• <th> (Table Header): Defines a heading cell; text is automatically formatted as BOLD and CENTER-ALIGNED.
• <td> (Table Data): Defines a regular data cell; text is regular weight and LEFT-ALIGNED.

Essential Attributes & CSS Properties:
• border: Specifies the border frame width around the table and cells (e.g., border='1').
• border-collapse: CSS property (border-collapse: collapse;) that collapses double-lined browser borders into a single clean crisp rule.
• cellpadding: Space between cell borders and the cell content.
• cellspacing: Distance between adjacent individual cells.
• colspan: Merges multiple horizontal columns into one wider cell (e.g., <td colspan='3'>).
• rowspan: Merges multiple vertical rows into one taller cell (e.g., <td rowspan='2'>).

### 7. Semantic Menus & Modern Web Architecture

In modern industry web development (Google, Amazon, YouTube, Wikipedia):
• Navigation bars (navbars) are structurally constructed using unordered lists (<nav><ul><li><a href='...'>Home</a></li></ul></nav>).
• CSS Flexbox (display: flex;) or CSS Grid is applied to strip bullet markers (list-style: none;) and arrange list items horizontally.
• Screen readers and search engine crawlers rely on semantic list structures to understand the navigational hierarchy and site architecture of web applications.

---

## 3. Standardized Question Bank (74 Authentic Items)

### Multiple Choice Questions (MCQ) (17 Items)

#### [ICT_CH05_001] Which one is the default bullet style in an unordered list of items in HTML?
- **Source**: `textbook_exercise` | **Topic**: Unordered List Default Bullet | **Difficulty**: `easy` | **Marks**: 1
- **Options**:
  - (a) Disc
  - (b) Square
  - (c) Rectangle
  - (d) None of these
- **Correct Answer**: `(a) Disc`
- **Explanation / Marking Scheme**: In HTML, an unordered list (<ul>) defaults to 'disc' (a solid filled black circle). Other valid styles are 'circle' and 'square'. 'Rectangle' is not a valid bullet type.

#### [ICT_CH05_002] By which tag, an unordered list is represented?
- **Source**: `textbook_exercise` | **Topic**: Unordered List Tag | **Difficulty**: `easy` | **Marks**: 1
- **Options**:
  - (a) <U>
  - (b) <I>
  - (c) <UL>
  - (d) <OL>
- **Correct Answer**: `(c) <UL>`
- **Explanation / Marking Scheme**: An unordered list is defined using the <UL> (Unordered List) container tag. <OL> defines an ordered list, <U> underlines text, and <I> italicizes text.

#### [ICT_CH05_003] Which among the following list allows symbols (bullets)?
- **Source**: `textbook_exercise` | **Topic**: List Marker Types | **Difficulty**: `easy` | **Marks**: 1
- **Options**:
  - (a) Ordered
  - (b) Unordered
  - (c) Definition
  - (d) None of these
- **Correct Answer**: `(b) Unordered`
- **Explanation / Marking Scheme**: Unordered lists use symbols (such as discs, circles, or squares) as bullet markers. Ordered lists use numbers or letters, and definition lists use term-description pairings without markers.

#### [ICT_CH05_004] Which among the following cannot be the value of the attribute TYPE in a <UL> tag?
- **Source**: `textbook_exercise` | **Topic**: Invalid List Attributes | **Difficulty**: `easy` | **Marks**: 1
- **Options**:
  - (a) Square
  - (b) Rectangle
  - (c) Circle
  - (d) Both (a) and (b)
- **Correct Answer**: `(b) Rectangle`
- **Explanation / Marking Scheme**: The valid values for the TYPE attribute in a <UL> tag are 'disc', 'circle', and 'square'. 'Rectangle' is completely invalid and not recognized by HTML specifications.

#### [ICT_CH05_005] Which attribute of the <IMG> tag is used to display some text, if for some reason the image cannot be displayed?
- **Source**: `textbook_exercise` | **Topic**: Image Tag Attributes | **Difficulty**: `easy` | **Marks**: 1
- **Options**:
  - (a) SRC
  - (b) ALT
  - (c) HREF
  - (d) None of these
- **Correct Answer**: `(b) ALT`
- **Explanation / Marking Scheme**: The ALT (Alternative Text) attribute specifies replacement descriptive text that appears if the image fails to load or for visually impaired users utilizing screen readers. SRC provides the image path, and HREF is used in anchor (<a>) links.

#### [ICT_CH05_028] Which among these is the default type of <OL> tag in HTML?
- **Source**: `worksheet_5` | **Topic**: Default Ordered List Type | **Difficulty**: `easy` | **Marks**: 1
- **Options**:
  - (a) Alphabet letters
  - (b) Roman numbers
  - (c) Arabic numbers
  - (d) None of these
- **Correct Answer**: `(c) Arabic numbers`
- **Explanation / Marking Scheme**: By default, an ordered list in HTML numbers items sequentially with Arabic numbers (1, 2, 3, 4, etc.).

#### [ICT_CH05_029] Which one of the following is a type of list that HTML supports?
- **Source**: `worksheet_5` | **Topic**: Supported List Types | **Difficulty**: `easy` | **Marks**: 1
- **Options**:
  - (a) Ordered lists
  - (b) Unordered lists
  - (c) Description lists
  - (d) All of the above
- **Correct Answer**: `(d) All of the above`
- **Explanation / Marking Scheme**: HTML supports three fundamental list types: Ordered lists (<ol>), Unordered lists (<ul>), and Description/Definition lists (<dl>).

#### [ICT_CH05_030] By which tag, an ordered list is represented?
- **Source**: `worksheet_5` | **Topic**: Ordered List Representation | **Difficulty**: `easy` | **Marks**: 1
- **Options**:
  - (a) <U>
  - (b) <I>
  - (c) <UL>
  - (d) <OL>
- **Correct Answer**: `(d) <OL>`
- **Explanation / Marking Scheme**: <OL> stands for 'Ordered List'. <UL> stands for 'Unordered List'.

#### [ICT_CH05_031] Which of the following tag allows you to provide List Items?
- **Source**: `worksheet_5` | **Topic**: List Items Tag | **Difficulty**: `easy` | **Marks**: 1
- **Options**:
  - (a) <LIST>
  - (b) <OL>
  - (c) <LI>
  - (d) All of these
- **Correct Answer**: `(c) <LI>`
- **Explanation / Marking Scheme**: The <LI> (List Item) tag defines an individual list item inside both ordered (<ol>) and unordered (<ul>) lists.

#### [ICT_CH05_032] Which among the following tag is used to define a definition term?
- **Source**: `worksheet_5` | **Topic**: Definition Term Tag | **Difficulty**: `easy` | **Marks**: 1
- **Options**:
  - (a) <DD>
  - (b) <DT>
  - (c) <DL>
  - (d) <HT>
- **Correct Answer**: `(b) <DT>`
- **Explanation / Marking Scheme**: <DT> stands for 'Definition Term'. <DD> stands for 'Definition Description / Data', and <DL> stands for 'Definition List'.

#### [ICT_CH05_053] Which tag is used to create a standard data cell within an HTML table row?
- **Source**: `school_blueprint` | **Topic**: Table Cell Tag | **Difficulty**: `medium` | **Marks**: 1
- **Options**:
  - (a) <TH>
  - (b) <TD>
  - (c) <TR>
  - (d) <TABLE>
- **Correct Answer**: `(b) <TD>`
- **Explanation / Marking Scheme**: <TD> stands for 'Table Data' and creates a regular data cell. <TR> defines the row, <TH> defines a bold header cell, and <TABLE> is the container.

#### [ICT_CH05_054] How does text inside a <TH> (Table Header) tag differ in default formatting from text inside a <TD> tag?
- **Source**: `school_blueprint` | **Topic**: Table Header Properties | **Difficulty**: `medium` | **Marks**: 1
- **Options**:
  - (a) <TH> is italic and left-aligned
  - (b) <TH> is bold and center-aligned
  - (c) <TH> is underlined and right-aligned
  - (d) <TH> is red and capitalized
- **Correct Answer**: `(b) <TH> is bold and center-aligned`
- **Explanation / Marking Scheme**: Browsers automatically format text inside <TH> cells as BOLD and CENTER-ALIGNED, whereas <TD> cells default to normal weight and left alignment.

#### [ICT_CH05_055] Which attribute is used to merge three horizontal columns into a single wider cell?
- **Source**: `school_blueprint` | **Topic**: Cell Spanning | **Difficulty**: `medium` | **Marks**: 1
- **Options**:
  - (a) rowspan='3'
  - (b) colspan='3'
  - (c) span='3'
  - (d) colmerge='3'
- **Correct Answer**: `(b) colspan='3'`
- **Explanation / Marking Scheme**: 'colspan' (Column Span) merges multiple horizontal columns into one cell. 'rowspan' merges vertical rows.

#### [ICT_CH05_056] Which attribute merges two or more vertical rows into a single taller cell?
- **Source**: `school_blueprint` | **Topic**: Row Spanning | **Difficulty**: `medium` | **Marks**: 1
- **Options**:
  - (a) rowspan
  - (b) colspan
  - (c) rowmerge
  - (d) vertical-span
- **Correct Answer**: `(a) rowspan`
- **Explanation / Marking Scheme**: 'rowspan' specifies the number of vertical rows a table cell should span.

#### [ICT_CH05_057] Which marquee behavior causes the content to bounce continuously back and forth between opposite edges?
- **Source**: `school_blueprint` | **Topic**: Marquee Behavior | **Difficulty**: `medium` | **Marks**: 1
- **Options**:
  - (a) scroll
  - (b) slide
  - (c) alternate
  - (d) rebound
- **Correct Answer**: `(c) alternate`
- **Explanation / Marking Scheme**: behavior='alternate' causes the marquee content to reverse direction every time it hits an edge, creating a continuous bouncing effect.

#### [ICT_CH05_058] Which CSS property is used to replace bullet points with a custom graphical image file?
- **Source**: `school_blueprint` | **Topic**: CSS List Marker Image | **Difficulty**: `hard` | **Marks**: 1
- **Options**:
  - (a) list-style-type
  - (b) list-style-image
  - (c) list-image-bullet
  - (d) marker-icon
- **Correct Answer**: `(b) list-style-image`
- **Explanation / Marking Scheme**: The 'list-style-image: url('bullet.png');' CSS property replaces default bullet glyphs with custom image files.

#### [ICT_CH05_059] Which HTML5 attribute causes an ordered list to count downwards in descending order?
- **Source**: `school_blueprint` | **Topic**: List Reversal Attribute | **Difficulty**: `medium` | **Marks**: 1
- **Options**:
  - (a) desc
  - (b) reverse
  - (c) reversed
  - (d) countdown
- **Correct Answer**: `(c) reversed`
- **Explanation / Marking Scheme**: The boolean attribute 'reversed' (<ol reversed>) causes the ordered list to display its numbers in descending order.

### Fill in the Blanks / One-Word Answers (13 Items)

#### [ICT_CH05_006] ____________ are used to group and associate together related content so that it is easy to read.
- **Source**: `textbook_exercise` | **Topic**: Function of Lists | **Difficulty**: `easy` | **Marks**: 1
- **Acceptable Answer(s)**: `Lists`
- **Explanation / Marking Scheme**: Lists structure disparate pieces of related information into clean, sequential, or bulleted groupings that enhance legibility and visual structure on a webpage.

#### [ICT_CH05_007] ____________ list of HTML looks like a bullet list.
- **Source**: `textbook_exercise` | **Topic**: Unordered List Appearance | **Difficulty**: `easy` | **Marks**: 1
- **Acceptable Answer(s)**: `Unordered`
- **Explanation / Marking Scheme**: An Unordered list (<ul>) presents list entries preceded by graphical bullet markers (disc, circle, or square) rather than sequential numbers.

#### [ICT_CH05_008] ____________ list of HTML looks like a numbered list.
- **Source**: `textbook_exercise` | **Topic**: Ordered List Appearance | **Difficulty**: `easy` | **Marks**: 1
- **Acceptable Answer(s)**: `Ordered`
- **Explanation / Marking Scheme**: An Ordered list (<ol>) presents list entries preceded by numerical or alphabetical sequence markers (1, 2, 3... or A, B, C...).

#### [ICT_CH05_009] Src stands for ____________ in the <IMG> tag.
- **Source**: `textbook_exercise` | **Topic**: Source Attribute Definition | **Difficulty**: `easy` | **Marks**: 1
- **Acceptable Answer(s)**: `Source`
- **Explanation / Marking Scheme**: In the <img> tag, 'src' is an abbreviation for 'Source'. It specifies the URL or relative directory path pointing to the graphic image file.

#### [ICT_CH05_037] ALT stands for ____________.
- **Source**: `worksheet_5` | **Topic**: ALT Acronym | **Difficulty**: `easy` | **Marks**: 1
- **Acceptable Answer(s)**: `Alternate Text`
- **Explanation / Marking Scheme**: ALT stands for Alternate Text (or Alternative Text). It provides descriptive text when graphics fail to render or when screen readers read pages.

#### [ICT_CH05_038] The individual items of the list are marked with ______ tag.
- **Source**: `worksheet_5` | **Topic**: List Items Tag | **Difficulty**: `easy` | **Marks**: 1
- **Acceptable Answer(s)**: `<LI>`
- **Explanation / Marking Scheme**: The <LI> (List Item) tag encapsulates each distinct entry inside ordered (<ol>) or unordered (<ul>) lists.

#### [ICT_CH05_039] An __________ is a type of list that does not have any special order or sequence.
- **Source**: `worksheet_5` | **Topic**: Unordered List Definition | **Difficulty**: `easy` | **Marks**: 1
- **Acceptable Answer(s)**: `unordered list`
- **Explanation / Marking Scheme**: An unordered list (<ul>) presents related items without sequential ordering, utilizing bullet symbols.

#### [ICT_CH05_040] GIF stands for ____________.
- **Source**: `worksheet_5` | **Topic**: GIF Acronym | **Difficulty**: `easy` | **Marks**: 1
- **Acceptable Answer(s)**: `Graphics Interchange Format`
- **Explanation / Marking Scheme**: GIF stands for Graphics Interchange Format. It is an 8-bit image format supporting up to 256 colors, simple transparency, and frame animations.

#### [ICT_CH05_045] The ________ attribute is used to specify the alternate text for an image in HTML.
- **Source**: `test_paper_1` | **Topic**: Image Alternate Text | **Difficulty**: `easy` | **Marks**: 1
- **Acceptable Answer(s)**: `ALT`
- **Explanation / Marking Scheme**: The 'ALT' attribute supplies the fallback text for image elements.

#### [ICT_CH05_060] In an HTML table, each horizontal row is defined using the ________ tag.
- **Source**: `school_blueprint` | **Topic**: Table Row Tag | **Difficulty**: `easy` | **Marks**: 1
- **Acceptable Answer(s)**: `<TR>`
- **Explanation / Marking Scheme**: <TR> stands for 'Table Row' and serves as the container for table header (<TH>) and data (<TD>) cells.

#### [ICT_CH05_061] To merge separate double-line cell borders into a single clean border line, the CSS property ________ is used.
- **Source**: `school_blueprint` | **Topic**: Border Collapse Property | **Difficulty**: `medium` | **Marks**: 1
- **Acceptable Answer(s)**: `border-collapse: collapse`
- **Explanation / Marking Scheme**: 'border-collapse: collapse;' instructs the browser to combine adjacent cell borders into a single unified rule.

#### [ICT_CH05_062] The distance or space between the cell border and the text content inside the cell is known as ________.
- **Source**: `school_blueprint` | **Topic**: Cell Padding Definition | **Difficulty**: `medium` | **Marks**: 1
- **Acceptable Answer(s)**: `cellpadding`
- **Explanation / Marking Scheme**: Cellpadding controls internal padding between a cell's perimeter borders and its internal content.

#### [ICT_CH05_063] The space or distance between adjacent individual cells in a table is called ________.
- **Source**: `school_blueprint` | **Topic**: Cell Spacing Definition | **Difficulty**: `medium` | **Marks**: 1
- **Acceptable Answer(s)**: `cellspacing`
- **Explanation / Marking Scheme**: Cellspacing sets the distance between individual cell boundaries in an HTML table.

### True / False Statements (10 Items)

#### [ICT_CH05_010] An unordered list is a set of related information that does not have any special order or sequence.
- **Source**: `textbook_exercise` | **Topic**: Unordered List Concept | **Difficulty**: `easy` | **Marks**: 1
- **Answer**: `True`
- **Explanation / Marking Scheme**: Unordered lists are engineered precisely for collections of related items where order does not affect meaning, such as grocery items or feature bullet points.

#### [ICT_CH05_011] Use of images in a web page makes it more visually appealing.
- **Source**: `textbook_exercise` | **Topic**: Purpose of Web Images | **Difficulty**: `easy` | **Marks**: 1
- **Answer**: `True`
- **Explanation / Marking Scheme**: Images break up dense blocks of text, capture user interest, illustrate complex concepts, and significantly improve visual design and emotional engagement.

#### [ICT_CH05_012] The type attribute is used to define the symbol for the bullets.
- **Source**: `textbook_exercise` | **Topic**: Bullet Type Attribute | **Difficulty**: `easy` | **Marks**: 1
- **Answer**: `True`
- **Explanation / Marking Scheme**: In an unordered list (<ul type='square'>), the 'type' attribute controls the marker symbol (disc, circle, or square).

#### [ICT_CH05_013] There are 3 tags used to create a definition list.
- **Source**: `textbook_exercise` | **Topic**: Definition List Tags | **Difficulty**: `easy` | **Marks**: 1
- **Answer**: `True`
- **Explanation / Marking Scheme**: A definition list requires three distinct tags: <dl> (delimits the list container), <dt> (specifies the definition term), and <dd> (provides the definition description/data).

#### [ICT_CH05_014] Ordered list cannot be in reverse order.
- **Source**: `textbook_exercise` | **Topic**: Ordered List Reversal | **Difficulty**: `medium` | **Marks**: 1
- **Answer**: `False`
- **Explanation / Marking Scheme**: False. HTML5 introduced the boolean 'reversed' attribute (<ol reversed>). When added to an <ol> tag, the list numbers count backwards in descending order (e.g., 5, 4, 3, 2, 1).

#### [ICT_CH05_046] Ordered list in HTML is used to list the items in a sequence.
- **Source**: `test_paper_1` | **Topic**: Ordered List Sequence | **Difficulty**: `easy` | **Marks**: 1
- **Answer**: `True`
- **Explanation / Marking Scheme**: True. An ordered list (<ol>) automatically assigns ascending numerical or alphabetical markers to enforce sequence.

#### [ICT_CH05_047] BGCOLOR is used to set the background colour of a web page.
- **Source**: `test_paper_1` | **Topic**: Background Color Attribute | **Difficulty**: `easy` | **Marks**: 1
- **Answer**: `True`
- **Explanation / Marking Scheme**: True. When applied to the <body> tag (<body bgcolor='cyan'>), BGCOLOR sets the page canvas background color.

#### [ICT_CH05_064] The <img> tag is an empty (void) tag and does not require a closing </img> tag.
- **Source**: `school_blueprint` | **Topic**: Empty Tag Validation | **Difficulty**: `easy` | **Marks**: 1
- **Answer**: `True`
- **Explanation / Marking Scheme**: True. The <img> tag is an empty element in HTML. It contains only attributes and has no closing counterpart.

#### [ICT_CH05_065] The START attribute in an <OL> tag can accept alphabetical letters such as 'C' if type='A'.
- **Source**: `school_blueprint` | **Topic**: Start Attribute Rule | **Difficulty**: `medium` | **Marks**: 1
- **Answer**: `False`
- **Explanation / Marking Scheme**: False. The 'start' attribute value must ALWAYS be specified as an integer number (e.g., start='3' to start at 'C'). Specifying letters causes syntax errors.

#### [ICT_CH05_066] The <caption> tag must be inserted immediately after the opening <table> tag.
- **Source**: `school_blueprint` | **Topic**: Table Caption Placement | **Difficulty**: `easy` | **Marks**: 1
- **Answer**: `True`
- **Explanation / Marking Scheme**: True. By HTML standard specifications, the <caption> tag must immediately follow the <table> opening tag to correctly label the table.

### Short Answer Conceptual Questions (2-3 Marks) (24 Items)

#### [ICT_CH05_015] What is an ordered list? What does LI mean?
- **Source**: `textbook_exercise` | **Topic**: Ordered List & LI Tag | **Difficulty**: `medium` | **Marks**: 2
- **Model Solution / Answer**:
1. Ordered List: An ordered list (<ol>) is a list of related items arranged in a definite numerical or alphabetical sequence where order matters (such as recipes, rankings, or algorithms).
2. LI Meaning: 'LI' stands for 'List Item'. It is used within both ordered and unordered lists (<li>...</li>) to encapsulate and mark each individual entry.
- **Explanation / Marking Scheme**: Full 2-mark answer: 1 mark for defining ordered list with sequential context; 1 mark for decoding LI as 'List Item' and stating its role.

#### [ICT_CH05_016] Name two situations where you can use definition lists.
- **Source**: `textbook_exercise` | **Topic**: Definition List Situations | **Difficulty**: `medium` | **Marks**: 2
- **Model Solution / Answer**:
Two ideal situations for using definition lists (<dl>) are:
1. Glossary or Dictionary Pages: Pairing technical terms (<dt>) directly with their conceptual definitions (<dd>).
2. Frequently Asked Questions (FAQ) or Product Specifications: Pairing questions or feature labels (<dt>) with detailed answers or technical specs (<dd>).
- **Explanation / Marking Scheme**: Award 1 mark each for two realistic web design scenarios (e.g., glossaries, FAQs, recipe ingredients with measures, or product specification sheets).

#### [ICT_CH05_017] Why do we insert images in a web page?
- **Source**: `textbook_exercise` | **Topic**: Significance of Web Images | **Difficulty**: `easy` | **Marks**: 2
- **Model Solution / Answer**:
We insert images into web pages for several important reasons:
1. Aesthetic & Visual Appeal: Images make websites visually vibrant, modern, and engaging rather than plain and monotone.
2. Cognitive Clarity: Visual illustrations, diagrams, and photos explain complex ideas, products, or steps far more quickly and effectively than text alone.
- **Explanation / Marking Scheme**: Award 1 mark for visual aesthetic enhancement and 1 mark for communication/explanatory value.

#### [ICT_CH05_018] What is the use of ALT attribute with image?
- **Source**: `textbook_exercise` | **Topic**: ALT Attribute Purpose | **Difficulty**: `medium` | **Marks**: 2
- **Model Solution / Answer**:
The ALT (Alternate Text) attribute in the <img> tag serves two primary purposes:
1. Fallback Text: Displays descriptive text in place of the image if the image file fails to load due to a slow internet connection or broken file URL.
2. Accessibility: Read aloud by assistive screen readers to describe the visual content to visually impaired or blind users.
- **Explanation / Marking Scheme**: Award 1 mark for fallback display on load failure and 1 mark for screen reader accessibility.

#### [ICT_CH05_025] Sunidhi has created a web page on plants using images and text, but her page looks cluttered and unprofessional. Can you explain to her how she can represent the text in an organised manner and how to properly resize images?
- **Source**: `textbook_exercise` | **Topic**: Application: Sunidhi's Unprofessional Page | **Difficulty**: `medium` | **Marks**: 3
- **Model Solution / Answer**:
Recommendations for Sunidhi:
1. Organise Text Using Lists: Instead of messy paragraphs, group plant species and care guidelines into Unordered Lists (<ul>) for feature bullets and Ordered Lists (<ol>) for step-by-step watering/fertilizing instructions.
2. Proportional Image Resizing: Her images look distorted or oversized because dimensions are missing. She must add 'width' and 'height' attributes inside the <img> tag (e.g., <img src='rose.jpg' alt='Red Rose' width='300' height='200'>) or use CSS (style='max-width: 100%; height: auto;') to ensure clean, proportional scaling.
3. Add ALT Descriptions: Include descriptive alt text for accessibility and search engine visibility.
- **Explanation / Marking Scheme**: Award 1.5 marks for recommending <ul>/<ol> list structures for organized reading and 1.5 marks for explaining image width/height scaling and alt attributes.

#### [ICT_CH05_026] Supriya has created a web page for her sister's makeover studio. She wants to insert a moving text banner on the web page to announce promotional discount packages. Can you help her in her task by writing the exact HTML tag and code snippet?
- **Source**: `textbook_exercise` | **Topic**: Application: Supriya's Makeover Studio Ticker | **Difficulty**: `medium` | **Marks**: 2
- **Model Solution / Answer**:
Supriya can achieve this moving discount ticker using the <marquee> tag:

Code Snippet:
<marquee behavior='scroll' direction='left' scrollamount='7' bgcolor='#fce7f3' style='color:#be185d; font-weight:bold; font-size:18px;'>
  Special Bridal Package: Get 30% Off on All Advance Bookings This Festive Season!
</marquee>

Explanation: 'behavior=scroll' keeps it looping smoothly, 'direction=left' moves it right-to-left, 'scrollamount=7' gives a moderate reading speed, and 'bgcolor' highlights the strip.
- **Explanation / Marking Scheme**: Award 1 mark for identifying the <marquee> tag and 1 mark for providing the functional snippet with direction, behavior, and bgcolor.

#### [ICT_CH05_027] Synthesize the core differences in tags, attributes, and visual appearances between Unordered Lists (<ul>) and Ordered Lists (<ol>).
- **Source**: `textbook_exercise` | **Topic**: Discussion Time: List Synthesis | **Difficulty**: `medium` | **Marks**: 3
- **Model Solution / Answer**:
Comparative Synthesis:
1. Tags: Unordered lists use <ul>; Ordered lists use <ol>. Both use <li> for list entries.
2. Visual Marker: <ul> displays graphical bullets (disc, circle, square); <ol> displays sequential numbers or letters (1, A, a, I, i).
3. Conceptual Usage: <ul> is used when item sequence does not matter; <ol> is mandatory when chronological or procedural order is critical.
4. Supported Attributes: <ul> supports 'type'; <ol> supports 'type', 'start' (integer offset), and 'reversed' (descending countdown in HTML5).
- **Explanation / Marking Scheme**: Award 1 mark each for markers, tags, usage distinction, and attribute comparisons.

#### [ICT_CH05_033] Define: Unordered list in HTML
- **Source**: `worksheet_5` | **Topic**: Definition: Unordered List | **Difficulty**: `easy` | **Marks**: 2
- **Model Solution / Answer**:
An Unordered List is an HTML list structure (created with the <ul> tag) used to present a collection of related items where sequence or numerical order does not matter. Each item is marked with a bullet symbol (default is 'disc').
- **Explanation / Marking Scheme**: Full marks for stating non-sequential grouping, <ul> tag, and bullet marker display.

#### [ICT_CH05_034] Define: .jpg (or JPEG)
- **Source**: `worksheet_5` | **Topic**: Definition: .jpg format | **Difficulty**: `easy` | **Marks**: 2
- **Model Solution / Answer**:
.jpg (Joint Photographic Experts Group) is a widely used lossy compression graphic file format on the web. It supports 16.7 million colors (24-bit true color) and is exceptionally well-suited for photographic images and real-world scenes.
- **Explanation / Marking Scheme**: Full marks for decoding JPEG, noting 24-bit color depth, and identifying suitability for photographs.

#### [ICT_CH05_035] Define: Src attribute
- **Source**: `worksheet_5` | **Topic**: Definition: Src attribute | **Difficulty**: `easy` | **Marks**: 2
- **Model Solution / Answer**:
'src' (Source) is an essential, mandatory attribute of the <img> tag in HTML. It specifies the uniform resource locator (URL) or local relative directory path from which the browser downloads and displays the image file.
- **Explanation / Marking Scheme**: Full marks for defining 'src' as Source and explaining its role in pointing to the image file location.

#### [ICT_CH05_036] Define: Nested Lists
- **Source**: `worksheet_5` | **Topic**: Definition: Nested Lists | **Difficulty**: `medium` | **Marks**: 2
- **Model Solution / Answer**:
A Nested List is an HTML list placed completely inside an individual list item (<li>) of another list. It creates multi-level outlines, hierarchical sub-categories, or multi-tiered website navigation dropdown menus.
- **Explanation / Marking Scheme**: Full marks for defining list inside list and mentioning hierarchical structuring or sub-categories.

#### [ICT_CH05_041] What is the significance of lists in a web page?
- **Source**: `worksheet_5` | **Topic**: Significance of Lists | **Difficulty**: `medium` | **Marks**: 3
- **Model Solution / Answer**:
Lists play a vital structural and visual role on web pages:
1. Organisation & Readability: They transform cluttered blocks of continuous text into concise, digestible, bulleted points that users can scan effortlessly.
2. Semantic Structure: Search engine web crawlers and assistive technologies (screen readers) use list tags to interpret hierarchies and relationships.
3. Modern Navigation Menus: Industry web navigation headers (navbars) are semantically built using list tags (<ul> and <li>).
- **Explanation / Marking Scheme**: Award 1 mark each for readability/formatting, semantic browser accessibility, and modern navbar implementation.

#### [ICT_CH05_042] Explain the attributes of <OL> tag.
- **Source**: `worksheet_5` | **Topic**: Attributes of OL Tag | **Difficulty**: `medium` | **Marks**: 3
- **Model Solution / Answer**:
The <OL> tag supports three primary attributes:
1. type: Defines the numbering marker ('1' for numbers, 'A' for uppercase letters, 'a' for lowercase letters, 'I' for uppercase Roman, 'i' for lowercase Roman).
2. start: Specifies the integer value from which numbering begins (e.g., start='5' starts at 5, or 'E' if type='A').
3. reversed: A modern boolean attribute that numbers list items in descending reverse order (e.g., 5, 4, 3, 2, 1).
- **Explanation / Marking Scheme**: Award 1 mark each for explaining 'type', 'start', and 'reversed'.

#### [ICT_CH05_043] What are the various CSS list properties?
- **Source**: `worksheet_5` | **Topic**: CSS List Properties | **Difficulty**: `medium` | **Marks**: 3
- **Model Solution / Answer**:
The primary CSS list styling properties are:
1. list-style-type: Specifies the marker type (e.g., disc, circle, square, decimal, lower-alpha, upper-roman, none).
2. list-style-image: Replaces bullet symbols with a custom image file (e.g., url('star.png')).
3. list-style-position: Controls marker alignment relative to the text block ('outside' for hanging indent; 'inside' to flow with the text margin).
4. list-style (Shorthand): Combines type, position, and image into a single line declaration.
- **Explanation / Marking Scheme**: Award 1 mark each for list-style-type, list-style-image, and list-style-position.

#### [ICT_CH05_044] Explain the attributes of the image (<img>) tag.
- **Source**: `worksheet_5` | **Topic**: Attributes of IMG Tag | **Difficulty**: `medium` | **Marks**: 3
- **Model Solution / Answer**:
Key attributes of the <img> tag include:
1. src: Specifies the path or URL of the image file (e.g., src='logo.png').
2. alt: Provides alternate descriptive text if the image fails to render and for accessibility.
3. width & height: Defines dimensions in pixels or percentages (e.g., width='200' height='150').
4. title: Displays a hover tooltip when the user places the cursor over the image.
- **Explanation / Marking Scheme**: Award 1 mark each for src, alt, and width/height dimensions.

#### [ICT_CH05_048] Write a short note on comments in HTML. What is their syntax?
- **Source**: `test_paper_1` | **Topic**: HTML Comments | **Difficulty**: `easy` | **Marks**: 2
- **Model Solution / Answer**:
Comments in HTML are non-executable explanatory notes written into the source code to help developers document program logic. Browsers completely ignore comments when rendering the web page.
Syntax: <!-- This is an HTML comment -->
- **Explanation / Marking Scheme**: Award 1 mark for purpose (developer documentation, ignored by browser) and 1 mark for exact syntax (<!-- ... -->).

#### [ICT_CH05_049] Write a short note on Marquees in HTML.
- **Source**: `test_paper_1` | **Topic**: Marquees in HTML | **Difficulty**: `medium` | **Marks**: 2
- **Model Solution / Answer**:
A marquee in HTML (created with the <marquee> tag) is a scrolling banner of text or images that moves horizontally or vertically across the webpage. It is used to draw immediate attention to announcements, breaking news tickers, and special offers. Key attributes include direction, behavior, and scrollamount.
- **Explanation / Marking Scheme**: Award 1 mark for definition and 1 mark for typical use cases and attributes.

#### [ICT_CH05_050] Define: List in HTML
- **Source**: `test_paper_1` | **Topic**: Define List in HTML | **Difficulty**: `easy` | **Marks**: 2
- **Model Solution / Answer**:
A List in HTML is a structural formatting method used to group related items together in a systematic, easy-to-read manner. HTML supports three main types of lists: Unordered lists (<ul>), Ordered lists (<ol>), and Definition lists (<dl>).
- **Explanation / Marking Scheme**: Award 1 mark for general definition and 1 mark for naming the three core types.

#### [ICT_CH05_051] What is the significance of definition lists?
- **Source**: `test_paper_1` | **Topic**: Significance of Definition Lists | **Difficulty**: `medium` | **Marks**: 2
- **Model Solution / Answer**:
Definition lists (<dl>) are uniquely designed to format paired terms and descriptions without artificial bullet markers or numbers. They automatically indent the description (<dd>) under the term (<dt>), producing clean, professional dictionary, glossary, and FAQ layouts.
- **Explanation / Marking Scheme**: Award 1 mark for term-description pairing without markers and 1 mark for automatic indentation and glossary/FAQ relevance.

#### [ICT_CH05_067] Distinguish between 'colspan' and 'rowspan' attributes with a concise example.
- **Source**: `school_blueprint` | **Topic**: Colspan vs Rowspan | **Difficulty**: `medium` | **Marks**: 2
- **Model Solution / Answer**:
1. colspan: Merges cells horizontally across multiple columns (e.g., <td colspan='2'> spans across 2 columns).
2. rowspan: Merges cells vertically down across multiple rows (e.g., <td rowspan='3'> spans down across 3 rows).
- **Explanation / Marking Scheme**: Award 1 mark for colspan (horizontal column merge) and 1 mark for rowspan (vertical row merge).

#### [ICT_CH05_068] What is the primary technical difference between .jpg and .png image formats on the web?
- **Source**: `school_blueprint` | **Topic**: Image Formats: JPG vs PNG | **Difficulty**: `medium` | **Marks**: 2
- **Model Solution / Answer**:
1. .jpg (JPEG): Uses lossy compression, supporting 16.7M colors; ideal for natural photographs with small file sizes. It does NOT support transparency.
2. .png: Uses lossless compression and supports alpha-channel transparency, allowing transparent backgrounds for logos, icons, and diagrams.
- **Explanation / Marking Scheme**: Award 1 mark for compression type and photographic usage, and 1 mark for transparency capability in PNG.

#### [ICT_CH05_069] Explain the difference between 'inside' and 'outside' values for the CSS list-style-position property.
- **Source**: `school_blueprint` | **Topic**: CSS list-style-position | **Difficulty**: `medium` | **Marks**: 2
- **Model Solution / Answer**:
1. outside (default): The bullet marker is placed outside the principal content block. When a list item wraps to a second line, the text aligns under the first word, not under the bullet.
2. inside: The bullet marker is placed inside the text block. When text wraps to a second line, it indents directly underneath the bullet marker.
- **Explanation / Marking Scheme**: Award 1 mark each for describing marker placement and text wrap alignment for outside and inside.

#### [ICT_CH05_070] Why is the <marquee> tag considered deprecated and discouraged in modern web design? What is the modern replacement?
- **Source**: `school_blueprint` | **Topic**: HTML5 Deprecation of Marquee | **Difficulty**: `medium` | **Marks**: 3
- **Model Solution / Answer**:
1. Deprecation Reasons: The <marquee> tag causes major accessibility problems for users with cognitive or visual impairments, fails Web Content Accessibility Guidelines (WCAG), cannot be easily paused, and distracts readers from absorbing content.
2. Modern Replacement: Modern web developers create smooth, controllable, and responsive scrolling animations using CSS3 animations (@keyframes) and JavaScript.
- **Explanation / Marking Scheme**: Award 2 marks for accessibility and usability issues, and 1 mark for naming CSS @keyframes animations as modern standard.

#### [ICT_CH05_073] Find and correct two syntax errors in the following HTML code snippet:
<ol type="a" start="d">
  <list>Step 1</list>
</ol>
- **Source**: `school_blueprint` | **Topic**: HTML Code Debugging | **Difficulty**: `medium` | **Marks**: 2
- **Model Solution / Answer**:
Errors and Corrections:
1. Error: start="d" is invalid because the 'start' attribute value must ALWAYS be an integer, not a letter.
   Correction: start="4" (since 'd' is the 4th letter).
2. Error: <list> is not a valid HTML tag for list entries.
   Correction: Replace <list> with <li> (List Item).

Corrected Code:
<ol type="a" start="4">
  <li>Step 1</li>
</ol>
- **Explanation / Marking Scheme**: Award 1 mark for correcting start='d' to start='4', and 1 mark for correcting <list> to <li>.

### Long Answer & Multi-Step Practical Drills (4 Marks) (10 Items)

#### [ICT_CH05_019] Explain the definition list and its tags with syntax and an example.
- **Source**: `textbook_exercise` | **Topic**: Definition List Architecture | **Difficulty**: `hard` | **Marks**: 4
- **Model Solution / Answer**:
Definition List Architecture:
A Definition List (<dl>) is used to present terms and their corresponding descriptions in an indented format without bullet markers or numbers.

The Three Component Tags:
1. <dl>...</dl>: Delimits the container for the entire definition list.
2. <dt>...</dt>: (Definition Term) Declares the term or heading being defined. Rendered flush with the left margin.
3. <dd>...</dd>: (Definition Description / Data) Contains the explanation, definition, or data corresponding to the preceding <dt>. Browsers automatically indent <dd> beneath its term.

HTML Code Example:
<dl>
  <dt>HTML</dt>
  <dd>HyperText Markup Language used for structuring web pages.</dd>
  <dt>CSS</dt>
  <dd>Cascading Style Sheets used for styling and designing web layouts.</dd>
</dl>
- **Explanation / Marking Scheme**: Award 1 mark for conceptual definition, 1.5 marks for detailing all 3 tags (<dl>, <dt>, <dd>), and 1.5 marks for a syntactically correct HTML code demonstration.

#### [ICT_CH05_020] What is the purpose of using TYPE and START attributes in an ordered list (<OL>)? Explain with examples.
- **Source**: `textbook_exercise` | **Topic**: OL Attributes: TYPE and START | **Difficulty**: `medium` | **Marks**: 4
- **Model Solution / Answer**:
1. TYPE Attribute:
   • Purpose: Defines the numbering or lettering style for the list items.
   • Supported Values: '1' (Arabic: 1, 2, 3), 'A' (Uppercase alphabet: A, B, C), 'a' (Lowercase alphabet: a, b, c), 'I' (Uppercase Roman: I, II, III), 'i' (Lowercase Roman: i, ii, iii).
   • Default: If omitted, the default is '1'.
   • Example: <ol type='A'> generates A., B., C.

2. START Attribute:
   • Purpose: Specifies the initial numerical starting point for the list sequence.
   • Rule: The value of 'start' must ALWAYS be an integer (Arabic number), even if the 'type' is set to Roman numerals or letters.
   • Example: <ol type='A' start='4'> starts numbering from 'D' (since D is the 4th letter of the alphabet). <ol type='I' start='10'> starts from 'X'.
- **Explanation / Marking Scheme**: Award 2 marks for TYPE attribute (purpose, all 5 options, syntax) and 2 marks for START attribute (purpose, integer rule, code example).

#### [ICT_CH05_021] What are the different types of lists you can create in HTML? Compare their structure and usage.
- **Source**: `textbook_exercise` | **Topic**: Different Types of HTML Lists | **Difficulty**: `hard` | **Marks**: 4
- **Model Solution / Answer**:
HTML supports three core list types plus nested lists:

1. Unordered List (<ul>):
   • Marker: Bullets (disc, circle, square).
   • Usage: Items where chronological or numerical order does not matter (e.g., shopping lists, site navigation menus).
   • Tag: <ul> with <li>.

2. Ordered List (<ol>):
   • Marker: Numbers or letters (1, A, a, I, i).
   • Usage: Sequential instructions, ranking tables, algorithmic steps, recipes.
   • Tag: <ol> with <li>. Supports 'type', 'start', and 'reversed'.

3. Definition List (<dl>):
   • Marker: No bullets or numbers; uses left-aligned terms with indented descriptions.
   • Usage: Dictionaries, glossaries, FAQs, product feature lists.
   • Tags: <dl> container with <dt> (term) and <dd> (description).

4. Nested Lists:
   • Created by embedding a sub-list (either <ul> or <ol>) inside a list item (<li>) of a parent list to display hierarchical outlines.
- **Explanation / Marking Scheme**: Award 1 mark each for complete coverage of Unordered, Ordered, Definition, and Nested lists with tags, markers, and practical usage.

#### [ICT_CH05_022] Explain the <Marquee> tag with its attributes using an example.
- **Source**: `textbook_exercise` | **Topic**: Marquee Tag Deep-Dive | **Difficulty**: `hard` | **Marks**: 4
- **Model Solution / Answer**:
The <marquee> Tag:
The <marquee> tag is used in HTML to create scrolling text, animated tickers, or moving images across a webpage.

Key Attributes:
1. direction: Sets motion direction ('left', 'right', 'up', 'down'). Default is 'left'.
2. behavior: Sets movement type: 'scroll' (loops across and out), 'slide' (moves in and stops at margin), 'alternate' (bounces back and forth).
3. scrollamount: Controls speed (higher number = faster speed, e.g., '10').
4. loop: Controls number of repetitions (e.g., '3' or 'infinite').
5. bgcolor: Sets the background color of the scrolling banner.
6. width & height: Sets dimensions of the marquee display area in pixels or percentage.

Code Example:
<marquee direction='right' behavior='alternate' scrollamount='8' bgcolor='yellow'>
  Special 50% Mid-Term Discount on All Online Courses!
</marquee>
- **Explanation / Marking Scheme**: Award 1 mark for tag definition, 2 marks for explaining 4+ attributes accurately, and 1 mark for functional HTML code demonstration.

#### [ICT_CH05_023] Write the complete HTML code to create a webpage on 'Stress Management' using an ordered list for tips and an unordered list for symptoms.
- **Source**: `textbook_exercise` | **Topic**: Lab Time: Stress Management Webpage | **Difficulty**: `hard` | **Marks**: 4
- **Model Solution / Answer**:
<!DOCTYPE html>
<html>
<head>
  <title>Stress Management</title>
</head>
<body bgcolor='#f0f9ff'>
  <h1 style='color: #0369a1;'>Stress Management Guide</h1>
  <p>Managing stress is vital for physical health and academic success.</p>

  <h2 style='color: #0284c7;'>Common Symptoms of Stress</h2>
  <ul type='square'>
    <li>Frequent headaches and fatigue</li>
    <li>Difficulty concentrating during exams</li>
    <li>Changes in sleep patterns</li>
  </ul>

  <h2 style='color: #0284c7;'>Top 3 Actionable Tips</h2>
  <ol type='1' start='1'>
    <li>Practice deep breathing and 15 minutes of daily meditation.</li>
    <li>Maintain a consistent 8-hour sleep schedule.</li>
    <li>Engage in daily outdoor physical sports or walking.</li>
  </ol>
</body>
</html>
- **Explanation / Marking Scheme**: Award 1 mark for basic document tags (<html>, <head>, <body>), 1.5 marks for correct <ul> with type attribute, and 1.5 marks for correct <ol> with type and start attributes.

#### [ICT_CH05_024] Write the HTML code to create the following webpage:
• Title of the page is 'Indian Mangoes'.
• Font style for the page is Arial.
• Heading of the page is blue.
• Include an image of a mango with alt text, width 250, and a list of famous varieties.
- **Source**: `textbook_exercise` | **Topic**: Lab Time: Indian Mangoes Webpage | **Difficulty**: `hard` | **Marks**: 4
- **Model Solution / Answer**:
<!DOCTYPE html>
<html>
<head>
  <title>Indian Mangoes</title>
</head>
<body style='font-family: Arial, sans-serif;'>
  <h1 style='color: blue;'>Famous Indian Mangoes</h1>
  <img src='mango.jpg' alt='Ripe Alphonso Mango' width='250' height='180'>
  <p>India is the largest producer of delicious mango varieties in the world:</p>
  <ol type='A'>
    <li>Alphonso (Hapus) - Ratnagiri, Maharashtra</li>
    <li>Kesar - Gir, Gujarat</li>
    <li>Dasheri - Malihabad, Uttar Pradesh</li>
    <li>Langra - Varanasi, Uttar Pradesh</li>
  </ol>
</body>
</html>
- **Explanation / Marking Scheme**: Award 1 mark for title and font styling, 1 mark for blue heading, 1 mark for <img> tag with src, alt, and dimensions, and 1 mark for ordered list of mango varieties.

#### [ICT_CH05_052] Write the complete HTML and CSS code to create a table displaying details of friends (Name, Address, Date of Birth) satisfying:
1. Page background color: Cyan
2. Table, th, td border: 1px solid black
3. Border-collapse property applied
4. th and td padding: 10px
5. Font-family: 'Courier New', font-size: 16px
- **Source**: `test_paper_1` | **Topic**: CSS Table Creation Drill | **Difficulty**: `hard` | **Marks**: 4
- **Model Solution / Answer**:
<!DOCTYPE html>
<html>
<head>
  <title>Friends Directory</title>
  <style>
    body {
      background-color: cyan;
      font-family: 'Courier New', monospace;
      font-size: 16px;
    }
    table {
      border-collapse: collapse;
      width: 70%;
      margin: 20px auto;
      background-color: white;
    }
    th, td {
      border: 1px solid black;
      padding: 10px;
      text-align: left;
    }
    th {
      background-color: #e0f2fe;
    }
  </style>
</head>
<body>
  <h2 style='text-align:center;'>My Friends List</h2>
  <table>
    <tr>
      <th>Name</th>
      <th>Address</th>
      <th>Date of Birth</th>
    </tr>
    <tr>
      <td>Pushti</td>
      <td>Green Valley, Ahmedabad</td>
      <td>14-March-2013</td>
    </tr>
    <tr>
      <td>Aarav</td>
      <td>Satellite Road, Ahmedabad</td>
      <td>22-July-2013</td>
    </tr>
  </table>
</body>
</html>
- **Explanation / Marking Scheme**: Award 1 mark for body styling (cyan, Courier New), 1 mark for table CSS (border-collapse, border, 10px padding), 1 mark for semantic table tags (<table>, <tr>, <th>, <td>), and 1 mark for valid friend data rows.

#### [ICT_CH05_071] Write the complete HTML code to generate a 3x3 student exam marksheet table with:
• Table headers: 'Roll No', 'Student Name', 'Marks (out of 100)'
• Border width of 2px
• Two data rows for students Pushti (98) and Aarav (94)
• A caption titled 'Class 7 Mid-Term ICT Examination'
- **Source**: `school_blueprint` | **Topic**: Practical HTML Table Drill | **Difficulty**: `hard` | **Marks**: 4
- **Model Solution / Answer**:
<table border='2' cellpadding='8' cellspacing='0'>
  <caption><b>Class 7 Mid-Term ICT Examination</b></caption>
  <tr bgcolor='#e2e8f0'>
    <th>Roll No</th>
    <th>Student Name</th>
    <th>Marks (out of 100)</th>
  </tr>
  <tr>
    <td align='center'>101</td>
    <td>Pushti</td>
    <td align='center'>98</td>
  </tr>
  <tr>
    <td align='center'>102</td>
    <td>Aarav</td>
    <td align='center'>94</td>
  </tr>
</table>
- **Explanation / Marking Scheme**: Award 1 mark for <table> and <caption>, 1 mark for header row (<tr bgcolor>, <th>), 1 mark for data rows (<td>), and 1 mark for valid syntax and formatting.

#### [ICT_CH05_072] Write the HTML code to create a nested list demonstrating the hierarchy of Computer Hardware and Software:
1. Computer System (Ordered)
   a. Hardware (Unordered sub-list: Input Devices, Output Devices, Storage)
   b. Software (Unordered sub-list: System Software, Application Software)
- **Source**: `school_blueprint` | **Topic**: Hierarchical Nested List Drill | **Difficulty**: `hard` | **Marks**: 4
- **Model Solution / Answer**:
<ol type='1'>
  <li><b>Computer Hardware</b>
    <ul type='square'>
      <li>Input Devices (Keyboard, Mouse, Scanner)</li>
      <li>Output Devices (Monitor, Printer, Speaker)</li>
      <li>Storage Devices (SSD, Hard Disk, Pen Drive)</li>
    </ul>
  </li>
  <li><b>Computer Software</b>
    <ul type='circle'>
      <li>System Software (Operating System, Device Drivers)</li>
      <li>Application Software (MS Excel, Web Browsers, Games)</li>
    </ul>
  </li>
</ol>
- **Explanation / Marking Scheme**: Award 1 mark for outer <ol type='1'>, 1.5 marks for inner <ul> under hardware, and 1.5 marks for inner <ul> under software with proper nesting inside <li> tags.

#### [ICT_CH05_074] Write an HTML document that combines:
1. An animated marquee announcement ticker at the top
2. An image with alternate text and dimensions
3. An ordered list with Roman numerals starting at 5 (V)
4. A definition list for two key computing terms
- **Source**: `school_blueprint` | **Topic**: Comprehensive Multimedia Webpage Drill | **Difficulty**: `hard` | **Marks**: 4
- **Model Solution / Answer**:
<!DOCTYPE html>
<html>
<head>
  <title>ICT Tech Portal</title>
</head>
<body>
  <!-- 1. Scrolling Announcement Ticker -->
  <marquee bgcolor='#dbeafe' scrollamount='6' style='color:#1e40af; font-weight:bold;'>
    Welcome to Class 7 ICT Study Portal - Mid-Term Revision Underway!
  </marquee>

  <!-- 2. Embedded Image -->
  <h2>Computing Innovations</h2>
  <img src='ai_robot.jpg' alt='Humanoid Robot' width='280' height='180'>

  <!-- 3. Ordered List starting at V -->
  <h3>Advanced Units of Study</h3>
  <ol type='I' start='5'>
    <li>Lists and Images in HTML</li>
    <li>Tables and Form Controls</li>
    <li>Introduction to Python Programming</li>
  </ol>

  <!-- 4. Definition List -->
  <h3>Key Definitions</h3>
  <dl>
    <dt><b>Hyperlink</b></dt>
    <dd>A reference or connection point that links one webpage to another document.</dd>
    <dt><b>Semantic Tag</b></dt>
    <dd>An HTML tag that carries meaningful context about its content (such as &lt;nav&gt; or &lt;article&gt;).</dd>
  </dl>
</body>
</html>
- **Explanation / Marking Scheme**: Award 1 mark each for correct implementation of: 1. Marquee, 2. Image with alt and dimensions, 3. Ordered list with type='I' start='5', and 4. Definition list (<dl>, <dt>, <dd>).
