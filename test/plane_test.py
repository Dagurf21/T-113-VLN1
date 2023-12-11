import unittest
from logic.plane_logic import *
from test.mock_data_wrapper import MockDataWrapper
from model import *
from copy import copy

class TestPlane(unittest.TestCase):
    MOCK_PLANES = [
        Plane(
            id=0,
            name="Terminator",
            ty="737",
            manufacturer="Boeing",
            capacity=300,
        ),
        Plane(
            id=1,
            name="Terminator 2",
            ty="A320",
            manufacturer="Airbus",
            capacity=350,
        ),
        Plane(
            id=2,
            name="Terminator",
            ty="777",
            manufacturer="Boeing",
            capacity=250,
        ),
    ]

    def test_create_plane_valid(self):
        data = MockDataWrapper()
        plane_logic = PlaneLogic(data)

        plane_logic.create_plane(self.MOCK_PLANES[0])

        self.assertEqual(data.get_first_plane(), self.MOCK_PLANES[0])

    def test_create_plane_invalid_capacity(self):
        data = MockDataWrapper()
        plane_logic = PlaneLogic(data)

        plane = copy(self.MOCK_PLANES[0])
        plane.capacity = -1

        plane_logic.create_plane(plane)

        self.assertIsNone(data.get_first_plane())
    
    def test_get_all_planes(self):
        data = MockDataWrapper()
        plane_logic = PlaneLogic(data)

        for plane in self.MOCK_PLANES:
            data.create_plane(plane)
        
        self.assertEqual(self.MOCK_PLANES, plane_logic.get_all_planes())
    
    def test_get_all_planes(self):
        data = MockDataWrapper()
        plane_logic = PlaneLogic(data)

        for plane in self.MOCK_PLANES:
            data.create_plane(plane)
        
        self.assertEqual(self.MOCK_PLANES[1], plane_logic.get_plane(1))
    
    def test_update_plane(self):
        data = MockDataWrapper()
        plane_logic = PlaneLogic(data)

        for plane in self.MOCK_PLANES:
            data.create_plane(plane)
        
        for plane in self.MOCK_PLANES:
            plane = copy(plane)
            plane.capacity = 5
            plane.flights = [5, 2]
            #plane.

            # Needs flights to be fixed
            raise NotImplementedError

    def test_delete_plane(self):
        data = MockDataWrapper()
        plane_logic = PlaneLogic(data)

        for plane in self.MOCK_PLANES:
            data.create_plane(plane)
        
        id_to_remove = 0
        plane_logic.delete_plane(id_to_remove)
        expect = [plane for plane in self.MOCK_PLANES if plane.id != id_to_remove]
        self.assertListEqual(expect, data.get_all_planes())
