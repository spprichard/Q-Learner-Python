"""
Template for implementing QLearner  (c) 2015 Tucker Balch
"""

import numpy as np
import random as rand

class QLearner(object):

    def __init__(self, \
        num_states=100, \
        num_actions = 4, \
        alpha = 0.2, \
        gamma = 0.9, \
        rar = 0.5, \
        radr = 0.99, \
        dyna = 0, \
        verbose = False):

        self.verbose = verbose
        self.num_actions = num_actions
        self.num_states = num_states
        self.s = 0
        self.a = 0
        # self.Q = np.random.rand(num_states,num_actions)
        self.Q = np.zeros((num_states, num_actions))
        self.Tcount = np.full((num_states, 3), 0.00001)
        self.R = np.zeros((num_states, num_actions))
        self.dyna = dyna
        self.rar = rar
        self.radr = radr
        self.gamma = gamma
        self.alpha = alpha
        self.actionList = list(range(0, num_actions))
        # self.experience = np.full((num_states, 3), 0.00001)
        self.experience = []


    def querysetstate(self, s):
        """
        @summary: Update the state without updating the Q-table
        @param s: The new state
        @returns: The selected action
        """
         # Decide weather we sohuld take random action or not
        if rand.random() < self.rar:
            action = rand.sample(self.actionList, 1)
            self.s = s
            self.a = action
            return action

        action = self.Q[self.s].argmax()
        # Save state
        self.s = s
        # Save action
        self.a = action
        
        if self.verbose: print "s =", s,"a =",action
        
        return action

    def query(self,s_prime,r):
        """
        @summary: Update the Q table and return an action
        @param s_prime: The new state
        @param r: The ne state
        @returns: The selected action
        """
        # Update Q-Table <self.s, self.a, s_prime, r> 
        existing = (1 - self.alpha)*(self.Q[self.s, self.a])
        nextActionQValue =  self.Q[s_prime,self.Q[s_prime].argmax()]
        estimate = self.alpha*(r + (self.gamma * nextActionQValue))
        update = existing + estimate
        self.Q[self.s, self.a] = update

        # Decide weather we sohuld take random action or not
        if rand.random() < self.rar:
        # if self.SomeRandNum < self.rar:
            # choose random action
            action = rand.sample(self.actionList, 1)
            self.s = s_prime
            self.a = action
            # Update random action selection criteria
            self.rar = self.rar * self.radr
            return action

        # Update random action selection criteria
        self.rar = self.rar * self.radr

        # Determine action
        action = self.Q[s_prime].argmax()


        self.experience.append((self.s, self.a, s_prime, r))
        # Dyna-Q
        dyna(self)

        if self.verbose: print "s =", s_prime,"a =",action,"r =",r
        self.s = s_prime
        self.a = action
        
        return action

    def author(self):
        return "sprichard"

if __name__=="__main__":
    print "Remember Q from Star Trek? Well, this isn't him"


def dyna(self):
    i = 0
    while i <= self.dyna:
        randNum = np.random.randint(0,len(self.experience))
        expTuple = self.experience[randNum]
        # state = 0, action = 1, s_prime = 2
        state = expTuple[0]
        action = expTuple[1]
        s_prime = expTuple[2]
        r = expTuple[3]
        # Update Q-Table
        self.Q[state, action] = (1 - self.alpha) * self.Q[state,action] + self.alpha * (r + self.gamma * self.Q[s_prime, self.Q[s_prime].argmax()])
        i += 1
        
        
        
    
    
