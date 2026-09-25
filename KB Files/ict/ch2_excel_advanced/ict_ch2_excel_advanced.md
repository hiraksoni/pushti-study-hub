# Grade 7 ICT — Chapter 2: Advanced Features of Excel
**Knowledge Base Version**: 2.0-exhaustive | **Total Verified Items**: 74
**Subject**: Information and Communications Technology | **Curriculum**: CBSE / KVS Grade 7

---

## 1. Chapter Executive Summary
Exhaustive Knowledge Base for Grade 7 ICT Chapter 2 covering Charts (Anatomy, Taxonomy, Creation, Formatting, Moving), Data Sorting (Ascending, Descending, Multi-Level), Data Filtering (AutoFilter, Custom Criteria, Removal), Formulas & Cell References, and Spreadsheet History.

### Core Competencies & Learning Outcomes:
- Visual data representation through diverse chart types (Column, Bar, Line, Pie, Doughnut, Area, Scatter, Surface, Radar)
- Chart anatomy mastery (Chart Area, Plot Area, Category Axis X, Value Axis Y, Data Series, Data Marker, Legend, Gridlines)
- Operational chart procedures (Insert tab, Chart Design contextual tab, Moving to New Sheet vs Object In)
- Sequential data sorting (Ascending A-Z, Descending Z-A, Multi-level Sort Dialog Box)
- Targeted data filtering (AutoFilter drop-down arrows, Number/Text filters, temporary visibility vs deletion)
- Formula cell referencing (Relative, Absolute $A$1, Mixed $A1/A$1) and calculation mechanics
- Historical computing context (VisiCalc 1979, modern Excel dimensions 1,048,576 rows × 16,384 columns)

---

## 2. Exhaustive Theoretical Framework

### 1. Graphical Representation & Introduction to Charts

A Chart in Microsoft Excel is a pictorial or graphical representation of data stored in a worksheet. Charts make complex numerical figures immediately understandable, appealing, and easy to analyze by revealing patterns, trends, relationships, and outliers that are otherwise obscured in raw tabular data.

Key Advantages of Charts:
• Visual Impact: Enables rapid comparison across different data series.
• Trend Identification: Easily demonstrates growth, decline, or cyclical patterns over time.
• Decision Making: Summarizes large datasets into actionable management summaries.
• Dynamic Updates: Whenever worksheet cell values change, Excel automatically updates the linked chart.

Instant Keyboard Shortcuts:
• F11: Instantly creates a default Column chart on a brand new dedicated Chart Sheet (named Chart1, Chart2, etc.).
• Alt + F1: Instantly embeds a default chart within the current active worksheet as an embedded object.
• Ctrl + Shift + L: Toggles AutoFilter on/off for the selected data table.

### 2. Complete Anatomy & Components of an Excel Chart

An Excel chart is constructed from several interconnected visual elements:

1. Chart Area: The total overarching region containing the chart and all its peripheral elements (titles, legend, data labels, and plot area).
2. Plot Area: The inner rectangular window bounded by the axes containing the actual graphic markers (bars, columns, lines) and gridlines.
3. Category Axis (X-Axis): The horizontal axis used to display category labels or text headings (e.g., student names, months, product names).
4. Value Axis (Y-Axis): The vertical axis used to measure and plot numerical quantities along a graduated scale.
5. Data Series: A related collection of data points originating from a single row or column of worksheet numbers, plotted in a unique color or pattern.
6. Data Marker: An individual graphical bar, column, slice, point, or symbol physically representing a single data value in the chart.
7. Data Label: An optional text box displaying the exact numerical value, percentage, or category name directly adjacent to a data marker.
8. Legend: A key box identifying the colors, shadings, or symbols assigned to distinguish each data series.
9. Gridlines: Horizontal and vertical reference lines extending across the plot area to facilitate precise visual measurement of values against the axes.
10. Chart Title & Axis Titles: Descriptive headings placed at the top of the chart and alongside axes to identify the dataset and units of measurement.

### 3. Comprehensive Taxonomy of Chart Types

Excel provides diverse chart families, each engineered for specific analytical objectives:

• Column Chart: Uses vertical rectangular bars. Best for comparing individual values across categories over time. Categories on horizontal axis, values on vertical axis.
• Bar Chart: Uses horizontal rectangular bars. Best for comparing discrete categories, especially when category labels are long or numerous. Categories on vertical axis, values on horizontal axis.
• Line Chart: Connects individual data points with continuous lines at equal intervals. Best for tracking continuous trends, fluctuations, and rate of change over time (e.g., monthly sales, stock prices).
• Pie Chart: A circular disk divided into proportional sectors/slices. Shows the contribution of each item to a whole (100%). Rule: Can plot only ONE data series.
• Doughnut Chart: Similar to a pie chart with a hollow center ring. Unlike a pie chart, a doughnut chart can display MULTIPLE concentric data series rings.
• Area Chart: A variation of the line chart where the area beneath the line is filled with solid color or shading. Emphasizes the magnitude of change over time and total volume.
• Scatter (XY) Chart: Plots data points using numerical values along BOTH the X and Y axes. Used in scientific and statistical analysis to display relationships, clusters, and correlations between two numeric variables with uneven intervals.
• Surface Chart: Displays data in a 3D topographic mesh. Useful for finding optimum combinations between two sets of data (like a topographical contour map).
• Radar Chart: Plots data on separate axes radiating outward from a central point, forming a spider-web pattern. Compares the aggregate values of several data series.

### 4. Chart Operations: Insertion, Formatting, Sizing & Relocation

Procedures to build and customize charts in Excel:

1. Inserting a Chart:
   Step a: Select the cell range including row/column headers and numeric data.
   Step b: Click the 'Insert' tab on the Ribbon.
   Step c: In the 'Charts' group, click the desired chart category (Column, Bar, Pie, etc.) and select a 2D or 3D subtype.

2. Contextual Tabs (Chart Tools):
   When a chart is selected, two dynamic contextual tabs appear on the Ribbon:
   • Chart Design: For changing chart type, switching rows/columns, modifying chart layouts/styles, and moving the chart.
   • Format: For formatting chart shapes, text styles, fill colors, outline weights, and alignment.

3. Moving a Chart:
   Step a: Select the chart.
   Step b: On the 'Chart Design' tab, click 'Move Chart' (in the Location group).
   Step c: Choose either 'New sheet' (creates a standalone chart sheet) or 'Object in' (selects an existing worksheet), then click OK.

4. Sizing and Deleting:
   • Sizing: Drag the eight sizing handles on the chart border. Corner handles resize proportionally; side handles adjust width/height.
   • Deleting: Click the chart border to select it, then press the 'Delete' key on the keyboard.

### 5. Sorting Techniques (Ascending, Descending & Multi-Level)

Sorting is the physical rearrangement of worksheet rows into a defined alphabetical, numerical, or chronological sequence without hiding or deleting any records.

Sort Orders:
• Ascending: A to Z (text), 0 to 9 (numbers), Oldest to Newest (dates).
• Descending: Z to A (text), 9 to 0 (numbers), Newest to Oldest (dates).

Single-Column Quick Sort:
1. Click any single cell within the target column.
2. Go to 'Home' tab $\rightarrow$ 'Editing' group $\rightarrow$ click 'Sort & Filter' $\rightarrow$ choose 'Sort A to Z' or 'Sort Z to A'.
(Alternatively: 'Data' tab $\rightarrow$ 'Sort & Filter' group $\rightarrow$ click 'AZ' or 'ZA' button).

Multi-Level (Custom) Sorting:
When multiple records share identical values in the primary column (e.g., students with the same department), secondary sorting is required:
1. Click anywhere inside the data table.
2. On the 'Data' tab, in the 'Sort & Filter' group, click the 'Sort' button to open the Sort Dialog Box.
3. Ensure 'My data has headers' is checked.
4. Under 'Column', select the primary sort field in 'Sort by' (e.g., Department) and choose Order (A to Z).
5. Click 'Add Level' button to insert a secondary sort rule under 'Then by' (e.g., Salary) and choose Order (Largest to Smallest).
6. Click OK to execute.

### 6. Data Filtering (AutoFilter & Custom Criteria)

Filtering is the process of displaying only those worksheet rows that meet specified conditions, while temporarily hiding all non-matching rows from view.

Critical Distinction — Sorting vs. Filtering:
• Sorting: Changes the physical order of rows; ALL rows remain visible.
• Filtering: Retains the original row order; HIDES non-qualifying rows (rows are hidden, NOT deleted).

Applying AutoFilter:
1. Click any cell within the data table.
2. Go to 'Data' tab $\rightarrow$ 'Sort & Filter' group $\rightarrow$ click 'Filter' (or Home tab $\rightarrow$ Sort & Filter $\rightarrow$ Filter).
3. Drop-down filter arrows appear in the header of each column.
4. Click the filter arrow in the desired column:
   • Checkbox Filter: Uncheck '(Select All)' and check specific items.
   • Number Filters: Greater Than, Less Than, Between, Equals, Top 10, Above Average.
   • Text Filters: Begins With, Ends With, Contains, Equals.
5. Click OK. The row numbers turn blue to indicate filtered display.

Clearing / Removing Filter:
• To clear filter from one column: Click the filter funnel icon in that column header $\rightarrow$ click 'Clear Filter From [Column]'.
• To clear all filters: Go to 'Data' tab $\rightarrow$ click 'Clear' button.
• To remove filter arrows entirely: Click the 'Filter' toggle button on the Data tab.

### 7. Advanced Data Management, Cell Referencing & Historical Foundations

Key Architectural Fundamentals of Microsoft Excel:

1. Cell Referencing Formats:
   • Relative Reference (e.g., A1): Both column and row change when the formula is copied to another cell.
   • Absolute Reference (e.g., $A$1): Both column letter and row number are locked with a dollar sign ($); does not change when copied.
   • Mixed Reference (e.g., $A1 or A$1): One coordinate is locked while the other remains relative.
     Example: If formula '=B$2 * 5' in cell C2 is copied vertically down to cell C5, the formula remains '=B$2 * 5' because row 2 is locked.

2. Modern Spreadsheet Capacity (Excel 2007 through Modern 365):
   • Total Rows: 1,048,576 rows (numbered 1 to 1,048,576).
   • Total Columns: 16,384 columns (lettered A to XFD).

3. Historical Milestone:
   • The world's first electronic spreadsheet program was VisiCalc ('Visible Calculator'), invented and released in 1979 for the Apple II computer by Dan Bricklin and Bob Frankston. It revolutionized personal computing by turning personal computers into serious business tools.

---

## 3. Question Bank (74 Standardized Items)

### Multiple Choice Questions (MCQ) (23 Items)

#### [ICT_CH02_001] The rearrangement of data in ascending (A-Z) or descending (Z-A) order is called _______.
- **Source**: `textbook_exercise` | **Topic**: Sorting Techniques | **Difficulty**: `easy` | **Marks**: 1
- **Options**:
  - Filtering
  - Clear Rules
  - Sorting
  - Custom Filter
- **Correct Answer**: `Sorting`
- **Explanation / Marking Scheme**: Sorting is the process of arranging data in a specific order (either ascending or descending) to make it easier to read and analyze.

#### [ICT_CH02_002] To quickly sort a list based on one column, on the Home tab, in the Editing group, click _______.
- **Source**: `textbook_exercise` | **Topic**: Sorting Techniques | **Difficulty**: `easy` | **Marks**: 1
- **Options**:
  - Filter
  - Sort and Filter
  - Sort
  - Review
- **Correct Answer**: `Sort and Filter`
- **Explanation / Marking Scheme**: In Microsoft Excel, the 'Sort and Filter' button is located in the Editing group on the Home tab, providing quick access to Sort A to Z, Sort Z to A, and Custom Sort.

#### [ICT_CH02_003] Which chart displays data in the form of a circle divided into sectors?
- **Source**: `textbook_exercise` | **Topic**: Chart Types Taxonomy | **Difficulty**: `easy` | **Marks**: 1
- **Options**:
  - Line
  - Pie
  - Bar
  - None of these
- **Correct Answer**: `Pie`
- **Explanation / Marking Scheme**: A Pie chart represents data as slices/sectors of a circular pie, where each slice represents the proportional share of a category to the total whole (100%).

#### [ICT_CH02_004] Which feature allows us to arrange the given data according to a specific field in Excel?
- **Source**: `textbook_exercise` | **Topic**: Sorting Techniques | **Difficulty**: `easy` | **Marks**: 1
- **Options**:
  - Data form
  - Sort
  - Filter
  - None of these
- **Correct Answer**: `Sort`
- **Explanation / Marking Scheme**: The Sort feature physically arranges records in an ascending or descending sequence based on the values in a specified field or column.

#### [ICT_CH02_005] Which function key is used to insert a chart in a new chart sheet automatically?
- **Source**: `textbook_exercise` | **Topic**: Introduction to Charts | **Difficulty**: `easy` | **Marks**: 1
- **Options**:
  - F6
  - F8
  - F11
  - F2
- **Correct Answer**: `F11`
- **Explanation / Marking Scheme**: Pressing the F11 function key instantly generates a default column chart on a new, separate chart sheet named Chart1, Chart2, etc.

#### [ICT_CH02_025] A _______ can be defined as a graphical representation of data in a worksheet.
- **Source**: `school_worksheet` | **Topic**: Introduction to Charts | **Difficulty**: `easy` | **Marks**: 1
- **Options**:
  - Chart
  - Filter
  - Table
  - Format
- **Correct Answer**: `Chart`
- **Explanation / Marking Scheme**: A chart is the graphical representation of data in a worksheet that enables quick visual comparison and analysis.

#### [ICT_CH02_026] It refers to the set of data values that are plotted in a chart.
- **Source**: `school_worksheet` | **Topic**: Chart Anatomy & Components | **Difficulty**: `easy` | **Marks**: 1
- **Options**:
  - Category Axis
  - Data series
  - Gridlines
  - Chart Area
- **Correct Answer**: `Data series`
- **Explanation / Marking Scheme**: Data series refers to the set of related data values plotted in a chart, typically drawn from a single row or column.

#### [ICT_CH02_027] A _______ chart is used to show the changes in values over a period of time.
- **Source**: `school_worksheet` | **Topic**: Chart Types Taxonomy | **Difficulty**: `easy` | **Marks**: 1
- **Options**:
  - Pie
  - Line
  - Bar
  - Scatter
- **Correct Answer**: `Line`
- **Explanation / Marking Scheme**: A Line chart connects continuous data points with lines to display trends, rises, and drops over equal time intervals.

#### [ICT_CH02_028] Which of the following chart types allows you to display data across a concentric ring format?
- **Source**: `school_worksheet` | **Topic**: Chart Types Taxonomy | **Difficulty**: `medium` | **Marks**: 1
- **Options**:
  - Radar
  - Pie
  - Doughnut
  - Area
- **Correct Answer**: `Doughnut`
- **Explanation / Marking Scheme**: A Doughnut chart displays data in concentric rings, allowing multiple data series to be compared in proportional slices, unlike a Pie chart which only supports one.

#### [ICT_CH02_035] The rearrangement of data in ascending (A-Z) or descending (Z-A) order in a worksheet is known as:
- **Source**: `exam_trap` | **Topic**: Sorting Techniques | **Difficulty**: `medium` | **Marks**: 1
- **Options**:
  - Filtering
  - Validation
  - Sorting
  - Formatting
- **Correct Answer**: `Sorting`
- **Explanation / Marking Scheme**: Sorting rearranges data in alphabetical, numerical, or chronological order.

#### [ICT_CH02_036] To quickly sort a list based on one column, on the Home tab, in the Editing group, which button is clicked?
- **Source**: `exam_trap` | **Topic**: Sorting Techniques | **Difficulty**: `medium` | **Marks**: 1
- **Options**:
  - Filter
  - Sort & Filter
  - Find & Select
  - Data Analysis
- **Correct Answer**: `Sort & Filter`
- **Explanation / Marking Scheme**: Sort & Filter is the drop-down menu in the Editing group of the Home tab.

#### [ICT_CH02_037] Which chart displays data in the form of a circle divided into sectors proportional to percentages of a whole?
- **Source**: `exam_trap` | **Topic**: Chart Types Taxonomy | **Difficulty**: `medium` | **Marks**: 1
- **Options**:
  - Line Chart
  - Pie Chart
  - Bar Chart
  - Scatter Chart
- **Correct Answer**: `Pie Chart`
- **Explanation / Marking Scheme**: Pie charts display data in circular proportional sectors, representing parts of a whole.

#### [ICT_CH02_038] Which function key is used to instantly create a default column chart on a new chart sheet?
- **Source**: `exam_trap` | **Topic**: Introduction to Charts | **Difficulty**: `medium` | **Marks**: 1
- **Options**:
  - F2
  - F7
  - F11
  - F12
- **Correct Answer**: `F11`
- **Explanation / Marking Scheme**: F11 generates a chart on a new chart sheet; Alt + F1 creates an embedded chart on the current sheet.

#### [ICT_CH02_039] Which of the following chart types allows you to display data across concentric rings for multiple data series?
- **Source**: `exam_trap` | **Topic**: Chart Types Taxonomy | **Difficulty**: `medium` | **Marks**: 1
- **Options**:
  - Radar Chart
  - Doughnut Chart
  - Area Chart
  - Surface Chart
- **Correct Answer**: `Doughnut Chart`
- **Explanation / Marking Scheme**: A Doughnut chart displays data in concentric rings, supporting multiple data series.

#### [ICT_CH02_040] In a standard Column chart, the horizontal axis is called the _______ axis.
- **Source**: `exam_trap` | **Topic**: Chart Anatomy & Components | **Difficulty**: `medium` | **Marks**: 1
- **Options**:
  - Category
  - Value
  - Legend
  - Plot
- **Correct Answer**: `Category`
- **Explanation / Marking Scheme**: The horizontal axis represents category names/labels and is termed the Category Axis (X-axis).

#### [ICT_CH02_041] The box that displays the unique colors, patterns, or symbols assigned to differentiate each data series is called the:
- **Source**: `exam_trap` | **Topic**: Chart Anatomy & Components | **Difficulty**: `medium` | **Marks**: 1
- **Options**:
  - Gridlines
  - Data Marker
  - Legend
  - Plot Box
- **Correct Answer**: `Legend`
- **Explanation / Marking Scheme**: The Legend acts as the chart key identifying each data series.

#### [ICT_CH02_042] Which feature temporarily hides rows that do not meet specified criteria without deleting them?
- **Source**: `exam_trap` | **Topic**: Data Filtering | **Difficulty**: `medium` | **Marks**: 1
- **Options**:
  - Sort
  - AutoFilter
  - Format Painter
  - Conditional Format
- **Correct Answer**: `AutoFilter`
- **Explanation / Marking Scheme**: AutoFilter temporarily hides non-qualifying rows and can be cleared at any time.

#### [ICT_CH02_043] An individual bar, slice, or symbol that visually represents a single data value in a chart is a:
- **Source**: `exam_trap` | **Topic**: Chart Anatomy & Components | **Difficulty**: `medium` | **Marks**: 1
- **Options**:
  - Data Marker
  - Data Series
  - Plot Area
  - Tick Mark
- **Correct Answer**: `Data Marker`
- **Explanation / Marking Scheme**: A Data Marker represents an individual value or point in a chart.

#### [ICT_CH02_044] The complete region containing the chart, all elements, titles, and legends is known as the:
- **Source**: `exam_trap` | **Topic**: Chart Anatomy & Components | **Difficulty**: `medium` | **Marks**: 1
- **Options**:
  - Plot Area
  - Chart Area
  - Worksheet Canvas
  - Grid Region
- **Correct Answer**: `Chart Area`
- **Explanation / Marking Scheme**: The Chart Area is the outer boundary containing all chart elements and the inner plot area.

#### [ICT_CH02_063] Which cell reference format indicates an Absolute reference where both column letter and row number are locked?
- **Source**: `researched_enrichment` | **Topic**: Advanced Data Management | **Difficulty**: `easy` | **Marks**: 1
- **Options**:
  - A1
  - $A1
  - A$1
  - $A$1
- **Correct Answer**: `$A$1`
- **Explanation / Marking Scheme**: In an absolute cell reference, a dollar sign ($) precedes both the column letter and the row number ($A$1), preventing either from changing when copied.

#### [ICT_CH02_066] How many total rows does a standard Microsoft Excel worksheet contain?
- **Source**: `researched_enrichment` | **Topic**: Advanced Data Management | **Difficulty**: `easy` | **Marks**: 1
- **Options**:
  - 65,536
  - 1,048,576
  - 256
  - 16,384
- **Correct Answer**: `1,048,576`
- **Explanation / Marking Scheme**: Since Excel 2007, every worksheet contains exactly 1,048,576 rows (and 16,384 columns ending at XFD).

#### [ICT_CH02_070] Which keyboard shortcut creates an embedded chart directly on the CURRENT worksheet?
- **Source**: `researched_enrichment` | **Topic**: Introduction to Charts | **Difficulty**: `medium` | **Marks**: 1
- **Options**:
  - F11
  - Alt + F1
  - Ctrl + F1
  - Shift + F11
- **Correct Answer**: `Alt + F1`
- **Explanation / Marking Scheme**: Alt + F1 embeds a default chart on the current worksheet, whereas F11 creates a chart on a new dedicated chart sheet.

#### [ICT_CH02_071] Which chart type is specifically designed to plot two groups of numbers as one series of XY coordinates?
- **Source**: `researched_enrichment` | **Topic**: Chart Types Taxonomy | **Difficulty**: `medium` | **Marks**: 1
- **Options**:
  - Line Chart
  - Area Chart
  - Scatter (XY) Chart
  - Surface Chart
- **Correct Answer**: `Scatter (XY) Chart`
- **Explanation / Marking Scheme**: A Scatter (XY) chart plots numeric coordinates along both the X and Y axes, demonstrating correlation and clustering.

### Fill in the Blanks / One-Word Answers (10 Items)

#### [ICT_CH02_029] It can be defined as a graphical representation of data in a worksheet: ________.
- **Source**: `school_worksheet` | **Topic**: Introduction to Charts | **Difficulty**: `easy` | **Marks**: 1
- **Acceptable Answer(s)**: `Chart`
- **Explanation / Marking Scheme**: A Chart is the pictorial representation of numerical worksheet figures.

#### [ICT_CH02_030] This feature is useful when you want to view the data in a specific sequential order: ________.
- **Source**: `school_worksheet` | **Topic**: Sorting Techniques | **Difficulty**: `easy` | **Marks**: 1
- **Acceptable Answer(s)**: `Sorting`
- **Explanation / Marking Scheme**: Sorting rearranges data in ascending or descending order.

#### [ICT_CH02_031] This feature hides unwanted data from the worksheet and shows only records matching criteria: ________.
- **Source**: `school_worksheet` | **Topic**: Data Filtering | **Difficulty**: `easy` | **Marks**: 1
- **Acceptable Answer(s)**: `Filtering`
- **Explanation / Marking Scheme**: Filtering (or AutoFilter) temporarily conceals non-matching rows.

#### [ICT_CH02_032] It contains the chart, axes and gridlines within the inner window: ________.
- **Source**: `school_worksheet` | **Topic**: Chart Anatomy & Components | **Difficulty**: `easy` | **Marks**: 1
- **Acceptable Answer(s)**: `Plot Area`
- **Explanation / Marking Scheme**: The Plot Area is the inner bounding box containing data markers, axes, and gridlines.

#### [ICT_CH02_045] The horizontal axis of a standard column chart is also known as the ________ axis.
- **Source**: `exam_trap` | **Topic**: Chart Anatomy & Components | **Difficulty**: `medium` | **Marks**: 1
- **Acceptable Answer(s)**: `Category Axis`
- **Explanation / Marking Scheme**: The horizontal axis displays category titles and is called the Category Axis (X-axis).

#### [ICT_CH02_046] A Pie chart can display only ________ data series at a time.
- **Source**: `exam_trap` | **Topic**: Chart Types Taxonomy | **Difficulty**: `medium` | **Marks**: 1
- **Acceptable Answer(s)**: `One`
- **Explanation / Marking Scheme**: Pie charts can plot strictly one single data series; for multiple series, a Doughnut chart is used.

#### [ICT_CH02_047] ________ means arranging data in ascending or descending order in Excel.
- **Source**: `exam_trap` | **Topic**: Sorting Techniques | **Difficulty**: `easy` | **Marks**: 1
- **Acceptable Answer(s)**: `Sorting`
- **Explanation / Marking Scheme**: Sorting rearranges data in alphabetical, numerical, or chronological order.

#### [ICT_CH02_048] The ________ area contains the actual chart data markers, axes, and gridlines.
- **Source**: `exam_trap` | **Topic**: Chart Anatomy & Components | **Difficulty**: `medium` | **Marks**: 1
- **Acceptable Answer(s)**: `Plot Area`
- **Explanation / Marking Scheme**: The Plot Area is the inner rectangular region bounded by axes.

#### [ICT_CH02_049] The shortcut function key to instantly insert a chart on a new sheet is ________.
- **Source**: `exam_trap` | **Topic**: Introduction to Charts | **Difficulty**: `easy` | **Marks**: 1
- **Acceptable Answer(s)**: `F11`
- **Explanation / Marking Scheme**: Pressing F11 creates a chart on a new dedicated chart sheet.

#### [ICT_CH02_069] Filtering in Microsoft Excel changes the ________ of rows rather than deleting them from the worksheet.
- **Source**: `researched_enrichment` | **Topic**: Data Filtering | **Difficulty**: `medium` | **Marks**: 1
- **Acceptable Answer(s)**: `Visibility`
- **Explanation / Marking Scheme**: Filtering alters row visibility (hiding non-matches) while keeping all original data intact.

### True / False Statements (12 Items)

#### [ICT_CH02_006] Data series in a chart refers to the bars, slices, or points that show the data values.
- **Source**: `textbook_exercise` | **Topic**: Chart Anatomy & Components | **Difficulty**: `easy` | **Marks**: 1
- **Answer**: `True`
- **Explanation / Marking Scheme**: True. A data series is a collection of related data points (plotted as bars, columns, slices, or dots) that originate from a single row or column of spreadsheet data.

#### [ICT_CH02_007] You can sort data only in ascending order in Microsoft Excel.
- **Source**: `textbook_exercise` | **Topic**: Sorting Techniques | **Difficulty**: `easy` | **Marks**: 1
- **Answer**: `False`
- **Explanation / Marking Scheme**: False. Excel allows sorting in both Ascending (A to Z, smallest to largest) and Descending (Z to A, largest to smallest) orders, as well as Custom Lists.

#### [ICT_CH02_008] Y-axis is the vertical axis that is used to plot the numerical values in a standard Column chart.
- **Source**: `textbook_exercise` | **Topic**: Chart Anatomy & Components | **Difficulty**: `easy` | **Marks**: 1
- **Answer**: `True`
- **Explanation / Marking Scheme**: True. In a standard 2D column chart, the vertical axis is known as the Value Axis or Y-axis, which measures and plots numerical quantities.

#### [ICT_CH02_009] Quick Sort buttons on the Home tab can be used directly to sort data by multiple columns simultaneously.
- **Source**: `textbook_exercise` | **Topic**: Sorting Techniques | **Difficulty**: `medium` | **Marks**: 1
- **Answer**: `False`
- **Explanation / Marking Scheme**: False. The quick sort buttons (Sort A to Z and Sort Z to A) sort by only one column at a time. Sorting by multiple columns requires the Sort Dialog Box ('Add Level').

#### [ICT_CH02_010] AutoFilter permanently hides or deletes the data that does not meet the specified criteria.
- **Source**: `textbook_exercise` | **Topic**: Data Filtering | **Difficulty**: `easy` | **Marks**: 1
- **Answer**: `False`
- **Explanation / Marking Scheme**: False. AutoFilter only temporarily hides non-qualifying rows. No data is deleted, and all records can be restored instantly by clearing the filter.

#### [ICT_CH02_050] You can sort data only in ascending order in Microsoft Excel.
- **Source**: `exam_trap` | **Topic**: Sorting Techniques | **Difficulty**: `easy` | **Marks**: 1
- **Answer**: `False`
- **Explanation / Marking Scheme**: False. Excel supports both ascending and descending sorting, as well as custom list orders.

#### [ICT_CH02_051] AutoFilter permanently deletes rows that do not meet the specified filter criteria.
- **Source**: `exam_trap` | **Topic**: Data Filtering | **Difficulty**: `medium` | **Marks**: 1
- **Answer**: `False`
- **Explanation / Marking Scheme**: False. Rows are only temporarily hidden from display and can be restored anytime by clearing the filter.

#### [ICT_CH02_052] A Bar chart displays comparison of data using horizontal bars.
- **Source**: `exam_trap` | **Topic**: Chart Types Taxonomy | **Difficulty**: `easy` | **Marks**: 1
- **Answer**: `True`
- **Explanation / Marking Scheme**: True. Bar charts plot categories along the vertical axis and draw horizontal bars.

#### [ICT_CH02_053] A Legend helps to identify and differentiate between multiple data series using colors or patterns.
- **Source**: `exam_trap` | **Topic**: Chart Anatomy & Components | **Difficulty**: `easy` | **Marks**: 1
- **Answer**: `True`
- **Explanation / Marking Scheme**: True. The Legend is the key that clarifies what each color/pattern represents.

#### [ICT_CH02_054] The Sort Dialog Box allows sorting data across multiple columns simultaneously using the 'Add Level' feature.
- **Source**: `exam_trap` | **Topic**: Sorting Techniques | **Difficulty**: `medium` | **Marks**: 1
- **Answer**: `True`
- **Explanation / Marking Scheme**: True. The Sort dialog box lets you define primary ('Sort by') and secondary ('Then by') sorting levels.

#### [ICT_CH02_068] A Pie chart can display multiple data series simultaneously in concentric rings.
- **Source**: `researched_enrichment` | **Topic**: Chart Types Taxonomy | **Difficulty**: `easy` | **Marks**: 1
- **Answer**: `False`
- **Explanation / Marking Scheme**: False. A Pie chart is strictly limited to ONE data series. Displaying multiple concentric data series requires a Doughnut chart.

#### [ICT_CH02_072] When data in a worksheet is sorted, formulas referencing those sorted cells update their cell references automatically to preserve mathematical correctness.
- **Source**: `researched_enrichment` | **Topic**: Sorting Techniques | **Difficulty**: `medium` | **Marks**: 1
- **Answer**: `True`
- **Explanation / Marking Scheme**: True. Excel's calculation engine automatically maintains relationship integrity during row reordering.

### Short Answer Conceptual Questions (2-3 Marks) (19 Items)

#### [ICT_CH02_011] Define sorting in Excel and state its primary orders.
- **Source**: `textbook_exercise` | **Topic**: Sorting Techniques | **Difficulty**: `medium` | **Marks**: 2
- **Model Solution / Answer**:
Sorting is the process of arranging worksheet data in a specific sequential order—either ascending (A to Z, 0 to 9) or descending (Z to A, 9 to 0)—so that records can be located, analyzed, and comprehended quickly without hiding any data.
- **Explanation / Marking Scheme**: Award 1 mark for the definition of sorting, and 1 mark for mentioning ascending and descending orders.

#### [ICT_CH02_012] What is a chart? Why is it useful?
- **Source**: `textbook_exercise` | **Topic**: Introduction to Charts | **Difficulty**: `medium` | **Marks**: 2
- **Model Solution / Answer**:
A chart is a pictorial or graphical representation of data in a worksheet. It is useful because it makes large volumes of complex numerical data easy to understand, compare, and analyze, allowing trends, patterns, and relationships to be identified at a glance.
- **Explanation / Marking Scheme**: Award 1 mark for the definition of a chart and 1 mark for explaining its utility (visual comparison, pattern detection).

#### [ICT_CH02_013] How is a Column chart different from a Bar chart?
- **Source**: `textbook_exercise` | **Topic**: Chart Types Taxonomy | **Difficulty**: `medium` | **Marks**: 2
- **Model Solution / Answer**:
1. Column Chart: Displays data using vertical rectangular bars; categories appear on the horizontal X-axis and values on the vertical Y-axis.
2. Bar Chart: Displays data using horizontal rectangular bars; categories appear on the vertical axis and values on the horizontal axis. It is particularly effective when category labels are long.
- **Explanation / Marking Scheme**: Award 1 mark for contrasting bar orientation (vertical vs horizontal) and 1 mark for axis allocation and use cases.

#### [ICT_CH02_014] What is the difference between sorting data and filtering data?
- **Source**: `textbook_exercise` | **Topic**: Data Filtering | **Difficulty**: `medium` | **Marks**: 2
- **Model Solution / Answer**:
• Sorting rearranges the physical sequence of rows based on specific column values, and all rows remain visible.
• Filtering displays only the rows that satisfy specified criteria while temporarily hiding all other non-matching rows without altering their relative order.
- **Explanation / Marking Scheme**: Award 1 mark for sorting (reorders, keeps all visible) and 1 mark for filtering (preserves order, hides non-matches).

#### [ICT_CH02_015] Name and define any two components of a chart.
- **Source**: `textbook_exercise` | **Topic**: Chart Anatomy & Components | **Difficulty**: `medium` | **Marks**: 2
- **Model Solution / Answer**:
Any two of the following:
1. Chart Area: The total region containing the chart and all its elements, including titles, legends, data labels, and plot area.
2. Plot Area: The inner window bounded by the axes where the actual chart data markers and gridlines are plotted.
3. Legend: A key box that displays the unique colors, patterns, or symbols assigned to differentiate each data series.
4. Category Axis (X-axis): The horizontal axis used to represent data categories or labels.
- **Explanation / Marking Scheme**: Award 1 mark for each correctly identified and defined chart component.

#### [ICT_CH02_021] Match the following chart components with their correct descriptions:
(a) Plot area
(b) Data Marker
(c) Gridlines
(d) Data Series
(e) Legend
(f) Chart Area
- **Source**: `textbook_exercise` | **Topic**: Chart Anatomy & Components | **Difficulty**: `medium` | **Marks**: 3
- **Model Solution / Answer**:
Correct Matches:
(a) Plot area $\rightarrow$ Area containing the chart, axes and gridlines
(b) Data Marker $\rightarrow$ Symbol (bar, slice, dot) representing a value in a chart
(c) Gridlines $\rightarrow$ Reference lines measuring and comparing values in a chart
(d) Data Series $\rightarrow$ Collection of bars/values identifying each plotted data series
(e) Legend $\rightarrow$ Box that displays the unique colors, patterns, or symbols assigned to data series
(f) Chart Area $\rightarrow$ Entire area containing the chart and all its elements
- **Explanation / Marking Scheme**: Award 0.5 marks for each correct match (6 items × 0.5 = 3 marks).

#### [ICT_CH02_023] Application Q1 (Textbook p. 38): Radha has created a worksheet containing information about her bakery items, prices and monthly sales. She wants to see the sales in a chart. Help her accomplish this task.
- **Source**: `textbook_exercise` | **Topic**: Chart Types Taxonomy | **Difficulty**: `medium` | **Marks**: 2
- **Model Solution / Answer**:
Advice for Radha:
1. Select the cell range containing bakery item names and monthly sales figures.
2. Click on the 'Insert' tab on the Ribbon.
3. In the 'Charts' group, select a 'Column Chart' or 'Bar Chart' to visually compare sales across items, or select a 'Line Chart' if she wants to observe monthly sales trends.
4. Alternatively, she can simply press the 'F11' key to instantly create a default chart on a new sheet.
- **Explanation / Marking Scheme**: Award 1 mark for data selection and navigating to Insert > Charts group, and 1 mark for recommending Column/Bar/Line chart.

#### [ICT_CH02_024] Application Q2 (Textbook p. 38): Shubham has created a worksheet of his tuition students containing marks in 5 subjects. He wants to check the result of students in ascending order of their total marks. How can he achieve this?
- **Source**: `textbook_exercise` | **Topic**: Sorting Techniques | **Difficulty**: `medium` | **Marks**: 2
- **Model Solution / Answer**:
Advice for Shubham:
1. Click on any cell within the 'Total Marks' column.
2. Go to the 'Home' tab on the Ribbon.
3. In the 'Editing' group, click on the 'Sort & Filter' button.
4. Select 'Sort Smallest to Largest' (Ascending order). The student records will immediately reorder with the lowest marks at the top and highest at the bottom.
- **Explanation / Marking Scheme**: Award 1 mark for column cell selection and 1 mark for navigating to Sort & Filter > Sort Smallest to Largest.

#### [ICT_CH02_034] What do you understand by sorting? Explain with an example (Worksheet 2 Section D).
- **Source**: `school_worksheet` | **Topic**: Sorting Techniques | **Difficulty**: `medium` | **Marks**: 3
- **Model Solution / Answer**:
Sorting is the process of arranging data in a specific order, either ascending or descending, to facilitate faster reading and analysis.

Example: Suppose an unsorted list contains student test marks: 45, 12, 89, 34, 67.
• Ascending Sort (Smallest to Largest): 12, 34, 45, 67, 89.
• Descending Sort (Largest to Smallest): 89, 67, 45, 34, 12.
Sorting preserves all records without hiding or deleting any information.
- **Explanation / Marking Scheme**: Award 1.5 marks for definition and 1.5 marks for a clear practical ascending/descending example.

#### [ICT_CH02_055] Define sorting and state its two primary orders with examples.
- **Source**: `exam_trap` | **Topic**: Sorting Techniques | **Difficulty**: `medium` | **Marks**: 2
- **Model Solution / Answer**:
Sorting is arranging data in a specific sequential order:
1. Ascending Order: Smallest to largest (e.g., 10, 20, 30) or alphabetical A to Z.
2. Descending Order: Largest to smallest (e.g., 30, 20, 10) or reverse alphabetical Z to A.
- **Explanation / Marking Scheme**: Award 1 mark for definition and 1 mark for distinguishing ascending and descending orders with examples.

#### [ICT_CH02_056] What is a chart? Why is it preferred over raw tabular figures?
- **Source**: `exam_trap` | **Topic**: Introduction to Charts | **Difficulty**: `medium` | **Marks**: 2
- **Model Solution / Answer**:
A chart is a visual or pictorial representation of worksheet data. It is preferred over raw figures because human cognition processes visual shapes and colors much faster than dense rows of text, allowing patterns, comparisons, and outliers to be recognized instantly.
- **Explanation / Marking Scheme**: Award 1 mark for chart definition and 1 mark for pedagogical cognitive rationale.

#### [ICT_CH02_057] How is a Column chart different from a Bar chart? When is a Bar chart preferred?
- **Source**: `exam_trap` | **Topic**: Chart Types Taxonomy | **Difficulty**: `medium` | **Marks**: 2
- **Model Solution / Answer**:
• Orientation: Column charts use vertical bars, while Bar charts use horizontal bars.
• Axis Position: In a column chart, categories are on the horizontal X-axis; in a bar chart, categories are on the vertical axis.
• Preference: A Bar chart is preferred when category names are long or numerous, preventing label overlap.
- **Explanation / Marking Scheme**: Award 1 mark for structural difference and 1 mark for explaining when Bar charts are preferred.

#### [ICT_CH02_058] Differentiate between sorting data and filtering data with respect to row visibility and order.
- **Source**: `exam_trap` | **Topic**: Data Filtering | **Difficulty**: `medium` | **Marks**: 2
- **Model Solution / Answer**:
1. Sorting: Rearranges the sequence of rows in ascending or descending order. All original rows remain visible.
2. Filtering: Preserves the existing row order but temporarily conceals (hides) rows that do not satisfy the filter conditions.
- **Explanation / Marking Scheme**: Award 1 mark for sorting mechanics and 1 mark for filtering visibility behavior.

#### [ICT_CH02_059] Name and define any two components of a chart.
- **Source**: `exam_trap` | **Topic**: Chart Anatomy & Components | **Difficulty**: `medium` | **Marks**: 2
- **Model Solution / Answer**:
1. Category Axis (X-axis): The horizontal baseline used to display textual labels or categories.
2. Value Axis (Y-axis): The vertical baseline used to plot and measure numerical quantities.
(Alternatively: Legend, Chart Area, Plot Area, Data Marker).
- **Explanation / Marking Scheme**: Award 1 mark each for two correctly named and defined components.

#### [ICT_CH02_060] What is the difference between the Chart Area and the Plot Area in Excel?
- **Source**: `exam_trap` | **Topic**: Chart Anatomy & Components | **Difficulty**: `medium` | **Marks**: 2
- **Model Solution / Answer**:
• Chart Area: The entire boundary that includes the chart graphic, chart title, axis titles, legend, and data labels.
• Plot Area: The inner rectangular window bounded by the X and Y axes where the actual data markers and gridlines are plotted.
- **Explanation / Marking Scheme**: Award 1 mark for Chart Area boundary and 1 mark for Plot Area interior.

#### [ICT_CH02_064] If the formula '=B$2 * 5' in cell C2 is copied down to cell C5, what will the formula become in cell C5? Explain why.
- **Source**: `researched_enrichment` | **Topic**: Advanced Data Management | **Difficulty**: `hard_hots` | **Marks**: 2
- **Model Solution / Answer**:
The formula in cell C5 will be '=B$2 * 5'.

Explanation: The formula uses a mixed reference where row 2 is locked with an absolute anchor ('$2') while the column is relative ('B'). Since the formula was copied vertically down within the same column (from C2 to C5), the column does not change, and the locked row 2 cannot change.
- **Explanation / Marking Scheme**: Award 1 mark for the correct resulting formula and 1 mark for explaining absolute row anchoring.

#### [ICT_CH02_065] What is the difference between a Data Marker and a Data Label in an Excel chart?
- **Source**: `researched_enrichment` | **Topic**: Chart Anatomy & Components | **Difficulty**: `medium` | **Marks**: 2
- **Model Solution / Answer**:
• Data Marker: The actual physical graphical element—such as a vertical bar, horizontal column, pie slice, or line dot—that represents a specific data value in the plot area.
• Data Label: The text or numeric label placed directly on or beside a data marker that displays its exact numeric value, percentage, or category name.
- **Explanation / Marking Scheme**: Award 1 mark for defining Data Marker and 1 mark for defining Data Label.

#### [ICT_CH02_067] What was the name of the world's first electronic spreadsheet program, and who were its creators?
- **Source**: `researched_enrichment` | **Topic**: Advanced Data Management | **Difficulty**: `medium` | **Marks**: 2
- **Model Solution / Answer**:
The world's first electronic spreadsheet was VisiCalc ('Visible Calculator'), created in 1979 by Dan Bricklin and Bob Frankston for the Apple II computer.
- **Explanation / Marking Scheme**: Award 1 mark for naming VisiCalc and 1979, and 1 mark for creators Dan Bricklin and Bob Frankston.

#### [ICT_CH02_073] Explain the difference between a Doughnut Chart and a Pie Chart with regard to data series capability.
- **Source**: `researched_enrichment` | **Topic**: Chart Types Taxonomy | **Difficulty**: `medium` | **Marks**: 2
- **Model Solution / Answer**:
• Pie Chart: Represents data as proportional slices of a circle and can plot ONLY ONE data series at a time.
• Doughnut Chart: Contains a hollow central hole and can display MULTIPLE data series simultaneously, with each data series appearing as a separate concentric circular ring.
- **Explanation / Marking Scheme**: Award 1 mark for single series limitation of Pie charts and 1 mark for concentric multi-series capability of Doughnut charts.

### Long Answer & Multi-Step Practical Drills (4 Marks) (10 Items)

#### [ICT_CH02_016] Explain any four common types of charts available in Microsoft Excel.
- **Source**: `textbook_exercise` | **Topic**: Chart Types Taxonomy | **Difficulty**: `hard_hots` | **Marks**: 4
- **Model Solution / Answer**:
1. Column Chart: Uses vertical bars to compare data categories over time; ideal for showing changes in values across distinct groups.
2. Bar Chart: Uses horizontal bars to compare discrete items; especially effective for displaying data when category labels are lengthy.
3. Line Chart: Connects individual data points with continuous lines at equal intervals; ideal for showing continuous trends and patterns over time (e.g., temperature changes, sales growth).
4. Pie Chart: A circular chart divided into proportional slices; shows the relationship of parts to a whole (percentages of 100%). It can plot only one data series.
- **Explanation / Marking Scheme**: Award 1 mark for each correctly explained chart type with its structure and specific analytical purpose.

#### [ICT_CH02_017] Explain the major elements/components of a chart in Microsoft Excel.
- **Source**: `textbook_exercise` | **Topic**: Chart Anatomy & Components | **Difficulty**: `hard_hots` | **Marks**: 4
- **Model Solution / Answer**:
Major elements of an Excel chart include:
1. Chart Area: The entire boundary containing the chart and all its components (titles, labels, legend, plot area).
2. Plot Area: The interior area bounded by the axes where the actual data series and gridlines reside.
3. Category Axis (X-Axis): The horizontal reference line representing the categories or textual labels of data being plotted.
4. Value Axis (Y-Axis): The vertical reference line measuring and plotting the numerical values.
5. Data Series: The collection of related values plotted in a chart (e.g., all bars of the same color).
6. Data Marker: An individual bar, slice, point, or symbol representing a specific numerical value.
7. Legend: A color-coded key identifying the dataset assigned to each data series.
8. Gridlines: Horizontal and vertical reference lines that facilitate accurate reading of values.
- **Explanation / Marking Scheme**: Award 0.5 to 1 mark per well-defined element up to a total of 4 marks.

#### [ICT_CH02_018] Explain the step-by-step procedure to move a chart to another location in Excel.
- **Source**: `textbook_exercise` | **Topic**: Chart Operations | **Difficulty**: `hard_hots` | **Marks**: 4
- **Model Solution / Answer**:
Steps to move a chart to another location:
1. Click on the chart border to select it. Contextual tabs ('Chart Design' and 'Format') will appear on the Ribbon.
2. Click on the 'Chart Design' tab.
3. In the 'Location' group at the far right of the ribbon, click the 'Move Chart' button.
4. In the Move Chart dialog box, choose one of two options:
   • 'New sheet': Type a name to place the chart on a brand new full-page chart sheet.
   • 'Object in': Click the drop-down list to select an existing worksheet in the workbook.
5. Click 'OK'. The chart will immediately move to the selected destination.
- **Explanation / Marking Scheme**: Award 1 mark each for selection, accessing Chart Design tab, clicking Move Chart, and explaining the two dialog destinations.

#### [ICT_CH02_019] Write the complete steps to apply multi-level custom sorting on a worksheet.
- **Source**: `textbook_exercise` | **Topic**: Sorting Techniques | **Difficulty**: `hard_hots` | **Marks**: 4
- **Model Solution / Answer**:
Steps to apply multi-level custom sorting:
1. Click any cell within the data table to be sorted.
2. Navigate to the 'Data' tab on the Ribbon, and in the 'Sort & Filter' group, click the 'Sort' button (or Home tab $\rightarrow$ Editing $\rightarrow$ Sort & Filter $\rightarrow$ Custom Sort).
3. In the Sort dialog box, ensure the 'My data has headers' checkbox is selected.
4. In the first row, select the primary field from the 'Sort by' drop-down list (e.g., Department) and choose the Order (e.g., A to Z).
5. Click the 'Add Level' button to insert a secondary sort rule.
6. In the new 'Then by' row, select the secondary field (e.g., Salary) and select its Sort Order (e.g., Largest to Smallest).
7. Click 'OK' to execute the multi-level sort.
- **Explanation / Marking Scheme**: Award 1 mark each for table selection, opening Sort dialog, setting primary level, adding level, and finalizing with OK.

#### [ICT_CH02_020] How can filters once applied to a worksheet be cleared or completely removed?
- **Source**: `textbook_exercise` | **Topic**: Data Filtering | **Difficulty**: `hard_hots` | **Marks**: 4
- **Model Solution / Answer**:
Filters in Excel can be cleared or removed using the following methods:

1. Clearing a Filter from a Single Column:
   • Click the Filter Funnel icon in the header of the filtered column.
   • Select 'Clear Filter From [Column Name]' from the drop-down menu. Only that column's filter is removed.

2. Clearing All Filters in the Worksheet Simultaneously:
   • Go to the 'Data' tab on the Ribbon.
   • In the 'Sort & Filter' group, click the 'Clear' button. All rows will reappear while filter drop-down arrows remain in the headers.

3. Completely Removing Filters and Drop-Down Arrows:
   • Click any cell inside the data range.
   • Go to the 'Data' tab $\rightarrow$ 'Sort & Filter' group $\rightarrow$ click the 'Filter' toggle button (or press Ctrl + Shift + L). The drop-down arrows disappear and all hidden records are permanently unhidden.
- **Explanation / Marking Scheme**: Award 1.5 marks for clearing a single column filter, 1.5 marks for clearing all filters, and 1 mark for removing the filter tool entirely.

#### [ICT_CH02_022] Lab Activity B (Textbook p. 39): Create an Excel Sheet containing the following marksheet data:
Roll No 1: Amrita Singh (Math: 45, Eng: 46, Science: 39)
Roll No 2: Fatima Begam (Math: 44, Eng: 35, Science: 38)
Roll No 3: Jack D'souza (Math: 38, Eng: 39, Science: 32)
Roll No 4: Gautam Sethi (Math: 39, Eng: 41, Science: 34)
Roll No 5: Hemant Rao (Math: 36, Eng: 37, Science: 48)
Roll No 6: Ishaan Verma (Math: 43, Eng: 40, Science: 42)

State the precise steps to:
(a) Sort the worksheet in ascending order of Science marks.
(b) Filter records to display only students scoring more than 40 in Mathematics.
- **Source**: `textbook_exercise` | **Topic**: Sorting & Filtering Drills | **Difficulty**: `hard_hots` | **Marks**: 4
- **Model Solution / Answer**:
Solution Steps:
(a) Ascending Sort by Science Marks:
1. Click any cell within the 'Science' column (e.g., column E).
2. Go to 'Home' tab $\rightarrow$ 'Editing' group $\rightarrow$ click 'Sort & Filter' $\rightarrow$ select 'Sort Smallest to Largest'.
Reordered list: Jack (32), Gautam (34), Fatima (38), Amrita (39), Ishaan (42), Hemant (48).

(b) Filter Mathematics > 40:
1. Click inside the table and go to 'Data' tab $\rightarrow$ click 'Filter' (filter drop-down arrows appear).
2. Click the filter arrow in the 'Math' header $\rightarrow$ hover over 'Number Filters' $\rightarrow$ select 'Greater Than...'.
3. In the dialog box, type 40 and click OK.
Visible filtered records: Amrita Singh (45), Fatima Begam (44), Ishaan Verma (43).
- **Explanation / Marking Scheme**: Award 2 marks for part (a) sort steps and 2 marks for part (b) number filter steps.

#### [ICT_CH02_033] Write a short note on different types of charts available in Microsoft Excel (Worksheet 2 Section C).
- **Source**: `school_worksheet` | **Topic**: Chart Types Taxonomy | **Difficulty**: `hard_hots` | **Marks**: 3
- **Model Solution / Answer**:
Different types of charts in Excel include:
1. Column Chart: Displays data using vertical bars; best for comparing items across categories over time.
2. Bar Chart: Uses horizontal bars; excellent for displaying comparisons between individual items when category names are long.
3. Line Chart: Connects data points with lines; best for showing trends and continuous changes at regular intervals.
4. Pie Chart: A circular chart divided into slices representing proportional shares of a whole (limited to 1 data series).
5. Doughnut Chart: Similar to a pie chart but contains a hollow center and can represent multiple data series.
- **Explanation / Marking Scheme**: Award 0.5 to 1 mark for each correctly described chart type with its distinguishing structure.

#### [ICT_CH02_061] Explain four common types of charts available in Excel and state suitable scenarios for each.
- **Source**: `exam_trap` | **Topic**: Chart Types Taxonomy | **Difficulty**: `hard_hots` | **Marks**: 4
- **Model Solution / Answer**:
1. Column Chart:
   • Structure: Vertical bars.
   • Scenario: Comparing quarterly sales across different product departments.

2. Bar Chart:
   • Structure: Horizontal bars.
   • Scenario: Comparing candidate votes where candidate names or constituencies are long.

3. Line Chart:
   • Structure: Data points connected by continuous lines.
   • Scenario: Tracking patient body temperature fluctuations every hour in a hospital.

4. Pie Chart:
   • Structure: Circular disk divided into percentage slices.
   • Scenario: Showing the proportion of household monthly budget spent on rent, food, and education.
- **Explanation / Marking Scheme**: Award 1 mark for each chart type and its matching real-world scenario.

#### [ICT_CH02_062] (a) Write the steps to apply Custom Multi-Level Sorting on a worksheet.
(b) Write the steps to apply and remove AutoFilter in Excel.
- **Source**: `exam_trap` | **Topic**: Sorting & Filtering Drills | **Difficulty**: `hard_hots` | **Marks**: 4
- **Model Solution / Answer**:
(a) Custom Multi-Level Sorting Steps:
1. Click inside the data table.
2. Go to Data tab $\rightarrow$ Sort & Filter group $\rightarrow$ click 'Sort'.
3. In the Sort dialog, ensure 'My data has headers' is checked.
4. Select the primary sort column in 'Sort by' (e.g., Section) and choose Order.
5. Click 'Add Level', choose the secondary column in 'Then by' (e.g., Percentage), and choose Order.
6. Click OK.

(b) Applying and Removing AutoFilter Steps:
1. Applying: Click any cell in the table $\rightarrow$ Data tab $\rightarrow$ click 'Filter' (drop-down arrows appear).
2. Filtering: Click any header arrow $\rightarrow$ select required values $\rightarrow$ click OK.
3. Removing: Click 'Clear' on the Data tab to unhide rows, or click the 'Filter' button again to remove arrows.
- **Explanation / Marking Scheme**: Award 2 marks for part (a) multi-level sorting steps and 2 marks for part (b) filter application and removal.

#### [ICT_CH02_074] Case Study: The school sports committee has recorded 150 participant scores across House, Grade, and 100m Sprint Time (seconds).
Explain how the committee can utilize Excel's advanced data features to:
(a) Identify the top 3 fastest sprinters in Grade 7.
(b) Group all participants by House in alphabetical order, and within each House, rank them from fastest to slowest sprint time.
- **Source**: `researched_enrichment` | **Topic**: Sorting & Filtering Drills | **Difficulty**: `hard_hots` | **Marks**: 4
- **Model Solution / Answer**:
Workflow for Sports Committee:

(a) Finding Top 3 Fastest Sprinters in Grade 7:
1. Apply AutoFilter ('Data' tab $\rightarrow$ 'Filter').
2. Click the 'Grade' column filter arrow, uncheck '(Select All)' and check 'Grade 7'.
3. Click the 'Sprint Time' column filter arrow $\rightarrow$ 'Number Filters' $\rightarrow$ 'Top 10...'.
4. In the dialog box, change 'Top' to 'Bottom' (since a lower sprint time is faster) and enter '3' Items.
5. Click OK. The 3 fastest Grade 7 sprinters are displayed.

(b) Grouping by House & Ranking by Speed:
1. Select the sports dataset and click 'Sort' on the 'Data' tab.
2. Under 'Sort by', choose 'House' with Order 'A to Z' (groups houses alphabetically: Blue, Green, Red, Yellow).
3. Click 'Add Level' button to insert a secondary sort rule.
4. Under 'Then by', select 'Sprint Time' with Order 'Smallest to Largest' (fastest time first).
5. Click OK. The table is neatly clustered by House with internal sprint rankings.
- **Explanation / Marking Scheme**: Award 2 marks for part (a) filtering/Top 10 bottom logic, and 2 marks for part (b) multi-level sorting setup.
