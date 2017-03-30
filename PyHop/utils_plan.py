import pyhop
import copy
#result format: ('print_a_concept_1', 'Concept B'), ('print_a_concept_2', 'Concept A'),
def simulate_plan(result):
    print "\n\nSimulating result, type q to quit\n"
    for tuple in result:
        print tuple
        s = raw_input("")
        if s == "q":
            exit(0)

def simulate_plan_execute(result, state, wait_for_user = False):
    if wait_for_user:
        print "\n\nSimulating result, type q to quit\n"
    tick = 0
    data = {}
    record_state_to_data(state, data, tick)
    for tuple in result:
        print tuple
        operator = pyhop.operators[tuple[0]]
        state = operator(state, *tuple[1:])
        pyhop.print_state(state)
        record_state_to_data(state, data, tick)
        tick += 1
        if wait_for_user:
            s = raw_input("")
            if s == "q":
                exit(0)
    print "data: ", data
    return data



def record_state_to_data(state, data, tick, prefix = ""):
    """Print each variable in state, indented by indent spaces."""
    if state != False:
        for (name,val) in vars(state).items():
            if isinstance(val, pyhop.State):
                record_state_to_data(val, data, tick, prefix)
                continue
            if name != '__name__':
                var_name = prefix + "/" + state.__name__ + '/' + name
                val = copy.deepcopy(val)
                if var_name not in data:
                    data[var_name] = []
                if isinstance(val, DictEx):
                    data[var_name].append(val.dict)
                else:
                    data[var_name].append(val)

class DictEx:
    def __init__(self, default_value):
        self.default_value = default_value
        self.dict = {}

    def __getitem__(self, key):
        if key in self.dict:
            return self.dict[key]
        return self.default_value

    def __setitem__(self, key, value):
        self.dict[key] = value

    # def __repr__(self): return '{{Any: {0!r}}}'.format(self.value)