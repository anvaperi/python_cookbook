from dataclasses import dataclass, make_dataclass, field, fields
from math import asin, cos, radians, sin, sqrt
from typing import Any


@dataclass
class InventoryItem:
	"""Class for keeping track of an item in inventory."""
	name: str
	unit_price: float
	quantity_on_hand: int = 0

	def total_cost(self) -> float:
		return self.unit_price * self.quantity_on_hand

#=========================================================================================================

# latitude +-90N/S, Longitude +-180EW

Coordinate = make_dataclass('Coordinate', ['name', 'latitude_sn_deg', 'longitude_we_deg']) # eq to following

@dataclass
class Coordinate:
	name: str
	latitude_sn_deg: float = .0
	longitude_we_deg: float = .0


	def distance_to(self, other):
		earth_radius_km = 6371
		sinsq = lambda z: (sin(radians(z))) ** 2
		cos_deg = lambda z: cos(radians(z))

		radicand = sinsq((other.latitude_sn_deg  - self.latitude_sn_deg)  / 2) + \
							 sinsq((other.longitude_we_deg - self.longitude_we_deg) / 2) * \
				       cos_deg(other.latitude_sn_deg) * cos_deg(self.latitude_sn_deg)

		return 2 * earth_radius_km * asin(sqrt(radicand))

# oslo = Coordinate('Oslo', 59.9, 10.8)
# vancouver = Coordinate('Vancouver', 49.3, -123.1)
# print(f'{oslo.name} is at {oslo.latitude_sn_deg}°N, {oslo.longitude_we_deg}°E')
# print(f'{oslo.distance_to(vancouver)=}')

# The field() specifier is used to customize each field of a data class individually.
# For reference, these are the parameters field() supports:
# -	default: Default value of the field
# -	default_factory: Function that returns the initial value of the field
# -	init: Use field in .__init__() method? (Default is True.)
# -	repr: Use field in repr of the object? (Default is True.)
# -	compare: Include the field in comparisons? (Default is True.)
# -	hash: Include the field when calculating hash()? (Default is to use the same as for compare.)
# -	metadata: A mapping with information about the field

@dataclass
class Position:
	name: str
	lat: float = field(default=0.0, metadata={'unit': 'degrees', 'term': 'latitude'})
	lon: float = field(default=0.0, metadata={'unit': 'degrees', 'term': 'longitude'})


# lat_unit = fields(Position)[2].metadata['unit']
# for each_field in fields(Position):
# 	print()
# 	for each_subfield in ((str(each_field))[6:-1]).replace('=', ':\t').split(','):
# 		print(each_subfield)

#========================================================================================================

@dataclass
class WithoutExplicitTypes:
	name: Any
	value: Any = 42

#========================================================================================================
from dataclasses import dataclass

@dataclass(frozen=True)
class Position:
	name: str
	lon: float = 0.0
	lat: float = 0.0

