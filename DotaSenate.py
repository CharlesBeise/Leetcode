def predictPartyVictory(senate):
    senate = list(senate)
    countR = 0
    countD = 0

    # Count how many of each party are in the senate
    for i in senate:
        if i == "D":
            countD += 1
        else:
            countR += 1

    vote = 0

    while True:
        # Iterate through the voters and tally votes or remove voter
        i = 0
        while i < len(senate):
            if senate[i] == 'D':
                if vote > 0:
                    senate.pop(i)
                    countD -= 1
                else:
                    i += 1
                vote -= 1
            else:
                if vote < 0:
                    senate.pop(i)
                    countR -= 1
                else:
                    i += 1
                vote += 1
        # Check if someone won
        if vote > countD:
            return "Radiant"
        elif vote < -countR:
            return "Dire"


if __name__ == '__main__':
    senString = "RDRDRDRDRDRDRDRDRDDDDDDDDDDDD"
    print(predictPartyVictory(senString))




"""
- Keep running count of votes:
    - R = +1
    - D = -1
- At each voter check state of vote:
    - If voter is D 
        - And vote is positive:
            - Delete voter
            - Decrease vote by 1
        - If vote is negative:
            - Decrease vote by 1
    - If voter is R
        - And vote is positive:
            - Increase vote by 1
        - If vote is negative:
            - Delete voter
            - Increase vote by 1
- Loop through string until only R or D remains
    - Possible checks to see if finished:
        - Iterate through string to see if only R or D remains
        - Check if vote increased/decreased by an amount equal to length of 
            "senate" string
        - Keep a count of how many members are in each party, if the vote is
            ever more than one party can overcome then the vote is over
"""
