from pytest import *
from television import *

tv = Television()

def test_init():
    assert tv.status == False
    assert tv.channel == 0
    assert tv.volume == 0

def test_power():
    tv.power()
    assert tv.status == True
    tv.power()
    assert tv.status == False
    assert tv.channel == 0
    assert tv.volume == 0

def test_mute():
    tv.status = True
    tv.volume_up()
    tv.mute()
    assert tv.muted == True
    assert tv.volume == 0

    tv.mute()
    assert tv.muted == False
    assert tv.volume > 0

    tv.status = False
    tv.mute()
    assert tv.muted == True

    tv.mute()
    assert tv.muted == True

def test_channel_up():
    tv.status = False
    tv.channel_up()
    assert tv.channel == 0

    tv.status = True
    tv.channel_up()
    assert tv.channel > 0

    tv.channel = tv.MAX_CHANNEL
    tv.channel_up()
    assert tv.channel == tv.MIN_CHANNEL

def test_channel_down():
    tv.status = False
    tv.channel_down()
    assert tv.channel == 0

    tv.status = True
    tv.channel = tv.MIN_CHANNEL
    tv.channel_down()
    assert tv.channel == tv.MAX_CHANNEL

def test_volume_up():
    tv.status = False
    tv.volume_up()
    assert tv.volume == 0

    tv.status = True
    tv.volume_up()
    assert tv.volume > 0

    tv.muted = True
    tv.volume_up()
    assert tv.volume == tv.MIN_VOLUME

    tv.volume = tv.MAX_VOLUME
    tv.volume_up()
    assert tv.volume == tv.MIN_VOLUME

def test_volume_down():
    tv.status = False
    tv.volume_down()
    assert tv.volume == 0

    tv.status = True
    tv.volume = tv.MAX_VOLUME
    tv.volume_down()
    assert tv.volume < tv.MAX_VOLUME

    tv.muted = True
    tv.volume_down()
    assert tv.volume == tv.MIN_VOLUME

    tv.muted = False
    tv.volume = tv.MIN_VOLUME
    tv.volume_down()
    assert tv.volume == tv.MAX_VOLUME

