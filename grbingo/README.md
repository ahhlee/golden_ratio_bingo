# Golden Ratio Bingo

This is a project created for the /r/thegoldenratio4 subreddit as a fun way to play bingo based on content that frequently comes up in social media account about a family of 5 golden retrievers.

The project takes in a Google Sheet with a list of common scenarios that happen to the dogs, such as "Venk did a dance at dinner time". The program randomly selects 24 entries from the spreadsheet, and a "Free Space" and generates a 5 x 5 Bingo Card Grid of scenarios to be checked off.

********************************

## Requirements:
-random
-requests
-pandas
-io
-tabulate

*****

## To Run:

To run install required modules via pip install. 

Once random, requests, pandas, io, and tabulate modules have been installed use the following command to run the program in the terminal:

**python grbingo.py**

*********
###Example Output:

+---------------------------+--------------------------+-----------------------+-------------------------+------------------------+
| B                         | I                        | N                     | G                       | O                      |
+===========================+==========================+=======================+=========================+========================+
| Venk dances for a meal    | Guac spins               | Voodoo chomps someone | Chief Brody lays on his | Hopper does a schnoop  |
|                           |                          |                       | back with a toy         | loop while playing tug |
+---------------------------+--------------------------+-----------------------+-------------------------+------------------------+
| Voodoo tries to eat       | WAFFLES                  | Someone eats a roasty | Voodoo spins            | Venk spins             |
| something that's not      |                          |                       |                         |                        |
| VoodsFoods                |                          |                       |                         |                        |
+---------------------------+--------------------------+-----------------------+-------------------------+------------------------+
| Venk is the MOON!         | Hopper gets the ball     | Free Space            | Voodoo lays down in the | Hopper goes for a run  |
|                           | first when playing fetch |                       | middle of a walk        |                        |
|                           | in the water             |                       |                         |                        |
+---------------------------+--------------------------+-----------------------+-------------------------+------------------------+
| Venk hides under the desk | Hopper food slide (so    | Guac eats inside      | VoodsFoods is served on | Voodoo states his      |
| to avoid walking          | cool)                    |                       | the patio               | opinions (whines)      |
+---------------------------+--------------------------+-----------------------+-------------------------+------------------------+
| Guac growls or barks at a | Hopper has a ball that   | Elevator ride         | At least three dogs are | Greeeeeeen Beeeeeeans! |
| ball                      | Guac wants               |                       | playing together        |                        |
+---------------------------+--------------------------+-----------------------+-------------------------+------------------------+
