import tkinter as tk
from gif_handler_gd import GifHandlerGD
import disco_effect_gd

class DiscoAppGD:
    def __init__(self, root):
        self.root = root
        self.root.title("NO PARTY :(")
        self.root.geometry("800x800")
        self.root.config(bg="white")

        #Inicializálás
        self.party_button = tk.Button(root, text="PARTY TIME", font=("Gill Sans MT", 12), command=self.start_party_gd)
        self.party_button.pack(pady=20)
        self.party_button.config(bg="white", fg="black")
        self.label = tk.Label(root, text="NOT PARTY TIME :(", font=("Gill Sans MT", 24), bg="white")
        self.label.pack(pady=20)
        self.gif_label = tk.Label(root, bd=0, highlightthickness=0, bg="white", width=1, height=1)
        self.gif_label.pack(pady=20)
        self.partying = False
        self.title_text = "PARTY TIME!"
        self.title_index = 0
        self.gif_handler = GifHandlerGD(["dancing.gif", "dancing1.gif", "dancing2.gif"])

    def start_party_gd(self):
        #Party mód ki be kapcsolása
        self.partying = not self.partying
        if self.partying:
            self.party_button.config(text="STOP THE FUN!")
            self.label.config(text="PARTY TIME!")
            self.title_index = 0  # Reset title index
            self.change_color_gd()
            self.update_title_gd()
            new_size = self.gif_handler.load_random_gif_GD()
            self.gif_label.config(width=new_size[0], height=new_size[1])
            self.animate_gif_gd()
        else:
            self.party_button.config(text="PARTY TIME")
            self.label.config(text="NOT PARTY TIME :(")
            self.root.config(bg="white")
            self.label.config(bg="white", fg="black")
            self.party_button.config(bg="white", fg="black")
            self.root.title("NO PARTY :( ")
            self.gif_label.config(image='', bg="white", width=1, height=1)

    def change_color_gd(self):
        #random háttér szín
        if self.partying:
            app_color = disco_effect_gd.get_random_color_gd()
            buttonlabel_color = disco_effect_gd.get_random_color_gd()
            text_color = disco_effect_gd.get_random_color_gd()
            self.root.config(bg=app_color)
            self.party_button.config(bg=buttonlabel_color, fg=text_color)
            self.label.config(bg=buttonlabel_color, fg=text_color)
            self.root.after(500, self.change_color_gd)

    def update_title_gd(self):
        #cím animálása
        if self.partying and self.title_index < len(self.title_text):
            self.root.title(self.title_text[:self.title_index + 1])
            self.title_index += 1
            self.root.after(200, self.update_title_gd)
        elif not self.partying:
            self.title_index = 0

    def animate_gif_gd(self):
        #gif animálása
        if self.partying:
            self.gif_label.config(image=self.gif_handler.get_next_frame_GD())
            self.root.after(100, self.animate_gif_gd)

if __name__ == "__main__":
    root = tk.Tk()
    app = DiscoAppGD(root)
    root.mainloop()