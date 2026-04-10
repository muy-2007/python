class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MAX_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self):
        status = False
        muted = False
        volume = Television.MIN_VOLUME
        channel = Television.MIN_CHANNEL

    def power(self):
        if self.status == True:
            self.status = False
        elif self.status == False:
            self.status = True

    def mute(self):
        if self.muted == True:
            self.muted = False
        elif self.muted == False:
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
        pass

    def volume_down(self):
        pass

    def __str__(self):
        pass


