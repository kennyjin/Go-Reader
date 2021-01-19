# **Go-Reader**

## **What**

This is a program that could analyze Go games. LeelaZero engine will be used to generate winning rate and next moves for the analysis.

## **Basic Features**

This program has 1 basic functionality:

1. SGF file analysis.


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

- [ ] Generate winrate plots. (using matplotlib or plotly)
- [ ] Modify the definition of matching. (e.g. first 2 moves)
- [ ] Generate bar plot & scatter plot for winrate difference mean and variance.
- [ ] Generate bar plot for matching rate. (for different stages of a game)
- [ ] Display worst moves (and best moves), connect with the winrate plot.
- [ ] Need to figure out a way to read lz-analyze outputs. (Now we can only read lz-genmove_analyze)