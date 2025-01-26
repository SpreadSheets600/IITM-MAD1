## Week 2 Graded Assesment

**Question 1**: Consider the following code:

```html
<p id="“abc”" class="“First" Second”>This is a paragraph</p>
```

Which of the following statements is true with respect to the above code?

**Explanation**: The Paragraph has two different classes, “First” and “Second”.

**Question 2**: Consider a character set Q, which consists of only those
characters used in the sentence, "the five boxing wizards jump quickly" If this sentence is to be saved in a document with minimum encoding, what will be the size of the document given that no other information or context is to be saved?

**Explanation**: The sentence uses 26 unique characters. To encode each
character, we need 5 bits. The sentence has 36 characters, so the total size is 180 bits.

**Question 3**: Suppose you have a document which contains only lower
case alphabets. How many bits are required to encode a character such that the size of the document is minimum?

**Explanation**: There are 26 lowercase
alphabets. To encode each character with the same length, we need 5 bits.

**Question 4**: Consider the following code :

```html
<! DOCTYPE html>
<html lang="en">
  <head>
    <title>Document</title>
    <style>
      body {
      color: red;
      color: green;
      color: yellow;
    </style>
  </head>
  <body>
    IIT Madras
  </body>
</html>
```

What will be the color of text “IIT Madras”?

**Explanation**: The last color specified in the CSS will be applied. Therefore, the text "IIT Madras" will be yellow.

**Question 5**: How will a browser render the following code?

```html
<div>
  Welcome to<span style="visibility: hidden">Modern</span>Application
  Development<span style="display: none">Course</span> Test.
</div>
```

**Explanation**: The `visibility: hidden` style hides the text but still takes up space, while `display: none` removes the text and its space. Therefore, the rendered text will be "Welcome to Application Development Test."

**Question 6**: Which of the following code segments will display the result given below?

```html
<!DOCTYPE html>
<html>
  <body>
    <h1>Welcome to IITM ONLINE DEGREE</h1>
    <p>
      <b>IIT Madras</b>, India’s top technical institute, <br />
      welcomes you to the <b> world’s first BSc Degree program </b> <br />
      in Programming and Data Science.
    </p>
    <a url="https://onlinedegree.iitm.ac.in/">Click here for more details</a>
  </body>
</html>
```

```html
<!DOCTYPE html>
<html>
  <body>
    <h1>Welcome to IITM ONLINE DEGREE</h1>
    <p>
      <b>IIT Madras</b>, India’s top technical institute, <br />
      welcomes you to the <strong> world’s first BSc Degree program </strong>
      <br />
      in Programming and Data Science.
    </p>
    <a href="https://onlinedegree.iitm.ac.in/">Click here</a>
    for more details
  </body>
</html>
```
