class Team:

    def __init__(self):
        # left player
        # offensive stats
        self.left_shots = 0
        self.left_makes = 0

        self.left_back_cups = 0
        self.left_middle_cups = 0
        self.left_front_cups = 0
        self.left_touchdowns = 0

        self.left_misses = 0
        self.left_offensive_sacks = 0
        self.left_offensive_interceptions = 0

        # defensive stats
        self.left_sacks = 0
        self.left_interceptions = 0
        self.left_sacks_dropped = 0
        self.left_interceptions_dropped = 0

        # special teams stats
        self.left_xp_attempts = 0
        self.left_xp_makes = 0
        self.left_xp_misses = 0
        self.left_fg_attempts = 0
        self.left_fg_makes = 0
        self.left_fg_misses = 0

        # right player
        # offensive stats
        self.right_shots = 0
        self.right_makes = 0

        self.right_back_cups = 0
        self.right_middle_cups = 0
        self.right_front_cups = 0
        self.right_touchdowns = 0

        self.right_misses = 0
        self.right_offensive_sacks = 0
        self.right_offensive_interceptions = 0

        # defensive stats
        self.right_sacks = 0
        self.right_interceptions = 0
        self.right_sacks_dropped = 0
        self.right_interceptions_dropped = 0

        # special teams stats
        self.right_xp_attempts = 0
        self.right_xp_makes = 0
        self.right_xp_misses = 0
        self.right_fg_attempts = 0
        self.right_fg_makes = 0
        self.right_fg_misses = 0

        # team status
        self.possession = False
        self.shooter = None
        self.front_cups = 3
        self.middle_cups = 2
        self.back_cups = 1

    def get_possession(self):
        self.possession = True

    def set_left_shooter(self):
        self.shooter = 'left'

    def set_right_shooter(self):
        self.shooter = 'right'

    def reset_rack(self):
        self.front_cups = 3
        self.middle_cups = 2
        self.back_cups = 1
