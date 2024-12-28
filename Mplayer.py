import tkinter as tk
from tkinter import filedialog
import pygame

class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Music Player")
        self.root.geometry("300x150")
        self.root.configure(bg="#000000")

        self.audio_file = None
        self.is_playing = False

        # Create widgets
        self.open_button = tk.Button(root, text="Open File", command=self.open_file)
        self.play_button = tk.Button(root, text="Play", state=tk.DISABLED, command=self.play_music)
        self.pause_button = tk.Button(root, text="Pause", state=tk.DISABLED, command=self.pause_music)
        self.resume_button = tk.Button(root, text="Resume", state=tk.DISABLED, command=self.resume_music)

        # Place widgets
        self.open_button.pack(pady=10)
        self.play_button.pack(pady=5)
        self.pause_button.pack(pady=5)
        self.resume_button.pack(pady=5)

        # Initialize pygame
        pygame.mixer.init()

    def open_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3 *.wav")])
        if file_path:
            self.audio_file = file_path
            self.play_button.config(state=tk.NORMAL)

    def play_music(self):
        if self.audio_file:
            pygame.mixer.music.load(self.audio_file)
            pygame.mixer.music.play()
            self.is_playing = True
            self.play_button.config(state=tk.DISABLED)
            self.pause_button.config(state=tk.NORMAL)

    def pause_music(self):
        if self.is_playing:
            pygame.mixer.music.pause()
            self.is_playing = False
            self.pause_button.config(state=tk.DISABLED)
            self.resume_button.config(state=tk.NORMAL)

    def resume_music(self):
        if not self.is_playing:
            pygame.mixer.music.unpause()
            self.is_playing = True
            self.resume_button.config(state=tk.DISABLED)
            self.pause_button.config(state=tk.NORMAL)

if __name__ == "__main__":
    root = tk.Tk()
    player = MusicPlayer(root)
    root.mainloop()