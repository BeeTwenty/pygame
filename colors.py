class Colors:
    color_dict = {
        "black": [(0, 0, 0)],
        "white": [(255, 255, 255)],
        "red": [(255, 0, 0)],
        "green": [(0, 255, 0)],
        "blue": [(0, 0, 255)],
        "gray": [(128, 128, 128)],
        "yellow": [(255, 255, 0)],
        "orange": [(255, 165, 0)],
        "purple": [(128, 0, 128)],
        "pink": [(255, 192, 203)],
        "brown": [(165, 42, 42)],
        "cyan": [(0, 255, 255)],
        "lime": [(0, 255, 0)],
        "magenta": [(255, 0, 255)],
        "olive": [(128, 128, 0)],
        "teal": [(0, 128, 128)],
        "navy": [(0, 0, 128)],
        "salmon": [(250, 128, 114)],
        "gold": [(255, 215, 0)],
        "violet": [(238, 130, 238)],
        "turquoise": [(64, 224, 208)],
        "indigo": [(75, 0, 130)],
        "peach": [(255, 218, 185)],
    }

    def __getattr__(self, name):
        if name in self.color_dict:
            return self.color_dict[name]
        raise AttributeError(f"'{self.__class__.__name__}' object has no attribute '{name}'")

colors = Colors()
