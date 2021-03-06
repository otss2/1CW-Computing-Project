# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""Unit test for the station module"""

from floodsystem.station import MonitoringStation, inconsistent_typical_range_stations
from test_geo import get_test_stations
from floodsystem.flood import stations_level_over_threshold
from floodsystem.stationdata import *

def test_create_monitoring_station():

    # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    assert s.station_id == s_id
    assert s.measure_id == m_id
    assert s.name == label
    assert s.coord == coord
    assert s.typical_range == trange
    assert s.river == river
    assert s.town == town

def test_inconsistent_typical_range_stations():
    test_stats = get_test_stations()
    out = inconsistent_typical_range_stations(test_stats)
    assert out == [test_stats[0], test_stats[2], test_stats[3], test_stats[4]]

def test_stations_level_over_threshold():
    test_stats = build_station_list()
    update_water_levels(test_stats)
    out = stations_level_over_threshold(test_stats, 2)
    for i, item in enumerate(out):
        assert type(item[0]) == type(test_stats[0])
        assert type(item[1]) == type(1) or type(item[1]) == type(1.2)
        if i >= 1:
            assert item[1] < out[i - 1][1]