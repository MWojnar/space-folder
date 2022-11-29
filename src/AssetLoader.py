import pygame
from Sprite import Sprite

class AssetLoader(object):
    def __init__(self, world):
        # Player sprites
        self.spaceguyStand = Sprite(world, pygame.image.load("images\\spr_spaceguy_stand.png").convert_alpha(), 1)
        self.spaceguyJump = Sprite(world, pygame.image.load("images\\spr_spaceguy_jump.png").convert_alpha(), 1)
        self.spaceguyFloat = Sprite(world, pygame.image.load("images\\spr_spaceguy_float.png").convert_alpha(), 1)
        self.spaceguyCrouch = Sprite(world, pygame.image.load("images\\spr_spaceguy_crouch.png").convert_alpha(), 1)
        self.spaceguyDie = Sprite(world, pygame.image.load("images\\spr_spaceguy_die_8frames.png").convert_alpha(), 8)
        self.spaceguyDieHead = Sprite(world, pygame.image.load("images\\spr_spaceguy_die_head.png").convert_alpha(), 1)
        self.spaceguyRespawn = Sprite(world, pygame.image.load("images\\spr_spaceguy_spawn_10frames.png").convert_alpha(), 10)
        
        # Spike sprites
        self.smallSpikes = Sprite(world, pygame.image.load("images\\spr_small_spikes.png"), 1)
        self.mediumSpikes = Sprite(world, pygame.image.load("images\\spr_medium_spikes.png"), 1)
        self.bigSpikes = Sprite(world, pygame.image.load("images\\spr_big_spikes.png"), 1)
        
        # Pull Orb, Tether, Range sprites
        self.pullOrb = Sprite(world, pygame.image.load("images\\spr_attract_4frames.png").convert_alpha(), 4)
        self.pullTether = Sprite(world, pygame.image.load("images\\spr_attract_tether_3frames.png").convert_alpha(), 3)
        self.pullRange = Sprite(world, pygame.image.load("images\\spr_attract_range.png").convert_alpha(), 1)
        
        self.repelOrb = Sprite(world, pygame.image.load("images\\spr_repel_4frames.png").convert_alpha(), 4)
        self.repelTether = Sprite(world, pygame.image.load("images\\spr_repel_tether_3frames.png").convert_alpha(), 3)
        self.repelRange = self.pullRange#Sprite(world, pygame.image.load("images\\spr_repel_range").convert_alpha(), 1)
        
        self.bgEarth = Sprite(world, pygame.image.load("images\\bg_earth.png").convert_alpha(), 1)
        self.bgSpace = pygame.image.load("images\\bg_space.png").convert()
        
        # Platform sprites
        self.satellitePlatform = Sprite(world, pygame.image.load("images\\ts_satellite_platform.png").convert_alpha(), 10, 0)
        
        # Bouncy sprites
        self.bouncy = Sprite(world, pygame.image.load("images\\spr_bouncy_5frames.png").convert_alpha(), 5)
        
        # Checkpoint sprites
        self.checkpoint = Sprite(world, pygame.image.load("images\\spr_checkpoint_not_got.png").convert_alpha(), 1)
        self.checkpointGet = Sprite(world, pygame.image.load("images\\spr_checkpoint_get_10frames.png").convert_alpha(), 10)
        self.checkpointGot = Sprite(world, pygame.image.load("images\\spr_checkpoint_6frames.png").convert_alpha(), 6)
        
        # Rocket sprites
        self.endRocket = Sprite(world, pygame.image.load("images\\spr_end_rocket.png").convert_alpha(), 1)
        self.endRocketTakeoff = Sprite(world, pygame.image.load("images\\spr_end_rocket_exit_3frames.png").convert_alpha(), 3)
        
        # Arrow sprites
        self.arrowSegment = Sprite(world, pygame.image.load("images\\spr_arrow_segment.png").convert_alpha(), 1)
        self.arrowTip = Sprite(world, pygame.image.load("images\\spr_arrow_tip.png").convert_alpha(), 1)
        
        # UI sprites
        self.mouse = Sprite(world, pygame.image.load("images\\spr_mouse.png").convert_alpha(), 1)
        self.mouseCanClick = Sprite(world, pygame.image.load("images\\spr_mouse_canclick.png").convert_alpha(), 1)
        
        self.start = Sprite(world, pygame.image.load("images\\spr_start.png").convert_alpha(), 1)
        self.startSelected = Sprite(world, pygame.image.load("images\\spr_start_selected.png").convert_alpha(), 1)
        
        self.quit = Sprite(world, pygame.image.load("images\\spr_quit.png").convert_alpha(), 1)
        self.quitSelected = Sprite(world, pygame.image.load("images\\spr_quit_selected.png").convert_alpha(), 1)
        
        self.title = Sprite(world, pygame.image.load("images\\spr_title.png").convert_alpha(), 1)
        
        self.victory = Sprite(world, pygame.image.load("images\\spr_victory.png").convert_alpha(), 1)
        
        self.tutorial = Sprite(world, pygame.image.load("images\\spr_Instructions.png").convert_alpha(), 1)
        
        self.wojWorks = Sprite(world, pygame.image.load("images\\spr_WojWorks.png").convert_alpha(), 1)
        
        self.dribblePromo = Sprite(world, pygame.image.load("images\\spr_promo.png").convert_alpha(), 1)
        self.dribblePromoSelected = Sprite(world, pygame.image.load("images\\spr_promo_selected.png").convert_alpha(), 1)

        
        # Main theme song
        self.sndMainTheme = pygame.mixer.music.load("sounds\\SpaceSong_Loop.mp3")
        
        # Sounds
        # Entity sounds
        self.sndDie = pygame.mixer.Sound("sounds\\snd_die.wav")
        self.sndJump = pygame.mixer.Sound("sounds\\snd_jump.wav")
        self.sndLand = pygame.mixer.Sound("sounds\\snd_land.wav")
        
        self.sndPullOrb = pygame.mixer.Sound("sounds\\snd_attract.wav")
        self.sndBouncy = pygame.mixer.Sound("sounds\\snd_bouncy.wav")
        self.sndRepelOrb = pygame.mixer.Sound("sounds\\snd_repel.wav")
        self.sndRocket = pygame.mixer.Sound("sounds\\snd_rocket.wav")
        
        # Menu sounds
        self.sndSelect = pygame.mixer.Sound("sounds\\snd_select.wav") # FIXME: Implement