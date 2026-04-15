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
        elif not self.status:
            self.status = True

    def mute(self):
        '''
        Used to make the television muted
        :return: None
        '''

        self.muted: bool
        if self.muted:
            self.muted = False
        elif not self.muted:
            self.muted = True

    def channel_up(self):
        '''
        Used to raise the channel
        :return: None
        '''

        self.channel: int

        if self.channel == Television.MAX_VOLUME:
            self.channel = Television.MIN_CHANNEL
        else:
            self.channel += 1

    def channel_down(self):
        '''
        Used to lower the channel
        :return: None
        '''

        self.channel: int

        if self.channel == Television.MIN_VOLUME:
            self.channel = Television.MAX_CHANNEL
        else:
            self.channel -= 1

    def volume_up(self):
        '''
        Used to raise the volume
        :return: None
        '''

        self.volume: int

        if self.volume == Television.MAX_VOLUME:
            self.volume = Television.MAX_VOLUME
        else:
            self.volume += 1

    def volume_down(self):
        '''
        Used to lower the volume
        :return: None
        '''

        self.volume: int

        if self.volume == Television.MIN_VOLUME:
            self.volume = Television.MIN_VOLUME
        else:
            self.volume -= 1

    def __str__(self):
        '''
        Used to format the values of the television object
        :return: Three f strings, values of status, channel, and volume
        '''
        status = str(self.status)
        channel = str(self.channel)
        volume = str(self.volume)

        print(f'Power = {status}')
        print(f'Channel = {channel}')
        print(f'Volume = {volume}')


