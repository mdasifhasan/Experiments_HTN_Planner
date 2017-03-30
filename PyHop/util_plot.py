from bokeh.plotting import figure, output_file, show, ColumnDataSource
from bokeh.models import HoverTool

def test():
    output_file("plots.html")

    x = range(1, 6)
    y = [10, 5, 7, 1, 6]
    plot = figure(title='Line example', x_axis_label='x', y_axis_label='y')
    plot.line(x, y, legend='Test', line_width=4)
    show(plot)


#result format: ('print_a_concept_1', 'Concept B'), ('print_a_concept_2', 'Concept A'),
def plot_plan_bokeh_1(plan):
    output_file("plots.html")
    x = []
    y = []
    ys = []
    i = 0
    for (o, v) in plan:
        s = str(o) + " - " + str(v)
        if s not in ys:
            ys.append(s)
    for (o, v) in plan:
        x.append(i)
        i += 1
        s = str(o) + " - " + str(v)
        y.append(ys.index(s))
    print "X:", x
    print "Y:", y

    source = ColumnDataSource(
        data=dict(
            x=x,
            y=y,
            desc=[ys[k] for k in y],
        )
    )

    hover = HoverTool(
        tooltips=[
            ("desc", "@desc"),
        ]
    )
    plot = figure(title='plan', x_axis_label='step', y_axis_label='operator with param', tools=[hover])
    # plot.line(x, y, legend='plan', line_width=4, source=source)
    plot.line('x', 'y', line_width=4, source=source)
    show(plot)



def plot_plan_bokeh_2(plan):
    import numpy as np
    from bokeh.charts import Line, output_file, show

    x = []
    y = []
    ys = []
    i = 0
    for (o, v) in plan:
        # s = str(o) + " - " + str(v)
        s = str(o)
        if s not in ys:
            ys.append(s)
    for (o, v) in plan:
        i += 1
        x.append(i)
        # s = str(o) + " - " + str(v)
        s = str(o)
        y.append(ys.index(s))


    # xyvalues = np.array([[2, 3, 7, 5, 26], [12, 33, 47, 15, 126], [22, 43, 10, 25, 26]])
    xyvalues = np.array(y)
    line = Line(xyvalues, title="plan", legend="top_left", ylabel='operator')

    output_file('line.html')
    show(line)


def plot_plan_sns(plan):
    import pandas as pd
    import seaborn as sns
    import matplotlib.pyplot as plt

    fake = pd.DataFrame({'cat': ['red', 'green', 'blue'], 'val': [1, 2, 3]})
    ax = sns.barplot(x='val', y='cat',
                     data=fake,
                     color='black')
    ax.set(xlabel='common xlabel', ylabel='common ylabel')
    plt.show()

def plot_plan(plan):
    import matplotlib.pyplot as plt
    import seaborn as sns

    x = []
    y = []
    ys = []
    i = 0
    for (o, v) in plan:
        s = str(o) + " - " + str(v)
        # s = str(o)
        if s not in ys:
            ys.append(s)
    for (o, v) in plan:
        x.append(i)
        i += 1
        s = str(o) + " - " + str(v)
        # s = str(o)
        y.append(ys.index(s))

    sns.set_style("darkgrid")
    labels = ys
    plt.yticks(y, labels)
    plt.plot(x, y)
    plt.show()