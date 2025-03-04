from abc import ABC
from dataclasses import asdict, fields


class BaseEntity(ABC):
	@property
	def to_dict(self):
		return asdict(self)

	@classmethod
	def from_dict(cls, d):
		data = cls.clean_data(d)
		cls.validate(data)
		return cls(**data)

	@classmethod
	def validate(cls, d):
		raise NotImplementedError

	@classmethod
	def clean_data(cls, d) -> dict:
		clean = {}
		for field in fields(cls):
			clean[field.name] = d.get(field.name)
		return clean