import unittest
from unittest.mock import MagicMock
from ChattyCat_Client import ChatClient  # Make sure this matches your filename
import tkinter as tk

class TestChatClient(unittest.TestCase):
    def setUp(self):
        self.root = tk.Tk()
        self.client = ChatClient(self.root)
        self.client.client_socket = MagicMock()

    def tearDown(self):
        self.root.destroy()

    def test_send_message(self):
        self.client.msg_entry.insert(0, "Hello Test")
        self.client.send_message()
        self.client.client_socket.send.assert_called_with(b"Hello Test")

    def test_send_quit_message(self):
        self.client.msg_entry.insert(0, "quit")
        self.client.quit = MagicMock()
        self.client.send_message()
        self.client.quit.assert_called_once()

if __name__ == '__main__':
    unittest.main()
