import os
from libqtile import bar, widget
from libqtile.lazy import lazy
from libqtile.config import Screen

from functions import PWA
# widget_defaults = dict(
#     font="Ubuntu Mono",
#     fontsize = 12,
#     padding = 2,
#     background=colors[2]
# )

# extension_defaults = widget_defaults.copy()


class MyWidgets:
    def __init__(self, home):
        self.home = home
        self.colors = [
            ["#383838", "#383838"],  # panel background
            # background for current screen tab
            ["#434758", "#434758"],
            ["#ffffff", "#ffffff"],  # font color for group names
            # border line color for current tab
            ["#bc13fe", "#bc13fe"],  # Group down color
            # border line color for other tab and odd widgets
            ["#8d62a9", "#8d62a9"],
            ["#668bd7", "#668bd7"],  # color for the even widgets
            ["#e1acff", "#e1acff"],  # window name

            ["#000000", "#000000"],
            ["#AD343E", "#AD343E"], #8
            ["#f76e5c", "#f76e5c"],
            ["#F39C12", "#F39C12"],
            ["#F7DC6F", "#F7DC6F"],
            ["#f1ffff", "#f1ffff"],
            ["#4c566a", "#4c566a"], 
        ]

        self.terminal = "alacritty"

    def init_widgets_list(self):
        '''
        Function that returns the desired widgets in form of list
        '''
        widgets_list = [
            widget.Sep(
                linewidth=0,
                padding=10,
                foreground=self.colors[2],
                background=self.colors[0]
            ),
            widget.GroupBox(
                font="Ubuntu Bold",
                fontsize=12,
                margin_y=2,
                margin_x=0,
                padding_y=5,
                padding_x=3,
                borderwidth=3,
                active=self.colors[-2],
                inactive=self.colors[-1],
                # rounded=True,
                rounded=False,
                # highlight_color=self.colors[9],
                # highlight_method="line",
                highlight_method='block',
                urgent_alert_method='block',
                # urgent_border=self.colors[9],
                this_current_screen_border=self.colors[9],
                this_screen_border=self.colors[4],
                other_current_screen_border=self.colors[0],
                other_screen_border=self.colors[0],
                foreground=self.colors[2],
                background=self.colors[0],
                disable_drag=True
            ),
            widget.Prompt(
                prompt=lazy.spawncmd(),
                font="Ubuntu Mono",
                padding=10,
                foreground=self.colors[3],
                background=self.colors[1]
            ),
            widget.Sep(
                linewidth=0,
                padding=10,
                foreground=self.colors[2],
                background=self.colors[0]
            ),
            widget.TaskList(
                highlight_method = 'block', # or block
                icon_size=17,
                max_title_width=100,
                rounded=True,
                padding=4,
                margin_y=0,
                fontsize=14,
                border= self.colors[8],
                foreground=self.colors[2],
                margin=2,
                txt_floating='🗗',
                txt_minimized='>_ ',
                borderwidth = 2,
                background=self.colors[0],
                urgent_border=self.colors[3]
                #unfocused_border = 'border'
            ),
            widget.TextBox(
                text='',
                background=self.colors[0],
                foreground=self.colors[11],
                padding=0,
                fontsize=37
            ),
            widget.CPU(
                font="Ubuntu Mono",
                format = '{freq_current}GHz {load_percent}%',
                update_interval = 1,
                fontsize = 12,
                foreground=self.colors[7],
                background=self.colors[11],
                #mouse_callbacks = {'Button1': lambda qtile: qtile.cmd_spawn('alacritty -e htop')},
            ),
            widget.TextBox(
                text=" |",
                foreground=self.colors[7],
                background=self.colors[11],
                padding=0,
                fontsize=14
            ),
            widget.Memory(
                foreground=self.colors[7],
                background=self.colors[11],
                # format='{{}}-{MemTotal}',
                # mouse_callbacks={'Button1': lambda qtile: qtile.cmd_spawn(
                #     self.termite + ' -e htop')},
                padding=5
            ),
            widget.TextBox(
                text='',
                background=self.colors[11],
                foreground=self.colors[10],
                padding=0,
                fontsize=37
            ),
            widget.TextBox(
                text="  ",
                foreground=self.colors[7],
                background=self.colors[10],
                padding=0,
                # mouse_callbacks={
                #     "Button1": lambda qtile: qtile.cmd_spawn("pavucontrol")}
            ),
            widget.Volume(
                foreground=self.colors[7],
                background=self.colors[10],
                padding=5
            ),
            widget.TextBox(
                text='',
                background=self.colors[10],
                foreground=self.colors[9],
                padding=0,
                fontsize=37
            ),
            widget.CurrentLayoutIcon(
                custom_icon_paths=[os.path.expanduser(
                    "~/.config/qtile/icons")],
                foreground=self.colors[0],
                background=self.colors[9],
                padding=0,
                scale=0.7
            ),
            widget.CurrentLayout(
                foreground=self.colors[7],
                background=self.colors[9],
                padding=5
            ),
            widget.TextBox(
                text='',
                foreground=self.colors[8],
                background=self.colors[9],
                padding=0,
                fontsize=37
            ),
            widget.Clock(
                foreground=self.colors[2],
                background=self.colors[8],
                # mouse_callbacks={
                #     "Button1": lambda qtile: qtile.cmd_spawn(PWA.calendar())},
                format="%B %d  [ %H:%M ]"
            ),
            widget.Sep(
                linewidth=0,
                padding=5,
                foreground=self.colors[0],
                background=self.colors[8]
            ),
            widget.BatteryIcon(
                background=self.colors[8],
                theme_path=self.home + "/.config/qtile/icons/battery-icons",
                update_interval=1
            ),
            widget.Systray(
                background=self.colors[8],
                padding=5
            ),
        ]
        return widgets_list

    def init_widgets_screen(self):
        '''
        Function that returns the widgets in a list.
        It can be modified so it is useful if you  have a multimonitor system
        '''
        widgets_screen = self.init_widgets_list()

        widgets_screen.append(
            widget.Sep(
                    linewidth=0,
                    padding=10,
                    foreground=self.colors[2],
                    background=self.colors[8]
                ),
        )

        return widgets_screen

    def init_widgets_screen2(self):
        '''
        Function that returns the widgets in a list.
        It can be modified so it is useful if you  have a multimonitor system
        '''
        widgets_screen2 = self.init_widgets_screen()
        widgets_screen2.pop()
        return widgets_screen2

    def init_screen(self):
        '''
        Init the widgets in the screen
        '''
        configs = {
            "opacity": 1.0, 
            "margin": [5, 10, 0, 10],
            "size": 20, 
        }

        return [
            Screen(top=bar.Bar(widgets=self.init_widgets_screen(), **configs)),
            Screen(top=bar.Bar(widgets=self.init_widgets_screen2(), **configs))
        ]
