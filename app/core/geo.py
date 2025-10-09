from __future__ import annotations

from haversine import haversine, Unit


def compute_distance_km(lat1: float, lng1: float, lat2: float, lng2: float) -> float:
    return haversine((lat1, lng1), (lat2, lng2), unit=Unit.KILOMETERS)
