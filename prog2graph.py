import sys
import importlib.util
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QPushButton, QVBoxLayout, QWidget, QMenuBar, QMenu, QAction, QFileDialog, QMessageBox
from PyQt5.QtGui import QIcon  # Import QIcon to set the icon
import time

# Check if pygame or turtle is installed
pygame_installed = importlib.util.find_spec("pygame") is not None
turtle_installed = importlib.util.find_spec("turtle") is not None

class Programming2Graphics(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Programming2Graphics")
        self.setGeometry(100, 100, 600, 400)

        # Set the application icon
        self.setWindowIcon(QIcon('icon.ico'))  # Load icon.ico as the window icon

        self.text_edit = QTextEdit(self)
        self.run_button = QPushButton("Run Script", self)
        self.run_button.clicked.connect(self.run_script)

        layout = QVBoxLayout()
        layout.addWidget(self.text_edit)
        layout.addWidget(self.run_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.current_file = None  # To track the current file

        # Set up the menu bar
        self.create_menu()

    def create_menu(self):
        # Create the menu bar and add actions
        menu_bar = self.menuBar()

        file_menu = menu_bar.addMenu("File")
        
        # Create File menu actions
        new_action = QAction("New", self)
        new_action.triggered.connect(self.new_file)
        file_menu.addAction(new_action)

        open_action = QAction("Open", self)
        open_action.triggered.connect(self.open_file)
        file_menu.addAction(open_action)

        save_as_action = QAction("Save As...", self)
        save_as_action.triggered.connect(self.save_as_file)
        file_menu.addAction(save_as_action)

        about_action = QAction("About Programming2Graphics", self)
        about_action.triggered.connect(self.show_about)
        file_menu.addAction(about_action)

    def show_about(self):
        # Show the "About" message box
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Programming2Graphics Version 1.0")
        msg.setInformativeText("Our scripting language is based in Python and the version is 1.0.")
        msg.setWindowTitle("About Programming2Graphics")
        msg.exec_()

    def show_error(self, message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText("Script Error")
        msg.setInformativeText(message)
        msg.setWindowTitle("Error")
        msg.exec_()

    def run_script(self):
        script = self.text_edit.toPlainText()
        try:
            if pygame_installed:
                self.run_pygame(script)
            elif turtle_installed:
                self.run_turtle(script)
            else:
                self.show_error("Neither Pygame nor Turtle is installed.")
        except Exception as e:
            self.show_error(f"An error occurred: {str(e)}")

    def run_pygame(self, script):
        import pygame
        pygame.init()
        screen = pygame.display.set_mode((500, 500))
        pygame.display.set_caption("Pygame Drawing")
        clock = pygame.time.Clock()
        running = True
        screen.fill((255, 255, 255))
        color = (0, 0, 0)
        x, y = 250, 250
        animating = False

        commands = script.split("\n")
        i = 0
        while i < len(commands):
            line = commands[i].strip()
            if not line:
                i += 1
                continue

            parts = line.split()
            command = parts[0].upper()

            try:
                if command == "MOVE" and len(parts) == 3:
                    x, y = int(parts[1]), int(parts[2])

                elif command == "LINE" and len(parts) == 3:
                    x2, y2 = int(parts[1]), int(parts[2])
                    pygame.draw.line(screen, color, (x, y), (x2, y2), 2)
                    x, y = x2, y2

                elif command == "CIRCLE" and len(parts) == 2:
                    r = int(parts[1])
                    pygame.draw.circle(screen, color, (x, y), r, 2)

                elif command == "RECT" and len(parts) == 3:
                    w, h = int(parts[1]), int(parts[2])
                    pygame.draw.rect(screen, color, (x, y, w, h), 2)

                elif command == "COLOR" and len(parts) == 4:
                    color = (int(parts[1]), int(parts[2]), int(parts[3]))

                elif command == "CLEAR":
                    screen.fill((255, 255, 255))

                elif command == "ANIM_START":
                    animating = True

                elif command == "ANIM_END":
                    animating = False

                elif command == "WAIT" and len(parts) == 2:
                    time.sleep(int(parts[1]) / 1000.0)

                else:
                    raise ValueError(f"Unknown command: {command}")

                if animating:
                    pygame.display.flip()
                    clock.tick(30)  # Limits frame rate to smooth animation

            except Exception as e:
                self.show_error(f"Error in script at line {i+1}: {line}\n{str(e)}")
                return

            i += 1

        pygame.display.flip()

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            clock.tick(30)

        pygame.quit()

    def run_turtle(self, script):
        import turtle
        turtle.speed(0)
        turtle.pensize(2)
        turtle.clear()
        turtle.up()
        animating = False

        commands = script.split("\n")
        i = 0
        while i < len(commands):
            line = commands[i].strip()
            if not line:
                i += 1
                continue

            parts = line.split()
            command = parts[0].upper()

            try:
                if command == "MOVE" and len(parts) == 3:
                    turtle.goto(int(parts[1]), int(parts[2]))

                elif command == "LINE" and len(parts) == 3:
                    turtle.down()
                    turtle.goto(int(parts[1]), int(parts[2]))
                    turtle.up()

                elif command == "CIRCLE" and len(parts) == 2:
                    turtle.down()
                    turtle.circle(int(parts[1]))
                    turtle.up()

                elif command == "RECT" and len(parts) == 3:
                    w, h = int(parts[1]), int(parts[2])
                    turtle.down()
                    for _ in range(2):
                        turtle.forward(w)
                        turtle.right(90)
                        turtle.forward(h)
                        turtle.right(90)
                    turtle.up()

                elif command == "COLOR" and len(parts) == 4:
                    turtle.pencolor(int(parts[1]) / 255, int(parts[2]) / 255, int(parts[3]) / 255)

                elif command == "CLEAR":
                    turtle.clear()

                elif command == "ANIM_START":
                    animating = True

                elif command == "ANIM_END":
                    animating = False

                elif command == "WAIT" and len(parts) == 2:
                    time.sleep(int(parts[1]) / 1000.0)

                else:
                    raise ValueError(f"Unknown command: {command}")

                if animating:
                    turtle.update()

            except Exception as e:
                self.show_error(f"Error in script at line {i+1}: {line}\n{str(e)}")
                return

            i += 1

        turtle.done()

    def open_file(self):
        # Open a .ptg file
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "Open Project File", "", "Programming2Graphics Files (*.ptg)", options=options)
        if file_name:
            try:
                with open(file_name, 'r') as f:
                    script = f.read()
                    self.text_edit.setText(script)
                    self.current_file = file_name
            except Exception as e:
                self.show_error(f"Failed to open file: {str(e)}")

    def new_file(self):
        # Create a new project file (clear the text editor)
        self.text_edit.clear()
        self.current_file = None

    def save_as_file(self):
        # Save the current script to a .ptg file
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getSaveFileName(self, "Save Project As", "", "Programming2Graphics Files (*.ptg)", options=options)
        if file_name:
            if not file_name.endswith('.ptg'):
                file_name += '.ptg'
            try:
                with open(file_name, 'w') as f:
                    script = self.text_edit.toPlainText()
                    f.write(script)
                    self.current_file = file_name
            except Exception as e:
                self.show_error(f"Failed to save file: {str(e)}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Programming2Graphics()
    window.show()
    sys.exit(app.exec_())

