class Television:

    MIN_VOLUME: int = 0
    MAX_VOLUME: int = 2
    MIN_CHANNEL: int = 0
    MAX_CHANNEL: int = 3

    def __init__(self):
        '''
        Used to set the default instance variables
        :return: None
        '''

        self.status: bool = False
        self.muted: bool = False
        self.volume: int = Television.MIN_VOLUME
        self.channel: int = Television.MIN_CHANNEL

    def power(self):
        '''
        Used to determine the current status of the television
        :return: None
        '''

        self.status: bool
        if self.status:
            self.status = False
            self.muted = True
            self.channel = 1
        elif not self.status:
            self.status = True
            self.muted = False
            self.volume = Television.MIN_VOLUME
            self.channel = Television.MIN_CHANNEL

    def mute(self):
        '''
        Used to make the television muted
        :return: None
        '''

        self.muted: bool
        if self.status:
            if self.muted:
                self.muted = False
                self.volume = Television.MIN_VOLUME + 1
            elif not self.muted:
                self.muted = True
                self.volume = Television.MIN_VOLUME

    def channel_up(self):
        '''
        Used to raise the channel
        :return: None
        '''

        self.channel: int

        if not self.status:
            self.channel = 0
        elif self.channel == Television.MAX_CHANNEL and self.status:
            self.channel = Television.MIN_CHANNEL
        else:
            self.channel += 1

    def channel_down(self):
        '''
        Used to lower the channel
        :return: None
        '''

        self.channel: int

        if not self.status:
            self.channel = 0
        elif self.channel == Television.MIN_CHANNEL and self.status:
            self.channel = Television.MAX_CHANNEL
        else:
            self.channel -= 1

    def volume_up(self):
        '''
        Used to raise the volume
        :return: None
        '''

        self.volume: int

        if not self.status or self.muted:
            self.volume = self.MIN_VOLUME
        elif self.volume == Television.MAX_VOLUME:
            self.volume = Television.MIN_VOLUME
        else:
            self.volume += 1

    def volume_down(self):
        '''
        Used to lower the volume
        :return: None
        '''

        self.volume: int

        if not self.status or self.muted:
            self.volume = self.MIN_VOLUME
        elif self.volume == Television.MIN_VOLUME and self.status:
            self.volume = Television.MAX_VOLUME
        else:
            self.volume -= 1

    def __str__(self):
        '''
        Used to format the values of the television object
        :return: Three f strings, values of status, channel, and volume
        '''
        return (f'Power = {self.status}\nChannel = {self.channel}\nVolume = {self.volume}\n')


