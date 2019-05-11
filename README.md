# **Go-Reader**

## **What**

This is a program that could analyze Go games. LeelaZero engine will be used to generate winning rate and next moves for the analysis.

## **Basic Features**

This program has 2 basic functionalities:

1. Go board image processing.
2. SGF file analysis.

### Go board image processing

This part transforms an image of a Go board to an SGF game record file.

There are 2 types of Go board images to consider:

* A screenshot of Go board from applications.
* A photo of a Go board from the real world.

It might be easy to identify all the positions of stones in a screenshot, but identifying stone positions from a real world Go board could be harder, as the stones could be improperly placed.

### SGF file analysis

SGF format is usually used to store Go game records. This part of the program will take an SGF file as input and use LeelaZero to generate statistics of this particular Go game.

Specifically, we wanted to generate the following:

1. A **curve** (or graph) of the winning rates, for each move being played. 
Example graphs:

2. **Worst moves** analysis. Record the worst moves for each player and show the **drops** (in percentage) in winning rate. We could specifiy the number of moves being displayed for each player, e.g, 10 worst moves for each.

3. AI **matching rate**. Indicate the matching rate of each player. One move is *"matched"* with LeelaZero when the actual move being played matches one of the options considered by LeelaZero. The matching rate is calculated as **number of matched moves** / **number of total moves**. The matching rate can also be calculated in different stages of a game, e.g, move 1-60, 60-180 and after 180. The matching rate could be displayed as a **bar graph**.

4. **Mean & Variance** of winning rate differences (including the possibility of increased winning rate). Still, this could be calculated in different stages of a game.

**Problem: what file format should we use to store all these information? How do we display these information?**

Maybe a txt file will suffice.

We can further generate a new SGF file containing information about **winning rates**, **bad moves** and **LeelaZero recommended moves** for actual moves that are not matched with LeelaZero. Winning rate, bad moves could be put into the **comment** of SGF, while LeelaZero recommended moves could be added as **new branches**.

## Next Steps

- [ ] Take an SGF file to generate winning rate for each move, put into a file.
- [ ] Implement data analysis mechanisms, put new stats into a file.
- [ ] Transform **screenshots** of the Go board into SGF files.