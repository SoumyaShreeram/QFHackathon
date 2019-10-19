def Volume_Calculations(results):
    key_results = np.zeros([number_of_keys])
    #print(count)
    states = list(count.keys())
    probabilities = list(count.values())
    #print('states',states)
    #print('probailities',probabilities)
    for i in range(len(states)): 
        state = states[i]
        #print(range(len(str(state))))
        for j in range(len(str(state))):
            #print('Qbit val', int(state[j]))
            if int(state[j]) == 1:
                #print(probabilities[i])
                key_results[j]+=probabilities[i]
    key_results=key_results/float(shots)
    return(key_results)
