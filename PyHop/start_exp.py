"""
The "travel from home to the park" example from my lectures.
Author: Dana Nau <nau@cs.umd.edu>, May 31, 2013
This file should work correctly in both Python 2.7 and Python 3.2.
"""

import pyhop
import random
# state variables

state1 = pyhop.State('state')
state1.status = 3
state1.concepts = ["Concept A", "Concept B", "Concept C"]
state1.relations = ["Relation A", "Relation B", "Relation C"]
state1.concepts_heard_count = [0,0,0]
state1.relations_heard_count = [0,0,0]

# end - state variables

# Operators

# TEST: what if we do not intake state as an argument?
def print_a_concept_1(state, c):
    state.status -= 1
    state.concepts_heard_count[state.concepts.index(c)] += 1
    # print "Style 1", c
    return state # TEST: what if we do not return anything?

def print_a_concept_2(state, c):
    state.concepts_heard_count[state.concepts.index(c)] += 1
    state.status -= 1
    # print "Style 2", c
    return state # TEST: what if we do not return anything?

def print_a_relation_1(state, r):
    state.relations_heard_count[state.relations.index(r)] += 1
    state.status -= 1
    # print r
    return state

def print_a_relation_2(state, r):
    state.relations_heard_count[state.relations.index(r)] += 1
    state.status -= 1
    # print r
    return state

def ask_true_false_on_concept(state, c):
    state.status += 1
    # print "Is it true?\n", c
    return state

def ask_true_false_on_relation(state, r):
    state.status += 1
    # print "Is it true?\n", r
    return state

def show_congrats(state, a = 0):
    return state

pyhop.declare_operators(print_a_concept_1, print_a_concept_2, print_a_relation_1, print_a_relation_2, ask_true_false_on_concept, ask_true_false_on_relation, show_congrats)
# pyhop.print_operators()

# End - Operators

# Methods

def present_a_concept(state, c):
    if state.status > -3:
        if random.randint(0,100) < 50:
            return [('print_a_concept_1', c)]
        else:
            return [('print_a_concept_2', c)]
    return []

def present_a_relation(state, r):
    if state.concepts_heard_count[state.relations.index(r)] > 0:
        if state.status > -3:
            if random.randint(0,100) < 50:
                return [('print_a_relation_1', r)]
            else:
                return [('print_a_relation_2', r)]
    return []

def quest_on_concept(state, c):
    if state.concepts_heard_count[state.concepts.index(c)] > 0:
        if state.status < 3:
            return [('ask_true_false_on_concept', c)]
    return []

def quest_on_relation(state, r):
    if state.relations_heard_count[state.relations.index(r)] > 0:
        if state.status < 3:
            return [('ask_true_false_on_relation', r)]
    return []

def get_random_entry(collection, a = 0):
    return collection[random.randint(0, len(collection)-1)]

def next_step(state, a = 0):
    r = random.randint(0,100)
    if r < 25:
        return [("present_a_concept", get_random_entry(state.concepts))]
    elif r < 50:
        return [("present_a_relation", get_random_entry(state.relations))]
    elif r < 75:
        return [("quest_on_concept", get_random_entry(state.concepts))]
    else:
        return [("quest_on_relation", get_random_entry(state.relations))]

def done(state, a = 0):
    return [("show_congrats", a)]

def teach_knowledge(state, a = 0):
    for hc in state.concepts_heard_count:
        if hc < 5:
            return [('next_step', a), ('teach', a)]
    for hc in state.relations_heard_count:
        if hc < 5:
            return [('next_step', a), ('teach', a)]
    return [('done', a)]

# have to specify the data structure of map and then how that is to be disseminated using the existing methods
pyhop.declare_methods('present_a_concept',present_a_concept)
pyhop.declare_methods('present_a_relation',present_a_relation)
pyhop.declare_methods('quest_on_concept',quest_on_concept)
pyhop.declare_methods('quest_on_relation',quest_on_relation)
pyhop.declare_methods('next_step',next_step)
pyhop.declare_methods('done',done)
pyhop.declare_methods('teach',teach_knowledge)

# print('')
# pyhop.print_methods()

# End - Methods

# query

pyhop.pyhop(state1,[('teach', 'a')], verbose=3)
#end - query


