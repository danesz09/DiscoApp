from PIL import Image, ImageTk, ImageSequence
import random

class GifHandlerGD:
    def __init__(self, gif_files):
        self.gif_files = gif_files
        self.gif_frames = []
        self.current_frame = 0

    def load_random_gif_GD(self):
        # GIF random betöltése
        gif_file = random.choice(self.gif_files)
        gif = Image.open(gif_file)
        original_width, original_height = gif.size
        max_width, max_height = 750, 750  # Update max size to 750x750
        ratio = min(max_width / original_width, max_height / original_height)
        new_size = (int(original_width * ratio), int(original_height * ratio))
        self.gif_frames = [ImageTk.PhotoImage(img.resize(new_size, Image.Resampling.LANCZOS)) for img in ImageSequence.Iterator(gif)]
        self.current_frame = 0
        return new_size

    def get_next_frame_GD(self):
        #gif következő frameje
        frame = self.gif_frames[self.current_frame]
        self.current_frame = (self.current_frame + 1) % len(self.gif_frames)
        return frame