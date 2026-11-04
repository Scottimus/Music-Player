import os
os.environ.setdefault("PYGAME_HIDE_SUPPORT_PROMPT", "1")
import unittest
from unittest.mock import MagicMock, patch
from MusicPlayer import MusicPlayer


class PlayerTests(unittest.TestCase):
    def player(self, files, current=None):
        player = MusicPlayer.__new__(MusicPlayer)
        player.music_files = files
        player.current_track = current
        player.paused = False
        player.music_directory = "."
        player.playlist = MagicMock()
        player.current_track_info = MagicMock()
        return player

    def test_previous_selects_and_plays(self):
        player = self.player(["a.mp3", "b.mp3"], "b.mp3")
        player.play_music = MagicMock()
        player.previous_track()
        player.playlist.activate.assert_called_once_with(0)
        player.play_music.assert_called_once()

    def test_empty_navigation_is_safe(self):
        player = self.player([])
        player.next_track()
        player.previous_track()
        player.playlist.activate.assert_not_called()

    def test_stop_works_while_paused(self):
        player = self.player(["a.mp3"], "a.mp3")
        player.paused = True
        with patch("MusicPlayer.pygame.mixer.music") as music:
            music.get_busy.return_value = False
            player.stop_music()
            music.stop.assert_called_once()


if __name__ == "__main__":
    unittest.main()
