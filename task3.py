class AudioPlayer:
    def play_audio(self):
        print("Playing audio")


class VideoPlayer:
    def play_video(self):
        print("Playing video")


class MultimediaPlayer(AudioPlayer, VideoPlayer):
    def play(self):
        print("Multimedia player is playing.")


player = MultimediaPlayer()
player.play_audio()
player.play_video()
player.play()