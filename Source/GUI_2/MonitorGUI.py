import plotting_function
import os
import tkinter as tk
from matplotlib import pyplot as plt
from matplotlib import style
import matplotlib.animation as animation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib

matplotlib.use("TkAgg")

# Defining some style and fonts 
style.use("dark_background")
fontstyle = "Helvetica"
small_fsize = 13
large_fsize = 15

# Creating an object for the figure to be plot
f = plt.figure()

select_param = None

chartLoad = True
paneCount = 1


# Creating a method for menu parameters
def changeParam(toWhat):
    """Function to set the parameter whose graph needs to be displayed

    Arguments:
        toWhat {string} -- Parameter to be set
    """
    global select_param
    select_param = toWhat


# Creating an animate function for the matplotlib graphs
def animate(i):
    """Function used to display live graphs
    
    Arguments:
        i {int} -- time interval
    """
    if chartLoad:
        if paneCount == 1:
            csvData = []
            with open("TimeElapsed.csv") as w:
                for row in w:
                    csvData.append((row.split(",")))
            try:

                if select_param == "OIL":
                    a = plt.subplot2grid((6, 4), (0, 0), rowspan=5, colspan=4)
                    time = float(csvData[0][0])
                    engineOilReliability = plotting_function.dataManipulation()
                    # sample txt would be replaced with a file
                    engineOilReliability.computeX(time)
                    engineOilReliability.computeY("1-np.exp(-(i/5190)**1.55)")

                    a.clear()
                    a.set_xlabel("time (hours)")
                    a.set_ylabel("Failure Probability")
                    a.plot(engineOilReliability.x_values,
                           engineOilReliability.y_values, label="live data")
                    a.legend(bbox_to_anchor=(0, 1.02, 1, .102), loc=3,
                             ncol=2, borderaxespad=0)
                    title = "OIL HEALTH "
                    a.set_title(title)

                elif select_param == "TIRE":
                    a = plt.subplot2grid((6, 4), (0, 0), rowspan=5, colspan=4)
                    time = float(csvData[0][1])
                    engineOilReliability = plotting_function.dataManipulation()
                    # sample txt would be replaced with a file
                    engineOilReliability.computeX(time)
                    engineOilReliability.computeY("1-np.exp(-(i/41667)**1.37)")

                    a.clear()
                    a.set_xlabel("distance (kms)")
                    a.set_ylabel("Failure Probability")
                    a.plot(engineOilReliability.x_values,
                           engineOilReliability.y_values, label="live data")
                    a.legend(bbox_to_anchor=(0, 1.02, 1, .102), loc=3,
                             ncol=2, borderaxespad=0)
                    title = "TIRE HEALTH "
                    a.set_title(title)

            except Exception as e:
                print(e)


# BASE-LINE code for adding pages

class HealthGraphs(tk.Tk):
    """Class to define frame of the GUI
    
    """

    def __init__(self, *args, **kwargs):
        """Initialize the frame as an object of class HealthGraphs
        """
        tk.Tk.__init__(self, *args, **kwargs)

        # Adding an icon for the GUI
        tk.Tk.iconbitmap(self, r"graph.ico")

        # Adding the GUI title
        tk.Tk.wm_title(self, "Car Health Monitor")

        # Setting up a minimum size for the GUI
        tk.Tk.wm_minsize(self, 850, 600)
        tk.Tk.wm_maxsize(self, 850, 600)

        # Adding a window frame
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        # 0 is the min size, weight is the priority
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        container.config(bg="black")

        # creating an empty dictionary for all the frames that we will create
        self.frames = {}

        # creating a for loop for every new page
        for F in (StartPage, PageOne, PageTwo):
            # creating a start page for the GUI
            frame = F(container, self)

            self.frames[F] = frame

            # assigning the location
            # nswe = north,south,east,west. Can be expanded in all directions
            frame.grid(row=0, column=0, sticky="nsew")

        # showing up of a frame StartPage whenever this GUI opens
        self.show_frame(StartPage)

    def show_frame(self, cont):
        """Function to bring the frame to the top 
        
        Arguments:
            cont  -- represents the page container
        """
        # cont is the key for the self.frames dictionary in the __init method
        frame = self.frames[cont]
        frame.tkraise()  # brings up thw window to the top

    def restart_notif(self):
        """Function to call notification executable
        """
        os.startfile("alertloop.exe")


# Adding a Start page
class StartPage(tk.Frame):
    """Inititalize the start page of the GUI
    """

    def __init__(self, parent, controller):
        """Initialize object of class StartPage
        
        Arguments:
            parent  -- object of tk.frame
            controller  -- object of class HealthGraphs

        """
        tk.Frame.__init__(self, parent, bg='black')

        label = tk.Label(self, text="CAR HEALTH MONITOR",
                         bg="black", fg="cyan2",
                         font=(fontstyle, 30))
        label.place(x=190, y=80)

        label2 = tk.Label(self, text="Select the component", bg="black",
                          fg="white",
                          font=(fontstyle, 18))
        label2.place(x=310, y=240)

        label3 = tk.Label(self, text="When maintenance is carried out, click here",
                          bg="black", fg="white",
                          font=(fontstyle, large_fsize))
        label3.place(x=130, y=500)

        button1 = tk.Button(self, bg="black", bd=5, fg="cyan2", height=3,
                            width=10,
                            relief='ridge', text="Engine Oil",
                            command=lambda: [controller.show_frame(PageOne),
                                             changeParam("OIL")])
        button1.place(x=470, y=300)

        button2 = tk.Button(self, bg="black", relief='ridge', fg="cyan2", bd=5,
                            height=3, width=10, text="Tire",
                            command=lambda: [controller.show_frame(PageOne),
                                             changeParam("TIRE")])
        button2.place(x=300, y=300)

        button3 = tk.Button(self, bg="black", fg="cyan2", relief='ridge',
                            height=3, width=15, bd=5,
                            text="Service complete",
                            command=lambda: controller.restart_notif())
        button3.place(x=560, y=485)


# Adding Page 1
class PageOne(tk.Frame):
    """ Inititalize the page one of the GUI
    """

    def __init__(self, parent, controller):
        """Initialize object of class PageOne
        
        Arguments:
            parent  -- object of tk.frame
            controller  -- object of class HealthGraphs

        """
        tk.Frame.__init__(self, parent, bg='black')
        label = tk.Label(self, text="Failure Graphs", bg="black", fg="white",
                         font=(fontstyle, 17))
        label.place(x=360, y=30)

        button1 = tk.Button(self, bg="black", fg="cyan2", height=3, width=10,
                            text="Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.place(x=0, y=10)

        button2 = tk.Button(self, bg="black", fg="cyan2", height=2, width=10,
                            text="Tire", font=(fontstyle, 11),
                            command=lambda: [controller.show_frame(PageOne),
                                             changeParam("TIRE")])
        button2.place(x=260, y=90)

        button3 = tk.Button(self, bg="black", fg="cyan2", height=2, width=10,
                            text="Engine Oil", font=(fontstyle, 11),
                            command=lambda: [controller.show_frame(PageOne),
                                             changeParam("OIL")])
        button3.place(x=530, y=90)

        button4 = tk.Button(self, bg="black", fg="cyan2", height=3, width=10,
                            text="Next",
                            command=lambda: controller.show_frame(PageTwo))
        button4.place(x=770, y=10)

        canvas1 = FigureCanvasTkAgg(f, self)
        canvas1.draw()
        canvas1.get_tk_widget().place(x=110, y=150)


class PageTwo(tk.Frame):
    """Inititalize the page two of the GUI
    """

    def __init__(self, parent, controller):
        """Initialize object of class PageTwo
        
        Arguments:
            parent  -- object of tk.frame
            controller  -- object of class HealthGraphs

        """
        tk.Frame.__init__(self, parent, bg='black')
        label = tk.Label(self, text="Project by:", bg="black",
                         fg="cyan2", font=(fontstyle, 14))
        label.place(x=355, y=220)

        labe2 = tk.Label(self, text="Ajaykumar Mudaliar\nSameer Todkar\nChinmay Mulay\n\
                        Pranav Jain", bg="black", fg="white", font=(fontstyle, 13))
        labe2.place(x=325, y=260)

        button1 = tk.Button(self, bg="black", fg="cyan2", height=3, width=10,
                            text="Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.place(x=0, y=10)

# Creating an object of the class HealthGraphs()
app = HealthGraphs()

# plotting the graph using Funcanimation and the animate function
graph = animation.FuncAnimation(f, animate, interval=1000)
app.mainloop()
