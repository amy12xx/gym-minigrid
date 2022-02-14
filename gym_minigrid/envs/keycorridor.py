from gym_minigrid.roomgrid import RoomGrid
from gym_minigrid.register import register

class KeyCorridor(RoomGrid):
    """
    A ball is behind a locked door, the key is placed in a
    random room.
    """

    def __init__(
        self,
        num_rows=3,
        obj_type="ball",
        room_size=6,
        seed=None,
        randomize=False,
    ):
        self.obj_type = obj_type
        self.randomize = randomize

        super().__init__(
            room_size=room_size,
            num_rows=num_rows,
            max_steps=30*room_size**2,
            seed=seed,
        )

    def _gen_grid(self, width, height):
        super()._gen_grid(width, height)

        # Connect the middle column rooms into a hallway
        for j in range(1, self.num_rows):
            self.remove_wall(1, j, 3)

        if self.randomize:
            color, obj_type = None, None
        else:
            color, obj_type = "red", self.obj_type

        # Add a locked door on the bottom right
        # Add an object behind the locked door
        room_idx = self._rand_int(0, self.num_rows)
        door, _ = self.add_door(2, room_idx, 2, locked=True, color=color)
        obj, _ = self.add_object(2, room_idx, kind=obj_type, color=color)

        # Add a key in a random room on the left side
        self.add_object(0, self._rand_int(0, self.num_rows), 'key', door.color)

        # Place the agent in the middle
        self.place_agent(1, self.num_rows // 2)

        # Make sure all rooms are accessible
        self.connect_all()

        self.obj = obj
        self.mission = "pick up the %s %s" % (obj.color, obj.type)

    def step(self, action):
        obs, reward, done, info = super().step(action)

        if action == self.actions.pickup:
            if self.carrying and self.carrying == self.obj:
                reward = self._reward()
                done = True

        return obs, reward, done, info

class KeyCorridorS3R1(KeyCorridor):
    def __init__(self, seed=None):
        super().__init__(
            room_size=3,
            num_rows=1,
            seed=seed,
            randomize=False
        )

class KeyCorridorS3R2(KeyCorridor):
    def __init__(self, seed=None):
        super().__init__(
            room_size=3,
            num_rows=2,
            seed=seed,
            randomize=False
        )

class KeyCorridorS3R3(KeyCorridor):
    def __init__(self, seed=None):
        super().__init__(
            room_size=3,
            num_rows=3,
            seed=seed,
            randomize=False
        )

class KeyCorridorS4R3(KeyCorridor):
    def __init__(self, seed=None):
        super().__init__(
            room_size=4,
            num_rows=3,
            seed=seed,
            randomize=False
        )

class KeyCorridorS5R3(KeyCorridor):
    def __init__(self, seed=None):
        super().__init__(
            room_size=5,
            num_rows=3,
            seed=seed,
            randomize=False
        )

class KeyCorridorS6R3(KeyCorridor):
    def __init__(self, seed=None):
        super().__init__(
            room_size=6,
            num_rows=3,
            seed=seed,
            randomize=False
        )

register(
    id='MiniGrid-KeyCorridorS3R1-v0',
    entry_point='gym_minigrid.envs:KeyCorridorS3R1'
)

register(
    id='MiniGrid-KeyCorridorS3R2-v0',
    entry_point='gym_minigrid.envs:KeyCorridorS3R2'
)

register(
    id='MiniGrid-KeyCorridorS3R3-v0',
    entry_point='gym_minigrid.envs:KeyCorridorS3R3'
)

register(
    id='MiniGrid-KeyCorridorS4R3-v0',
    entry_point='gym_minigrid.envs:KeyCorridorS4R3'
)

register(
    id='MiniGrid-KeyCorridorS5R3-v0',
    entry_point='gym_minigrid.envs:KeyCorridorS5R3'
)

register(
    id='MiniGrid-KeyCorridorS6R3-v0',
    entry_point='gym_minigrid.envs:KeyCorridorS6R3'
)
