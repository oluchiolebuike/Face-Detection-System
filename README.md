# Pink Tux Tracer 🐧🩷
A face detection system that maps Linux Tux across your face in real time. Hand-drawn with 3 years of Computer Science concepts from UCT and stamped at every landmark point. In pink, obviously. 🐧🩷

Tux Tracer uses MediaPipe to map 468 face landmarks (decided to set it to 1 face landmark), 21 hand dots per hand and 33 body pose points onto your webcam feed. Every landmark is replaced with a hand-drawn Tux stamp instead of a boring dot.

---

## The Drawing

The stencil of Tux isn't just some cool penguin (that took me forever to draw) — it's 3 years of Computer Science completed at UCT living inside one drawing.

Every line on Tux was drawn with something I actually learned, struggled through and eventually understood:

- **First year** — recursion, the idea that a function can call itself and somehow that's not chaos
- **Second year** — data structures and algorithms: binary heaps, AVL trees, Bellman-Ford, Dijkstra's shortest path
- **Databases** — hidden at the bottom of Tux's feet, a quiet little love note:
  ```sql
  SELECT * FROM ScienceFaculty WHERE Dept = 'Comp Sci' AND Year = 'Final'
  ```
- **Z test season** — z-test attempt 158 on his crown
- **PCP (Parallel & Concurrent Programming)** — synchronisation and locks woven into his outline
- **Networks** — IP addresses scattered across his body
- **Operating Systems** — paging algorithms from OSI hiding in the details

Three years of late nights, confusing lectures and concepts that finally clicked — all drawn by hand into one little penguin who now dances across your face in real time.

---

## Requirements

**Python version:** 3.11.x (MediaPipe does not support 3.12+)

**MediaPipe version:** 0.10.14 (newer versions break the solutions API)

**Dependencies:**
```
opencv-python
mediapipe==0.10.14
numpy
```

Install everything at once:
```cmd
pip install opencv-python mediapipe==0.10.14 numpy
```

**Files needed:**
- `tux_tracer.py` — the main script
- `tux.png` — the hand-drawn stamp, PNG with transparent background works best

---

## Setup

**1. Make sure you're on Python 3.11:**
```cmd
python --version
```

**2. Create a virtual environment:**
```cmd
py -3.11 -m venv tux_trace-env
```

**3. Activate it (Command Prompt — recommended over PowerShell):**
```cmd
tux_trace-env\Scripts\activate
```

**4. Install dependencies:**
```cmd
pip install opencv-python mediapipe==0.10.14 numpy
```

**5. Drop `tux.png` in the same folder as `tux_tracer.py`, then run:**
```cmd
python tux_tracer.py
```

Press `Q` or click the X button to close.

> **VS Code tip:** if your terminal is PowerShell, switch to Command Prompt via `Ctrl + Shift + P` → Terminal: Select Default Profile → Command Prompt

---

## How it works

Instead of rendering MediaPipe's default dots and lines, Tux Tracer stamps your drawing at every detected landmark point in real time. The face mesh alone has 468 points — so Tux shows up everywhere.

To swap the drawing out, replace `tux.png` with any PNG and update this line:
```python
tux = cv2.imread("your_drawing.png", cv2.IMREAD_UNCHANGED)
```

---

## Built with

- [OpenCV](https://opencv.org/) — webcam feed and rendering
- [MediaPipe](https://mediapipe.dev/) — landmark detection and tracking
- [NumPy](https://numpy.org/) — image blending
