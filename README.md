<p align="center">
    <picture>
      <source 
        srcset="./banner.png"
        media="(prefers-color-scheme: dark)"
      />
      <img 
        src="https://github.com/Chathura-De-Silva/Artificial-Intelligence-Labs/blob/master/banner.png" 
        alt="Academease Preview"
        width="800"
       />
    </picture>
  </p>

## Assignment 1: Delivery Optimization

Optimize delivery routes for a courier service within a city using the Hill-Climbing algorithm.
<br>
**Python version 3.8 Recommended.**


<br>

## Assignment 2 - Markov Decision Process



## Overview

*   Pretend an agent is trying to plan how to act in a 3x2 world.
Figure 1 shows the world, the rewards associated with each state, and the dynamics.
*   There are 5 possible actions: north, east, south, west and stay still. The first 4 actions
succeed with probability 0.9 and go to a right angle of the desired direction with
probability 0.05.
* The fifth action, “do nothing,”
succeeds with probability 1.
*   The rewards associated with each state are
R(1 : 6) = [−0.1, − 0.1, + 1, − 0.1, − 0.1, − 0.05] respectively and are also shown in figure 1.
*   State 3 is the only terminal state.
*   Goal is calculating utilities and then deciding best policies for each state.

Figure 1 :
#### States
4 |  5|6
:-------------------------:|:-------------------------:|:-------------------------:
1  |  2|3

#### Immediate Rewards
-0.01|  -0.01|-0.05
:-------------------------:|:-------------------------:|:-------------------------:
-0.01  |  -0.01|0 

* Utility of 3 = +1

<br>

**Python version 3.12 Recommended.**

<br>

---
*   For more information about the lab exercises or specific implementations, refer the README files included in respective assignment directory.

*   **Note:** This repository is maintained for educational purposes. Please refer to your institution's guidelines on academic integrity and code sharing before using any code from this repository in your own assignments or projects.
