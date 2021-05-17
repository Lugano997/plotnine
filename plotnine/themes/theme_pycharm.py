from .elements import element_line, element_rect, element_text, element_blank
from .theme import theme
from .theme_gray import theme_gray


class theme_pycharm(theme_gray):
    """
    The dark cousin of :class:`theme_light`, with similar line
    sizes but a dark background. Useful to make thin colored
    lines pop out.

    Parameters
    ----------
    base_size : int, optional
        Base font size. All text sizes are a scaled versions of
        the base font size. Default is 11.
    base_family : str, optional
        Base font family.
    """

    def __init__(self, base_size=11, base_family=None):
        theme_gray.__init__(self, base_size, base_family)
        self.add_theme(theme(
            axis_ticks=element_line(color='#2B2B2B', size=0.5),
            axis_ticks_minor=element_blank(),
            legend_key=element_rect(
                fill='#7F7F7F', color='#666666', size=0.5),
            panel_background=element_rect(fill='#363636', color='None'),
            plot_background=element_rect(fill='#2B2B2B', color='None'),
            panel_grid_major=element_line(color='#2B2B2B', size=0.5),
            panel_grid_minor=element_line(color='#2B2B2B', size=0.25),
            strip_background=element_rect(fill='#2B2B2B', color='None'),
            strip_text_x=element_text(color='#9D9D9D'),
            strip_text_y=element_text(color='#9D9D9D', angle=-90),
            figure_size=(10, 7), plot_margin=0.15,
            legend_background=element_rect(fill='#2B2B2B'),
            legend_text=element_text(color='#9D9D9D'),
            text=element_text(color='#9D9D9D')
        ), inplace=True)
