# JevDoom

Confidence-aware NPC decision system built with [ViZDoom](https://github.com/Farama-Foundation/ViZDoom) and TypeSafe Jev.

The project explores structured decision-making for game NPCs using Jev.

## Architecture

```text
ViZDoom
   ↓
Game State
   ↓
Jev
   ↓
Decision
   ↓
NPC Action
   ↓
ViZDoom
```

## Current Status

### Phase 0 — Environment

* [x] Python project
* [x] `uv` environment
* [x] ViZDoom installed
* [x] Basic graphical environment
* [x] pytest
* [x] Ruff
* [x] Project configuration

### Phase 1 — Jev

Coming next.

## Development

Install dependencies:

```bash
uv sync
```

Run tests:

```bash
uv run pytest
```

Run linting:

```bash
uv run ruff check .
```

Run the ViZDoom environment:

```bash
uv run python src/jev_doom/game.py
```
