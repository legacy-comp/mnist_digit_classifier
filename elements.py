import pygame
import numpy as np


class rect_button:
    def __init__(self, *, origin: tuple[int, int]=(0, 0), width: int, height: int,
                 label: str='', font: str=None, font_color: tuple[int, int, int], font_size: int, action=None) -> None:
        """Rectangular Button widget provides user interaction through button presses.

        Parameters
        ----------
        origin : tuple[int, int]
            coordinate of the top left point of the button (in pixels)
        width : int
            width of the button (in pixels)
        height : int
            height of the button (in pixels)
        label : str
            text to be rendered on the button
        font : str
            type of font to be rendered on the button
        font_color : tuple[int, int, int]
            color of font to be rendered on the button (in rgb)
        font_size : int
            size of the font to be rendered on the button
        action : `user_function` or `None`
            defines the action performed by the button
        """

        # default colors
        self.colors = {
            'GRAY1': (80, 80, 80),    # button color on hover 
            'GRAY2': (100, 100, 100), # button color without hover
            'GRAY3': (170, 170, 170)  # border color on hover
        }
        self.origin = origin
        self.width = width
        self.height = height
        self.label = label
        self.label_font_color = font_color
        self.render_font = pygame.font.SysFont(font, font_size)
        self.surface = pygame.surface.Surface((width, height))
        self.rects = (pygame.rect.Rect(0, 0, width, height),
                      pygame.rect.Rect(1, 1, width - 2, height -2))
        self.func_action = action


    def get_pressed(self):
        """Defines the action performed by the widget.

        Can be customized to anything.

        DEFAULT_BEHAVIOR: None

        To change behavior, pass any function in the `action` parameter of the widget object.
        """

        if self.func_action is None:
            return
        self.func_action()


    def area_of_action(self) -> bool:
        """Defines the area in which the user can interact with the button.

        Returns
        -------
        aoa : bool
            returns `True` if cursor is within the defined confinements of the button
        """

        pos = pygame.mouse.get_pos()
        aoa = self.origin[0] < pos[0] < self.origin[0] + self.width and self.origin[1] < pos[1] < self.origin[1] + self.height
        return aoa


    def update_widget(self) -> None:
        """Updates the button state.

        This function is meant to be called ***every*** iteration of the program.
        """

        if self.area_of_action():
            pygame.draw.rect(surface=self.surface, color=self.colors.get('GRAY3'), rect=self.rects[0], width=1)
            pygame.draw.rect(surface=self.surface, color=self.colors.get('GRAY1'), rect=self.rects[1])
        else:
            pygame.draw.rect(surface=self.surface, color=self.colors.get('GRAY2'), rect=self.rects[0])

        text = self.render_font.render(self.label, 1, self.label_font_color)
        text_rect = text.get_rect()
        text_rect.center = self.rects[0].center
        self.surface.blit(text, text_rect)



class canvas:
    def __init__(self, *, origin: tuple[int, int]=(0, 0), cell_size: int, fps: int=24) -> None:
        """Interactive display widget of 28x28 resolution used to take ***Handwritten Digit Input (HDI)*** from the user.

        Parameters
        ----------
        origin : tuple[int, int]
            coordinate of the top left point of the canvas (in pixels)
        cell_size : int
            size of the side of 1x1 cell in the canvas
        fps : int
            frame rate at which the widget is updating
        """

        self.origin = origin
        self.cell_size = cell_size
        self.fps = fps
        self.arr = np.zeros((28, 28))    # stores the user HDI
        self.colors = {
            'BLACK': (0, 0, 0),
            'GRAY1': (35, 35, 35),
            'GRAY2': (75, 75, 75),
            'GRAY3': (135, 135, 135),
            'WHITE': (255, 255, 255)
        }
        self.surface = pygame.surface.Surface((28*cell_size, 28*cell_size))
        self.dump = None                # temporary storage of HDI (shape: 1x784)


    def canvas_dump(self) -> None:
        """Dumps the content of the canvas in the `dump` while reshaping it (shape: 1x784).
        """

        self.dump = self.arr.copy().reshape(-1)


    def reset_canvas(self) -> None:
        """Clears the canvas.
        """

        self.arr = np.zeros((28, 28))


    def drawing_on_canvas(self) -> None:
        """This function handles the ***drawing*** on canvas.

        It calculates the mouse position relative to the canvas and increments the corresponding cell values.
        """

        pos = pygame.mouse.get_pos()
        X, Y = pos[0] - self.origin[0], pos[1] - self.origin[1]
        col_indx, row_indx = X // self.cell_size, Y // self.cell_size
        if col_indx not in (0, 27):
            if row_indx not in (0, 27):
                for x in (-1, 0, 1):
                    for y in (-1, 0, 1):
                        if (x, y) in ((0, -1), (-1, 0), (1, 0), (0, 1)):
                            rate = 15 / self.fps
                        elif (x, y) in ((-1, -1), (1, 1), (1, -1), (-1, 1)):
                            rate = 5 / self.fps
                        else:
                            rate = 45 / self.fps
                        curr_val = self.arr[row_indx + x, col_indx + y]
                        if curr_val < 1:
                            curr_val += rate
                            self.arr[row_indx + x, col_indx + y] = min(1, curr_val)


    def area_of_action(self) -> bool:
        """Defines the area in which the user can interact with the canvas.

        Returns
        -------
        aoa : bool
            returns `True` if cursor is within the defined confinements of the canvas
        """

        pos = pygame.mouse.get_pos()
        aoa = self.origin[0] < pos[0] < self.origin[0] + self.surface.get_width() and self.origin[1] < pos[1] < self.origin[1] + self.surface.get_height()
        return aoa


    def update_widget(self) -> None:
        """Updates the canvas state.

        This function is meant to be called ***every*** iteration of the program.
        """

        for row, col in np.ndindex(self.arr.shape):
            curr_val = self.arr[row, col]
            if curr_val == 0:
                color = self.colors.get('BLACK')
            elif 0.1 <= curr_val < 0.4:
                color = self.colors.get('GRAY1')
            elif 0.4 <= curr_val < 0.6:
                color = self.colors.get('GRAY2')
            elif 0.6 < curr_val < 1:
                color = self.colors.get('GRAY3')
            else:
                color = self.colors.get('WHITE')
            pygame.draw.rect(self.surface, color, (self.cell_size*col, self.cell_size*row, self.cell_size, self.cell_size))



class plot_prediction:
    def __init__(self, *, origin: tuple[int, int]=(0, 0), prediction: float=0, label: str='', font: str=None, font_size: int) -> None:
        """Used to present the `mnist model` prediction about the user provided handwritten digit.

        Parameters
        ----------
        origin : tuple[int, int]
            coordinate of the top left point of the plot_prediction_widget (in pixels)
        prediction : float
            the confidence rating of the `mnist model` about the `label`
        label : str
            label of the class to be presented
        font : str
            type of font to be rendered on the label
        font_size : int
            size of the font to be rendered on the label
        """

        self.origin = origin
        self.prediction = prediction
        self.color = {
            'WHITE': (255, 255, 255),
            'OFFWHITE': (180, 180, 180)
        }
        self.label = label
        self.render_font = pygame.font.SysFont(font, font_size)
        self.surface = pygame.surface.Surface((400, 20))


    def update_widget(self) -> None:
        """Updates the plot_prediction_widget state.

        This function is meant to be called ***every*** iteration of the program.
        """

        self.surface.fill((40, 40, 40))
        pygame.draw.rect(self.surface, self.color.get('WHITE'), (33, 3, 290 * self.prediction - 3, 17))
        pygame.draw.rect(self.surface, self.color.get('OFFWHITE'), (30, 0, 290 * self.prediction, 20), 3)

        text = self.render_font.render(self.label, 1, self.color.get('WHITE'))
        text_rect = text.get_rect()
        text_rect.topleft = (10, 0)
        self.surface.blit(text, text_rect)

        text = self.render_font.render(f'{self.prediction*100:.2f}%', 1, self.color.get('WHITE'))
        text_rect = text.get_rect()
        text_rect.topleft = (320, 0)
        self.surface.blit(text, text_rect)
