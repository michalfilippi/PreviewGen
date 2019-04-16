import logging
from typing import Tuple, List, Iterable
from pathlib import Path

from schema import Optional

logger = logging.getLogger(__name__)

scanner_config_schema = {
    'source_dir': str,
    'destination_dir': str,
    Optional('ignore_hidden'): bool,
}


class Scanner:
    def __init__(self, source_dir: str, destination_dir: str, ignore_hidden: bool = True):
        self.source_dir = Path(source_dir)
        self.destination_dir = Path(destination_dir)
        self.ignore_hidden = ignore_hidden

    def run(self) -> List[Tuple[Path, Path]]:
        paths = self._scan_source()
        paths = self._relative_paths(paths)
        if self.ignore_hidden:
            paths = self._ignore_hidden(paths)
        logger.debug(f"Found {len(paths)} relevant images.")

        return self._filter_existing(self._pair_files(paths))

    def _scan_source(self) -> List[Path]:
        logger.debug(f"Scanning \"{self.source_dir}\" for photos.")

        if not self.source_dir.exists():
            raise FileNotFoundError(f"Directory \"{self.source_dir}\" does not exist.")
        if not self.source_dir.is_dir():
            raise FileNotFoundError(f"File \"{self.source_dir}\" is not a directory.")

        result = list(Path(self.source_dir).rglob("*.[jJ][pP][gG]"))
        logger.info(f"Found {len(result)} photos in \"{self.source_dir}\".")

        return result

    def _relative_paths(self, paths: Iterable[Path]) -> List[Path]:
        return [p.relative_to(self.source_dir) for p in paths]

    def _pair_files(self, paths: List[Path]) -> List[Tuple[Path, Path]]:
        return [(self.source_dir.joinpath(path), self.destination_dir.joinpath(path)) for path in paths]

    @staticmethod
    def _ignore_hidden(paths: List[Path]):
        hidden = {p for p in paths if any(map(lambda s: s.startswith('.'), p.parts))}
        logging.info(f"Ignoring {len(hidden)} hidden photos or photos under hidden subtree.")

        return list(set(paths).difference(hidden))

    @staticmethod
    def _filter_existing(path_pairs: List[Tuple[Path, Path]]) -> List[Tuple[Path, Path]]:
        filtered_path_pairs = list(filter(lambda p: not p[1].exists(), path_pairs))
        logger.debug(f"Skipping {len(path_pairs) - len(filtered_path_pairs)} already processed photos.")

        return filtered_path_pairs
