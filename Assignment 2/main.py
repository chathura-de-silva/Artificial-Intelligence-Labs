def get_state_utilities(epsilon, rewards):
    utilities = [0] * len(rewards)
    delta = epsilon + 1
    while delta > epsilon:
        delta = 0
        for state in range(len(rewards)):
            old_utilities = utilities[:]
            utilities[state] = max(
                
            )
    return utilities



# def get_state_utilities(epsilon, rewards):
#     utilities = [0] * len(rewards)
#     delta = epsilon + 1
#     while delta > epsilon:
#         delta = 0
#         for i in range(len(rewards)):
#             old_utility = utilities[i]
#             utilities[i] = rewards[i] + max(utilities[i-1], utilities[i+1])
#             delta = max(delta, abs(old_utility - utilities[i]))
#     return utilities