import time

class Actions:
    no      = 'none'
    shoot   = "shoot"
    shield  = "shield"
    grenade = "grenade"
    reload  = "reload"
    logout  = "logout"
    all = [no, shoot, shield, grenade, reload]

class Player:

    def __init__(self, id: int):
        self.id = id

        self.max_grenades       = 2
        self.max_shields        = 3
        self.bullet_hp          = 10
        self.grenade_hp         = 30
        self.shield_max_time    = 10
        self.shield_health_max  = 30
        self.magazine_size      = 6
        self.max_hp             = 100

        self.hp             = self.max_hp
        self.action         = 'none'
        self.bullets        = self.magazine_size
        self.grenades       = self.max_grenades
        self.shield_time    = 0
        self.shield_health  = 0
        self.num_shield     = self.max_shields
        self.num_deaths     = 0
        
        self.shield_start_time = time.time()-30

    def get_bullet_count(self):
        return self.bullets

    def get_shield_count(self):
        return self.num_shield
    
    def get_grenade_count(self):
        return self.grenades

    def get_action(self):
        return self.action

    def set_action(self, action):
        self.action = action

    def get_dict (self):
        _player = dict()
        _player['hp']               = self.hp
        _player['action']           = self.action
        _player['bullets']          = self.bullets
        _player['grenades']         = self.grenades
        _player['shield_time']      = self.shield_time
        _player['shield_health']    = self.shield_health
        _player['num_deaths']       = self.num_deaths
        _player['num_shield']       = self.num_shield
        return _player

    def is_action_valid(self, action):
        ret = True
        # check if the shield has to reduced
        if action == Actions.shield:
            if self.shield_time > 0:
                # invalid
                return False

        elif action == Actions.shoot:
            if self.bullets <= 0:
                # invalid
                return False

        elif action == Actions.grenade:
            if self.grenades <= 0:
                # invalid
                return False

        elif action == Actions.reload:
            if self.bullets > 0:
                # invalid
                return False

        return True


    def update(self, is_in_sight, action_self, action_opponent, action_opponent_is_valid):
        self.action = action_self

        # check if the shield has to reduced
        if self.shield_time > 0:
            if action_self == Actions.shield:
                # invalid
                pass
            self.shield_time = max(self.shield_max_time - (time.time() - self.shield_start_time), 0)

        elif action_self == Actions.shield:
            if self.num_shield > 0:
                self.num_shield        -= 1
                self.shield_time        = self.shield_max_time
                self.shield_health      = self.shield_health_max
                self.shield_start_time  = time.time()

        # update shield HP
        if self.shield_time <= 0:
            self.shield_health = 0

        # check for harm
        if action_opponent_is_valid:
            if not is_in_sight:
                # we are protected from harm
                pass
            else:
                hp_reduction = 0
                if action_opponent == Actions.shoot:
                    hp_reduction = self.bullet_hp
                elif action_opponent == Actions.grenade:
                    hp_reduction = self.grenade_hp
                if self.shield_time > 0:
                    if self.shield_health > 0:
                        self.shield_health -= hp_reduction
                    if self.shield_health < 0:
                        # we loose health
                        hp_reduction = -1*self.shield_health
                        self.shield_health = 0
                    else:
                        hp_reduction = 0
                # change the health
                self.hp -= hp_reduction
                if self.hp <= 0:
                    # we are dead
                    self.hp = self.max_hp
                    self.num_deaths += 1
                    self.hp         = self.max_hp
                    self.action     = action_self
                    self.bullets    = self.magazine_size
                    self.grenades   = self.max_grenades
                    self.shield_time = 0
                    self.shield_health = 0
                    self.num_shield = self.max_shields

        # check for reduction in ammo
        if action_self == Actions.shoot:
            self.bullets = max(0, self.bullets - 1)

        if action_self == Actions.grenade:
            self.grenades = max(0, self.grenades-1)

        if action_self == Actions.reload:
            if self.bullets > 0:
                # invalid
                pass
            else:
                self.bullets = self.magazine_size


    def check_and_update_correct_state(self, correct_data: dict) -> bool:

        isCorrect = True
        
        if self.hp != correct_data['hp']:
            print("current HP of player %d is %d, but should be %d" % (self.id, self.hp, correct_data['hp']))
            self.hp = correct_data['hp']
            isCorrect = False

        if self.action != correct_data['action']:
            print(f"current action of player %d is %s, but should be %s" % (self.id, self.action, correct_data['action']))
            self.action = correct_data['action']
            isCorrect = False

        if self.bullets != correct_data['bullets']:
            print(f"current bullets of player %d is %d, but should be %d" % (self.id, self.bullets, correct_data['bullets']))
            self.bullets = correct_data['bullets']
            isCorrect = False

        if self.grenades != correct_data['grenades']:
            print(f"current grenades of player %d is %d, but should be %d" % (self.id, self.grenades, correct_data['grenades']))
            self.grenades = correct_data['grenades']
            isCorrect = False

        if self.shield_time != correct_data['shield_time']:
            print(f"current shield time of player %d is %d, but should be %d" % (self.id, self.shield_time, correct_data['shield_time']))
            self.shield_time = correct_data['shield_time']
            isCorrect = False

        if self.shield_health != correct_data['shield_health']:
            print(f"current shield health of player %d is %d, but should be %d" % (self.id, self.shield_health, correct_data['shield_health']))
            self.shield_health = correct_data['shield_health']
            isCorrect = False

        if self.num_deaths != correct_data['num_deaths']:
            print(f"current num deaths of player %d is %d, but should be %d"  % (self.id, self.num_deaths, correct_data['num_deaths']))
            self.num_deaths = correct_data['num_deaths']
            isCorrect = False

        if self.num_shield != correct_data['num_shield']:
            print(f"current num shield of player %d is %d, but should be %d"  % (self.id, self.num_shield, correct_data['num_shield']))
            self.num_shield = correct_data['num_shield']
            isCorrect = False

        if isCorrect:
            print("State of " + str(self.id) + " is correct! :)")

        return isCorrect
