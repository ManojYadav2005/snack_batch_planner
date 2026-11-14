# Reflection

When I first walked up to Ramesh's stall I thought the problem was simple: he opens too much and wastes it. I planned to just count cups and suggest a number. What I got wrong was assuming he had one type of customer. He doesn't. Students hit the stall between 12 and 2, the warden and hostel staff come specifically for vada between 3 and 4, and there's a small late-night group he serves more out of habit than profit. That's three different demand windows I had flattened into one average.

The first thing I would cut is the carry_over column in the CSV. I tracked it thinking it would matter for the algorithm, but it added confusion during data entry and I never ended up using it in the final script. Next time I'd keep the sheet to three columns: item, hour, sold.

AI saved me real time on the script skeleton and the README structure. I described what I wanted the output to look like and it generated a working draft in a few minutes. Where it wasted time was the first version of the algorithm — it averaged liters opened instead of liters consumed. I had to go back, explain the unsold-milk problem, and get it re-done. That back-and-forth cost me about 40 minutes I should have spent at the stall for a second visit.

The thing Ramesh said that actually changed what I built: "Puff sabse zyada waste hoti hai." He said it casually, like it was obvious, but it made me realize the puff problem is not a quantity problem — it's a time-of-day problem. Puffs go soft after two hours no matter how many you fry. I added a note in the output for that instead of pretending the tool solves it.

This tool should not be trusted on exam days, event days, or any Monday after a long weekend. Those days need a manual override, not an average.
