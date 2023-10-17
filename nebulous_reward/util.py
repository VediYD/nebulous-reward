import tkinter as tk


class StatusWindow:
    def __init__(self):
        self.root = None
        self.label_epoch = None
        self.label_step = None
        self.label_laction = None
        self.label_lreward = None

        self.label_epoch_text = None
        self.label_step_text = None
        self.label_laction_text = None
        self.label_lreward_text = None

        self.label_epoch_widget = None
        self.label_step_widget = None
        self.label_laction_widget = None
        self.label_lreward_widget = None

        self.label_epoch_name = None
        self.label_step_name = None
        self.label_laction_name = None
        self.label_lreward_name = None

        self.window_size = (300, 150)

        self.title = 'Status Window'

    def initialize(self):
        self.root = tk.Tk()
        self.root.title("Status Window")
        self.root.configure(background='black')
        self.root.attributes("-topmost", True)
        self.root.geometry(f"{self.window_size[0]}x{self.window_size[1]}")

        self.label_epoch_text = tk.StringVar()
        self.label_step_text = tk.StringVar()
        self.label_laction_text = tk.StringVar()
        self.label_lreward_text = tk.StringVar()

        self.label_epoch_name = tk.Label(
            self.root,
            text='Epoch',
            font=("Arial", 20),
            fg="white",
            bg="black",
            anchor='w',
            justify='left'
        )
        self.label_step_name = tk.Label(
            self.root,
            text='Step',
            font=("Arial", 20),
            fg="white",
            bg="black",
            anchor='w',
            justify='left'
        )
        self.label_laction_name = tk.Label(
            self.root,
            text='Last Action',
            font=("Arial", 20),
            fg="white",
            bg="black",
            anchor='w',
            justify='left'
        )
        self.label_lreward_name = tk.Label(
            self.root,
            text='Reward',
            font=("Arial", 20),
            fg="white",
            bg="black",
            anchor='w',
            justify='left'
        )

        self.label_epoch_widget = tk.Label(
            self.root,
            textvariable=self.label_epoch_text,
            font=("Arial", 20),
            fg="white",
            bg="black",
            anchor='w',
            justify='left'
        )
        self.label_step_widget = tk.Label(
            self.root,
            textvariable=self.label_step_text,
            font=("Arial", 20),
            fg="white",
            bg="black",
            anchor='w',
            justify='left'
        )
        self.label_laction_widget = tk.Label(
            self.root,
            textvariable=self.label_laction_text,
            font=("Arial", 20),
            fg="white",
            bg="black",
            anchor='w',
            justify='left'
        )
        self.label_lreward_widget = tk.Label(
            self.root,
            textvariable=self.label_lreward_text,
            font=("Arial", 20),
            fg="white",
            bg="black",
            anchor='w',
            justify='left'
        )

        # Use the grid geometry manager to create a table-like structure
        self.label_epoch_name.grid(row=0, column=0, sticky='w')
        self.label_step_name.grid(row=1, column=0, sticky='w')
        self.label_laction_name.grid(row=2, column=0, sticky='w')
        self.label_lreward_name.grid(row=3, column=0, sticky='w')

        self.update_label()

    def update_label(self):
        self.label_epoch_text.set(self.label_epoch)
        self.label_step_text.set(self.label_step)
        self.label_laction_text.set(self.label_laction)
        self.label_lreward_text.set(self.label_lreward)
        # Create labels for values
        self.label_epoch_widget.grid(row=0, column=1, sticky='w')
        self.label_step_widget.grid(row=1, column=1, sticky='w')
        self.label_laction_widget.grid(row=2, column=1, sticky='w')
        self.label_lreward_widget.grid(row=3, column=1, sticky='w')

        self.root.update()

    def update(self, epoch, step, action, reward):
        self.label_epoch = f'{epoch}'
        self.label_step = f'{step}'
        self.label_laction = f'{action}'
        self.label_lreward = f'{reward}'
        self.update_label()

    def close(self):
        self.root.quit()
        self.root.destroy()
