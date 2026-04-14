import pygame, random, sys, math
import base64, io
import pygame

pygame.init()

WIDTH, HEIGHT = 800, 600
FPS = 60
screen=pygame.display.set_mode((WIDTH,HEIGHT))

# ── Base64 데이터 ──
SHEET_B64 = "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"

# ── 시트 로드 ──
sheet_bytes = base64.b64decode(SHEET_B64)
player_sheet = pygame.image.load(io.BytesIO(sheet_bytes)).convert_alpha()

# ── 프레임 리스트 (인덱스 0 ~ 27) ──
FRAME_W, FRAME_H = 8, 11
COLS = 7

player_frames = []
# 애니메이션 변수
anim_index = 0
anim_timer = 0
anim_speed = 8  # 프레임 속도 (작을수록 빠름)
player_dir = "middle"  # left, middle, right

for i in range(28):
    row, col = divmod(i, COLS)
    rect = pygame.Rect(col * FRAME_W, row * FRAME_H, FRAME_W, FRAME_H)
    player_frames.append(player_sheet.subsurface(rect))

PlayerFrames_Middle = [player_frames[i] for i in [1, 8, 15, 22]]
PlayerFrames_Left = [player_frames[i] for i in [0, 7, 14, 21]]
PlayerFrames_Right = [player_frames[i] for i in [2, 9, 16, 23]]

WHITE=(255,255,255)
GRAY=(20,20,40)
BLUE=(50,150,255)
RED=(220,50,50)
YELLOW=(240,220,0)
GREEN=(50,220,80)
ORANGE=(240,140,0)


clock=pygame.time.Clock()
font=pygame.font.SysFont("malgungothic",24)
font_big=pygame.font.SysFont("malgungothic",64)

MENU,PLAYING,GAME_OVER=0,1,2
PLAYER_W, PLAYER_H = 40,40

def draw_player(surf, rect, last_hit):
    global anim_index, anim_timer, player_dir

    now = pygame.time.get_ticks()

    # 방향별 프레임 선택
    if player_dir == "left":
        frames = PlayerFrames_Left
    elif player_dir == "right":
        frames = PlayerFrames_Right
    else:
        frames = PlayerFrames_Middle

    # 애니메이션 진행
    anim_timer += 1
    if anim_timer >= anim_speed:
        anim_timer = 0
        anim_index = (anim_index + 1) % len(frames)

    img = frames[anim_index]

    # 크기 확대 (원하면 조절)
    img = pygame.transform.scale(img, (rect.width, rect.height))

    # 피격 무적 깜빡임
    if now - last_hit < 1500:
        if (now // 200) % 2 == 0:
            surf.blit(img, rect.topleft)
    else:
        surf.blit(img, rect.topleft)

def create_bullet(pos, angle, speed=6, owner="enemy"):
    return {"x":pos[0],"y":pos[1],
            "dx":math.cos(angle)*speed,
            "dy":math.sin(angle)*speed,
            "owner":owner}

class Enemy:
    def __init__(self,x,y,level):
        self.rect=pygame.Rect(x,y,40,40)
        self.level=level
        self.hp=3+level
        self.spawn_time = pygame.time.get_ticks()  # ★ 추가

class EnemyA(Enemy):
    def __init__(self,x,y,level):
        super().__init__(x,y,level)
        self.cool=[2500,2000,1500][level]
        self.last=0
    def update(self,player):
        now=pygame.time.get_ticks()
        bullets=[]

        # ★ 스폰 후 1초 공격 금지
        if now - self.spawn_time < 1000:
            return []

        if now-self.last>self.cool:
            self.last=now
            dx=player.centerx-self.rect.centerx
            dy=player.centery-self.rect.centery
            angle=math.atan2(dy,dx)
            bullets.append(create_bullet(self.rect.center,angle))
            if self.level>=1:
                bullets.append(create_bullet(self.rect.center,angle+0.25))
                bullets.append(create_bullet(self.rect.center,angle-0.25))
        return bullets
    def draw(self,screen):
        pygame.draw.circle(screen,RED,self.rect.center,18)

class EnemyB(Enemy):
    def __init__(self,x,y,level):
        super().__init__(x,y,level)
        self.cool=[3500,3000,2500][level]
        self.state="idle"
        self.last=0
    def update(self,player):
        now=pygame.time.get_ticks()
        bullets=[]

        if now - self.spawn_time < 1000:
            return []

        if self.state=="idle" and now-self.last>self.cool:
            self.state="move"
            self.start=now
            self.target=(player.centerx, random.randint(50, HEIGHT//2))
        elif self.state=="move":
            t=(now-self.start)/500
            if t>=1:
                self.rect.centerx=self.target[0]
                self.rect.centery=self.target[1]
                self.state="shoot"
            else:
                self.rect.centerx += (self.target[0]-self.rect.centerx)*t
                self.rect.centery += (self.target[1]-self.rect.centery)*t
        elif self.state=="shoot":
            bullets.append(create_bullet(self.rect.center, math.pi/2, 8))
            self.state="idle"
            self.last=now
        return bullets
    def draw(self,screen):
        pygame.draw.polygon(screen,ORANGE,[
            (self.rect.left,self.rect.top),
            (self.rect.right,self.rect.top),
            (self.rect.centerx,self.rect.bottom),
        ])

class EnemyC(Enemy):
    def __init__(self,x,y,level):
        super().__init__(x,y,level)
        self.cool=[999999,4500,4000][level]
        self.state="idle"
        self.angle=0
        self.last=pygame.time.get_ticks()
        self.spin_step=0
        self.spin_last=0
    def update(self,player,game_level):
        now=pygame.time.get_ticks()
        bullets=[]

        if now - self.spawn_time < 1000:
            return []

        if game_level==0: return []

        if self.state=="idle" and now-self.last>self.cool:
            self.state="move"
            self.start=now
            self.target=(random.randint(50,WIDTH-50), random.randint(50,HEIGHT//2))
        elif self.state=="move":
            t=(now-self.start)/500
            if t>=1:
                self.rect.centerx=self.target[0]
                self.rect.centery=self.target[1]
                self.state="spin"
                self.spin_start=now
                self.spin_step=0
                self.spin_last=now
            else:
                self.rect.centerx += (self.target[0]-self.rect.centerx)*t
                self.rect.centery += (self.target[1]-self.rect.centery)*t
        elif self.state=="spin":
            if now - self.spin_last > 250 and self.spin_step<4:
                self.spin_last=now
                self.angle+=0.2
                for i in range(4):
                    a=self.angle+i*(math.pi/2)
                    bullets.append(create_bullet(self.rect.center,a,4))
                self.spin_step+=1
            if self.spin_step>=4:
                self.state="idle"
                self.last=now
        return bullets
    def draw(self,screen):
        pygame.draw.circle(screen,GREEN,self.rect.center,24)

def main():
    state=MENU
    player=pygame.Rect(WIDTH//2,HEIGHT-70,PLAYER_W,PLAYER_H)
    hp=5
    bullets=[]
    enemies=[]
    shoot_cd=0
    spawn_timer=0
    start_time=0
    last_hit=0
    level_prev=-1
    level_display_time=0

    while True:
        clock.tick(FPS)
        for e in pygame.event.get():
            if e.type==pygame.QUIT:
                pygame.quit(); sys.exit()
            if state==MENU and e.type==pygame.KEYDOWN:
                state=PLAYING
                start_time=pygame.time.get_ticks()

        if state==MENU:
            screen.fill((10,10,30))
            screen.blit(font_big.render("PRESS ANY KEY",True,WHITE),(200,250))
            pygame.display.flip()
            continue

        elapsed=(pygame.time.get_ticks()-start_time)//1000
        if elapsed<60: level=0
        elif elapsed<120: level=1
        else: level=2

        if level!=level_prev:
            level_display_time=pygame.time.get_ticks()
            level_prev=level
        
        keys=pygame.key.get_pressed()
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            player.x-=6
            player_dir = "left"
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            player.x+=6
            player_dir = "right"
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            player.y-=6
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            player.y+=6
            
        player.x = max(0, min(WIDTH-PLAYER_W, player.x))
        player.y = max(0, min(HEIGHT-PLAYER_H, player.y))

        shoot_cd-=1
        if keys[pygame.K_SPACE] and shoot_cd<=0:
            bullets.append(create_bullet(player.center,-math.pi/2,8,"player"))
            shoot_cd=15

        spawn_timer+=1

        # ★ 적 없으면 3초, 있으면 5초
        spawn_cool = FPS*3 if len(enemies)==0 else FPS*5

        if len(enemies)<5 and spawn_timer>spawn_cool:
            spawn_timer=0
            t=random.choice(["A","B"] if level==0 else ["A","B","C"])
            x=random.randint(50,WIDTH-50)
            y=random.randint(50,HEIGHT//2)
            if t=="A": enemies.append(EnemyA(x,y,level))
            if t=="B": enemies.append(EnemyB(x,y,level))
            if t=="C": enemies.append(EnemyC(x,y,level))

        new_bullets=[]
        for en in enemies:
            if isinstance(en,EnemyC):
                new_bullets+=en.update(player,level)
            else:
                new_bullets+=en.update(player)
        bullets+=new_bullets

        new=[]
        for b in bullets:
            b["x"]+=b["dx"]; b["y"]+=b["dy"]
            hit=False
            if b["owner"]=="enemy":
                if pygame.time.get_ticks()-last_hit>1500 and player.collidepoint(b["x"],b["y"]):
                    hp-=1; hit=True; last_hit=pygame.time.get_ticks()
            if b["owner"]=="player":
                for en in enemies:
                    if en.rect.collidepoint(b["x"],b["y"]):
                        en.hp-=1; hit=True; break
            if not hit: new.append(b)
        bullets=new

        removed = any(e.hp<=0 for e in enemies)
        enemies=[e for e in enemies if e.hp>0]
        if removed:
            spawn_timer=0

        if hp<=0: state=GAME_OVER

        if state==GAME_OVER:
            screen.fill((0,0,0))
            screen.blit(font_big.render("GAME OVER",True,RED),(200,250))
            pygame.display.flip()
            continue

        screen.fill(GRAY)
        draw_player(screen,player,last_hit)
        for en in enemies: en.draw(screen)
        for b in bullets:
            color=GREEN if b["owner"]=="player" else YELLOW
            pygame.draw.circle(screen,color,(int(b["x"]),int(b["y"])),4)
        screen.blit(font.render(f"HP:{hp}",True,WHITE),(10,10))
        screen.blit(font.render(f"Time:{elapsed}",True,WHITE),(10,40))

        if pygame.time.get_ticks()-level_display_time<1000:
            level_text = font_big.render(f"Level {level+1}",True,YELLOW)
            screen.blit(level_text,(WIDTH//2 - level_text.get_width()//2, HEIGHT//2 - level_text.get_height()//2))

        pygame.display.flip()

main()
