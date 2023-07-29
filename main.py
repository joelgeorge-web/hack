import kivy.app
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
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

        # Pass the message to the other chatbox
        other_chatbox = chatbox1 if self is chatbox2 else chatbox2
        other_chatbox.receive_message(message)

        # Clear the text input.
        self.send_message.text = ""

    def receive_message(self, message):
        # Update the chat history to receive the message
        self.history.text += f"\nReceived: {message}"

class ChatApp(kivy.app.App):
    def build(self):
        Window.clearcolor = get_color_from_hex('#FFFFFF')  # Set the window background color to white

        # Create a horizontal box layout and add two chatboxes side by side
        layout = BoxLayout(orientation='horizontal')
        global chatbox1, chatbox2
        chatbox1 = ChatPage()
        chatbox2 = ChatPage()
        layout.add_widget(chatbox1)
        layout.add_widget(chatbox2)

        return layout

if __name__ == "__main__":
    ChatApp().run()
