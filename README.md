# AI-Chatbot
## Introduction to Maya

Maya is a versatile personal assistant powered by speech recognition and natural language processing (NLP). This application can perform a variety of tasks based on voice commands, providing a hands-free experience for users. Whether you need to send an email, search the web, or get the latest news, Maya is designed to assist you efficiently.

## How Maya Works

### 1. Voice Interaction:
   - **Initialization**: Maya starts by greeting the user based on the time of day and introduces itself.
   - **Voice Recognition**: The `takeCommand()` function listens for and recognizes voice commands using Google's speech recognition service.
   - **Text-to-Speech**: The `speak()` function uses the `pyttsx3` library to convert text responses into speech, allowing for interactive communication.

### 2.Core Functionalities:
   - **Web Searches**: Maya can search Wikipedia, YouTube, and Google for user queries, providing summarized results or opening relevant pages.
   - **Communication**: Users can send emails and WhatsApp messages directly through voice commands.
   - **Daily Tasks**: Maya can tell the current day, date, and weather information, set alarms, and take screenshots.
   - **Entertainment**: It can play music, tell jokes, and find videos on YouTube.
   - **App Control**: Maya can open and close applications, as well as remember and recall user-specific information.

### 3. Special Features:
   - **Translation**: Maya can translate Hindi speech to English using the `transhindi()` and `trans()` functions.
   - **Weather Updates**: The `temp()` function fetches the current temperature from Google search results.
   - **Jokes and Fun**: Maya can tell jokes using the `pyjokes` library and play videos on YouTube through `pywhatkit`.
   - **News**: Maya can open news websites and provide the latest headlines.
   - **Reminder System**: It can remember and recall specific information provided by the user.

### 4.User Customization:
   - Users can interact with Maya to customize the assistant’s responses and actions.
   - The assistant is designed to handle multiple commands in a single session, providing continuous interaction.

This script listens continuously for voice commands using the microphone. When the phrase "wake up" is detected, it launches the `maya.py` script located on the desktop. If the phrase is not detected, it prints "Nothing........" and continues listening.

Maya is a voice-activated assistant capable of performing a range of tasks, primarily focusing on communication via WhatsApp in this implementation. It leverages Python libraries for speech recognition and text-to-speech conversion, providing an interactive and hands-free experience for the user.
