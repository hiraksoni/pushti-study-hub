# CHAPTER KNOWLEDGE BASE: ADVANCED FEATURES OF EXCEL
**Subject**: ICT | **Chapter**: 2 | **Standard**: Class 7 CBSE

## 1. Executive Summary
Mastering Excel formulas, functions (SUM, AVERAGE, COUNT, MAX, MIN), cell referencing (Relative, Absolute, Mixed), charts (Column, Bar, Line, Pie, Doughnut), chart components, sorting data, and filtering rows.

## 2. Core Conceptual Theory & Notes
### [chapter_notes] Formulas & Syntax
Every formula in Excel must begin with an equal sign (=). Operands are values or cell references; operators include +, -, *, /, ^. Order of operations follows PEMDAS / BODMAS.

### [chapter_notes] Types of Cell Referencing
1. Relative: Reference changes automatically when copied (e.g., A1 becomes A2). 2. Absolute: Reference remains fixed with dollar signs (e.g., $A$1). 3. Mixed: One coordinate is fixed, the other relative (e.g., $A1 or A$1).

### [chapter_notes] Excel Functions
Predefined built-in formulas: SUM(range) adds all numbers, AVERAGE(range) calculates mean, MAX(range) finds highest value, MIN(range) finds lowest value, COUNT(range) counts numeric cells.

### [chapter_notes] Charts & Visual Components
Chart Area (entire boundary), Plot Area (region holding data graphics and axes), Data Series (set of related data points), Data Markers (bars, slices, points representing individual values), Legend (key identifying series by colors/patterns), Category Axis (X-axis, horizontal), Value Axis (Y-axis, vertical).

### [chapter_notes] Sorting & Filtering
Sorting arranges data in a specific order (A-Z ascending, Z-A descending, or multi-level via Add Level). Filtering displays only rows that meet defined criteria and temporarily hides non-matching rows without deleting them.

## 3. Tagged Question & Assessment Bank
### Q1. [ict_ch2_tb_mcq1] | Chart Types
* **Source**: `textbook_exercise` | **Type**: `mcq` | **Difficulty**: `easy` | **Marks**: 1M
* **Question**: A ________ chart is used to show changes in values over a period of time.
* **Options**:
  - (a) Bar
  - (b) Column
  - (c) Line
  - (d) Pie
* **Answer**: (c) Line
* **Explanation**: Line charts connect individual data points with continuous lines, making them ideal for displaying trends over regular intervals.

### Q2. [ict_ch2_tb_mcq2] | Proportion Charts
* **Source**: `textbook_exercise` | **Type**: `mcq` | **Difficulty**: `easy` | **Marks**: 1M
* **Question**: Which chart type is best suited to show proportions of a whole?
* **Options**:
  - (a) Pie
  - (b) Line
  - (c) Bar
  - (d) Radar
* **Answer**: (a) Pie
* **Explanation**: A Pie chart displays a single data series divided into slices proportional to each value's contribution to the whole (100%).

### Q3. [ict_ch2_tb_mcq3] | Filtering Concept
* **Source**: `textbook_exercise` | **Type**: `mcq` | **Difficulty**: `easy` | **Marks**: 1M
* **Question**: Which feature in Excel allows you to display only the rows that meet certain criteria?
* **Options**:
  - (a) Sorting
  - (b) Filtering
  - (c) Charting
  - (d) Conditional Formatting
* **Answer**: (b) Filtering
* **Explanation**: Filtering extracts matching records and hides non-matching rows.

### Q4. [ict_ch2_tb_mcq4] | Chart Elements
* **Source**: `textbook_exercise` | **Type**: `mcq` | **Difficulty**: `easy` | **Marks**: 1M
* **Question**: Which chart element identifies the colours or patterns used for each data series?
* **Options**:
  - (a) Gridlines
  - (b) Legend
  - (c) Plot Area
  - (d) Axis Title
* **Answer**: (b) Legend
* **Explanation**: The Legend is the key that pairs colors/patterns with their corresponding data series names.

### Q5. [ict_ch2_tb_fib1] | Axes
* **Source**: `textbook_exercise` | **Type**: `fib` | **Difficulty**: `easy` | **Marks**: 1M
* **Question**: The horizontal axis of a chart is also called the ________ axis.
* **Answer**: category
* **Explanation**: The X-axis displays categories and is called the Category axis. The Y-axis is the Value axis.

### Q6. [ict_ch2_tb_fib2] | Filtering Behavior
* **Source**: `textbook_exercise` | **Type**: `fib` | **Difficulty**: `easy` | **Marks**: 1M
* **Question**: Filtering changes the ________ of rows rather than deleting them.
* **Answer**: visibility
* **Explanation**: Filtered-out rows are merely hidden from view; their data remains intact.

### Q7. [ict_ch2_tb_tf1] | Pie Chart Series
* **Source**: `textbook_exercise` | **Type**: `tf` | **Difficulty**: `medium` | **Marks**: 1M
* **Question**: A pie chart can display multiple data series simultaneously.
* **Answer**: False
* **Explanation**: False. A Pie chart can only display a single data series. To display multiple series as concentric rings, use a Doughnut chart.

### Q8. [ict_ch2_tb_tf2] | Sorting vs Filtering
* **Source**: `textbook_exercise` | **Type**: `tf` | **Difficulty**: `easy` | **Marks**: 1M
* **Question**: Sorting hides rows that do not meet a criterion.
* **Answer**: False
* **Explanation**: False. Sorting rearranges the order of all rows. Filtering hides non-matching rows.

### Q9. [ict_ch2_tb_short1] | Sorting Types
* **Source**: `textbook_exercise` | **Type**: `short_answer` | **Difficulty**: `medium` | **Marks**: 2M
* **Question**: Differentiate between Ascending and Descending sort.
* **Answer**: Ascending sort arranges data from A to Z, smallest to largest (0 to 9), or oldest to newest. Descending sort arranges data from Z to A, largest to smallest, or newest to oldest.
* **Explanation**: Both sort options are located on the Data tab under Sort & Filter.

### Q10. [ict_ch2_tb_short2] | Chart Components
* **Source**: `textbook_exercise` | **Type**: `short_answer` | **Difficulty**: `medium` | **Marks**: 2M
* **Question**: What is the difference between a Data Marker and a Data Label?
* **Answer**: A Data Marker is the physical graphical symbol (bar, column, point, slice) that represents a data value. A Data Label is the text or numeric value displayed directly beside the marker to show its exact numerical reading.
* **Explanation**: Data labels eliminate guessing values against gridlines.

### Q11. [ict_ch2_notes_mcq1] | Cell Referencing
* **Source**: `chapter_notes` | **Type**: `mcq` | **Difficulty**: `medium` | **Marks**: 1M
* **Question**: Which cell reference format indicates an Absolute reference where both column and row remain fixed when copied?
* **Options**:
  - (a) A1
  - (b) $A1
  - (c) A$1
  - (d) $A$1
* **Answer**: (d) $A$1
* **Explanation**: The dollar sign ($) locks the coordinate that immediately follows it. $A$1 locks column A and row 1.

### Q12. [ict_ch2_notes_short1] | Referencing Behavior
* **Source**: `chapter_notes` | **Type**: `short_answer` | **Difficulty**: `hard_hots` | **Marks**: 3M
* **Question**: If formula '=B$2 * 5' in cell C2 is copied to cell C5, what will the formula become?
* **Answer**: '=B$2 * 5'
* **Explanation**: The row coordinate is locked with '$2', so it will not change when copied vertically. The column remains B because copying is within column C (same relative horizontal offset).

### Q13. [ict_ch2_notes_long1] | Main Chart Components
* **Source**: `chapter_notes` | **Type**: `long_answer` | **Difficulty**: `medium` | **Marks**: 4M
* **Question**: Explain the major components of an Excel chart.
* **Answer**: 1. Chart Area: The total area containing the chart and all its elements.
2. Plot Area: The bounded rectangular region where actual data series graphics are drawn.
3. Data Series: The group of related data points plotted.
4. Axes: Category Axis (X, horizontal) and Value Axis (Y, vertical).
5. Legend: Identifier pairing series colors with names.
6. Gridlines: Horizontal/vertical lines aiding visual measurement.
* **Explanation**: All elements can be customized using Chart Tools (Design & Format tabs).

### Q14. [ict_ch2_enrich_mcq1] | Grid Capacity
* **Source**: `researched_enrichment` | **Type**: `mcq` | **Difficulty**: `easy` | **Marks**: 1M
* **Question**: How many total rows does a modern Microsoft Excel worksheet contain?
* **Options**:
  - (a) 65,536
  - (b) 1,048,576
  - (c) 500,000
  - (d) 16,384
* **Answer**: (b) 1,048,576
* **Explanation**: Modern Excel sheets have 1,048,576 rows and 16,384 columns (from column A to XFD), providing over 17 billion cells!

### Q15. [ict_ch2_enrich_short1] | Spreadsheet History
* **Source**: `researched_enrichment` | **Type**: `short_answer` | **Difficulty**: `easy` | **Marks**: 2M
* **Question**: What was the name of the first electronic spreadsheet program, and when was it launched?
* **Answer**: VisiCalc was the first electronic spreadsheet program, released in 1979 for the Apple II computer. It transformed personal computers from hobbyist toys into serious business tools.
* **Explanation**: Invented by Dan Bricklin and Bob Frankston.
