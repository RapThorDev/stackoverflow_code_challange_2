# [Stackoverflow](https://stackoverflow.com) Code Challenge #2: Secret messages in game boards

Code Challange #2 Stackoverflow URL: [https://stackoverflow.com/beta/challenges/79651567/code-challenge-2-secret-messages-in-game-boards](https://stackoverflow.com/beta/challenges/79651567/code-challenge-2-secret-messages-in-game-boards)

- [Summary](#summary)
- [Plan](#plan)
  - [Examples](#examples)

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
1-3 for value higher than 100 | 5 if this is the first character | 7-9 if the value higher than 100 and this is the first character (in this case we just subtract 1-3 from the 10)<br/>
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
<tr> <td data-status="P">1-9</td><td data-status="C">1-3</td><td>2-9</td> <tr>
<tr> <td>1-9</td><td>1-9</td> <td>1-9</td> <tr>
<tr> <td>1-9</td><td>1-9</td> <td>1-9</td> <tr>
</table>
<table>
<tr>  <td>1-9</td><td data-status="P">1-9</td><td data-status="C">1-9</td> <tr>
<tr>  <td>2-9</td> <td>1-9</td> <td>1-9</td> <tr>
<tr>  <td>1-9</td> <td>1-9</td><td>1-9</td> <tr>
</table>
<table>
<tr>  <td>1-9</td> <td>1-9</td><td data-status="P">1-9</td> <tr>
<tr> <td data-status="C">1-3</td> <td>1-9</td> <td>1-9</td> <tr>
<tr>  <td>1-9</td> <td>1-9</td> <td>1-9</td> <tr>
</table>
</div>

<div class="flex-row">
<table>
<tr>  <td>1-9</td> <td>1-9</td> <td>1-9</td> <tr>
<tr> <td data-status="P">1-9</td><td data-status="C">2-3</td> <td>1-9</td> <tr>
<tr>  <td>1-9</td> <td>1-9</td> <td>1-9</td> <tr>
</table>
<table>
<tr>  <td>1-9</td> <td>1-9</td> <td>1-9</td> <tr>
<tr>  <td>1-9</td><td data-status="P">1-9</td><td data-status="C">1-3</td> <tr>
<tr>  <td>2-9</td> <td>1-9</td> <td>1-9</td> <tr>
</table>
<table>
<tr>  <td>1-9</td> <td>1-9</td> <td>1-9</td> <tr>
<tr>  <td>1-9</td> <td>1-9</td><td data-status="P">1-9</td> <tr>
<tr> <td data-status="C">1-3</td> <td>2-9</td> <td>1-9</td> <tr>
</table>
</div>

<div class="flex-row">
<table>
<tr>  <td>1-9</td> <td>1-9</td> <td>1-9</td> <tr>
<tr>  <td>1-9</td> <td>1-9</td> <td>1-9</td> <tr>
<tr> <td data-status="P">1-9</td><td data-status="C">1-3</td> <td>2-9</td> <tr>
</table>
<table>
<tr>  <td>2-9</td> <td>1-9</td> <td>1-9</td> <tr>
<tr>  <td>1-9</td> <td>1-9</td> <td>1-9</td> <tr>
<tr>  <td>1-9</td><td data-status="P">1-9</td><td data-status="C">1-3</td> <tr>
</table>
<table>
<tr> <td data-status="C">1-3</td> <td>2-9</td> <td>1-9</td> <tr>
<tr>  <td>1-9</td> <td>1-9</td> <td>1-9</td> <tr>
<tr>  <td>1-9</td> <td>1-9</td><td data-status="P">1-9</td> <tr>
</table>
</div>
</div>
</div>


### Examples

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