def get_state_utilities(epsilon, rewards):
    utilities = [0] * 6
    delta = epsilon + 1
    
    def get_state(action,current_state):
        if action == "up":
            if current_state >= 3:
                return current_state
            else:
                return current_state + 3
        elif action == "down":
            if current_state <= 2:
                return current_state
            else:
                return current_state - 3
        elif action == "left":
            if current_state % 3 == 0:
                return current_state
            else:
                return current_state - 1
        elif action == "right":
            if current_state % 3 == 2:
                return current_state
            else:
                return current_state + 1

    def q_star(current_state,action):
        left_state = get_state("left", current_state)
        right_state = get_state("right", current_state)
        up_state = get_state("up", current_state)
        down_state = get_state("down", current_state)
        return (0.05 * (rewards[left_state] + old_utilities[left_state]) + 0.05 * (rewards[down_state] + old_utilities[down_state])
                + 0.9 * (rewards[up_state] + old_utilities[up_state]))
        
    while delta > epsilon:
        delta = 0 #check whethet this line is needed
        for current_state in range(len(rewards)):
            old_utilities = utilities[:]
            
            utilities[current_state] = max(
                q_star(current_state,"left")
            )
    return utilities

