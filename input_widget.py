from elements import canvas, rect_button, pygame, np
from model_ import mnist_model


class input_wgt:
    def __init__(self, *,origin: tuple[int, int]=(0, 0), model_obj: mnist_model, fps: int=24) -> None:
        self.origin = origin
        self.canvas = canvas(origin=(20 + origin[0], 90 + origin[1]), cell_size=13, fps=fps)
        self.predict_btn = rect_button(origin=(30 - origin[0], 490 - origin[1]), width=160, height=50, label='Predict',
                                     font_color=(255, 255, 255), font_size=40, action=self.pass_arr_to_model)
        self.clear_btn = rect_button(origin=(220 - origin[0], 490 - origin[1]), width=160, height=50, label='Clear',
                                     font_color=(255, 255, 255), font_size=40, action=self.reset)
        self.render_font = pygame.font.SysFont(None, 50)
        self.surface = pygame.surface.Surface((400, 600))
        self.model = model_obj

    def reset(self) -> None:
        self.canvas.reset_canvas()
        self.model.reset()
        

    def pass_arr_to_model(self) -> None:
        self.canvas.canvas_dump()
        self.model.predict(np.array([self.canvas.dump]))


    def update_widget(self) -> None:
        self.surface.fill((40, 40, 40))
        text = self.render_font.render('Canvas', 1, (255, 255, 255))
        text_rect = text.get_rect()
        text_rect.centerx, text_rect.centery = (self.canvas.surface.get_width() + self.canvas.origin[0]) // 2, 70
        self.surface.blit(text, text_rect)
        self.canvas.update_widget()
        self.predict_btn.update_widget()
        self.clear_btn.update_widget()
        self.surface.blit(self.canvas.surface, self.canvas.origin)
        self.surface.blit(self.predict_btn.surface, self.predict_btn.origin)
        self.surface.blit(self.clear_btn.surface, self.clear_btn.origin)
