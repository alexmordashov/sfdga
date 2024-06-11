import pygame
import time
from job import Job
from button import Button


def job_window(student, start_time):
    width = 475
    height = 600
    fps = 30
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Работа')

    button_6 = Button(382, 10, 83, 83,
                      "Работа", 18)

    font_spec = pygame.font.Font(None, 18)
    health = font_spec.render(f'Здоровье: {"{:.1f}".format(float(student.health))}', True, (0, 0, 0))
    mood = font_spec.render(f'Настроение: {"{:.1f}".format(float(student.mood))}', True, (0, 0, 0))
    energy = font_spec.render(f'Энергия: {student.energy}', True, (0, 0, 0))
    iq = font_spec.render(f'Интелект: {student.iq}', True, (0, 0, 0))
    rating = font_spec.render(f'Рейтинг в универе: {"{:.1f}".format(float(student.rating))}', True, (0, 0, 0))
    money = font_spec.render(f'Деньги: {student.money}', True, (0, 0, 0))
    date = font_spec.render(f'Дата: {student.date.day}.{student.date.month}.{student.date.year}', True,
                            (0, 0, 0))

    clock = pygame.time.Clock()
    running = True
    while running:
        clock.tick(fps)
        current_time = int(time.time())
        if (current_time - start_time) % 2 == 0 and current_time - start_time != 0:
            arg = student.next_day()
            if arg:
                # running = False
                return 0
            #

            health = font_spec.render(f'Здоровье: {"{:.1f}".format(float(student.health))}', True, (0, 0, 0))
            mood = font_spec.render(f'Настроение: {"{:.1f}".format(float(student.mood))}', True, (0, 0, 0))
            energy = font_spec.render(f'Энергия: {student.energy}', True, (0, 0, 0))
            iq = font_spec.render(f'Интелект: {student.iq}', True, (0, 0, 0))
            rating = font_spec.render(f'Рейтинг в универе: {"{:.1f}".format(float(student.rating))}', True, (0, 0, 0))
            money = font_spec.render(f'Деньги: {student.money}', True, (0, 0, 0))
            date = font_spec.render(f'Дата: {student.date.day}.{student.date.month}.{student.date.year}', True,
                                    (0, 0, 0))
            start_time = current_time
        screen.fill((255, 255, 255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 0
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if button_6.main_rect.collidepoint(event.pos):
                    button_6.on_click()
                    button_6.on_hover(action=False)
                    button_6.draw(screen)
                    #
                    job = Job(button_6.text, 1000, 0, 0, 0, 0)
                    job.is_job(student)
                    job.process(student)
                    #
                    print(button_6.text)
                    button_6.on_click(action=False)
        if button_6.main_rect.collidepoint(pygame.mouse.get_pos()):
            button_6.on_hover()
        elif not button_6.main_rect.collidepoint(pygame.mouse.get_pos()):
            button_6.on_hover(action=False)
        button_6.draw(screen)
        #
        screen.blit(health, (20, 20))
        screen.blit(mood, (20, 40))
        screen.blit(energy, (20, 60))
        screen.blit(iq, (20, 80))
        screen.blit(rating, (20, 100))
        screen.blit(money, (20, 120))
        screen.blit(date, (20, 140))

        pygame.display.flip()
    pygame.quit()
