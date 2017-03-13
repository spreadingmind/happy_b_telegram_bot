# -*- coding: utf-8 -*-
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

congratulations_db = {
    'от Вали и Антона': 'videos/video_2017-03-12_14-42-50.mov',
    'от Лены': 'videos/Movie_on_3-12-17_at_1_51_PM.mov',
    'от Кирилла': 'videos/video_2017-03-12_15-46-23.mov',
    'от Паши': 'videos/video_2017-03-12_15-47-02.mov',
    'от Яна и Оксаны': 'videos/video_2017-03-12_15-44-53.mov',
    "Тёмыч:'от души'": 'videos/VID_20170312_153731.mp4',
    'от Виталика':'videos/video_2017-03-12_16-29-23.mov',
    'от Вадика': 'videos/video_2017-03-12_16-28-25.mov',
    'от Ульяны': 'videos/video_2017-03-12_17-01-31.mov',
    'от Лидии и Игоря, ч1':'videos/VID_20170312_172846.mp4',
    'от Лидии и Игоря, ч2':'videos/VID_20170312_173139.mp4',
    'от Саши':'videos/video_2017-03-12_17-46-17.mov',
    'от Даши ': 'videos/video_2017-03-12_18-31-05.mov',
    'от Алёны': 'videos/video.mp4',
    'краткие пожелания от Полины': 'videos/video_2017-03-12_18-46-17.mov',
    'with body and mind from CyberfunCommunity': 'videos/photo_2017-03-12_19-14-13.jpg'
}


keyboard = [[InlineKeyboardButton(i, callback_data='%s'%i)] for i in congratulations_db]

