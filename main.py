import kivy.app
from kivy.core.window import Window
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.utils import get_color_from_hex

class ChatPage(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 1
        self.rows = 3
        self.background_color = get_color_from_hex('#FFFFFF')  # White background color

        # Create a label for the chat history.
        self.history = Label(size_hint_y=1, text_size=(None, None), color=(0, 0, 0, 1))  # Black text color
        self.add_widget(self.history)

        # Create a text input for the new message.
        self.send_message = TextInput(size_hint_y=0.1, width=Window.size[0] * 1, size_hint_x=None, multiline=False,
                                     background_color=get_color_from_hex('#FFFFFF'),  # White background color
                                     foreground_color=(0, 0, 0, 1))  # Black text color
        self.add_widget(self.send_message)

        # Create a button to send the message.
        self.send = Button(text="Send", size_hint_y=0.1, background_color=get_color_from_hex('#FFFFFF'),color=(0, 0, 0, 1))  # Black text color
        self.send.bind(on_press=self.send_message_to_server)
        self.add_widget(self.send)

    def send_message_to_server(self, _):
        # Send the message to the chat server.
        message = self.send_message.text
        print(f"Sending message: {message}")

        # Update the chat history.
        self.history.text += f"\nSent: {message}"
        
        # Clear the text input.
        self.send_message.text = ""

if __name__ == "__main__":
    Window.clearcolor = get_color_from_hex('#FFFFFF')  # Set the window background color to white

    chatbox1 = ChatPage()
    chatbox2 = ChatPage()

    kivy.app.runTouchApp(chatbox1)
    kivy.app.runTouchApp(chatbox2)
