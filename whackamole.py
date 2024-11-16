import pygame
import random


def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))

        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()

        mole_x, mole_y = 0,0
        mole_rect = mole_image.get_rect(topleft=(mole_x, mole_y))


        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    click_x, click_y = event.pos


                    if mole_rect.collidepoint(click_x, click_y):
                        mole_x = (random.randrange(0,20)) * 32 + 3
                        mole_y = (random.randrange(0,16)) * 32 + 4
                        mole_rect.topleft = (mole_x, mole_y)


            screen.fill("light green")

            #20 lines
            pygame.draw.line(screen, color="black", start_pos=(0, 0), end_pos=(0, 512))
            pygame.draw.line(screen, color="black", start_pos=(32, 0), end_pos=(32, 512))
            pygame.draw.line(screen, color="black", start_pos=(64, 0), end_pos=(64, 512))
            pygame.draw.line(screen, color="black", start_pos=(96, 0), end_pos=(96, 512))
            pygame.draw.line(screen, color="black", start_pos=(32, 0), end_pos=(32, 512))
            pygame.draw.line(screen, color="black", start_pos=(128, 0), end_pos=(128, 512))
            pygame.draw.line(screen, color="black", start_pos=(160, 0), end_pos=(160, 512))
            pygame.draw.line(screen, color="black", start_pos=(192, 0), end_pos=(192, 512))
            #pygame.draw.line(screen, color="black", start_pos=(32, 0), end_pos=(32, 512))
            pygame.draw.line(screen, color="black", start_pos=(224, 0), end_pos=(224, 512))
            pygame.draw.line(screen, color="black", start_pos=(256, 0), end_pos=(256, 512))
            pygame.draw.line(screen, color="black", start_pos=(288, 0), end_pos=(288, 512))
            pygame.draw.line(screen, color="black", start_pos=(320, 0), end_pos=(320, 512))
            pygame.draw.line(screen, color="black", start_pos=(352, 0), end_pos=(352, 512))
            pygame.draw.line(screen, color="black", start_pos=(384, 0), end_pos=(384, 512))
            pygame.draw.line(screen, color="black", start_pos=(416, 0), end_pos=(416, 512))
            pygame.draw.line(screen, color="black", start_pos=(448, 0), end_pos=(448, 512))
            pygame.draw.line(screen, color="black", start_pos=(480, 0), end_pos=(480, 512))
            pygame.draw.line(screen, color="black", start_pos=(512, 0), end_pos=(512, 512))
            pygame.draw.line(screen, color="black", start_pos=(544, 0), end_pos=(544, 512))
            pygame.draw.line(screen, color="black", start_pos=(576, 0), end_pos=(576, 512))
            pygame.draw.line(screen, color="black", start_pos=(608, 0), end_pos=(608, 512))
            pygame.draw.line(screen, color="black", start_pos=(640, 0), end_pos=(640, 512))
            # 16 lines
            pygame.draw.line(screen, color="black", start_pos=(0, 0), end_pos=(640, 0))
            pygame.draw.line(screen, color="black", start_pos=(0, 32), end_pos=(640, 32))
            pygame.draw.line(screen, color="black", start_pos=(0, 64), end_pos=(640, 64))
            pygame.draw.line(screen, color="black", start_pos=(0, 96), end_pos=(640, 96))
            pygame.draw.line(screen, color="black", start_pos=(0, 128), end_pos=(640, 128))
            pygame.draw.line(screen, color="black", start_pos=(0, 160), end_pos=(640, 160))
            pygame.draw.line(screen, color="black", start_pos=(0, 192), end_pos=(640, 192))
            pygame.draw.line(screen, color="black", start_pos=(0, 224), end_pos=(640, 224))
            pygame.draw.line(screen, color="black", start_pos=(0, 256), end_pos=(640, 256))
            pygame.draw.line(screen, color="black", start_pos=(0, 288), end_pos=(640, 288))
            pygame.draw.line(screen, color="black", start_pos=(0, 320), end_pos=(640, 320))
            pygame.draw.line(screen, color="black", start_pos=(0, 352), end_pos=(640, 352))
            pygame.draw.line(screen, color="black", start_pos=(0, 384), end_pos=(640, 384))
            pygame.draw.line(screen, color="black", start_pos=(0, 416), end_pos=(640, 416))
            pygame.draw.line(screen, color="black", start_pos=(0, 448), end_pos=(640, 448))
            pygame.draw.line(screen, color="black", start_pos=(0, 480), end_pos=(640, 480))
            pygame.draw.line(screen, color="black", start_pos=(0, 512), end_pos=(640, 512))



            screen.blit(mole_image, mole_rect)

            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
