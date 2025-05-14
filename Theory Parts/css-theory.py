# CSS TUTORIALS:
# 1. CSS Introduction.
# 2. CSS Syntax.
# 3. CSS Selectors.
# 4. CSS Colors.
# 5. CSS Backgrounds.
# 6. CSS Borders.
# 7. CSS Margins.
# 8. CSS Padding.
# 9. CSS Height and Width.
# 10. CSS Box Model.
# 11. CSS Display Property.
# 12. CSS Positioning.
# 13. CSS Floating Elements.
# 14. CSS Flexbox.
# 15. CSS Grid Layout.
# 16. CSS Responsive Web Design.
# 17. CSS Media.
# 18. CSS Animation.
# 19. CSS Transitions.
# 20. CSS Transformations.
# 21. CSS Filters.


# ------------------------------------------------------------------------------------------------------------------------------

# CSS Introduction:
# CSS (Cascading Style Sheets) is a stylesheet language used to describe the presentation of a document written in HTML or XML.
# CSS is used to control the layout of multiple web pages all at once. 
# It can be used to change the color, font, size, spacing, and many other aspects of HTML elements. 
# CSS is a powerful tool for web developers and designers to create visually appealing and user-friendly websites.
# CSS is a cornerstone technology of the World Wide Web, alongside HTML and JavaScript.
# CSS is maintained by the World Wide Web Consortium (W3C), which is an international community that develops open standards to ensure the long-term growth of the Web.
# CSS is a language that describes the style of an HTML document. 
# It controls the layout of multiple web pages all at once.


# ------------------------------------------------------------------------------------------------------------------------------

# CSS Syntax:
# CSS syntax consists of a set of rules that define how HTML elements should be displayed. 
# Each rule consists of a selector and a declaration block.
# The selector specifies which HTML elements the rule applies to, and the declaration block contains one or more declarations that define the styles to be applied.
# A declaration consists of a property and a value, separated by a colon. Multiple declarations are separated by semicolons.
# The syntax for a CSS rule is as follows:
# selector {
#     property: value;
#     property: value;
#     property: value;
# }
# For example, the following CSS rule sets the color of all <h1> elements to blue and the font size to 24 pixels:
# h1 {
#     color: blue;
#     font-size: 24px;
# }
# In this example, "h1" is the selector, "color" and "font-size" are properties, and "blue" and "24px" are values.
# The CSS rule applies to all <h1> elements in the HTML document, setting their text color to blue and font size to 24 pixels.
# CSS rules can be applied to HTML elements in several ways, including inline styles, internal stylesheets, and external stylesheets.
# Inline styles are applied directly to individual HTML elements using the "style" attribute. 
# Internal stylesheets are defined within the <style> tags in the <head> section of an HTML document. 
# External stylesheets are separate CSS files linked to an HTML document using the <link> tag.


# ------------------------------------------------------------------------------------------------------------------------------

# CSS Selectors:
# CSS selectors are patterns used to select the elements you want to style. 
# There are several types of selectors in CSS, including:
# 1. Universal Selector (*): Selects all elements in the document.
# 2. Type Selector (element): Selects all elements of a specific type (e.g., p, h1, div).
# 3. Class Selector (.classname): Selects all elements with a specific class attribute.
# 4. ID Selector (#idname): Selects a single element with a specific id attribute.
# 5. Descendant Selector (ancestor descendant): Selects all elements that are descendants of a specific ancestor element.


# ------------------------------------------------------------------------------------------------------------------------------


# CSS Colors:
# CSS colors can be specified using color names, hexadecimal values, RGB values, RGBA values, HSL values, and HSLA values.
# 1. Color Names: CSS supports a set of predefined color names 
#   (e.g., red, blue, green).
# 2. Hexadecimal Values: Colors can be specified using a six-digit hexadecimal code 
#   (e.g., #FF0000 for red).
# 3. RGB Values: Colors can be specified using the RGB color model, which combines red, green, and blue values 
#   (e.g., rgb(255, 0, 0) for red).
# 4. RGBA Values: Similar to RGB, but includes an alpha value for transparency 
#   (e.g., rgba(255, 0, 0, 0.5) for semi-transparent red).
# 5. HSL Values: Colors can be specified using the HSL color model, which uses hue, saturation, and lightness 
#   (e.g., hsl(0, 100%, 50%) for red).
# 6. HSLA Values: Similar to HSL, but includes an alpha value for transparency 
#   (e.g., hsla(0, 100%, 50%, 0.5) for semi-transparent red).
# CSS also supports color functions like "currentColor" and "transparent" to create dynamic and transparent colors.
# The "currentColor" value allows you to use the current text color of an element, while "transparent" creates a fully transparent color.
# CSS colors can be applied to various properties, including background-color, color, border-color, and more.
# You can also use CSS variables (custom properties) to define reusable color values throughout your stylesheet.
# CSS variables are defined using the "--" prefix and can be accessed using the "var()" function.


# ------------------------------------------------------------------------------------------------------------------------------


# CSS Backgrounds:
# CSS backgrounds can be applied to HTML elements using the "background" property. The background property can include multiple values, such as background color, image, position, size, and repeat.
# 1. Background Color: You can set the background color of an element using the "background-color" property (e.g., background-color: blue;).
# 2. Background Image: You can set a background image using the "background-image" property (e.g., background-image: url('image.jpg');).
# 3. Background Position: You can control the position of the background image using the "background-position" property (e.g., background-position: center;).
# 4. Background Size: You can control the size of the background image using the "background-size" property (e.g., background-size: cover;).
# 5. Background Repeat: You can control how the background image repeats using the "background-repeat" property (e.g., background-repeat: no-repeat;).
# 6. Background Attachment: You can control how the background image behaves when scrolling using the "background-attachment" property (e.g., background-attachment: fixed;).
# 7. Background Clip: You can control how the background is clipped using the "background-clip" property (e.g., background-clip: content-box;).
# 8. Background Origin: You can control the positioning of the background image using the "background-origin" property (e.g., background-origin: padding-box;).
# 9. Multiple Backgrounds: You can apply multiple background images to an element by separating them with commas (e.g., background-image: url('image1.jpg'), url('image2.jpg');).



# ------------------------------------------------------------------------------------------------------------------------------


# CSS Borders:
# CSS borders can be applied to HTML elements using the "border" property. The border property can include multiple values, such as border width, style, and color.
# 1. Border Width: You can set the width of the border using the "border-width" property (e.g., border-width: 2px;).
# 2. Border Style: You can set the style of the border using the "border-style" property (e.g., border-style: solid;).
# 3. Border Color: You can set the color of the border using the "border-color" property (e.g., border-color: blue;).
# 4. Border Radius: You can set the rounded corners of the border using the "border-radius" property (e.g., border-radius: 10px;).
# 5. Border Image: You can set a border image using the "border-image" property (e.g., border-image: url('image.png') 30 stretch;).
# 6. Border Collapse: You can control how borders are collapsed in tables using the "border-collapse" property (e.g., border-collapse: collapse;).
# 7. Border Spacing: You can control the spacing between borders in tables using the "border-spacing" property (e.g., border-spacing: 10px;).
# 8. Border Shadow: You can create a shadow effect for borders using the "box-shadow" property (e.g., box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);).
# 9. Border Outline: You can create an outline around elements using the "outline" property (e.g., outline: 2px solid red;).
# 10. Border Outline Offset: You can control the offset of the outline using the "outline-offset" property (e.g., outline-offset: 5px;).
# 11. Border Clip: You can control how the border is clipped using the "border-clip" property (e.g., border-clip: content-box;).


# ------------------------------------------------------------------------------------------------------------------------------


# CSS Margins:
# CSS margins are used to create space around elements. The margin property can include multiple values, such as margin width and margin direction.
# 1. Margin Width: You can set the width of the margin using the "margin" property (e.g., margin: 10px;).
# 2. Margin Direction: You can set the margin for specific directions using the "margin-top", "margin-right", "margin-bottom", and "margin-left" properties (e.g., margin-top: 20px;).
# 3. Margin Auto: You can set the margin to auto to center elements horizontally (e.g., margin: auto;).
# 4. Margin Collapse: Margins of adjacent elements can collapse into a single margin, which can be controlled using the "overflow" property (e.g., overflow: hidden;).
# 5. Margin Percentages: Margins can be set using percentage values, which are relative to the width of the containing element (e.g., margin: 5%;).
# 6. Margin Negative Values: Margins can be set to negative values to pull elements closer together (e.g., margin: -10px;).
# 7. Margin Shorthand: You can use shorthand notation to set all four margins at once (e.g., margin: 10px 20px 30px 40px;).
# 8. Margin Responsive Design: You can use media queries to set different margin values based on screen size (e.g., @media (max-width: 600px) { margin: 5px; }).
# 9. Margin Flexbox: You can use flexbox properties to control margins in flex containers (e.g., justify-content: space-between;).
# 10. Margin Grid: You can use grid properties to control margins in grid containers (e.g., grid-gap: 10px;).
# 11. Margin Variables: You can use CSS variables to define reusable margin values throughout your stylesheet (e.g., --main-margin: 10px;).
# 12. Margin Functions: You can use CSS functions like "calc()" to perform calculations for margin properties (e.g., margin: calc(100% - 20px);).
# 13. Margin Animations: You can animate margin properties using CSS animations and transitions (e.g., transition: margin 0.5s ease;).



# ------------------------------------------------------------------------------------------------------------------------------


# CSS Padding:
# CSS padding is used to create space inside elements, between the content and the border. 
# The padding property can include multiple values, such as padding width and padding direction.
# 1. Padding Width: You can set the width of the padding using the "padding" property (e.g., padding: 10px;).
# 2. Padding Direction: You can set the padding for specific directions using the "padding-top", "padding-right", "padding-bottom", and "padding-left" properties (e.g., padding-top: 20px;).
# 3. Padding Percentages: Padding can be set using percentage values, which are relative to the width of the containing element (e.g., padding: 5%;).
# 4. Padding Shorthand: You can use shorthand notation to set all four padding values at once (e.g., padding: 10px 20px 30px 40px;).
# 5. Padding Responsive Design: You can use media queries to set different padding values based on screen size (e.g., @media (max-width: 600px) { padding: 5px; }).
# 6. Padding Flexbox: You can use flexbox properties to control padding in flex containers (e.g., align-items: center;).
# 7. Padding Grid: You can use grid properties to control padding in grid containers (e.g., grid-gap: 10px;).
# 8. Padding Variables: You can use CSS variables to define reusable padding values throughout your stylesheet (e.g., --main-padding: 10px;).
# 9. Padding Functions: You can use CSS functions like "calc()" to perform calculations for padding properties (e.g., padding: calc(100% - 20px);).
# 10. Padding Animations: You can animate padding properties using CSS animations and transitions (e.g., transition: padding 0.5s ease;).
# 11. Padding Box Model: Padding is part of the CSS box model, which includes content, padding, border, and margin.
# 12. Padding Box Sizing: You can control how padding is calculated using the "box-sizing" property (e.g., box-sizing: border-box;).
# 13. Padding Background: Padding can affect the background color and image of an element, as it creates space between the content and the border.
# 14. Padding Overflow: Padding can affect how content overflows an element, especially when combined with the "overflow" property (e.g., overflow: hidden;).
# 15. Padding Clipping: Padding can affect how content is clipped within an element, especially when combined with the "clip-path" property (e.g., clip-path: circle(50%);).


# ------------------------------------------------------------------------------------------------------------------------------

# CSS Height and Width:
# CSS height and width properties are used to set the dimensions of HTML elements.
# 1. Height: You can set the height of an element using the "height" property (e.g., height: 100px;).
# 2. Width: You can set the width of an element using the "width" property (e.g., width: 200px;).
# 3. Height Percentages: Height can be set using percentage values, which are relative to the height of the containing element (e.g., height: 50%;).
# 4. Width Percentages: Width can be set using percentage values, which are relative to the width of the containing element (e.g., width: 50%;).
# 5. Min Height: You can set a minimum height for an element using the "min-height" property (e.g., min-height: 100px;).
# 6. Max Height: You can set a maximum height for an element using the "max-height" property (e.g., max-height: 500px;).
# 7. Min Width: You can set a minimum width for an element using the "min-width" property (e.g., min-width: 200px;).
# 8. Max Width: You can set a maximum width for an element using the "max-width" property (e.g., max-width: 800px;).
# 9. Height Auto: You can set the height to auto to allow the element to adjust its height based on its content (e.g., height: auto;).
# 10. Width Auto: You can set the width to auto to allow the element to adjust its width based on its content (e.g., width: auto;).
# 11. Height Viewport: You can set the height using viewport units (e.g., height: 100vh; for full viewport height).
# 12. Width Viewport: You can set the width using viewport units (e.g., width: 100vw; for full viewport width).
# 13. Height Flexbox: You can use flexbox properties to control height in flex containers (e.g., flex-grow: 1;).
# 14. Width Flexbox: You can use flexbox properties to control width in flex containers (e.g., flex-basis: 100px;).
# 15. Height Grid: You can use grid properties to control height in grid containers (e.g., grid-template-rows: 100px;).
# 16. Width Grid: You can use grid properties to control width in grid containers (e.g., grid-template-columns: 200px;).


# ------------------------------------------------------------------------------------------------------------------------------


# CSS Box Model:
# The CSS box model is a fundamental concept in web design that describes how elements are structured and how their dimensions are calculated.
# The box model consists of four main components: content, padding, border, and margin.
# 1. Content: The innermost part of the box model, which contains the actual content of the element (e.g., text, images).
# 2. Padding: The space between the content and the border. Padding creates space inside the element and can be set using the "padding" property (e.g., padding: 10px;).
# 3. Border: The line that surrounds the padding and content. Borders can be styled using the "border" property (e.g., border: 1px solid black;).
# 4. Margin: The outermost space that creates distance between the element and other elements. Margins can be set using the "margin" property (e.g., margin: 20px;).
# 5. Box Sizing: The "box-sizing" property controls how the width and height of an element are calculated. The default value is "content-box", which includes only the content area. The "border-box" value includes padding and border in the total width and height (e.g., box-sizing: border-box;).
# 6. Box Model Calculation: The total width and height of an element can be calculated using the following formulas:
# Total Width = Width + Padding Left + Padding Right + Border Left + Border Right + Margin Left + Margin Right
# Total Height = Height + Padding Top + Padding Bottom + Border Top + Border Bottom + Margin Top + Margin Bottom
# 7. Box Model Visualization: You can visualize the box model using browser developer tools, which show the content, padding, border, and margin areas of an element.
# 8. Box Model Debugging: You can use the "outline" property to visualize the box model of an element without affecting its layout (e.g., outline: 1px solid red;).
# 9. Box Model Flexbox: In flex containers, the box model properties can affect how flex items are sized and positioned (e.g., flex-grow, flex-shrink).
# 10. Box Model Grid: In grid containers, the box model properties can affect how grid items are sized and positioned (e.g., grid-template-areas).
# 11. Box Model Responsive Design: You can use media queries to adjust box model properties based on screen size (e.g., @media (max-width: 600px) { padding: 5px; }).
# 12. Box Model Variables: You can use CSS variables to define reusable box model values throughout your stylesheet (e.g., --main-padding: 10px;).
# 13. Box Model Functions: You can use CSS functions like "calc()" to perform calculations for box model properties (e.g., width: calc(100% - 20px);).


# ------------------------------------------------------------------------------------------------------------------------------


# CSS Display Property:
# The CSS display property controls how an element is displayed on the page. 
# It determines the layout behavior of the element and its children.
# 1. Block: The element is displayed as a block-level element, taking up the full width available (e.g., display: block;).
# 2. Inline: The element is displayed as an inline element, taking up only the width of its content (e.g., display: inline;).
# 3. Inline Block: The element is displayed as an inline block, allowing it to have width and height while still flowing with text (e.g., display: inline-block;).
# 4. Flex: The element is displayed as a flex container, allowing for flexible layouts (e.g., display: flex;).
# 5. Grid: The element is displayed as a grid container, allowing for grid-based layouts (e.g., display: grid;).


# ------------------------------------------------------------------------------------------------------------------------------

# CSS Positioning:
# CSS positioning controls how elements are positioned on the page. There are several positioning schemes in CSS:
# 1. Static: The default positioning scheme. Elements are positioned according to the normal flow of the document (e.g., position: static;).
# 2. Relative: The element is positioned relative to its normal position in the document flow (e.g., position: relative; top: 10px;).
# 3. Absolute: The element is positioned relative to its nearest positioned ancestor (e.g., position: absolute; top: 20px; left: 30px;).
# 4. Fixed: The element is positioned relative to the viewport, remaining in the same position even when scrolling (e.g., position: fixed; top: 0; left: 0;).
# 5. Sticky: The element is positioned based on the user's scroll position, becoming fixed after a certain point (e.g., position: sticky; top: 0;).
# 6. Z-Index: The z-index property controls the stacking order of positioned elements. Higher values are displayed on top of lower values (e.g., z-index: 10;).


# ------------------------------------------------------------------------------------------------------------------------------


# CSS Floating Elements:
# CSS floating elements allow you to position elements to the left or right of their container, allowing text and inline elements to wrap around them.
# 1. Float Left: The element is floated to the left of its container (e.g., float: left;).
# 2. Float Right: The element is floated to the right of its container (e.g., float: right;).
# 3. Clear: The clear property is used to control the behavior of floated elements. It can be set to left, right, both, or none (e.g., clear: both;).
# 4. Clearfix: A clearfix is a technique used to clear floated elements within a container. It can be achieved using the "clearfix" class or the "overflow" property (e.g., overflow: auto;).
# 5. Float and Clear: You can combine float and clear properties to create complex layouts (e.g., float: left; clear: right;).
# 6. Float and Flexbox: You can use float in combination with flexbox properties to create flexible layouts (e.g., display: flex; float: left;).
# 7. Float and Grid: You can use float in combination with grid properties to create grid-based layouts (e.g., display: grid; float: left;).
# 8. Float and Media Queries: You can use media queries to adjust float properties based on screen size (e.g., @media (max-width: 600px) { float: none; }).
# 9. Float and Responsive Design: You can use float to create responsive layouts that adapt to different screen sizes (e.g., float: left; width: 50%;).
# 10. Float and Accessibility: Be cautious when using float, as it can affect the accessibility of your layout. Use semantic HTML and ARIA roles to improve accessibility.
# 11. Float and Performance: Excessive use of float can lead to performance issues, especially in complex layouts. Consider using flexbox or grid for better performance.


# ------------------------------------------------------------------------------------------------------------------------------


# CSS Flexbox:
# CSS Flexbox is a layout model that allows you to create flexible and responsive layouts using a one-dimensional space.
# It provides an efficient way to align and distribute space among items in a container, even when their size is unknown or dynamic.
# 1. Flex Container: The parent element that contains flex items. It is defined using the "display: flex;" property.
# 2. Flex Items: The child elements within the flex container that are subject to flexbox properties.
# 3. Flex Direction: The direction in which flex items are placed in the flex container. It can be set to row, row-reverse, column, or column-reverse (e.g., flex-direction: row;).
# 4. Flex Wrap: Controls whether flex items should wrap onto multiple lines or stay on a single line. It can be set to nowrap, wrap, or wrap-reverse (e.g., flex-wrap: wrap;).
# 5. Justify Content: Aligns flex items along the main axis. It can be set to flex-start, flex-end, center, space-between, or space-around (e.g., justify-content: center;).
# 6. Align Items: Aligns flex items along the cross axis. It can be set to flex-start, flex-end, center, baseline, or stretch (e.g., align-items: center;).
# 7. Align Content: Aligns flex lines within the flex container when there is extra space on the cross axis. It can be set to flex-start, flex-end, center, space-between, space-around, or stretch (e.g., align-content: space-between;).
# 8. Flex Grow: Defines the ability of a flex item to grow relative to the rest of the flex items in the container. It can be set to a positive number (e.g., flex-grow: 1;).
# 9. Flex Shrink: Defines the ability of a flex item to shrink relative to the rest of the flex items in the container. It can be set to a positive number (e.g., flex-shrink: 1;).
# 10. Flex Basis: Defines the initial size of a flex item before space distribution occurs. It can be set to a length, percentage, or auto (e.g., flex-basis: 100px;).
# 11. Flex: A shorthand property that combines flex-grow, flex-shrink, and flex-basis into one declaration (e.g., flex: 1 1 100px;).
# 12. Align Self: Allows the default alignment (or the one specified by align-items) to be overridden for individual flex items. It can be set to auto, flex-start, flex-end, center, baseline, or stretch (e.g., align-self: center;).


# ------------------------------------------------------------------------------------------------------------------------------


# CSS Grid Layout:
# CSS Grid Layout is a two-dimensional layout system that allows you to create complex and responsive grid-based layouts using rows and columns.
# It provides a powerful way to control the placement and alignment of elements within a grid container.
# 1. Grid Container: The parent element that contains grid items. It is defined using the "display: grid;" property.
# 2. Grid Items: The child elements within the grid container that are subject to grid properties.
# 3. Grid Template Columns: Defines the number and size of columns in the grid container. It can be set using lengths, percentages, or the "fr" unit (e.g., grid-template-columns: 1fr 2fr;).
# 4. Grid Template Rows: Defines the number and size of rows in the grid container. It can be set using lengths, percentages, or the "fr" unit (e.g., grid-template-rows: 100px 200px;).
# 5. Grid Template Areas: Defines named grid areas for layout purposes. It can be set using a string representation of the grid layout (e.g., grid-template-areas: "header header" "sidebar content";).
# 6. Grid Gap: Defines the space between grid items. It can be set using lengths or percentages (e.g., grid-gap: 10px;).
# 7. Grid Column Start/End: Defines the starting and ending positions of a grid item within the grid columns (e.g., grid-column: 1 / 3;).
# 8. Grid Row Start/End: Defines the starting and ending positions of a grid item within the grid rows (e.g., grid-row: 1 / 2;).


# ------------------------------------------------------------------------------------------------------------------------------


# CSS Responsive Web Design:
# Responsive web design is an approach to web design that ensures that web pages look good and function well on a variety of devices and screen sizes.
# It involves using flexible layouts, images, and CSS media queries to adapt the design to different screen sizes and orientations.
# 1. Fluid Grids: Use relative units (e.g., percentages) instead of fixed units (e.g., pixels) to create flexible layouts that adapt to different screen sizes.
# 2. Flexible Images: Use CSS properties like max-width and height to ensure that images scale properly within their containers (e.g., img { max-width: 100%; height: auto; }).
# 3. Media Queries: Use CSS media queries to apply different styles based on the screen size or device type (e.g., @media (max-width: 600px) { /* styles */ }).
# 4. Breakpoints: Define breakpoints in your CSS to specify when the layout should change based on screen size (e.g., @media (min-width: 768px) { /* styles */ }).
# 5. Mobile-First Design: Start designing for the smallest screen size first and then add styles for larger screens using media queries (e.g., @media (min-width: 600px) { /* styles */ }).
# 6. Viewport Meta Tag: Use the viewport meta tag in the HTML document to control the layout on mobile browsers (e.g., <meta name="viewport" content="width=device-width, initial-scale=1.0">).
# 7. Responsive Typography: Use relative units (e.g., em, rem) for font sizes to ensure that text scales properly on different devices (e.g., font-size: 1.5em;).
# 8. Responsive Navigation: Use CSS techniques like hamburger menus or dropdowns to create responsive navigation menus that adapt to different screen sizes.
# 9. Responsive Tables: Use CSS properties like overflow and display to create responsive tables that adapt to different screen sizes (e.g., table { width: 100%; overflow-x: auto; }).
# 10. Responsive Frameworks: Consider using CSS frameworks like Bootstrap or Foundation that provide built-in responsive design features and components.
# 11. Responsive Images: Use the srcset attribute in the <img> tag to provide different image sources for different screen sizes (e.g., <img src="image.jpg" srcset="image-small.jpg 600w, image-large.jpg 1200w" alt="Responsive Image">).


# ------------------------------------------------------------------------------------------------------------------------------


# CSS Media:
# CSS media queries are used to apply different styles based on the characteristics of the device or viewport, such as screen size, resolution, and orientation.
# They are a key component of responsive web design and allow you to create adaptive layouts that work well on various devices.
# 1. Media Types: Media queries can target different media types, such as screen, print, and all (e.g., @media screen { /* styles */ }).
# 2. Media Features: Media queries can target specific features of the device, such as width, height, resolution, and orientation (e.g., @media (max-width: 600px) { /* styles */ }).
# 3. Logical Operators: You can combine multiple media queries using logical operators like and, or, and not (e.g., @media (max-width: 600px) and (orientation: landscape) { /* styles */ }).
# 4. Media Query Ranges: You can use media query ranges to target specific ranges of values (e.g., @media (min-width: 600px) and (max-width: 1200px) { /* styles */ }).
# 5. Media Query Breakpoints: Define breakpoints in your CSS to specify when the layout should change based on screen size (e.g., @media (min-width: 768px) { /* styles */ }).
# 6. Media Query Mobile-First: Start designing for the smallest screen size first and then add styles for larger screens using media queries (e.g., @media (min-width: 600px) { /* styles */ }).
# 7. Media Query Orientation: Target different orientations of the device, such as portrait and landscape (e.g., @media (orientation: landscape) { /* styles */ }).


# ------------------------------------------------------------------------------------------------------------------------------


# CSS Animations:
# CSS animations allow you to create dynamic and visually engaging effects on web pages. 
# They can be used to animate properties, transitions, and key frames.



# ------------------------------------------------------------------------------------------------------------------------------


# CSS Transitions:
# CSS transitions allow you to create smooth transitions between different states of an element.
# They are used to animate changes in CSS properties over a specified duration.
# 1. Transition Property: Specifies the CSS property to be animated (e.g., transition-property: background-color;).
# 2. Transition Duration: Specifies the duration of the transition (e.g., transition-duration: 0.5s;).
# 3. Transition Timing Function: Specifies the timing function for the transition, controlling the speed of the animation (e.g., transition-timing-function: ease-in-out;).
# 4. Transition Delay: Specifies a delay before the transition starts (e.g., transition-delay: 0.2s;).
# 5. Transition Shorthand: You can use shorthand notation to set all transition properties at once (e.g., transition: background-color 0.5s ease-in-out;).
# 6. Transition on Hover: You can create hover effects using transitions (e.g., .button:hover { background-color: blue; transition: background-color 0.5s; }).
# 7. Transition on Focus: You can create focus effects using transitions (e.g., .input:focus { border-color: blue; transition: border-color 0.5s; }).
# 8. Transition on Active: You can create active effects using transitions (e.g., .button:active { transform: scale(0.95); transition: transform 0.2s; }).
# 9. Transition on Load: You can create load effects using transitions (e.g., .fade-in { opacity: 0; transition: opacity 1s; animation: fadeIn 1s forwards; }).
# 10. Transition on Scroll: You can create scroll effects using transitions (e.g., .fade-in { opacity: 0; transition: opacity 1s; animation: fadeIn 1s forwards; }).
# 11. Transition on Resize: You can create resize effects using transitions (e.g., .box { width: 100px; transition: width 0.5s; }).
# 12. Transition on Media Queries: You can create responsive transitions using media queries (e.g., @media (max-width: 600px) { .box { width: 50px; transition: width 0.5s; } }).
# 13. Transition on JavaScript Events: You can create transitions triggered by JavaScript events (e.g., document.querySelector('.button').addEventListener('click', function() { this.classList.toggle('active'); });).
# 14. Transition on CSS Variables: You can create transitions using CSS variables (e.g., --main-color: blue; transition: background-color 0.5s;).


# ------------------------------------------------------------------------------------------------------------------------------


# CSS Keyframes:
# CSS keyframes allow you to create complex animations by defining a series of keyframes that describe the animation's states.
# 1. Keyframes Rule: The @keyframes rule is used to define the keyframes for an animation (e.g., @keyframes fadeIn { from { opacity: 0; } to { opacity: 1; } }).
# 2. Animation Name: The name of the keyframes animation (e.g., animation-name: fadeIn;).
# 3. Animation Duration: Specifies the duration of the animation (e.g., animation-duration: 1s;).
# 4. Animation Timing Function: Specifies the timing function for the animation (e.g., animation-timing-function: ease-in-out;).
# 5. Animation Delay: Specifies a delay before the animation starts (e.g., animation-delay: 0.5s;).
# 6. Animation Iteration Count: Specifies the number of times the animation should repeat (e.g., animation-iteration-count: infinite;).
# 7. Animation Direction: Specifies the direction of the animation (e.g., animation-direction: alternate;).
# 8. Animation Fill Mode: Specifies how the animation should apply styles before and after it is executing (e.g., animation-fill-mode: forwards;).
# 9. Animation Play State: Specifies whether the animation is running or paused (e.g., animation-play-state: paused;).
# 10. Animation Shorthand: You can use shorthand notation to set all animation properties at once (e.g., animation: fadeIn 1s ease-in-out 0.5s infinite alternate forwards;).


# ------------------------------------------------------------------------------------------------------------------------------


# CSS Transforms:
# CSS transforms allow you to manipulate the position, size, and shape of elements using various transformation functions.
# 1. Translate: Moves an element from its current position (e.g., transform: translate(50px, 100px);).
# 2. Scale: Resizes an element by a specified factor (e.g., transform: scale(1.5);).
# 3. Rotate: Rotates an element by a specified angle (e.g., transform: rotate(45deg);).
# 4. Skew: Skews an element along the X and Y axes (e.g., transform: skewX(20deg);).


# ------------------------------------------------------------------------------------------------------------------------------


# CSS Filters:
# CSS filters allow you to apply visual effects to elements, such as blurring, brightness, contrast, and more.
# 1. Blur: Applies a Gaussian blur to an element (e.g., filter: blur(5px);).
# 2. Brightness: Adjusts the brightness of an element (e.g., filter: brightness(150%);).
# 3. Contrast: Adjusts the contrast of an element (e.g., filter: contrast(200%);).
# 4. Grayscale: Converts an element to grayscale (e.g., filter: grayscale(100%);).
# 5. Sepia: Applies a sepia effect to an element (e.g., filter: sepia(100%);).
# 6. Invert: Inverts the colors of an element (e.g., filter: invert(100%);).
# 7. Opacity: Adjusts the opacity of an element (e.g., filter: opacity(50%);).
# 8. Hue Rotate: Rotates the hue of an element (e.g., filter: hue-rotate(90deg);).
# 9. Drop Shadow: Applies a drop shadow effect to an element (e.g., filter: drop-shadow(2px 2px 5px rgba(0, 0, 0, 0.5));).


# ------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------


# ALL THE BEST FOR YOUR FUTURE !
# I HOPE YOU WILL DO GREAT IN YOUR LIFE !
# KEEP LEARNING AND KEEP GROWING !

# STAY POSITIVE AND STAY MOTIVATED !
# BELIEVE IN YOURSELF AND YOUR ABILITIES !
# YOU CAN ACHIEVE ANYTHING YOU SET YOUR MIND TO !

# NEVER GIVE UP AND ALWAYS STRIVE FOR EXCELLENCE !
# REMEMBER, SUCCESS IS A JOURNEY, NOT A DESTINATION !
# ENJOY THE PROCESS AND HAVE FUN ALONG THE WAY !

# EMBRACE CHALLENGES AND TURN THEM INTO OPPORTUNITIES FOR GROWTH !
# STAY CURIOUS AND KEEP EXPLORING NEW HORIZONS !
# SURROUND YOURSELF WITH POSITIVE INFLUENCES AND SUPPORTIVE PEOPLE !

# LEARN FROM YOUR MISTAKES AND USE THEM AS STEPPING STONES TO SUCCESS !
# STAY HUMBLE AND GRATEFUL FOR ALL THE BLESSINGS IN YOUR LIFE !
# SHARE YOUR KNOWLEDGE AND HELP OTHERS ALONG THE WAY !

# YOU HAVE THE POWER TO MAKE A DIFFERENCE IN THE WORLD !
# BELIEVE IN YOUR DREAMS AND WORK HARD TO MAKE THEM A REALITY !
# STAY FOCUSED AND NEVER LOSE SIGHT OF YOUR GOALS !


# ------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------


# CREATOR : OJAS MANIYAR.
# DATE : 01/05/2025

# Portfolio : https://ojas-maniyar-portfolio.vercel.app
# LinkedIn : https://www.linkedin.com/in/ojasmaniyar25
# GitHub : https://www.github.com/ojasmaniyar5

# PYTHON FULL STACK DEVELOPER.
# FRONT-END DEVELOPER.
# WEBSITE CREATOR.
# WEBSITE DESIGNER.