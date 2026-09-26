/**
 * Pushti Study Hub - Concept Mastery Checklist (Part I) Tab Engine
 *
 * Injects a small "Checklist" tab into the chapter dock rail (alongside the
 * existing Concept Pillars / Practice / Audit Log style tabs) for Mathematics
 * chapters 1-8. Content is transcribed from the printed "Class 7 Mathematics -
 * Part I Concept Mastery Checklist" (Ganita Prakash Part I) revision audit.
 *
 * Features:
 *   - Per-item tick boxes persisted in localStorage
 *   - Topic names are clickable deep links into the chapter's own sections
 *     (unresolvable topics render as plain text for later notes)
 *   - Chapter confidence (Secure / Mostly secure / Needs more practice)
 *     + Priority topics field, both persisted
 *   - Live mastery progress in the dock rail badge and pane banner
 *   - Reset + Print (checklist-only) actions
 */

(function () {
    'use strict';

    /* ===================================================================== */
    /* 1. CHECKLIST DATA — Ganita Prakash Part I, Chapters 1-8               */
    /* ===================================================================== */
    /* item = [ text, query? ]                                               */
    /*   query omitted      -> inherits the section query                    */
    /*   query = string     -> exact deep-link target (heading substring)    */
    /*   query = [..]       -> first heading matching any entry              */
    /*   query = false      -> no link (topic pending notes)                 */

    var CHECKLISTS = {
        math_ch1: {
            title: 'Large Numbers Around Us',
            sections: [
                {
                    name: 'Large numbers and place value',
                    q: 'Numeration Systems & Powers of 10',
                    items: [
                        ['I can explain the size of a thousand, lakh, crore and larger quantities using familiar examples.', 'How Large Numbers are Built'],
                        ['I can read and write large numbers correctly in the Indian place value system and place commas in the correct positions.', 'The Indian System of Numeration'],
                        ['I can identify the place value and face value of any digit in a large number.', ['Place Value of a Digit', 'Face Value of a Digit']],
                        ['I can write a large number in expanded form and rebuild a numeral from its place-value parts.'],
                        ['I can compare and order large numbers using place value and the symbols <, > and =.', 'Comparing Numbers, Ascending']
                    ]
                },
                {
                    name: 'Indian and International naming systems',
                    q: 'Universal Bridge Table: Indian vs. International',
                    items: [
                        ['I can use lakh and crore correctly and relate them to thousands and powers of ten.', 'The Indian System of Numeration'],
                        ['I can read and write numbers using million and billion in the International system.', 'The International System of Numeration'],
                        ['I can translate simple quantities between the Indian and International systems (for example, lakhs/crores and millions/billions).'],
                        ['I understand the different comma-grouping patterns used in the two systems.', 'The Indian System of Numeration']
                    ]
                },
                {
                    name: 'Approximation and estimation',
                    q: 'Exact vs. Approximate Values & Nearest Neighbours',
                    items: [
                        ['I can distinguish between an exact value and an approximate value, and explain when each is appropriate.', 'Exact Values'],
                        ['I can round large numbers sensibly to a nearby thousand, lakh or crore.', 'The Nearest Neighbours Rounding Rules'],
                        ['I can decide when rounding up, rounding down or rounding to the nearest value makes sense in a real situation.', 'High-Yield Multi-Place Rounding'],
                        ['I can estimate large sums and differences and judge whether an exact answer is reasonable.', 'The General Rule of Estimation']
                    ]
                },
                {
                    name: 'Patterns, products and problem solving',
                    q: 'Product Digit Count Theorems, Palindromic Patterns',
                    items: [
                        ['I can use patterns when multiplying or dividing by 10, 100, 1000 and other powers of ten.', 'Metric System Powers of 10 Scale'],
                        ['I can use convenient factors such as 5, 25, 50, 125 and 250 to calculate some products efficiently.', 'Mental Multiplication Shortcuts'],
                        ['I can reason about the possible number of digits in a product without trying every multiplication.', 'The Fundamental Product Digit Count Theorem'],
                        ['I can break a very large calculation into manageable stages and keep track of units.'],
                        ['I can make reasonable assumptions and use estimation to answer real-life questions involving very large quantities.', 'Real-Life Large Numbers in Daily Life'],
                        ['I can interpret a large number in context rather than treating it as only a string of digits.', 'Real-Life Large Numbers in Daily Life']
                    ]
                }
            ]
        },

        math_ch2: {
            title: 'Arithmetic Expressions',
            sections: [
                {
                    name: 'Understanding expressions',
                    q: 'Core Concept 1: Expressions vs Equations',
                    items: [
                        ['I can explain what an arithmetic expression is and distinguish an expression from its value.'],
                        ['I can read expressions aloud using words such as sum, difference, product, quotient and times.'],
                        ['I can write an arithmetic expression to represent a verbal statement or a real-life situation.', 'Expression Formation & Real-Life Modeling'],
                        ['I can recognise that different expressions may have the same value.', 'Algebraic Laws of Arithmetic'],
                        ['I can compare two expressions using =, < or >, sometimes by reasoning without fully evaluating them.', 'Algebraic Laws of Arithmetic']
                    ]
                },
                {
                    name: 'Terms, signs and brackets',
                    q: 'Core Concept 2: Operator Precedence (BODMAS)',
                    items: [
                        ['I can identify the terms of an expression by viewing subtraction as addition of a negative term.', false],
                        ['I can use brackets to show clearly which calculation is to be performed first.', 'Order of Operations & BODMAS Mechanics'],
                        ['I can evaluate an expression by first dealing with brackets and the multiplication/division contained within each term, then combining the terms.', 'Order of Operations & BODMAS Mechanics'],
                        ['I can remove brackets preceded by a plus sign without changing the signs inside.', 'Parentheses, Nested Grouping & Sign Precedence'],
                        ['I can remove brackets preceded by a minus sign and correctly change the signs of the terms inside.', 'Parentheses, Nested Grouping & Sign Precedence']
                    ]
                },
                {
                    name: 'Properties and efficient calculation',
                    q: 'Core Concept 3: Algebraic Laws of Arithmetic',
                    items: [
                        ['I can use the commutative property of addition to swap terms when convenient.', 'Quick Reference: Laws of Arithmetic Operations'],
                        ['I can use the associative property of addition to regroup terms when convenient.', 'Quick Reference: Laws of Arithmetic Operations'],
                        ['I can use the distributive property to expand forms such as a(b + c) and a(b - c).', 'Core Concept 4: Distributive Property'],
                        ['I can work backwards and factor a common multiplier in simple expressions.', 'Distributive Law Area Model'],
                        ['I can rearrange or regroup an expression in a valid way to make a calculation easier.', 'Commutative & Associative Terms Reordering Playground'],
                        ['I can explain why a rearrangement is valid instead of relying only on a memorised rule.', 'Algebraic Laws of Arithmetic']
                    ]
                },
                {
                    name: 'Reasoning',
                    q: 'Section 1: Expression Formation & Real-Life Modeling',
                    items: [
                        ['I can spot an incorrect interpretation of an expression and explain what went wrong.', false],
                        ['I can create equivalent arithmetic expressions that represent the same number.', 'Algebraic Laws of Arithmetic'],
                        ['I can use brackets and operations strategically in number puzzles.', 'Interactive Parentheses Placer']
                    ]
                }
            ]
        },

        math_ch3: {
            title: 'A Peek Beyond the Point',
            sections: [
                {
                    name: 'Tenths, hundredths and thousandths',
                    q: '1. Place Value & Representation',
                    items: [
                        ['I understand why whole-number units are sometimes not precise enough for measurement.', 'The Need for Smaller Units'],
                        ['I can split one unit into 10 tenths, one tenth into 10 hundredths, and one hundredth into 10 thousandths.', 'A Tenth Part'],
                        ['I understand the relationships 1 = 10 tenths, 1 tenth = 10 hundredths and 1 hundredth = 10 thousandths.', 'The Decimal Place Value Chart'],
                        ['I can identify the place value of digits to the right of the decimal point.', 'The Decimal Place Value Chart'],
                        ['I understand that the decimal point separates the whole-number part from the fractional part.', 'The Decimal Place Value Chart']
                    ]
                },
                {
                    name: 'Fractions and decimal notation',
                    q: 'Conversions: Fractions & Decimals',
                    items: [
                        ['I can write fractions with denominators 10, 100 and 1000 as decimals and convert such decimals back to fractions.', 'Two-Way Conversion Protocol'],
                        ['I can recognise equivalent forms such as 0.5 = 0.50 and explain why adding trailing zeroes does not change the value.', 'Zero Dilemma'],
                        ['I can convert familiar fractions such as 1/2, 1/4, 3/4, 1/5 and 4/5 into decimal form.'],
                        ['I can read a decimal correctly using place value rather than reading the digits as a whole number.', 'The Decimal Place Value Chart']
                    ]
                },
                {
                    name: 'Comparing and locating decimals',
                    q: 'Rules for Comparing Decimals',
                    items: [
                        ['I can place decimal numbers accurately on a number line.', 'Decimals on the Number Line'],
                        ['I can compare and order decimals by comparing corresponding place values.'],
                        ['I can insert zeroes where helpful so that decimals can be compared or calculated more easily.', 'Like and Unlike Decimals'],
                        ['I can identify numbers lying between two given decimals.', 'Decimals on the Number Line']
                    ]
                },
                {
                    name: 'Operations and applications',
                    q: '3. Addition & Subtraction of Decimals',
                    items: [
                        ['I can add decimals by aligning digits with the same place value.', 'Fundamental Columnar Alignment Rule'],
                        ['I can subtract decimals accurately by aligning decimal points and regrouping where needed.', 'Fundamental Columnar Alignment Rule'],
                        ['I can solve measurement, money, mass, capacity and distance problems involving decimal addition or subtraction.', 'Metric Unit Conversion Matrix'],
                        ['I can move sensibly between related metric units when decimals are involved.', 'Metric Unit Conversion Matrix'],
                        ['I can recognise and extend simple patterns involving decimal numbers.', 'Multiplying by Powers of 10'],
                        ['I can estimate whether a decimal answer is sensible before or after calculating exactly.', 'Estimating Sums and Differences']
                    ]
                }
            ]
        },

        math_ch4: {
            title: 'Expressions Using Letter-Numbers',
            sections: [
                {
                    name: 'Letters as numbers',
                    q: 'Anatomy of an Algebraic Expression',
                    items: [
                        ['I understand that a letter-number (variable) can stand for an unknown or changing number.'],
                        ['I can distinguish a fixed numerical value from a letter-number whose value may vary.', 'Numerical vs. Literal Coefficients'],
                        ['I can translate a relationship stated in words into an algebraic expression.', 'Master Word-Problem Algebraic Translator'],
                        ['I can describe an algebraic expression in ordinary language.', 'Describing Real-Life Situations for Expressions'],
                        ['I can substitute a given value for a letter and correctly evaluate the expression.', 'Evaluating Expressions at Positive, Negative']
                    ]
                },
                {
                    name: 'Writing and simplifying expressions',
                    q: 'Terms, Factors, Coefficients & Classification',
                    items: [
                        ['I understand the convention of writing 4 x n as 4n, with the number written before the letter.', 'Numerical vs. Literal Coefficients'],
                        ['I can identify like terms and unlike terms in simple algebraic expressions.', 'Group like terms from the given list'],
                        ['I can combine like terms correctly and explain why unlike terms cannot be combined in the same way.', 'Combine like terms to simplify expressions'],
                        ['I can use the same valid rules of swapping, grouping and brackets that I use in arithmetic expressions.', 'Grid Grouping and Faster Simplification'],
                        ['I can use the distributive property to expand simple algebraic expressions.', 'Distributive Simplification & Substitution'],
                        ['I can simplify a simple algebraic expression without changing its value.', 'Simplifying Multi-Term Expressions']
                    ]
                },
                {
                    name: 'Patterns and general rules',
                    q: 'Flower Pattern Growth Rule',
                    items: [
                        ['I can use a letter such as n to describe the position of a term in a pattern or sequence.'],
                        ['I can write general expressions for patterns such as multiples, repeated shapes or regularly changing arrangements.', 'Formulas for matchstick and dot patterns'],
                        ['I can find the value of a general expression for a particular step or position.', 'Finding Specified Terms Using Algebraic Expressions'],
                        ['I can work backwards from a pattern or table to discover a possible algebraic rule.', 'Expression Transformation Flow Paths'],
                        ['I can use algebra to make predictions for large positions without drawing every previous step.', 'Tile Staircase Growth Sequence']
                    ]
                },
                {
                    name: 'Mathematical modelling and reasoning',
                    q: 'Algebraic Translation & Evaluation',
                    items: [
                        ['I can use an algebraic expression as a formula connecting two or more quantities.', 'Perimeter Formulas for Regular Polygons'],
                        ['I can interpret formulas arising from ages, costs, calendars, grids, matchstick patterns and similar situations.', 'Calendar 3x3 Grid Expressed with Centre'],
                        ['I can explain why a general rule works, not merely check it for one or two examples.', 'Algebraic Proof: Sum of three consecutive odd numbers'],
                        ['I understand why algebra is useful for expressing a whole family of cases concisely.']
                    ]
                }
            ]
        },

        math_ch5: {
            title: 'Parallel and Intersecting Lines',
            sections: [
                {
                    name: 'Intersecting and perpendicular lines',
                    q: 'Vertically Opposite Angles (Theorem & Proof)',
                    items: [
                        ['I can identify intersecting lines and the point at which they intersect.', 'Intersecting Lines XY and PQ'],
                        ['I know that two distinct straight lines can meet at most once on a plane.', 'Intersecting Lines XY and PQ'],
                        ['I can identify a linear pair and use the fact that its two angles add to 180\u00b0.', 'Linear Pairs of Angles'],
                        ['I can identify vertically opposite angles and use the fact that they are equal.'],
                        ['I can use these angle facts together to calculate missing angles at an intersection.', 'Three Straight Lines Intersecting at O'],
                        ['I can identify perpendicular lines and recognise that they form four right angles of 90\u00b0.', 'Perpendicular Lines']
                    ]
                },
                {
                    name: 'Parallel lines and transversals',
                    q: 'Transversals Cutting Parallel Lines',
                    items: [
                        ['I can identify parallel lines and explain that they must lie in the same plane and never meet however far extended.', 'Parallel Lines'],
                        ['I can identify a transversal cutting two lines and recognise the eight angles that are formed.'],
                        ['I can identify corresponding angles, alternate angles and interior angles on the same side of a transversal.', ['Corresponding Angles (The F-Rule)', 'Alternate Angles (The Z-Rule)']],
                        ['I know that when a transversal cuts parallel lines, corresponding angles are equal.', 'Corresponding Angles (The F-Rule)'],
                        ['I know that when a transversal cuts parallel lines, alternate angles are equal.', 'Alternate Angles (The Z-Rule)'],
                        ['I know that interior angles on the same side of a transversal add to 180\u00b0.', 'The C-Rule (Co-interior)'],
                        ['I can use equal corresponding angles as evidence that two lines are parallel.', 'Parallel Proof: Show that AB || EF']
                    ]
                },
                {
                    name: 'Drawing and reasoning',
                    q: 'Constructions & Paper Folding',
                    items: [
                        ['I can use angle relationships in multi-step diagrams to find unknown angles.', 'The 3 Master Zigzag Transversal Archetypes'],
                        ['I can draw or construct parallel and perpendicular lines accurately using suitable tools or paper-folding methods.'],
                        ['I can mark parallel and perpendicular relationships clearly in a diagram.'],
                        ['I can explain my angle reasoning using named properties rather than saying that angles merely "look equal".', 'The Four Fundamental Geometric Theorems'],
                        ['I understand that visual appearances or optical illusions do not override geometric properties.', 'The Four Fundamental Geometric Theorems']
                    ]
                }
            ]
        },

        math_ch6: {
            title: 'Number Play',
            sections: [
                {
                    name: 'Parity - odd and even reasoning',
                    q: 'The Arithmetic Laws of Parity',
                    items: [
                        ['I understand parity as the property of a whole number being even or odd.'],
                        ['I can explain why consecutive whole numbers alternate between even and odd.'],
                        ['I can determine the parity of a sum without calculating its exact value.'],
                        ['I can determine the parity of a product without calculating its exact value.', 'Multiplication Grid Parity'],
                        ['I can represent even numbers using 2n and odd numbers using forms such as 2n + 1 or 2n - 1.', 'Algebraic Parity Expressions'],
                        ['I can test whether a proposed algebraic form always gives even numbers, always gives odd numbers, or can give both.', 'Parity of the Algebraic Form'],
                        ['I can use parity to prove that a proposed arrangement or total is impossible.', 'Parity Grid Invariance']
                    ]
                },
                {
                    name: 'Grids and magic squares',
                    q: 'How Numbers Reveal Hidden Order',
                    items: [
                        ['I can interpret number information from positions or arrangements even when the actual numbers are not all known.'],
                        ['I can use row, column and diagonal sums as constraints in a number grid.', 'Deducing the Magic Sum'],
                        ['I can decide when a grid puzzle is impossible by using bounds or sum reasoning.', 'Central Cell Invariance'],
                        ['I understand the defining property of a magic square: every row, column and main diagonal has the same sum.', 'Canonical 3'],
                        ['I can complete or construct a small magic square using logical reasoning rather than random trial alone.', 'Magic Square Builder']
                    ]
                },
                {
                    name: 'Virahanka-Fibonacci patterns',
                    q: 'Recurrence Relation',
                    items: [
                        ['I recognise the Virahanka-Fibonacci sequence 1, 2, 3, 5, 8, 13, 21, ...'],
                        ['I can generate later terms by adding the previous two terms.'],
                        ['I can work backwards when consecutive terms are known.', 'Missing Terms in the'],
                        ['I can connect this recursive pattern to counting arrangements made from 1-step and 2-step choices.', 'Angaan'],
                        ['I can solve simple staircase or rhythm-counting problems using the same recurrence idea.', 'Sanskrit Prosody']
                    ]
                },
                {
                    name: 'Cryptarithms and logical deduction',
                    q: 'The Four Fundamental Axioms of Cryptarithms',
                    items: [
                        ['I understand that in a cryptarithm each letter represents a digit consistently.'],
                        ['I can use place value, carrying and arithmetic constraints to deduce missing digits.', 'Column Addition Cryptarithms'],
                        ['I can check that a proposed cryptarithm solution satisfies every condition.', 'Cryptarithm Deduction Sandbox'],
                        ['I can combine parity, bounds, patterns and elimination to solve unfamiliar number puzzles systematically.']
                    ]
                }
            ]
        },

        math_ch7: {
            title: 'A Tale of Three Intersecting Lines',
            sections: [
                {
                    name: 'Triangle basics and construction tools',
                    q: 'Equilateral Triangle Construction',
                    items: [
                        ['I can identify and name the vertices, sides and angles of a triangle using standard notation.', 'Master Vocabulary, Etymology'],
                        ['I can construct an equilateral triangle of a given side length using a ruler and compass.'],
                        ['I understand why intersecting arcs locate a point at fixed distances from two given points.', 'Step-by-Step Construction Protocol'],
                        ['I can construct a triangle from three given side lengths (SSS) using a ruler and compass.', 'SSS Triangle Construction'],
                        ['I can write clear construction steps and check the finished side lengths.', 'Step-by-Step Construction Protocol']
                    ]
                },
                {
                    name: 'Triangle inequality and possibility',
                    q: 'The Triangle Inequality Theorem',
                    items: [
                        ['I know that in any triangle, each side is shorter than the sum of the other two sides.'],
                        ['I can test three given lengths and decide whether they can form a triangle.', "Pushti's Quick-Test Method"],
                        ['I can determine the possible range for a third side when two side lengths are known.', 'Two Smallest Sides Rule'],
                        ['I understand that failure of the construction arcs to meet reflects the triangle inequality.', 'Degree of Freedom']
                    ]
                },
                {
                    name: 'Constructions using sides and angles',
                    q: 'SAS, ASA and RHS Triangle Constructions',
                    items: [
                        ['I can construct a triangle when two sides and the included angle are given (SAS).', 'Side-Angle-Side'],
                        ['I can construct a triangle when two angles and the included side are given (ASA).', 'Angle-Side-Angle'],
                        ['I can use a ruler, compass and protractor accurately and choose an appropriate base for a construction.'],
                        ['I can decide whether the information given is sufficient to determine the intended triangle.', 'Degree of Freedom']
                    ]
                },
                {
                    name: 'Angles, altitudes and classification',
                    q: 'The Angle Sum Property',
                    items: [
                        ['I know that the three interior angles of every triangle add to 180\u00b0.', 'Theorem: The Sum of Interior Angles'],
                        ['I can use the angle-sum property to calculate an unknown angle of a triangle.'],
                        ['I can define an altitude as a perpendicular line segment from a vertex to its opposite side (or the line containing that side).', 'Altitudes of Triangles'],
                        ['I can construct an altitude from a chosen vertex.', 'Constructing an Altitude with a Set-Square'],
                        ['I can classify triangles by sides as equilateral, isosceles or scalene.', 'Two-Way Classification Matrix'],
                        ['I can classify triangles by angles as acute-angled, right-angled or obtuse-angled.', 'Two-Way Classification Matrix'],
                        ['I can combine side and angle classifications correctly when describing a triangle.', 'Two-Way Classification Matrix']
                    ]
                }
            ]
        },

        math_ch8: {
            title: 'Working with Fractions',
            sections: [
                {
                    name: 'Multiplication of fractions',
                    q: 'Multiplication of a Fraction by a Whole Number',
                    items: [
                        ['I can interpret multiplication by a fraction as taking a fractional part of a quantity.', 'Fraction as an Operator'],
                        ['I can multiply a whole number by a fraction and a fraction by a whole number.'],
                        ['I can multiply two fractions using numerator x numerator and denominator x denominator.', "Brahmagupta's Product Rule"],
                        ['I can convert a mixed number to an improper fraction when this is useful for multiplication.', 'Mixed Fractions'],
                        ['I can cancel common factors before multiplying so that the arithmetic stays simple.', 'Apavartana: Simplification to Lowest Form'],
                        ['I can simplify a product to lowest terms and, when appropriate, write an improper fraction as a mixed number.', 'Reduction to Lowest Terms'],
                        ['I can use a diagram or area model to explain the meaning of a fraction multiplied by a fraction.', 'The Visual Area Grid Model']
                    ]
                },
                {
                    name: 'Size of products and reciprocals',
                    q: 'Three Cases of Product Magnitude',
                    items: [
                        ['I can predict that multiplying by a positive number between 0 and 1 makes a positive quantity smaller.'],
                        ['I can predict that multiplying by a number greater than 1 makes a positive quantity larger.'],
                        ['I understand the reciprocal of a non-zero fraction a/b is b/a.', 'Reciprocals of Fractions'],
                        ['I know that a non-zero fraction multiplied by its reciprocal equals 1.', 'Reciprocal Law']
                    ]
                },
                {
                    name: 'Division of fractions',
                    q: 'Why Do We Invert and Multiply',
                    items: [
                        ['I can interpret simple fraction division as "how many of this amount fit into that amount?".', 'Understanding Division as Measurement Grouping'],
                        ['I can divide by a fraction by multiplying by its reciprocal.'],
                        ['I can apply the fraction-division rule accurately to proper, improper and mixed fractions.', 'Division of a Fraction by Another Fraction'],
                        ['I can simplify the quotient and check it for reasonableness.', 'Comparing Quotients in Fraction Division'],
                        ['I can predict that dividing a positive quantity by a number between 0 and 1 makes the quotient larger.', 'Comparing Quotients in Fraction Division'],
                        ['I can predict that dividing a positive quantity by a number greater than 1 makes the quotient smaller.', 'Comparing Quotients in Fraction Division']
                    ]
                },
                {
                    name: 'Applications and problem solving',
                    q: 'Multi-Stage Sharing Problems',
                    items: [
                        ['I can choose whether multiplication, division, addition or subtraction of fractions is needed in a word problem.'],
                        ['I can solve fraction problems involving distance, time, rates, area, sharing and portions of a whole.', 'Real-World Measurement Units'],
                        ['I can solve multi-step problems in which fractions must first be converted or simplified.'],
                        ['I can estimate whether a fractional answer should be less than 1, between two whole numbers, or greater than the starting quantity.', 'Three Cases of Product Magnitude'],
                        ['I can explain the reasoning behind my operation choice instead of relying only on keywords.', false]
                    ]
                }
            ]
        }
    };

    /* ===================================================================== */
    /* 2. STATE & HELPERS                                                     */
    /* ===================================================================== */

    var chapterId = null;
    var data = null;
    var storeKey = null;
    var state = null;
    var totalItems = 0;

    var CONF_LEVELS = [
        { id: 'secure', label: 'Secure', color: '#34d399' },
        { id: 'mostly', label: 'Mostly secure', color: '#fbbf24' },
        { id: 'practice', label: 'Needs more practice', color: '#f87171' }
    ];

    function norm(s) {
        return String(s || '').replace(/\s+/g, ' ').replace(/\u00a0/g, ' ').trim().toLowerCase();
    }

    /* KaTeX rewrites headings (duplicated MathML + HTML text, lost spaces),
       so deep-link matching compares alphanumeric-only keys. */
    function keyOf(s) {
        return norm(s).replace(/[^a-z0-9]+/g, '');
    }

    function detectChapterId() {
        var m = location.pathname.match(/maths_ch(\d+)/i);
        if (m) return 'math_ch' + m[1];
        var btn = document.querySelector('[onclick*="openChapterLog"]');
        if (btn) {
            var mm = (btn.getAttribute('onclick') || '').match(/openChapterLog\(\s*['"]([^'"]+)['"]/);
            if (mm) return mm[1];
        }
        return null;
    }

    function loadState() {
        try {
            var raw = localStorage.getItem(storeKey);
            return raw ? JSON.parse(raw) : {};
        } catch (e) {
            return {};
        }
    }

    function saveState() {
        try {
            localStorage.setItem(storeKey, JSON.stringify(state));
        } catch (e) { /* private mode */ }
    }

    /* ===================================================================== */
    /* 3. DEEP-LINK RESOLVER                                                  */
    /* ===================================================================== */

    function toQueries(q) {
        if (q === false) return [];
        if (!q) return [];
        return Array.isArray(q) ? q : [q];
    }

    function findHeading(qList) {
        var nodes = document.querySelectorAll('h1, h2, h3, h4, h5, .topic-sec-title');
        var cache = [];
        for (var j = 0; j < nodes.length; j++) {
            var node = nodes[j];
            if (node.closest && node.closest('#tab-checklist, #sidebar, .sidebar')) continue;
            cache.push({ el: node, plain: norm(node.textContent), key: keyOf(node.textContent) });
        }
        for (var i = 0; i < qList.length; i++) {
            var plain = norm(qList[i]);
            var key = keyOf(qList[i]);
            if (!key) continue;
            for (var c = 0; c < cache.length; c++) {
                if (cache[c].key.indexOf(key) !== -1) return cache[c].el;
            }
            for (var p = 0; p < cache.length; p++) {
                if (cache[p].plain.indexOf(plain) !== -1) return cache[p].el;
            }
        }
        return null;
    }

    function findControl(id) {
        if (!id) return null;
        var selectors = [
            '.tab-btn[data-tab="' + id + '"]',
            '[data-subtab="' + id + '"]',
            '[data-topic="' + id + '"]',
            "[onclick*=\"'" + id + "'\"]",
            '[onclick*="' + id + '"]'
        ];
        for (var i = 0; i < selectors.length; i++) {
            var el = document.querySelector(selectors[i]);
            if (el) return el;
        }
        return null;
    }

    function activateChain(el) {
        var chain = [];
        var node = el;
        while (node && node !== document.body) {
            if (node.id) chain.push(node);
            node = node.parentElement;
        }
        chain.reverse();

        chain.forEach(function (anc) {
            var isTopPane = anc.classList.contains('tab-pane') || anc.classList.contains('tab-panel');
            var ctl = findControl(anc.id);
            if (ctl) {
                ctl.click();
            } else if (isTopPane && typeof window.switchTab === 'function') {
                window.switchTab(anc.id);
            }
        });
    }

    function jumpToTarget(el) {
        if (!el) return;
        activateChain(el);
        /* switchTab() may fire its own smooth scrollTo(0); scroll twice so the
           heading wins the animation race on every page. */
        function doScroll() {
            try {
                el.scrollIntoView({ behavior: 'smooth', block: 'center' });
            } catch (e) {
                el.scrollIntoView();
            }
        }
        setTimeout(function () {
            doScroll();
            el.classList.add('ck-flash');
            setTimeout(function () { el.classList.remove('ck-flash'); }, 2600);
        }, 220);
        /* final snap: switchTab()'s own smooth scrollTo(0) can still be
           animating; an instant pass guarantees the heading lands in view */
        setTimeout(function () {
            try {
                /* 'instant', not 'auto': pages set html{scroll-behavior:smooth},
                   which would make 'auto' resolve to smooth again */
                el.scrollIntoView({ behavior: 'instant', block: 'center' });
            } catch (e) {
                el.scrollIntoView();
            }
        }, 750);
    }

    /* ===================================================================== */
    /* 4. RENDERING                                                           */
    /* ===================================================================== */

    function countTicked() {
        var n = 0;
        for (var k in state.items) {
            if (state.items[k]) n++;
        }
        return n;
    }

    function updateBadges() {
        var done = countTicked();
        var pct = totalItems ? Math.round((done / totalItems) * 100) : 0;
        var badge = document.getElementById('ck-mini-badge');
        if (badge) badge.textContent = done + '/' + totalItems + ' ticked';
        var bar = document.getElementById('ck-progress-fill');
        if (bar) bar.style.width = pct + '%';
        var label = document.getElementById('ck-progress-label');
        if (label) label.textContent = pct + '% Mastered';
        var stat = document.getElementById('ck-stat-ticked');
        if (stat) stat.textContent = done;
        var statU = document.getElementById('ck-stat-unticked');
        if (statU) statU.textContent = totalItems - done;
    }

    function buildPane() {
        var wrap = document.querySelector('.main-content, .tab-content-area, main') || document.body;
        var pane = document.createElement('div');
        pane.id = 'tab-checklist';
        pane.className = (document.querySelector('.tab-panel') ? 'tab-panel' : 'tab-pane');

        var html = '';
        html += '<div class="ck-wrap">';

        /* Banner */
        html += '<div class="ck-banner">';
        html += '<div class="ck-banner-top">';
        html += '<div>';
        html += '<h2 class="ck-title"><i class="fas fa-list-check"></i> Concept Mastery Checklist &mdash; Part I</h2>';
        html += '<p class="ck-sub">' + data.title + ' &bull; Ganita Prakash Part I Revision Audit</p>';
        html += '<p class="ck-note">Use this as a revision audit. Tick a statement only when you can explain or apply it independently, without prompting.</p>';
        html += '</div>';
        html += '<div class="ck-actions">';
        html += '<button type="button" class="ck-btn" id="ck-print"><i class="fas fa-print"></i> Print</button>';
        html += '<button type="button" class="ck-btn ck-btn-danger" id="ck-reset"><i class="fas fa-rotate-right"></i> Reset</button>';
        html += '</div>';
        html += '</div>';
        html += '<div class="ck-progress-head"><span>Chapter Mastery</span><span id="ck-progress-label">0% Mastered</span></div>';
        html += '<div class="ck-progress-bg"><div class="ck-progress-fill" id="ck-progress-fill" style="width:0%;"></div></div>';
        html += '<div class="ck-stats">';
        html += '<span class="ck-pill">Total: ' + totalItems + '</span>';
        html += '<span class="ck-pill ck-pill-ok"><i class="fas fa-check-circle"></i> Ticked: <b id="ck-stat-ticked">0</b></span>';
        html += '<span class="ck-pill ck-pill-wait"><i class="fas fa-circle-notch"></i> Pending: <b id="ck-stat-unticked">' + totalItems + '</b></span>';
        html += '</div>';
        html += '</div>';

        /* Sections */
        data.sections.forEach(function (sec, si) {
            html += '<div class="ck-section">';
            html += '<div class="ck-section-head"><i class="fas fa-folder-open"></i> ' + sec.name + '</div>';
            html += '<ul class="ck-list">';
            sec.items.forEach(function (item, ii) {
                var text = item[0];
                var queries = toQueries(item.length > 1 ? item[1] : sec.q);
                if (!item.length || item.length === 1) queries = toQueries(sec.q);
                var target = queries.length ? findHeading(queries) : null;
                var key = si + '-' + ii;
                var checked = state.items[key] ? ' checked' : '';
                var label;
                if (target) {
                    var tTxt = String(target.textContent).replace(/\s+/g, ' ').trim();
                    if (tTxt.length > 90) tTxt = tTxt.slice(0, 90) + '\u2026';
                    label = '<a class="ck-link" href="#" data-ck-key="' + key + '" title="Jump to: ' +
                        tTxt.replace(/"/g, '&quot;') + '">' + text + '</a>';
                } else {
                    label = '<span class="ck-plain">' + text + '</span>';
                }
                html += '<li class="ck-item' + (target ? '' : ' ck-nolink') + '">' +
                    '<label class="ck-check">' +
                    '<input type="checkbox" data-ck="' + key + '"' + checked + '>' +
                    '<span class="ck-box" aria-hidden="true"><i class="fas fa-check"></i></span>' +
                    '</label>' +
                    '<span class="ck-text">' + label + '</span>' +
                    '</li>';
            });
            html += '</ul></div>';
        });

        /* Confidence + priority topics */
        html += '<div class="ck-conf">';
        html += '<div class="ck-conf-row">';
        html += '<span class="ck-conf-label">Chapter confidence:</span>';
        CONF_LEVELS.forEach(function (lvl) {
            var on = state.conf === lvl.id ? ' checked' : '';
            html += '<label class="ck-conf-opt" style="--opt-color:' + lvl.color + '">' +
                '<input type="radio" name="ck-confidence" value="' + lvl.id + '"' + on + '>' +
                '<span class="ck-radio"></span>' + lvl.label + '</label>';
        });
        html += '</div>';
        html += '<div class="ck-conf-row ck-prio-row">';
        html += '<span class="ck-conf-label">Priority topics:</span>';
        html += '<input type="text" class="ck-prio" id="ck-prio" placeholder="Topics to revise first..." value="' +
            (state.prio ? String(state.prio).replace(/"/g, '&quot;') : '') + '">';
        html += '</div>';
        html += '</div>';

        html += '</div>';

        pane.innerHTML = html;
        wrap.appendChild(pane);
        wirePane(pane);
        updateBadges();
    }

    function wirePane(pane) {
        pane.addEventListener('change', function (e) {
            var cb = e.target.closest('input[data-ck]');
            if (cb) {
                state.items[cb.getAttribute('data-ck')] = cb.checked;
                saveState();
                updateBadges();
                return;
            }
            if (e.target.name === 'ck-confidence') {
                state.conf = e.target.value;
                saveState();
            }
        });

        pane.addEventListener('input', function (e) {
            if (e.target.id === 'ck-prio') {
                state.prio = e.target.value;
                saveState();
            }
        });

        pane.addEventListener('click', function (e) {
            var link = e.target.closest('a.ck-link');
            if (link) {
                e.preventDefault();
                var key = link.getAttribute('data-ck-key');
                var parts = key.split('-');
                var sec = data.sections[parseInt(parts[0], 10)];
                var item = sec.items[parseInt(parts[1], 10)];
                var queries = toQueries(item.length > 1 ? item[1] : sec.q);
                if (!item.length || item.length === 1) queries = toQueries(sec.q);
                jumpToTarget(findHeading(queries));
                return;
            }
            if (e.target.closest('#ck-reset')) {
                if (confirm('Clear all ticked statements and confidence for this chapter?')) {
                    state = { items: {}, conf: '', prio: '' };
                    saveState();
                    rebuildPane();
                }
                return;
            }
            if (e.target.closest('#ck-print')) {
                window.print();
            }
        });
    }

    function rebuildPane() {
        var old = document.getElementById('tab-checklist');
        if (old) old.parentNode.removeChild(old);
        buildPane();
    }

    /* ===================================================================== */
    /* 5. TAB INJECTION                                                       */
    /* ===================================================================== */

    function injectTab() {
        var bar = document.querySelector('.sidebar-tabs, .sidebar-nav, .sidebar .tab-list');
        if (!bar || bar.querySelector('[data-tab="tab-checklist"]')) return;

        var btn = document.createElement('button');
        btn.type = 'button';
        btn.className = 'tab-btn';
        btn.setAttribute('data-tab', 'tab-checklist');
        btn.setAttribute('title', 'Concept Mastery Checklist (Part I Revision Audit)');
        btn.innerHTML =
            '<span class="tab-icon-wrap"><i class="fas fa-list-check" style="color:#22d3ee;"></i></span>' +
            '<div class="tab-label-group">' +
            '<span class="tab-label">Checklist</span>' +
            '<span class="tab-verified-date" id="ck-mini-badge">0/' + totalItems + ' ticked</span>' +
            '</div>';
        btn.addEventListener('click', function (e) {
            e.preventDefault();
            if (typeof window.switchTab === 'function') {
                window.switchTab('tab-checklist', btn);
            } else {
                document.querySelectorAll('.tab-pane, .tab-panel').forEach(function (p) { p.classList.remove('active'); });
                document.querySelectorAll('.tab-btn').forEach(function (b) { b.classList.remove('active'); });
                document.getElementById('tab-checklist').classList.add('active');
            }
            /* Some pages (ch4) activate buttons only via an onclick attribute
               selector, which this injected button does not have - re-assert. */
            if (document.getElementById('tab-checklist').classList.contains('active')) {
                btn.classList.add('active');
            }
        });
        bar.appendChild(btn);
    }

    function injectStyles() {
        if (document.getElementById('ck-styles')) return;
        var st = document.createElement('style');
        st.id = 'ck-styles';
        st.textContent = [
            '.ck-wrap{max-width:980px;margin:0 auto;padding:4px 2px 40px;}',
            '.ck-banner{background:linear-gradient(135deg,rgba(34,211,238,0.10),rgba(139,92,246,0.10));border:1px solid var(--border,rgba(255,255,255,0.12));border-radius:14px;padding:18px 20px;margin-bottom:22px;}',
            '.ck-banner-top{display:flex;justify-content:space-between;gap:16px;align-items:flex-start;flex-wrap:wrap;}',
            '.ck-title{margin:0;font-family:Outfit,sans-serif;font-size:1.25rem;color:var(--text-title,#e8ecff);}',
            '.ck-title i{color:#22d3ee;margin-right:6px;}',
            '.ck-sub{margin:4px 0 0;font-size:0.85rem;font-weight:700;color:#a5b4fc;}',
            '.ck-note{margin:8px 0 0;font-size:0.82rem;color:var(--text-muted,#9aa3c0);font-style:italic;}',
            '.ck-actions{display:flex;gap:8px;}',
            '.ck-btn{cursor:pointer;border:1px solid var(--border,rgba(255,255,255,0.14));background:var(--surface,rgba(255,255,255,0.05));color:var(--text-main,#e6e9f5);border-radius:8px;padding:7px 13px;font-size:0.8rem;font-weight:700;}',
            '.ck-btn:hover{border-color:#22d3ee;color:#22d3ee;}',
            '.ck-btn-danger:hover{border-color:#f87171;color:#f87171;}',
            '.ck-progress-head{display:flex;justify-content:space-between;font-size:0.78rem;font-weight:700;margin:16px 0 5px;color:var(--text-muted,#9aa3c0);}',
            '.ck-progress-bg{height:9px;border-radius:99px;background:rgba(255,255,255,0.08);overflow:hidden;}',
            '.ck-progress-fill{height:100%;border-radius:99px;background:linear-gradient(90deg,#22d3ee,#34d399);transition:width .35s ease;}',
            '.ck-stats{display:flex;gap:8px;flex-wrap:wrap;margin-top:12px;}',
            '.ck-pill{font-size:0.75rem;font-weight:700;padding:4px 10px;border-radius:99px;border:1px solid var(--border,rgba(255,255,255,0.14));color:var(--text-muted,#9aa3c0);}',
            '.ck-pill-ok{color:#34d399;border-color:rgba(52,211,153,0.4);background:rgba(52,211,153,0.08);}',
            '.ck-pill-wait{color:#fbbf24;border-color:rgba(251,191,36,0.4);background:rgba(251,191,36,0.08);}',
            '.ck-section{background:var(--bg-card,rgba(255,255,255,0.035));border:1px solid var(--border,rgba(255,255,255,0.10));border-radius:12px;padding:14px 16px;margin-bottom:14px;}',
            '.ck-section-head{font-family:Outfit,sans-serif;font-weight:700;font-size:0.95rem;color:var(--text-title,#e8ecff);border-bottom:1px dashed var(--border,rgba(255,255,255,0.12));padding-bottom:8px;margin-bottom:6px;}',
            '.ck-section-head i{color:#8b5cf6;margin-right:6px;}',
            '.ck-list{list-style:none;margin:0;padding:0;}',
            '.ck-item{display:flex;align-items:flex-start;gap:10px;padding:7px 4px;border-radius:7px;}',
            '.ck-item:hover{background:rgba(255,255,255,0.04);}',
            '.ck-check{position:relative;display:inline-flex;margin-top:2px;cursor:pointer;flex:0 0 auto;}',
            '.ck-check input{position:absolute;opacity:0;width:18px;height:18px;margin:0;cursor:pointer;}',
            '.ck-box{width:18px;height:18px;border-radius:5px;border:2px solid rgba(148,163,184,0.55);display:inline-flex;align-items:center;justify-content:center;transition:all .15s ease;}',
            '.ck-box i{font-size:10px;color:#04121a;opacity:0;}',
            '.ck-check input:checked + .ck-box{background:#22d3ee;border-color:#22d3ee;}',
            '.ck-check input:checked + .ck-box i{opacity:1;}',
            '.ck-text{font-size:0.88rem;line-height:1.55;color:var(--text-main,#e6e9f5);}',
            '.ck-link{color:#67e8f9;text-decoration:none;border-bottom:1px dotted rgba(103,232,249,0.5);}',
            '.ck-link:hover{color:#a5f3fc;border-bottom-style:solid;}',
            '.ck-link::after{content:"\\2197";font-size:0.65em;margin-left:3px;vertical-align:super;opacity:0.7;}',
            '.ck-plain{color:var(--text-main,#e6e9f5);}',
            '.ck-nolink .ck-text{opacity:0.92;}',
            '.ck-item:has(input:checked) .ck-text{opacity:0.62;}',
            '.ck-conf{background:var(--bg-card,rgba(255,255,255,0.035));border:1px solid var(--border,rgba(255,255,255,0.10));border-radius:12px;padding:14px 16px;}',
            '.ck-conf-row{display:flex;align-items:center;gap:14px;flex-wrap:wrap;}',
            '.ck-conf-row + .ck-conf-row{margin-top:12px;}',
            '.ck-conf-label{font-size:0.85rem;font-weight:700;color:var(--text-title,#e8ecff);}',
            '.ck-conf-opt{display:inline-flex;align-items:center;gap:6px;font-size:0.83rem;cursor:pointer;color:var(--text-muted,#9aa3c0);}',
            '.ck-conf-opt input{position:absolute;opacity:0;}',
            '.ck-radio{width:15px;height:15px;border-radius:50%;border:2px solid rgba(148,163,184,0.55);display:inline-block;position:relative;}',
            '.ck-conf-opt input:checked + .ck-radio{border-color:var(--opt-color);}',
            '.ck-conf-opt input:checked + .ck-radio::after{content:"";position:absolute;inset:2.5px;border-radius:50%;background:var(--opt-color);}',
            '.ck-conf-opt input:checked ~ *{color:var(--opt-color);}',
            '.ck-prio{flex:1;min-width:220px;background:rgba(0,0,0,0.18);border:1px solid var(--border,rgba(255,255,255,0.14));border-radius:8px;padding:7px 10px;font-size:0.83rem;color:var(--text-main,#e6e9f5);}',
            '.ck-prio:focus{outline:none;border-color:#22d3ee;}',
            '.ck-flash{animation:ckFlash 2.4s ease;}',
            '@keyframes ckFlash{0%,60%{box-shadow:0 0 0 3px rgba(34,211,238,0.55);border-radius:6px;}100%{box-shadow:0 0 0 0 rgba(34,211,238,0);}}',
            '@media(max-width:1366px){.ck-wrap{max-width:100%;}}',
            '@media print{body *{visibility:hidden !important;}#tab-checklist,#tab-checklist *{visibility:visible !important;}#tab-checklist{position:absolute;left:0;top:0;width:100%;}a.ck-link::after{display:none;}}'
        ].join('\n');
        document.head.appendChild(st);
    }

    /* ===================================================================== */
    /* 6. BOOT                                                                */
    /* ===================================================================== */

    function init() {
        chapterId = detectChapterId();
        if (!chapterId || !CHECKLISTS[chapterId]) return;

        data = CHECKLISTS[chapterId];
        storeKey = 'pushti_cklst_' + chapterId;

        totalItems = 0;
        data.sections.forEach(function (s) { totalItems += s.items.length; });

        state = loadState();
        if (!state.items) state.items = {};

        injectStyles();
        buildPane();
        injectTab();
        updateBadges(); /* mini badge is created with a hardcoded 0/N */
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }
})();
