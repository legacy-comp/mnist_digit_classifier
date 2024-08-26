from elements import plot_prediction, pygame, np


class output_wgt:
    def __init__(self, *, origin: tuple[int, int]=(400, 0), font: str=None, font_size: int=50) -> None:
        """Helper widget used to show output based on `model.prediction`.

        Parameters
        ----------
        origin : tuple[int, int]
            coordinate of the top left point of the output widget (in pixels)
        """

        self.origin = origin
        self.surface = pygame.surface.Surface((400, 600))
        self.label_0_pred = plot_prediction(origin=(0, 150), label='0', font_size=30)
        self.label_1_pred = plot_prediction(origin=(0, 180), label='1', font_size=30)
        self.label_2_pred = plot_prediction(origin=(0, 210), label='2', font_size=30)
        self.label_3_pred = plot_prediction(origin=(0, 240), label='3', font_size=30)
        self.label_4_pred = plot_prediction(origin=(0, 270), label='4', font_size=30)
        self.label_5_pred = plot_prediction(origin=(0, 300), label='5', font_size=30)
        self.label_6_pred = plot_prediction(origin=(0, 330), label='6', font_size=30)
        self.label_7_pred = plot_prediction(origin=(0, 360), label='7', font_size=30)
        self.label_8_pred = plot_prediction(origin=(0, 390), label='8', font_size=30)
        self.label_9_pred = plot_prediction(origin=(0, 420), label='9', font_size=30)
        self.render_font = pygame.font.SysFont(font, font_size)
        self.prediction_arr = np.zeros((10, ))


    def update_prediction(self, pred_arr: np.ndarray=np.array([np.zeros((10, ))])) -> None:
        """Updates the prediction output based on value of `pred_arr`.

        Parameters
        ----------
        pred_arr : np.ndarray
            2D numpy array containing the `model.prediction` (shape: 1x10).
        """

        self.label_0_pred.prediction = pred_arr[0][0]
        self.label_1_pred.prediction = pred_arr[0][1]
        self.label_2_pred.prediction = pred_arr[0][2]
        self.label_3_pred.prediction = pred_arr[0][3]
        self.label_4_pred.prediction = pred_arr[0][4]
        self.label_5_pred.prediction = pred_arr[0][5]
        self.label_6_pred.prediction = pred_arr[0][6]
        self.label_7_pred.prediction = pred_arr[0][7]
        self.label_8_pred.prediction = pred_arr[0][8]
        self.label_9_pred.prediction = pred_arr[0][9]


    def update_widget(self) -> None:
        """Updates the output_widget state.

        This function is meant to be called ***every*** iteration of the program.
        """

        self.surface.fill((40, 40, 40))
        text = self.render_font.render('Prediction', 1, (255, 255, 255))
        text_rect = text.get_rect()
        text_rect.center = (200, 70)
        self.surface.blit(text, text_rect)
        self.label_0_pred.update_widget()
        self.label_1_pred.update_widget()
        self.label_2_pred.update_widget()
        self.label_3_pred.update_widget()
        self.label_4_pred.update_widget()
        self.label_5_pred.update_widget()
        self.label_6_pred.update_widget()
        self.label_7_pred.update_widget()
        self.label_8_pred.update_widget()
        self.label_9_pred.update_widget()
        self.surface.blit(self.label_0_pred.surface, self.label_0_pred.origin)
        self.surface.blit(self.label_1_pred.surface, self.label_1_pred.origin)
        self.surface.blit(self.label_2_pred.surface, self.label_2_pred.origin)
        self.surface.blit(self.label_3_pred.surface, self.label_3_pred.origin)
        self.surface.blit(self.label_4_pred.surface, self.label_4_pred.origin)
        self.surface.blit(self.label_5_pred.surface, self.label_5_pred.origin)
        self.surface.blit(self.label_6_pred.surface, self.label_6_pred.origin)
        self.surface.blit(self.label_7_pred.surface, self.label_7_pred.origin)
        self.surface.blit(self.label_8_pred.surface, self.label_8_pred.origin)
        self.surface.blit(self.label_9_pred.surface, self.label_9_pred.origin)
