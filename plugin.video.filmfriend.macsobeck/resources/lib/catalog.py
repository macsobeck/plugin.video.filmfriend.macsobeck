# SPDX-License-Identifier: GPL-2.0-only

"""Pure helpers for translating Filmfriend catalogue metadata."""


def genre_records(container):
	"""Return valid genre dictionaries from optional API metadata."""
	if not isinstance(container, dict):
		return ()

	genres = container.get('genres')
	if not isinstance(genres, (list, tuple)):
		return ()
	return tuple(genre for genre in genres if isinstance(genre, dict))


def nested_season_number(season):
	"""Return a nested season number without assuming season is a mapping."""
	if not isinstance(season, dict):
		return None
	return season.get('seasonNumber')


def release_date_metadata(value):
	"""Return Kodi date metadata for a Filmfriend ISO date, if usable.

	Filmfriend catalogue records may explicitly contain ``releaseDate: null``.
	Keeping this helper independent of Kodi makes that API edge case directly
	testable without importing any Kodi modules.
	"""
	if not isinstance(value, str):
		return {}

	value = value.strip()
	if len(value) < 4 or not value[:4].isdigit():
		return {}

	metadata = {'year': value[:4]}
	if len(value) >= 10:
		metadata['premiered'] = value[:10]
		metadata['aired'] = value[:10]
	return metadata
