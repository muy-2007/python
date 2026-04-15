class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self):
        self.status = False
        self.muted = False
        self.volume = Television.MIN_VOLUME
        self.channel = Television.MIN_CHANNEL

    def power(self):
        if self.status:
            self.status = False
        elif not self.status:
            self.status = True

    def mute(self):
        if self.muted:
            self.muted = False
        elif not self.muted:
            self.muted = True

    def channel_up(self):
        if self.channel == Television.MAX_VOLUME:
            self.channel = Television.MIN_CHANNEL
        else:
            self.channel += 1

    def channel_down(self):
        if self.channel == Television.MIN_VOLUME:
            self.channel = Television.MAX_CHANNEL
        else:
            self.channel -= 1

    def volume_up(self):
        if self.volume == Television.MAX_VOLUME:
            self.volume = Television.MAX_VOLUME
        else:
            self.volume += 1

    def volume_down(self):
        if self.volume == Television.MIN_VOLUME:
            self.volume = Television.MIN_VOLUME
        else:
            self.volume -= 1

    def __str__(self):
        print(f'Power = {self.status}')
        print(f'Channel = {self.channel}')
        print(f'Volume = {self.volume}')


