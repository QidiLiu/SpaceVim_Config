#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"Hit a keyboard combo automatically"

__author__ = "QidiLiu"

from pynput.keyboard import Controller, Key

keyboard_controller = Controller()
exception = {'alt' : Key.alt, 
             'backspace' : Key.backspace, 
             'caps_lock' : Key.caps_lock,
             'cmd' : Key.cmd,
             'ctrl' : Key.ctrl,
             'delete' : Key.delete,
             'up' : Key.up,
             'down' : Key.down,
             'left' : Key.left,
             'right' : Key.right,
             'end' : Key.end,
             'enter' : Key.enter,
             'esc' : Key.esc,
             'f1' : Key.f1,
             'f2' : Key.f2,
             'f3' : Key.f3,
             'f4' : Key.f4,
             'f5' : Key.f5,
             'f6' : Key.f6,
             'f7' : Key.f7,
             'f8' : Key.f8,
             'f9' : Key.f9,
             'f10' : Key.f10,
             'f11' : Key.f11,
             'f12' : Key.f12,
             'f13' : Key.f13,
             'f14' : Key.f14,
             'f15' : Key.f15,
             'f16' : Key.f16,
             'f17' : Key.f17,
             'f18' : Key.f18,
             'f19' : Key.f19,
             'f20' : Key.f20,
             'home' : Key.home,
             'insert' : Key.insert,
             'media_next' : Key.media_next,
             'media_play_pause' : Key.media_play_pause,
             'media_previous' : Key.media_previous,
             'media_volume_down' : Key.media_volume_down,
             'media_volume_up' : Key.media_volume_up,
             'media_volume_mute' : Key.media_volume_mute,
             'menu' : Key.menu,
             'num_lock' : Key.num_lock,
             'page_down' : Key.page_down,
             'page_up' : Key.page_up,
             'pause' : Key.pause,
             'print_screen' : Key.print_screen,
             'shift' : Key.shift,
             'space' : Key.space,
             'tab' : Key.tab,}

def coding_helper(combo):
    for k in combo:
        if k not in exception:
            keyboard_controller.press(k)
            keyboard_controller.release(k)
        else:
            keyboard_controller.press(exception[k])
            keyboard_controller.release(exception[k])

if __name__ == '__main__':
    coding_helper(['esc', 'i', 'end', ';', 'enter'])
