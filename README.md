# Assignment 0 (Warm-Up, Variant A): Clean the Wumpus Cave

## Project Overview

This project involves validating existing cleaning plans for maps and generating new plans. The validation task ensures that given plans clean all designated empty cells on the map, while the generation task creates new plans to achieve the same goal.

## Approach

### Plan Validation (`CheckPlan` Class)

**Objective**: Verify if a given plan cleans all designated empty cells on the map.

**Logic and Ideas**:
1. **Start Positions and Portals**: Considers start positions znd follow the plan and check if all cells got cleand that makes it a good plan otherwise it's bad plan and if you land on portal you will automatically teleported to the other portal . when you don't have an intial satrt then you will iterate for each empty cell as a intial start and check the plan If all cells got cleaned in each start positin then it is a good plan othewise it is not
2. **Movement Logic**: Translates plan steps into movements (N, E, S, W) and handles teleportation with portals.
3. **Result Interpretation**: Classifies plans as "GOOD" or "BAD" based on whether all empty cells are cleaned.

### Plan Generation (`FindPlan` Class)

**Objective**: Generate plans that clean all designated empty cells on the map.

**Logic and Ideas**:
1. **Random Plan Generation**: Uses a randomly generated sequence to explore a wide range of potential solutions.
2. **Iterative Plan Refinement**: Starts with a random plan and increases its length iteratively until a valid plan is found.
3. **Validation Integration**: Validates generated plans using the validation logic to ensure effectiveness.

## Further improvement
1. **Better search plan**: There was an idea to use DFS to solve the find-plan problem for a given start. The idea was to use a DFS to store the S point and then add the neighbors and their directions at each step, untill the queue is empty. When there is no start, we could have the top left empty cell as a start, find a plan for it, and then add a set of NENENENE sequence to reach that cell, followed by the same DFS algorithm for the start position.  However, it was needless as the random solution performed very well. 

