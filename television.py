class Television:

    MIN_VOLUME: int = 0
    MAX_VOLUME: int = 2
    MIN_CHANNEL: int = 0
    MAX_CHANNEL: int = 3

    def __init__(self) -> None:
        """
        Used to set the default instance variables
        :return: None
        """

        self.__status: bool = False
        self.__muted: bool = False
        self.__volume: int = Television.MIN_VOLUME
        self.__channel: int = Television.MIN_CHANNEL

    def power(self) -> None:
        """
        Used to determine the current status of the television
        :return: None
        """

        if self.__status:
            self.__status = False
            self.__muted = True
            self.__channel = Television.MIN_CHANNEL
        elif not self.__status:
            self.__status = True
            self.__muted = False
            self.__volume = Television.MIN_VOLUME + 1
            self.__channel = Television.MIN_CHANNEL + 1

    def mute(self) -> None:
        """
        Used to make the television muted
        :return: None
        """

        if self.__status:
            if self.__muted:
                self.__muted = False
                self.__volume = Television.MIN_VOLUME + 1
            elif not self.__muted:
                self.__muted = True
                self.__volume = Television.MIN_VOLUME

    def channel_up(self) -> None:
        """
        Used to raise the channel
        :return: None
        """

        if not self.__status:
            self.__channel = Television.MIN_CHANNEL

        elif self.__status:
            if self.__channel == Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL
            else:
                self.__channel += 1

    def channel_down(self) -> None:
        """
        Used to lower the channel
        :return: None
        """

        if not self.__status:
            self.__channel = Television.MIN_CHANNEL

        elif self.__status
            if self.__channel == Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL
            else:
                self.__channel -= 1

    def volume_up(self) -> None:
        """
        Used to raise the volume
        :return: None
        """

        if not self.__status or self.__muted:
            self.__volume = self.MIN_VOLUME
        elif self.__volume == Television.MAX_VOLUME:
            self.__volume = Television.MIN_VOLUME
        else:
            self.__volume += 1

    def volume_down(self) -> None:
        """
        Used to lower the volume
        :return: None
        """

        if not self.__status or self.__muted:
            self.__volume = self.MIN_VOLUME
        elif self.__volume == Television.MIN_VOLUME:
            self.__volume = Television.MAX_VOLUME
        else:
            self.__volume -= 1

    def __str__(self) -> str:
        """
        Used to format the values of the television object
        :return: Three f strings, values of status, channel, and volume
        """
        return f'Power = {self.__status}\nChannel = {self.__channel}\nVolume = {self.__volume}\n'


