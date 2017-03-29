#result format: ('print_a_concept_1', 'Concept B'), ('print_a_concept_2', 'Concept A'),
def simulate_plan(result):
    print "\n\nSimulating result, type q to quit\n"
    for tuple in result:
        print tuple
        s = raw_input("")
        if s == "q":
            exit(0)


