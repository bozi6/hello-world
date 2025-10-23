# tiny_life.py
import random
import time
from collections import deque
from typing import Deque, List, Optional, Tuple

# Pálya és megjelenítés
MAP_WIDTH, MAP_HEIGHT = 30, 15  # pálya méret
GRASS_CHARSET = ". :;-=+*#%@"  # több fű sűrűbb karakter
CLEAR_SCREEN_ANSI = "\x1b[H\x1b[2J"

# Fű paraméterek
GRASS_MAX = 5
GRASS_GROW_AMOUNT = 1
GRASS_GROW_PROB = 0.8

# Ügynök paraméterek
START_AGENTS = 20
START_ENERGY = 8
MOVE_COST = 1
EAT_GAIN = 4
REPRODUCTION_ENERGY_THRESHOLD = 14
REPRODUCTION_COST = 7
REPRODUCTION_PROB = 0.35

# Időzítés
TICK_MS = 120

# Mozgás irányok (dx, dy)
MOVE_CHOICES: Tuple[Tuple[int, int], ...] = (
    (1, 0), (-1, 0), (0, 1), (0, -1), (0, 0)
)

random.seed(1)


def torus(x: int, y: int) -> Tuple[int, int]:
    return x % MAP_WIDTH, y % MAP_HEIGHT


def in_bounds_torus(x: int, y: int, dx: int, dy: int) -> Tuple[int, int]:
    return torus(x + dx, y + dy)


class Agent:
    __slots__ = ("x", "y", "energy")

    def __init__(self, x: int, y: int, energy: int = START_ENERGY) -> None:
        self.x = x
        self.y = y
        self.energy = energy

    def step(self, grass: List[List[int]]) -> Tuple[Optional["Agent"], bool]:
        self._move()
        self._eat(grass)
        child = self._maybe_reproduce()
        dead = self._is_dead()
        return child, dead

    def _move(self) -> None:
        dx, dy = random.choice(MOVE_CHOICES)
        self.x, self.y = in_bounds_torus(self.x, self.y, dx, dy)
        self.energy -= MOVE_COST

    def _eat(self, grass: List[List[int]]) -> None:
        cell_grass = grass[self.y][self.x]
        if cell_grass > 0:
            eaten = min(EAT_GAIN, cell_grass)
            grass[self.y][self.x] -= eaten
            self.energy += eaten

    def _maybe_reproduce(self) -> Optional["Agent"]:
        if self.energy >= REPRODUCTION_ENERGY_THRESHOLD and random.random() < REPRODUCTION_PROB:
            self.energy -= REPRODUCTION_COST
            cx, cy = in_bounds_torus(
                self.x, self.y,
                random.choice([-1, 0, 1]),
                random.choice([-1, 0, 1]),
            )
            return Agent(cx, cy, energy=START_ENERGY // 2)
        return None

    def _is_dead(self) -> bool:
        return self.energy <= 0


def init_world() -> Tuple[List[List[int]], List[Agent]]:
    grass = [[random.randint(0, GRASS_MAX) for _ in range(MAP_WIDTH)] for _ in range(MAP_HEIGHT)]
    agents = [Agent(random.randrange(MAP_WIDTH), random.randrange(MAP_HEIGHT)) for _ in range(START_AGENTS)]
    return grass, agents


def render(grass: List[List[int]], agents: List[Agent], tick: int, history: Deque[int]) -> None:
    screen_buffer: List[str] = []
    agent_positions = {(a.x, a.y) for a in agents}
    for y in range(MAP_HEIGHT):
        row_chars: List[str] = []
        for x in range(MAP_WIDTH):
            if (x, y) in agent_positions:
                row_chars.append("Ü")
            else:
                g = grass[y][x]
                row_chars.append(GRASS_CHARSET[min(g, len(GRASS_CHARSET) - 1)])
        screen_buffer.append("".join(row_chars))
    header = f"tick={tick} agents={len(agents)}"
    if history:
        avg_energy = sum(a.energy for a in agents) / len(agents) if agents else 0.0
        header += f" avgE={avg_energy:.1f}"
    print(CLEAR_SCREEN_ANSI, end="")
    print(header)
    print("\n".join(screen_buffer))


def grow_grass(grass: List[List[int]]) -> None:
    for y in range(MAP_HEIGHT):
        row = grass[y]
        for x in range(MAP_WIDTH):
            if row[x] < GRASS_MAX and random.random() < GRASS_GROW_PROB:
                row[x] += GRASS_GROW_AMOUNT


def reset_world_if_extinct(grass: List[List[int]], agents: List[Agent]) -> Tuple[List[List[int]], List[Agent]]:
    if agents:
        return grass, agents
    grass, agents = init_world()
    half_max = GRASS_MAX // 2
    for y in range(MAP_HEIGHT):
        for x in range(MAP_WIDTH):
            grass[y][x] = max(grass[y][x], half_max)
    return grass, agents


def simulate(steps: int = 300) -> None:
    grass, agents = init_world()
    history: Deque[int] = deque(maxlen=300)
    for tick in range(1, steps + 1):
        grow_grass(grass)

        new_agents: List[Agent] = []
        dead_count = 0
        for a in agents:
            child, dead = a.step(grass)
            if child:
                new_agents.append(child)
            if not dead:
                new_agents.append(a)
            else:
                dead_count += 1
        agents = new_agents

        history.append(len(agents))
        render(grass, agents, tick, history)

        grass, agents = reset_world_if_extinct(grass, agents)
        time.sleep(TICK_MS / 1000)


if __name__ == "__main__":
    simulate(steps=30)
