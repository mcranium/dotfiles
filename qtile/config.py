# Current modified config file for the qtile window manager
# Mario Schaedel 2020
# This config is developed from the default Arcolinux D config
# with inspiration from Derek Taylor's config at
# https://gitlab.com/dwt1/dotfiles/blob/master/.config/qtile/config.py

import os
import re
import socket
import subprocess
from libqtile import qtile
from libqtile.config import Drag, Key, Screen, Group, Click, Rule
from libqtile.command import lazy
from libqtile import layout, bar, widget, hook
from libqtile.widget import Spacer
import arcobattery
from Xlib import display as xdisplay # for the multi monitor stuff

#mod4 or mod = super key
mod = "mod4"
mod1 = "alt"
mod2 = "control"
home = os.path.expanduser('~')


@lazy.function
def window_to_prev_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i - 1].name)

@lazy.function
def window_to_next_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i + 1].name)

myTerm = 'alacritty'
myFM = 'thunar'

keys = [

# To do: arrange the keybindings in a more useful way

# SUPER + FUNCTION KEYS

    Key([mod], "f", lazy.spawn(myFM+' /home/mario/Documents/')),
    Key([mod], "v", lazy.spawn('pavucontrol')),
    Key([mod], "x", lazy.spawn('arcolinux-logout')),
    Key([mod], "Return", lazy.spawn(myTerm)),
    Key([mod], "d", lazy.spawn('libreoffice --writer')),
    Key([mod], "c", lazy.spawn('libreoffice --calc')),
    Key([mod], "z", lazy.spawn('zotero')),
    Key([mod], "w", lazy.spawn('firefox')),
    Key([mod], "i", lazy.spawn('inkscape')),
    Key([mod], "g", lazy.spawn('gimp')),
    Key([mod], "m", lazy.spawn('thunderbird')),
    Key([mod, "shift"], "t", lazy.spawn('sh /home/mario/Programs/deuteranop.sh')),
    Key([mod], "p", lazy.spawn('sh /home/mario/Programs/colorpicker.sh')),

# SUPER + SHIFT KEYS

    Key([mod, "shift"], "Return", lazy.spawn(myFM+' /home/mario/Documents/')),
    Key([mod, "shift"], "q", lazy.window.kill()),
    Key([mod, "shift"], "r", lazy.restart()),
    Key([mod, "control"], "r", lazy.restart()),
    # To do: the dmenu colours and font sizes should be adjusted
    Key([mod, "shift"], "d", lazy.spawn("dmenu_run -i -nb '#191919' -nf '#fea63c' -sb '#fea63c' -sf '#191919' -fn 'NotoMonoRegular:pixelsize=20'")),
    Key([mod, "shift"], "c", lazy.spawn(myTerm+' -e nvim /home/mario/.config/qtile/config.py')),
    Key([mod, "shift"], "n", lazy.spawn(myTerm+' -e nvim /home/mario/.config/nvim/init.vim')),

# HTOP
    Key([], "XF86Tools", lazy.spawn(myTerm+' -e htop')),

# SCREENSHOTS
    Key([], "Print", lazy.spawn('xfce4-screenshooter -r')),

# INCREASE/DECREASE BRIGHTNESS
    Key([], "XF86MonBrightnessUp", lazy.spawn("xbacklight -inc 10")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("xbacklight -dec 10")),

# SET UP MULTIPLE SCREENS
    Key([], "XF86Display", lazy.spawn("arandr")),

# INCREASE/DECREASE/MUTE VOLUME
    Key([], "XF86AudioMute", lazy.spawn("amixer -q set Master toggle")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("amixer -q set Master 5%-")),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer -q set Master 5%+")),

# QTILE LAYOUT KEYS
    Key([mod], "n", lazy.layout.normalize()),
    Key([mod], "Tab", lazy.next_layout()),

# CHANGE FOCUS
    Key([mod], "Up", lazy.layout.up()),
    Key([mod], "Down", lazy.layout.down()),
    Key([mod], "Left", lazy.layout.left()),
    Key([mod], "Right", lazy.layout.right()),
    Key([mod], "h", lazy.layout.left()),
    Key([mod], "j", lazy.layout.down()),
    Key([mod], "k", lazy.layout.up()),
    Key([mod], "l", lazy.layout.right()),

# For Column layout: toggle stack vs. rows
    Key([mod], "space", lazy.layout.toggle_split()),

# RESIZE UP, DOWN, LEFT, RIGHT
    Key([mod, "control"], "h",
        lazy.layout.grow_left(),
        lazy.layout.shrink(),
        lazy.layout.decrease_ratio(),
        #lazy.layout.add(),
        ),
    Key([mod, "control"], "j",
        lazy.layout.grow_down(),
        lazy.layout.shrink(),
        lazy.layout.increase_nmaster(),
        ),
    Key([mod, "control"], "k",
        lazy.layout.grow_up(),
        lazy.layout.grow(),
        lazy.layout.decrease_nmaster(),
        ),
    Key([mod, "control"], "l",
        lazy.layout.grow_right(),
        lazy.layout.grow(),
        lazy.layout.increase_ratio(),
        #lazy.layout.delete(),
        ),

# MOVE WINDOWS UP OR DOWN MONADTALL/MONADWIDE LAYOUT
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(),
            lazy.layout.client_to_previous()), # for stack layout
    Key([mod, "shift"], "k", lazy.layout.shuffle_up()),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down()),
        Key([mod, "shift"], "l", lazy.layout.shuffle_right(),
            lazy.layout.client_to_next()), # for stack layout

    Key([mod, "shift"], "Up", lazy.layout.shuffle_up()),
    Key([mod, "shift"], "Down", lazy.layout.shuffle_down()),
    Key([mod, "shift"], "Left", lazy.layout.shuffle_left()),
    Key([mod, "shift"], "Right", lazy.layout.shuffle_right()),

# TOGGLE FLOATING LAYOUT
    Key([mod, "shift"], "f", lazy.window.toggle_floating()),

# SWITCH FOCUS BETWEEN SCREENS
    Key([mod], "comma", lazy.prev_screen()),
    Key([mod], "period", lazy.next_screen()),

#CHANGE WORKSPACES (SUPER + CAPSLOCK + H/J/K/L)
    Key([mod], "grave", lazy.screen.togglegroup()),

    Key(["mod1"], "j", lazy.screen.next_group()),
    Key(["mod1"], "l", lazy.screen.next_group()),
    Key(["mod1"], "h", lazy.screen.prev_group()),
    Key(["mod1"], "k", lazy.screen.prev_group()),
    ]

groups = []
group_names = ["1", "2", "3", "4", "5", "6", "7",]
group_labels = ["", "", "🖉", "📚", "", "", "♫",]
group_layouts = ["columns", "columns", "columns", "columns", "max", "columns", "columns",]

for i in range(len(group_names)):
    groups.append(
        Group(
            name=group_names[i],
            layout=group_layouts[i].lower(),
            label=group_labels[i],
        ))


for i in groups:
    keys.extend([
        Key([mod], i.name, lazy.group[i.name].toscreen()), # go to another workspace
        Key([mod, "shift"], # move a window to another workspace
            i.name,
            lazy.window.togroup(i.name) ,
            lazy.group[i.name].toscreen()), # move with the window to the other workspace
    ])

def init_layout_theme():
    return {"margin":0,
            "border_width":2,
            "border_focus": "#5E9726",
            "border_normal": "#4c566a"
            }

layout_theme = init_layout_theme()

layouts = [
    layout.Columns(
        fair=False,
        insert_position=1,
        margin=0,
        num_columns=2,
        border_width=2,
        border_focus="#5E9726",
        border_normal="#4c566a",
        border_on_single=False,
        border_focus_stack="881111"),
    # layout.MonadTall(
        # margin=0,
        # border_width=2,
        # border_focus="#5E9726",
        # border_normal="#4c566a",
        # single_border_width=0,
        # ratio=0.6,
        # name='tall'),
    layout.Max(**layout_theme)
]


# COLORS FOR THE BAR

def init_colors():
    return [["#2F343F", "#2F343F"], # color 0
            ["#2F343F", "#2F343F"], # color 1
            ["#c0c5ce", "#c0c5ce"], # color 2
            ["#fba922", "#fba922"], # color 3
            ["#3384d0", "#3384d0"], # color 4
            ["#f3f4f5", "#f3f4f5"], # color 5
            ["#cd1f3f", "#cd1f3f"], # color 6
            ["#62FF00", "#62FF00"], # color 7
            ["#6790eb", "#6790eb"], # color 8
            ["#a9a9a9", "#a9a9a9"]] # color 9


colors = init_colors()


# WIDGETS FOR THE BAR

# def open_htop():
    # qtile.cmd.spawn('alacritty -e htop')

# def open_cal():
    # qtile.cmd.spawn('alacritty --hold -e cal')


def init_widgets_defaults():
    return dict(font="Noto Sans",
                fontsize = 12,
                padding = 2,
                background=colors[1])

widget_defaults = init_widgets_defaults()

def init_widgets_list():
    prompt = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())
    widgets_list = [
               widget.GroupBox(font="FontAwesome",
                        fontsize = 16,
                        margin_y = 2,
                        margin_x = 0,
                        padding_y = 6,
                        padding_x = 5,
                        borderwidth = 0,
                        disable_drag = True,
                        active = colors[9],
                        inactive = colors[5],
                        rounded = False,
                        highlight_method = "text",
                        this_current_screen_border = colors[8],
                        foreground = colors[2],
                        background = colors[1]
                        ),
               widget.Sep(
                        linewidth = 1,
                        padding = 10,
                        foreground = colors[2],
                        background = colors[1]
                        ),
               widget.CurrentLayout(
                        font = "Noto Sans Bold",
                        foreground = colors[5],
                        background = colors[1]
                        ),
               widget.Sep(
                        linewidth = 1,
                        padding = 10,
                        foreground = colors[2],
                        background = colors[1]
                        ),
               widget.WindowName(font="Noto Sans",
                        fontsize = 12,
                        foreground = colors[5],
                        background = colors[1],
                        ),
               arcobattery.BatteryIcon(
                        padding=0,
                        scale=0.7,
                        y_poss=2,
                        theme_path=home + "/.config/qtile/icons/battery_icons_horiz",
                        update_interval = 5,
                        background = colors[1]
                        ),
               # to do: CPU graph is not working
               #widget.CPUGraph(
                   #border_color = colors[2],
                   #fill_color = colors[8],
                   #graph_color = colors[8],
                   #background=colors[1],
                   #border_width = 1,
                   #line_width = 1,
                   #core = "all",
                   #type = "box"
                   #),
               widget.Sep(
                        linewidth = 1,
                        padding = 10,
                        foreground = colors[2],
                        background = colors[1]
                        ),
               widget.TextBox(
                        font="FontAwesome",
                        text="  ",
                        foreground=colors[4],
                        background=colors[1],
                        padding = 0,
                        mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(myTerm + ' -t htop -e htop')},
                        fontsize=16
                        ),
               widget.Memory(
                        font="Noto Sans",
                        format = '{MemUsed}M/{MemTotal}M',
                        mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(myTerm + ' -t htop -e htop')},
                        update_interval = 1,
                        fontsize = 12,
                        foreground = colors[5],
                        background = colors[1]
                       ),
               widget.Sep(
                        linewidth = 1,
                        padding = 10,
                        foreground = colors[2],
                        background = colors[1]
                        ),
               widget.TextBox(
                        font="FontAwesome",
                        text="  ",
                        foreground=colors[3],
                        background=colors[1],
                        padding = 0,
                        mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(myTerm + ' --hold -t cal -e cal -3')},
                        fontsize=16
                        ),
               widget.Clock(
                        font="Noto Sans",
                        foreground = colors[5],
                        background = colors[1],
                        fontsize = 14,
                        mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(myTerm + ' --hold -t cal -e cal -3')},
                        format="%a %d.%m.%Y "
                        ),
               widget.Clock(
                        font="Noto Sans Bold", 
                        foreground = colors[5],
                        background = colors[1],
                        fontsize = 14,
                        mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(myTerm + ' --hold -t cal -e cal -3')},
                        format="%H:%M"
                        ),
               widget.Sep(
                        linewidth = 1,
                        padding = 10,
                        foreground = colors[2],
                        background = colors[1]
                        ),
               widget.Systray(
                        background=colors[1],
                        icon_size=20,
                        padding = 4
                        ),
               widget.Sep(
                        linewidth = 1,
                        padding = 10,
                        foreground = colors[2],
                        background = colors[1]
                        ),
               widget.Volume(emoji=False),
              ]
    return widgets_list

widgets_list = init_widgets_list()


# SCREENS
# GET THE NUMBER OF SCREENS (needs: from Xlib import display as xdisplay)

def get_num_monitors():
    num_monitors = 0
    try:
        display = xdisplay.Display()
        screen = display.screen()
        resources = screen.root.xrandr_get_screen_resources()

        for output in resources.outputs:
            monitor = display.xrandr_get_output_info(output, resources.config_timestamp)
            preferred = False
            if hasattr(monitor, "preferred"):
                preferred = monitor.preferred
            elif hasattr(monitor, "num_preferred"):
                preferred = monitor.num_preferred
            if preferred:
                num_monitors += 1
    except Exception as e:
        # always setup at least one monitor
        return 1
    else:
        return num_monitors

num_monitors = get_num_monitors()

def init_widgets_screen1():
    widgets_screen1 = init_widgets_list()
    return widgets_screen1

def init_widgets_screen2():
    widgets_screen2 = init_widgets_list()
    return widgets_screen2

widgets_screen1 = init_widgets_screen1()
widgets_screen2 = init_widgets_screen2()


screens = [
    Screen(
        top=bar.Bar(widgets=init_widgets_screen1(), 
            size=26),
        wallpaper='~/Pictures/titanoptera_alder2.jpg', 
        wallpaper_mode='fill',
    )
]

if num_monitors > 1:
    for m in range(num_monitors - 1):
        screens.append(
                Screen(
                    top=bar.Bar(widgets=init_widgets_screen1(), 
                        size=26),
                    wallpaper='~/Pictures/titanoptera_alder2.jpg',
                    wallpaper_mode='fill',
                )
        )


# MOUSE CONFIGURATION
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size())
]

dgroups_key_binder = None
dgroups_app_rules = []


main = None

@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser('~')
    subprocess.call([home + '/.config/qtile/scripts/autostart.sh'])

@hook.subscribe.startup
def start_always():
    # Set the cursor to something sane in X
    subprocess.Popen(['xsetroot', '-cursor_name', 'left_ptr'])

@hook.subscribe.client_new
def set_floating(window):
    if (window.window.get_wm_transient_for()
            or window.window.get_wm_type() in floating_types):
        window.floating = True

floating_types = ["notification", "toolbar", "splash", "dialog"]


follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    {'wmclass': 'Arcolinux-welcome-app.py'},
    {'wmclass': 'Arcolinux-tweak-tool.py'},
    {'wmclass': 'confirm'},
    {'wmclass': 'dialog'},
    {'wmclass': 'download'},
    {'wmclass': 'error'},
    {'wmclass': 'file_progress'},
    {'wmclass': 'notification'},
    {'wmclass': 'splash'},
    {'wmclass': 'toolbar'},
    {'wmclass': 'confirmreset'},
    {'wmclass': 'makebranch'},
    {'wmclass': 'maketag'},
    {'wmclass': 'Arandr'},
    {'wmclass': 'feh'},
    {'wmclass': 'Galculator'},
    {'wmclass': 'arcolinux-logout'},
    #{'wmclass': 'xfce4-terminal'},
    {'wname': 'branchdialog'},
    {'wname': 'Open File'},
    {'wname': 'pinentry'},
    {'wmclass': 'ssh-askpass'},
    # {'wname': 'Quick Format Citation'},     
    # aesthetically pleasing but unusable because losing focus all the time
    {'wmclass': 'Arandr'},

],  fullscreen_border_width = 0, border_width = 0)
auto_fullscreen = True

focus_on_window_activation = "focus" # or smart

wmname = "LG3D"
