def get_state_utilities(epsilon, rewards):
    utilities = [0] * 6
    delta = epsilon + 1
    
    def q_star(current_state,action):
        
        def get_state(action,current_state):
            if action == 0:
                if current_state >= 3:
                    return current_state
                else:
                    return current_state + 3
            elif action == 2:
                if current_state <= 2:
                    return current_state
                else:
                    return current_state - 3
            elif action == 3:
                if current_state % 3 == 0:
                    return current_state
                else:
                    return current_state - 1
            elif action == 1:
                if current_state % 3 == 2:
                    return current_state
                else:
                    return current_state + 1
            
        if action > 3 or action < 0:
            if action == 4:
                return rewards[current_state] + old_utilities[current_state]
            else:    
                raise ValueError("Action must be between 0 and 4")
        
        side_state_1 = get_state(action-1 if action != 0 else 3, current_state)
        desired_state  = get_state(action, current_state)
        side_state_2 = get_state(action+1 if action != 3 else 0 , current_state)
        q_star_value = 0.05 * (rewards[side_state_1] + old_utilities[side_state_1]) + 0.05 * (rewards[side_state_2] + old_utilities[side_state_2]) + 0.9 * (rewards[desired_state] + old_utilities[desired_state])
        return q_star_value
   
    while delta > epsilon:
        delta = 0 #check whethet this line is needed
        old_utilities = utilities[:]
        for current_state in range(len(rewards)):
            utilities[current_state] = max(q_star(current_state,0), q_star(current_state,1), q_star(current_state,2), q_star(current_state,3), q_star(current_state,4))
            delta = max(delta, abs(old_utilities[current_state] - utilities[current_state]))
        print(utilities,delta)
    return utilities

print(get_state_utilities(1, [-0.1, -0.1, 1, -0.1, -0.1, -0.05]))