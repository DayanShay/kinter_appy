import tkinter


class Leaderboard:
    def __init__(self, root: tkinter):
        """

        :type root: tk
        """
        self.root = root.Tk()
        self.element = root
        self.root.geometry("500x400")
        self.create_widgets()
        self.update()

    def create_widgets(self):
        self.get_window_size()
        self.create_canvas()
        self.canvas_events_render()
        self.get_canvas_size()
    def update(self):
        self.update_canvas()
        self.root.after(2, self.update)

    def update_canvas(self):
        self.canvas1.config(width=self.width/3, height=self.height)
        self.canvas2.config(width=self.width/3, height=self.height)
        self.canvas_events.config(width=self.width/3, height=self.height)
        text_bbox = self.canvas_events.bbox(self.canvas_events_label)
        center_x = (self.canvas_width - text_bbox[2] + text_bbox[0]) / 2
        center_y = (self.canvas_height - text_bbox[3] + text_bbox[1]) / 2
        self.canvas_events.move(self.canvas_events_label, center_x - text_bbox[0], center_y - text_bbox[1])

    def create_canvas(self):
        self.canvas1 = self.element.Canvas(self.root, width=self.width/3, height=self.height, bg="Blue")
        self.canvas2 = self.element.Canvas(self.root, width=self.width/3, height=self.height, bg="Blue")
        self.canvas_events = self.element.Canvas(self.root, width=self.width/3, height=self.height, bg="Blue")
        self.canvas1.pack(side="left", fill="y")
        self.canvas2.pack(side="left", fill="y")
        self.canvas_events.pack(side="left", fill="y")

    def get_window_size(self):
        self.width = self.root.winfo_width()
        self.height = self.root.winfo_height()
        self.root.after(2,self.get_window_size)

    def get_canvas_size(self):
        self.canvas_width = self.canvas_events.winfo_width()
        self.canvas_height = self.canvas_events.winfo_height()
        self.root.after(2, self.get_canvas_size)

    def canvas_events_render(self):
        self.canvas_events_label = self.canvas_events.create_text(90, 20, text="Hello, Tkinter2!", font=("Arial", 12), fill="Black")


