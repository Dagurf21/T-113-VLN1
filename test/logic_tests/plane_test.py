import unittest
from logic.plane_logic import *
from .mock_data_wrapper import MockDataWrapper
from model import *
from copy import deepcopy

class TestPlane(unittest.TestCase):
    MOCK_PLANES = [
        Plane(
            name="Terminator",
            ty="737",
            manufacturer="Boeing",
            capacity=300,
        ),
        Plane(
            name="Terminator 2",
            ty="A320",
            manufacturer="Airbus",
            capacity=350,
        ),
        Plane(
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

        plane = data.get_first_plane()
        self.assertIsNotNone(plane.id)
        plane.id = None
        self.assertEqual(plane, self.MOCK_PLANES[0])

    def test_create_plane_invalid_capacity(self):
        data = MockDataWrapper()
        plane_logic = PlaneLogic(data)

        plane = deepcopy(self.MOCK_PLANES[0])
        plane.capacity = -1

        plane_logic.create_plane(plane)

        self.assertIsNone(data.get_first_plane())

    def test_create_plane_invalid_voyages(self):
        data = MockDataWrapper()
        plane_logic = PlaneLogic(data)

        plane = deepcopy(self.MOCK_PLANES[0])
        plane.voyages = [5]

        plane_logic.create_plane(plane)

        self.assertIsNone(data.get_first_plane())
    
    def test_get_all_planes(self):
        data = MockDataWrapper()
        plane_logic = PlaneLogic(data)

        for plane in self.MOCK_PLANES:
            data.create_plane(plane)
        
        planes = []
        for plane in data.get_all_planes():
            self.assertIsNotNone(plane.id)
            plane.id = None
            planes.append(plane)

        self.assertEqual(self.MOCK_PLANES, planes)
    
    def test_get_plane(self):
        data = MockDataWrapper()
        plane_logic = PlaneLogic(data)

        for plane in self.MOCK_PLANES:
            data.create_plane(plane)
        
        plane = plane_logic.get_plane(1)
        self.assertIsNotNone(plane.id)
        plane.id = None
        self.assertEqual(self.MOCK_PLANES[1], plane)
    
    def test_update_plane(self):
        data = MockDataWrapper()
        plane_logic = PlaneLogic(data)

        for plane in self.MOCK_PLANES:
            data.create_plane(plane)
        
        for plane in data.get_all_planes():
            plane = deepcopy(plane)
            plane.capacity = 5
            plane.voyages = [0]
            plane_logic.update_plane(plane)

        for (plane, original) in zip(data.get_all_planes(), self.MOCK_PLANES):
            self.assertEqual(plane.capacity, 5)
            self.assertListEqual(plane.voyages, original.voyages)
        

    def test_delete_plane(self):
        data = MockDataWrapper()
        plane_logic = PlaneLogic(data)

        for plane in self.MOCK_PLANES:
            data.create_plane(plane)
        
        id_to_remove = 0
        plane_logic.delete_plane(id_to_remove)

        planes = data.get_all_planes()
        for plane in planes:
            self.assertIsNotNone(plane.id)
            plane.id = None

        expect = [plane for plane in planes if plane.id != id_to_remove]

        self.assertListEqual(expect, planes)
