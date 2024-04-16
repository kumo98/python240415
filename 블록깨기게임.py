import pygame
import sys
from pygame.locals import *

# 화면 크기 설정
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 300

# 블럭 설정
BLOCK_WIDTH = 50
BLOCK_HEIGHT = 20
BLOCK_COLOR = (255, 0, 0)

# 패들 설정
PADDLE_WIDTH = 60
PADDLE_HEIGHT = 10
PADDLE_COLOR = (0, 255, 0)

# 공 설정
BALL_RADIUS = 10
BALL_COLOR = (0, 0, 255)

# 초기화
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("블럭 깨기 게임")

clock = pygame.time.Clock()

# 블럭 생성
blocks = []
for y in range(5):
    for x in range(8):
        block_rect = pygame.Rect(x * (BLOCK_WIDTH + 5) + 30, y * (BLOCK_HEIGHT + 5) + 30, BLOCK_WIDTH, BLOCK_HEIGHT)
        blocks.append(block_rect)

# 패들 생성
paddle = pygame.Rect((SCREEN_WIDTH - PADDLE_WIDTH) // 2, SCREEN_HEIGHT - PADDLE_HEIGHT - 10, PADDLE_WIDTH, PADDLE_HEIGHT)

# 공 생성
ball = pygame.Rect(200, 250, BALL_RADIUS, BALL_RADIUS)
ball_speed_x = 0
ball_speed_y = 0

def reset_ball():
    global ball_speed_x, ball_speed_y
    ball.left = 200
    ball.top = 250
    ball_speed_x = 3
    ball_speed_y = -3

reset_ball()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_SPACE:
                if ball_speed_y == 0:
                    ball_speed_y = -3

    # 패들 이동
    keys = pygame.key.get_pressed()
    if keys[K_LEFT]:
        paddle.x -= 5
    if keys[K_RIGHT]:
        paddle.x += 5

    # 화면을 검정색으로 지우기
    screen.fill((0, 0, 0))

    # 블럭 그리기
    for block in blocks:
        pygame.draw.rect(screen, BLOCK_COLOR, block)

    # 패들 그리기
    pygame.draw.rect(screen, PADDLE_COLOR, paddle)

    # 공 그리기
    pygame.draw.circle(screen, BALL_COLOR, (ball.x + BALL_RADIUS, ball.y + BALL_RADIUS), BALL_RADIUS)

    # 공 이동
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # 벽에 부딪히면 방향 반전
    if ball.left <= 0 or ball.right >= SCREEN_WIDTH:
        ball_speed_x *= -1
    if ball.top <= 0:
        ball_speed_y *= -1

    # 패들과 충돌 검사
    if ball.colliderect(paddle):
        ball_speed_y *= -1

    # 블럭과 충돌 검사
    for block in blocks[:]:
        if ball.colliderect(block):
            blocks.remove(block)
            ball_speed_y *= -1

    # 패들이 화면을 벗어나지 않도록 제한
    if paddle.left <= 0:
        paddle.left = 0
    elif paddle.right >= SCREEN_WIDTH:
        paddle.right = SCREEN_WIDTH

    # 공이 바닥에 닿으면 다시 시작
    if ball.top >= SCREEN_HEIGHT:
        reset_ball()

    # 화면 업데이트
    pygame.display.update()
    clock.tick(60)
