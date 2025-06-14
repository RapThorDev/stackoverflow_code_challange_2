# [Stackoverflow](https://stackoverflow.com) Code Challenge #2: Secret messages in game boards


> [!CAUTION]
> Sorry for my English!


Code Challange #2 Stackoverflow URL: [https://stackoverflow.com/beta/challenges/79651567/code-challenge-2-secret-messages-in-game-boards](https://stackoverflow.com/beta/challenges/79651567/code-challenge-2-secret-messages-in-game-boards)

- [Stackoverflow Code Challenge #2: Secret messages in game boards](#stackoverflow-code-challenge-2-secret-messages-in-game-boards)
  - [Summary](#summary)
  - [Plan](#plan)
    - [Examples](#examples)
      - [Values](#values)
      - [Words to encode with 8 or 9 characters](#words-to-encode-with-8-or-9-characters)
        - [SECRETED](#secreted)


> [!WARNING]  
> In Github Markdown can't use `<style>`, so it not render tables (in Plan examples and more correctly). <br/>Try to open another markdown reader what can handle `<style>` tags. 

## Summary

In this challange I create a Python application what encode secret messages to Sudoku boards.

It can encode every printable ASCII characters. 

> [!NOTE]
> After I done with the encoding mechanism, would like to create a decoding mechanism too.<br/>But with an opencv technology

## Plan

Sketch some plan about the mechanism and brainstorming: [Plan PDF](./README/Stackoverflow_-_Code_Challange_2_Plan.pdf)

Printable ASCII characters (DEC): `32` - `255`


Return SUDOKU table structure:

`P` : Next position (SUDOKU block) of the next character (value: 1 - 9)<br/>
<br/>
`C` : Commands ... (Yeah good name soo professional ...) (value: 1 - 3 or 5 or 7 - 8)<br/>
 1-3 for value higher than 100 | 5 if this is the first character | 7-9 if the value higher than 100 and this is the first character (in this case we just subtract  1-3 from the 10)<br/>
4 or 6 for NULL values (If the word length smaller than 9 we can ignore this blocks and generate random values in this block for some SALT ;D )
<br/>
`V` : Value: 1 - 9 except after the `C` first cell, because it just between 2 and 9. And if its 1 this is a number divisible by 10
<br/>

<style>
    .flex-wrap {
        display: flex;
        flex-flow: row wrap;
        gap: 12px
    }

    table {
        padding: 0;
        margin: 0;
    }

    td {
        border: 1px solid black;
        width: 24px;
        height: 24px;
        text-align: center;
        padding: 0;
    }

    .flex-col {
        display: flex;
        flex-flow: column;
        gap: 3px;
        padding-bottom: 32px
    }

    .flex-row {
        display: flex;
        flex-flow: row;
        gap: 4px;
    }

    td[data-status="P"] {
        background-color: rgba(255, 50, 50, 0.5)
    }

    td[data-status="C"] {
        background-color: rgba(50, 50, 250, 0.5)
    }
</style>

<div class="flex-wrap">
<div class="flex-col">
<div class="flex-row">
<table>
<tr> <td data-status="P">P</td><td data-status="C">C</td><td>V</td> <tr>
<tr> <td>V</td><td>V</td><td>V</td> <tr>
<tr> <td>V</td><td>V</td><td>V</td> <tr>
</table>
<table>
<tr> <td>V</td><td data-status="P">P</td><td data-status="C">C</td> <tr>
<tr> <td>V</td><td>V</td><td>V</td> <tr>
<tr> <td>V</td><td>V</td><td>V</td> <tr>
</table>
<table>
<tr> <td>V</td><td>V</td><td data-status="P">P</td> <tr>
<tr> <td data-status="C">C</td><td>V</td><td>V</td> <tr>
<tr> <td>V</td><td>V</td><td>V</td> <tr>
</table>
</div>
<div class="flex-row">
<table>
<tr> <td>V</td><td>V</td><td>V</td> <tr>
<tr> <td data-status="P">P</td><td data-status="C">C</td><td>V</td> <tr>
<tr> <td>V</td><td>V</td><td>V</td> <tr>
</table>
<table>
<tr> <td>V</td><td>V</td><td>V</td> <tr>
<tr> <td>V</td><td data-status="P">P</td><td data-status="C">C</td> <tr>
<tr> <td>V</td><td>V</td><td>V</td> <tr>
</table>
<table>
<tr> <td>V</td><td>V</td><td>V</td> <tr>
<tr> <td>V</td><td>V</td><td data-status="P">P</td> <tr>
<tr> <td data-status="C">C</td><td>V</td><td>V</td> <tr>
</table>
</div>
<div class="flex-row">
<table>
<tr> <td>V</td><td>V</td><td>V</td> <tr>
<tr> <td>V</td><td>V</td><td>V</td> <tr>
<tr> <td data-status="P">P</td><td data-status="C">C</td><td>V</td> <tr>
</table>
<table>
<tr> <td>V</td><td>V</td><td>V</td> <tr>
<tr> <td>V</td><td>V</td><td>V</td> <tr>
<tr> <td>V</td><td data-status="P">P</td><td data-status="C">C</td> <tr>
</table>
<table>
<tr> <td data-status="C">C</td><td>V</td><td>V</td> <tr>
<tr> <td>V</td><td>V</td><td>V</td> <tr>
<tr> <td>V</td><td>V</td><td data-status="P">P</td> <tr>
</table>
</div>
</div>
<div class="flex-col" style="font-size: 10px">
<div class="flex-row">
<table>
<tr> <td data-status="P">1-9</td><td data-status="C"> 1-9</td><td> 1-9</td> <tr>
<tr> <td>1-9</td><td>1-9</td> <td>1-9</td> <tr>
<tr> <td>1-9</td><td>1-9</td> <td>1-9</td> <tr>
</table>
<table>
<tr>  <td>1-9</td><td data-status="P">1-9</td><td data-status="C">1-9</td> <tr>
<tr>  <td> 1-9</td> <td>1-9</td> <td>1-9</td> <tr>
<tr>  <td>1-9</td> <td>1-9</td><td>1-9</td> <tr>
</table>
<table>
<tr>  <td>1-9</td> <td>1-9</td><td data-status="P">1-9</td> <tr>
<tr> <td data-status="C"> 1-9</td> <td>1-9</td> <td>1-9</td> <tr>
<tr>  <td>1-9</td> <td>1-9</td> <td>1-9</td> <tr>
</table>
</div>
<div class="flex-row">
<table>
<tr>  <td>1-9</td> <td>1-9</td> <td>1-9</td> <tr>
<tr> <td data-status="P">1-9</td><td data-status="C">1-9</td> <td>1-9</td> <tr>
<tr>  <td>1-9</td> <td>1-9</td> <td>1-9</td> <tr>
</table>
<table>
<tr>  <td>1-9</td> <td>1-9</td> <td>1-9</td> <tr>
<tr>  <td>1-9</td><td data-status="P">1-9</td><td data-status="C"> 1-9</td> <tr>
<tr>  <td> 1-9</td> <td>1-9</td> <td>1-9</td> <tr>
</table>
<table>
<tr>  <td>1-9</td> <td>1-9</td> <td>1-9</td> <tr>
<tr>  <td>1-9</td> <td>1-9</td><td data-status="P">1-9</td> <tr>
<tr> <td data-status="C"> 1-9</td> <td> 1-9</td> <td>1-9</td> <tr>
</table>
</div>
<div class="flex-row">
<table>
<tr>  <td>1-9</td> <td>1-9</td> <td>1-9</td> <tr>
<tr>  <td>1-9</td> <td>1-9</td> <td>1-9</td> <tr>
<tr> <td data-status="P">1-9</td><td data-status="C"> 1-9</td> <td> 1-9</td> <tr>
</table>
<table>
<tr>  <td> 1-9</td> <td>1-9</td> <td>1-9</td> <tr>
<tr>  <td>1-9</td> <td>1-9</td> <td>1-9</td> <tr>
<tr>  <td>1-9</td><td data-status="P">1-9</td><td data-status="C"> 1-9</td> <tr>
</table>
<table>
<tr> <td data-status="C"> 1-9</td> <td> 1-9</td> <td>1-9</td> <tr>
<tr>  <td>1-9</td> <td>1-9</td> <td>1-9</td> <tr>
<tr>  <td>1-9</td> <td>1-9</td><td data-status="P">1-9</td> <tr>
</table>
</div>
</div>
</div>


### Examples

#### Values

In these examples, we only examine the DEC value of ASCII characters. The `P` cell stay empty.

<div class="flex-wrap">
<table>
33
<tr><td data-status="P"> </td><td data-status="C"> </td><td>3</td><tr>
<tr><td> </td><td> </td><td> </td><tr>
<tr><td> </td><td> </td><td> </td><tr>
</table>

<table>
32
<tr><td data-status="P"> </td><td data-status="C"> </td><td>2</td><tr>
<tr><td> </td><td> </td><td> </td><tr>
<tr><td> </td><td> </td><td> </td><tr>
</table>

<table>
40
<tr><td data-status="P"> </td><td data-status="C"> </td><td>1</td><tr>
<tr><td>1</td><td> </td><td> </td><tr>
<tr><td> </td><td> </td><td> </td><tr>
</table>

<table>
41
<tr><td data-status="P"> </td><td data-status="C"> </td><td> </td><tr>
<tr><td>1</td><td> </td><td> </td><tr>
<tr><td> </td><td> </td><td> </td><tr>
</table>

<table>
99
<tr><td data-status="P"> </td><td data-status="C"> </td><td> </td><tr>
<tr><td> </td><td> </td><td> </td><tr>
<tr><td> </td><td> </td><td>9</td><tr>
</table>
</div>

<br/>

After value 100 we need to rethink this solution. So we need to use `C` cell.

The rules are simples:

 - After value 100 (100 - 167) we use it like 32 and write value 1 in the `C` cell.

And we have just another 67 solution to write DEC values (99 - 32)

 - 168 - 235, write value 2 in the `C` cell.
 - 236 - 255, write value 3 in the `C` cell.

<div class="flex-wrap">
<table>
100
<tr><td data-status="P"> </td><td data-status="C">1</td><td>2</td><tr>
<tr><td> </td><td> </td><td> </td><tr>
<tr><td> </td><td> </td><td> </td><tr>
</table>

<table>
101
<tr><td data-status="P"> </td><td data-status="C">1</td><td>3</td><tr>
<tr><td> </td><td> </td><td> </td><tr>
<tr><td> </td><td> </td><td> </td><tr>
</table>

<table>
108
<tr><td data-status="P"> </td><td data-status="C">1</td><td>1</td><tr>
<tr><td>1</td><td> </td><td> </td><tr>
<tr><td> </td><td> </td><td> </td><tr>
</table>

<table>
168
<tr><td data-status="P"> </td><td data-status="C">2</td><td>2</td><tr>
<tr><td> </td><td> </td><td> </td><tr>
<tr><td> </td><td> </td><td> </td><tr>
</table>

<table>
236
<tr><td data-status="P"> </td><td data-status="C">3</td><td>2</td><tr>
<tr><td> </td><td> </td><td> </td><tr>
<tr><td> </td><td> </td><td> </td><tr>
</table>
</div>


#### Words to encode with 8 or 9 characters

##### SECRETED

||||||||||||
|-|-|-|-|-|-|-|-|-|-|-|
|#BLOCK|-|1 |2 |3 |4 |5 |6 |7 |8 |9 |
|CHAR |-|S |E |C |R |E |T |E |D |-|
|DEC  |-|83|69|67|82|69|84|69|68|-|

<br/>

> [!NOTE]
> In this case we don't randomize the word characters.
 
<div class="flex-col" style="font-size: 10px">
<div class="flex-row">
<table>
<tr> <td data-status="P">2</td><td data-status="C">5</td><td>  </td> <tr>
<tr> <td> </td><td> </td> <td> </td> <tr>
<tr> <td> </td><td>3</td><td></td> <tr>
</table>
<table>
<tr>  <td> </td><td data-status="P">3</td><td data-status="C"> </td> <tr>
<tr>  <td>  </td> <td> </td> <td> </td> <tr>
<tr>  <td>9</td> <td> </td><td> </td> <tr>
</table>
<table>
<tr>  <td> </td> <td> </td><td data-status="P">4</td> <tr>
<tr> <td data-status="C">  </td> <td> </td> <td> </td> <tr>
<tr>  <td> </td> <td>7</td> <td> </td> <tr>
</table>
</div>
<div class="flex-row">
<table>
<tr>  <td></td> <td>2</td> <td> </td> <tr>
<tr> <td data-status="P">5</td><td data-status="C"> </td> <td> </td> <tr>
<tr>  <td> </td> <td> </td> <td> </td> <tr>
</table>
<table>
<tr>  <td>9</td> <td> </td> <td> </td> <tr>
<tr>  <td> </td><td data-status="P">6</td><td data-status="C">  </td> <tr>
<tr>  <td>  </td> <td> </td> <td> </td> <tr>
</table>
<table>
<tr>  <td> </td> <td> </td> <td> </td> <tr>
<tr>  <td>4</td> <td> </td><td data-status="P">7</td> <tr>
<tr> <td data-status="C">  </td> <td>  </td> <td> </td> <tr>
</table>
</div>
<div class="flex-row">
<table>
<tr>  <td> </td> <td> </td> <td>9</td> <tr>
<tr>  <td> </td> <td> </td> <td> </td> <tr>
<tr> <td data-status="P">8</td><td data-status="C">  </td> <td>  </td> <tr>
</table>
<table>
<tr>  <td>  </td> <td> </td> <td> </td> <tr>
<tr>  <td>8</td> <td> </td> <td> </td> <tr>
<tr>  <td> </td><td data-status="P">9</td><td data-status="C">  </td> <tr>
</table>
<table>
<tr> <td data-status="C">6</td> <td>  </td> <td> </td> <tr>
<tr>  <td> </td> <td>5</td><td> </td> <tr>
<tr>  <td> </td> <td> </td><td data-status="P">1</td> <tr>
</table>
</div>
</div>

We can use longer words, it render 2 or more Sudoku table. Now I don't know how to rendomize the sudoku blocks and get the first character. But maybe a generated 'fake' sudoku table what is an option table with 4 and 6 values in `C` cell and the `P` cell init the Sudoku tables sequence. BUT it just a FUTURE FEATURE.

Thanks!