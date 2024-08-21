import input_widget
import output_widget
import model_
import pygame

pygame.display.init()
pygame.font.init()
pygame.display.set_caption("Mnist Digit Classifier")

WIDTH, HEIGHT = 800, 600
FPS = 24

BLACK = (0, 0, 0)

DISPLAY = pygame.display.set_mode((WIDTH, HEIGHT))
model = model_.mnist_model()
input_wgt = input_widget.input_wgt(origin=(0, 0), model_obj=model, fps=FPS)
output_wgt = output_widget.output_wgt(origin=(400, 0))


def draw_screen(DISPLAY):
    DISPLAY.fill(BLACK)
    input_wgt.update_widget()
    output_wgt.update_widget()
    DISPLAY.blit(input_wgt.surface, input_wgt.origin)
    DISPLAY.blit(output_wgt.surface, output_wgt.origin)
    pygame.display.flip()


def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_wgt.predict_btn.area_of_action():
                    input_wgt.predict_btn.get_pressed()
                    output_wgt.update_prediction(model.prediction)
                if input_wgt.clear_btn.area_of_action():
                    input_wgt.clear_btn.get_pressed()
                    output_wgt.update_prediction()

            if pygame.mouse.get_pressed()[0]:
                if input_wgt.canvas.area_of_action():
                    input_wgt.canvas.drawing_on_canvas()
        draw_screen(DISPLAY)


if __name__ == '__main__':
    main()
