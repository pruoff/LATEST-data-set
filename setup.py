"""This is the module used to set up shared global variables

This module provides and initializes global variables
"""

__all__ = []
__version__ = '0.1'
__author__ = 'Patrick Ruoff'

import pandas as pd

inputSeries = []
outputSeries = []
seriesEnvironment = []
seriesBiosignal = []
seriesVote = []
categoricalSeries = []
availableUsers = []

# Data Collection Phase
# startTime = pd.Timestamp('2019-11-13 00:00:00-05:00')
# endTime = pd.Timestamp('2020-02-08 00:00:00-05:00')

# Temperature Control Phase
startTime = pd.Timestamp('2020-02-18 17:00:00-05:00')
endTime = pd.Timestamp('2020-03-06 17:00:00-05:00')

userSeries = {}
occGaps = []
replaceIntervals = []


def init():
    """ Initialize globally shared variables for full project

    :return:
    """
    global inputSeries
    global outputSeries
    global seriesEnvironment
    global seriesVote
    global seriesBiosignal
    global categoricalSeries
    global availableUsers
    global startTime
    global endTime
    global PERIODS
    global userSeries
    global occGaps
    global replaceIntervals

    input_series_file = open('series/inputSeriesKeys.txt')
    output_series_file = open('series/outputSeriesKeys.txt')
    inputSeries = input_series_file.read().split('\n')
    outputSeries = output_series_file.read().split('\n')
    seriesEnvironment = outputSeries[:20]
    seriesBiosignal = outputSeries[20:29]
    seriesVote = outputSeries[29:]
    categoricalSeries = ['o_condition']
    availableUsers = ['U1', 'U2', 'U3']

    # hardcoded gaps in data for the thesis project, for decreasing unnecessary data size
    occGaps = [[pd.Timestamp('2019-12-20 00:00:00-05:00'),
                pd.Timestamp('2020-01-12 23:59:59-05:00')],
               [pd.Timestamp('2019-12-14 00:00:00-05:00'),
                pd.Timestamp('2019-12-15 23:59:59-05:00')],
               [pd.Timestamp('2019-12-07 00:00:00-05:00'),
                pd.Timestamp('2019-12-08 23:59:59-05:00')],
               [pd.Timestamp('2019-12-11 00:00:00-05:00'),
                pd.Timestamp('2019-12-11 23:59:59-05:00')],
               [pd.Timestamp('2019-11-27 00:00:00-05:00'),
                pd.Timestamp('2019-12-01 23:59:59-05:00')]]

    # certain values need to be manually filled due to conditions at data collection
    replaceIntervals = [[pd.Timestamp('2019-11-13 10:00:00+00:00'),
                         pd.Timestamp('2019-11-13 16:38:30+00:00'),
                       'U3_desk_temp', 'IW_general_temp', -1],
                        [pd.Timestamp('2019-11-13 10:00:00+00:00'),
                       pd.Timestamp('2019-11-13 16:38:30+00:00'),
                       'U2_desk_temp', 'IW_general_temp', 0.5],
                        [pd.Timestamp('2019-11-13 10:00:00+00:00'),
                       pd.Timestamp('2019-11-13 16:38:30+00:00'),
                       'U1_desk_temp', 'IW_general_temp', 0.75],
                        [pd.Timestamp('2019-11-13 10:00:00+00:00'),
                        pd.Timestamp('2019-11-13 16:38:30+00:00'),
                        'U3_desk_hum', 'IW_general_hum', 5],
                        [pd.Timestamp('2019-11-13 10:00:00+00:00'),
                        pd.Timestamp('2019-11-13 16:38:30+00:00'),
                        'U2_desk_hum', 'IW_general_hum', 6],
                        [pd.Timestamp('2019-11-13 10:00:00+00:00'),
                        pd.Timestamp('2019-11-13 16:38:30+00:00'),
                        'U1_desk_hum', 'IW_general_hum', 4],
                        [pd.Timestamp('2019-11-13 10:00:00+00:00'),
                       pd.Timestamp('2019-11-13 16:38:30+00:00'),
                       'corridor_temp', 'IW_general_temp', -1],
                        [pd.Timestamp('2019-11-13 10:00:00+00:00'),
                        pd.Timestamp('2019-11-13 16:38:30+00:00'),
                        'corridor_hum', 'IW_general_hum', 7],
                        [pd.Timestamp('2020-01-15 00:00:00+00:00'),
                       pd.Timestamp('2020-01-22 15:39:30+00:00'),
                       'corridor_temp', 'U3_desk_temp', -1],
                        [pd.Timestamp('2020-01-15 00:00:00+00:00'),
                        pd.Timestamp('2020-01-22 15:39:30+00:00'),
                        'corridor_hum', 'U2_desk_hum', 1],
                        # delete these points for they were tests
                        [pd.Timestamp('2020-03-04 18:00:00+00:00'),
                         pd.Timestamp('2020-03-04 19:00:00+00:00'),
                         'U2_last_command_enc', 'U1_last_command_enc', 0],
                        [pd.Timestamp('2020-03-04 18:00:00+00:00'),
                         pd.Timestamp('2020-03-04 19:00:00+00:00'),
                         'U2_last_command', 'U1_last_command', 0]
                        ]
    return
