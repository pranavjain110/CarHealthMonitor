import matplotlib.pyplot as plt
import numpy as np

debug = False


class dataManipulation():
    """
        This class is used to read a text file, use the data to calculate
        corresponding value of reliability and plot the graph
    """

    def __init__(self):
        """Initialize the object of class dataManipulation
        """
        self.x_values = []
        self.y_values = []

    def computeX(self, time):
        """This function is used to convert a value of time
        into a discrete array of time from 0 to that number
        for the purpose plotting the equation

        Arguments:
            time {int} -- time to be entered in the equation
        """

        timeinc = 0

        for i in range(40+1):
            stepSize = time/40

            self.x_values.append(timeinc)
            timeinc = timeinc+stepSize

    def computeY(self, formula):
        """
        This method is used to calculate the value corresponding
        to x vector. It will compute the equation based on the x
        value and the formula provided.

        Arguments:
            formula {[string]} -- [Equation used to compute y]

        Returns:
            [list] -- [The calculated y value is stored in a form of list]
        """
        # i takes values of time from the x_values list
        for i in self.x_values:
            y = eval(formula)
            # eval function evaluates the “String” like a python
            # expression and returns the result as an integer
            self.y_values.append(y)

    def graph(self, x_label, y_label, graph_title):
        """
        This function can be used to plot the
        graphs based on equation of the curve.

        Arguments:
            x_label {[type]} -- [title of x axis]
            y_label {[type]} -- [title of y axis]
            graph_title {[type]} -- [title of graph]
            """
        x = np.array(self.x_values)

        y = self.y_values
        # Plotting the Graphs, X & Y Labels and title
        plt.plot(x, y)
        plt.title(graph_title)
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.show()


# Code present incase we need to test the code above
if debug is True:
    engineOilReliability = dataManipulation()
    engineOilReliability.computeX(18000)
    engineOilReliability.computeY("np.exp(-(i/5190)**1.55)")
    engineOilReliability.graph('Hours', 'Reliability',
                               'Running hours vs Reliability')
