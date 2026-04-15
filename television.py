class Television:

    MIN_VOLUME: int = 0
    MAX_VOLUME: int = 2
    MIN_CHANNEL: int = 0
    MAX_CHANNEL: int = 3

    def __init__(self):
        self.status: bool = False
        self.muted: bool = False
        self.volume: int = Television.MIN_VOLUME
        self.channel: int = Television.MIN_CHANNEL

    def power(self):
        self.status: bool
        if self.status:
            self.status = False
        elif not self.status:
            self.status = True

    def mute(self):
        self.muted: bool
        if self.muted:
            self.muted = False
        elif not self.muted:
            self.muted = True

    def channel_up(self):
        self.channel: int

        if self.channel == Television.MAX_CHANNEL:
            self.channel = Television.MIN_CHANNEL
        else:
            self.channel += 1

    def channel_down(self):
        self.channel: int

        if self.channel == Television.MIN_CHANNEL:
            self.channel = Television.MAX_CHANNEL
        else:
            self.channel -= 1

    def volume_up(self):
        self.volume: int

        if self.volume == Television.MAX_VOLUME:
            self.volume = Television.MAX_VOLUME
        else:
            self.volume += 1

    def volume_down(self):
        self.volume: int

        if self.volume == Television.MIN_VOLUME:
            self.volume = Television.MIN_VOLUME
        else:
            self.volume -= 1

    def __str__(self):
        return (f'Power = {self.status}\nChannel = {self.channel}\nVolume = {self.volume}\n')


