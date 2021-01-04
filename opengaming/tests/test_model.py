from ..location import Location
from ..model import add_location, clear_locations, get_all, get_by_id, get_available_locations, reserve_location, update


def setup_function():
    clear_locations()


def test_add_location():
    location = Location('Table 1')
    add_location(location)
    assert [location] == get_all()


def test_get_location():
    location1 = Location('Table 1', 'XXX')
    location2 = Location('Table 2', 'YYY')
    add_location(location1)
    add_location(location2)
    assert location1 == get_by_id('XXX')
    assert location2 == get_by_id('YYY')


def test_update_location():
    location_start = Location('Table 1', 'XXX')
    add_location(location_start)
    location_edit = get_by_id('XXX')
    location_edit.name = 'Table 1 edited'
    update(location_edit)
    assert 'Table 1 edited' == get_by_id('XXX').name


def test_reserve_location():
    add_location(Location('Table 1', 'XXX'))
    location = get_by_id('XXX')
    reserve_location(location)
    assert False == get_by_id('XXX').available


def test_locations_id():
    location1 = Location('Table 1')
    location2 = Location('Table 2')
    location3 = Location('Table 3')
    assert location1 != location2 and location2 != location3


def test_get_available_locations():
    location1 = Location('Table 1')
    location2 = Location('Table 2')
    add_location(location1)
    add_location(location2)
    assert [location1, location2] == get_available_locations()
    reserve_location(location1)
    assert [location2] == get_available_locations()
