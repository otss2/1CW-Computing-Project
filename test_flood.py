from floodsystem.station import MonitoringStation, inconsistent_typical_range_stations
from test_geo import get_test_stations
from floodsystem.flood import stations_highest_rel_level, stations_level_over_threshold
from floodsystem.stationdata import *

def test_stations_highest_rel_level():
    test_stats = build_station_list()
    update_water_levels(test_stats)
    out = stations_highest_rel_level(test_stats, 10)
    for i, item in enumerate(out):
        assert type(item) == type(test_stats[0])
        if i >= 1:
            assert item.relative_water_level() < out[i - 1].relative_water_level()