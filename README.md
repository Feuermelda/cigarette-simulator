# Cigarette Simulator
*A surreal little terminal-based smoking experience - complete with ANSI colors, flickable ash, and a dramatic sense of burn.*

## What is this?

`cigarette_sim.py` is a weird, wonderful, and purely decorative Python program that simulates the act of smoking a cigarette in your terminal.
You8 light up, drag, flick the ash, and watch the cigarette burn away in glorious `█` and `░` blocks.

This is **not** a pro-smoking app. It's just a lovingly crafted simulation of a quiet moment - with slightly chaotic energy.

## Requirements
- Python 3.6 or higher
- A terminal that supports ANSI escape codes (most modern terminals do)

## Features

- **Filter**: (`█` in yellow)
- **Tobacco stick**: (`█` in normal color)
- **Burning tip**: (`█` in red)
- **Ash**: (`░` grows with each drag)
- **Drag**: Press `D` to take a drag and increase the ash.
- **Flick**: Press `F` to flick off the ash manually.
- **Auto-Flick**: Too much ash? It falls off on its own.
- **State Tracking**: Tracks ash length, remaining cigarette, and resets when needed.

## How to Run
```bash
python cigarette_sim.py
```
- Press any key to light up.
- Use `D` to drag.
- Use `F` to flick the ash.
- Enjoy the burn... until it's gone.

## Upcoming Features
Planned for future releases:
- **Coffee & Energy Drink Sips** (multi-tasking mechanic)
- **Cigarette Pack:** Track how many are left and simulate lighting a new one
- **Long Drag:** A deeper inhale that burns more tobacco, doubles ash
- **Nicotine meter** (for aesthetic purposes only)
- **Poop Resistance System** (working title... may or may not make the cut)
- **Zen Mode:** Achieve inner terminal peace when cigarette + coffee combo is perfect
- **Stats Page:** Track how many cigarettes smoked, ash flicked, etc.
- **Idle Mode:** Just let it smolder while you vibe

## Why?
This started as a small experiment with ANSI color codes and Unicode block characters - and evolved into a bizarre little simulation that's equal parts nostalgic and nonsense.

It also became a fun way to:
- Practice state management
- Experiment with text-based visuals
- Prototype ideas for interactive storytelling

## Inspiration
Inspired by:
- Terminal art (`█`, `░`)
- ANSI color codes
- Late-night coffee
- Real-life rituals
- A healthy dose of absurdity

## Disclaimer
This is a *simulator*, not an endorsement. Please don't start smoking - it's bad for your lungs, and your keyboard deserves better.

## Built With
- Python 3
- Terminal
- Good Vibes
  