# Free Open Source Graphic Application
this is a free,open source application to convert code to graphics
it uses its own custom language "Prog2Graph Language" (it does not have any name)

# learning the language

**How to Use Prog2Graph**

Prog2Graph uses its own custom scripting language based on Python. This language allows users to create graphics and animations using simple commands. **DO NOT ADD HASHTAGS TO THE SCRIPT** as they are not supported.

---

**Basic Commands:**

- `COLOR R G B` – Sets the drawing color using RGB values (0-255)
- `CLEAR` – Clears the screen
- `CIRCLE RADIUS` – Draws a circle with the specified radius
- `RECT WIDTH HEIGHT` – Draws a rectangle with the given width and height
- `MOVE X Y` – Moves the cursor to a specific coordinate
- `LINE X Y` – Draws a line from the current position to (X, Y)
- `ROTATE ANGLE` – Rotates the drawing cursor by the given degrees
- `WAIT MS` – Pauses execution for a specified time in milliseconds
- `TEXT "MESSAGE"` – Displays a text message on the screen

---

**Animation Commands:**

- `ANIM_START` – Starts an animation sequence
- `ANIM_END` – Ends an animation sequence
- `LOOP N` – Repeats a block of code N times
- `IF CONDITION` – Executes the following code block if the condition is met
- `ENDIF` – Ends an IF statement

---

**Example Script:**

```
COLOR 255 0 0
CLEAR
CIRCLE 100
MOVE 200 200
RECT 50 50
ANIM_START
LOOP 10
    MOVE 10 10
    CIRCLE 30
    WAIT 500
ENDLOOP
ANIM_END
```

This script sets the color to red, draws a circle and rectangle, and then creates an animation that moves and redraws a smaller circle every half-second.

For further details, experiment with different values and commands to see their effects.
