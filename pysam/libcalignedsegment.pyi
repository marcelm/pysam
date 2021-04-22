import enum
import re
from array import array
from typing import Any, List, Optional, Dict, Tuple, Union, Literal, overload
from pysam import AlignmentHeader

CMATCH: int
CINS: int
CDEL: int
CREF_SKIP: int
CSOFT_CLIP: int
CHARD_CLIP: int
CPAD: int
CEQUAL: int
CDIFF: int
CBACK: int

FPAIRED: int
FPROPER_PAIR: int
FUNMAP: int
FMUNMAP: int
FREVERSE: int
FMREVERSE: int
FREAD1: int
FREAD2: int
FSECONDARY: int
FQCFAIL: int
FDUP: int
FSUPPLEMENTARY: int

CIGAR2CODE: Dict[int, str]
CIGAR_REGEX: re.Pattern
DATATYPE2FORMAT: Dict[int, Tuple[str, int]]
KEY_NAMES: List[str]

TagValue = Union[str, int, float, array]


class CIGAR_OPS(enum.IntEnum):
    CBACK: int
    CDEL: int
    CDIFF: int
    CEQUAL: int
    CHARD_CLIP: int
    CINS: int
    CMATCH: int
    CPAD: int
    CREF_SKIP: int
    CSOFT_CLIP: int

class SAM_FLAGS(enum.IntEnum):
    FDUP: int
    FMREVERSE: int
    FMUNMAP: int
    FPAIRED: int
    FPROPER_PAIR: int
    FQCFAIL: int
    FREAD1: int
    FREAD2: int
    FREVERSE: int
    FSECONDARY: int
    FSUPPLEMENTARY: int
    FUNMAP: int

class AlignedSegment:
    header: AlignmentHeader
    query_name: Optional[str]
    flag: int
    reference_name: Optional[str]
    reference_id: int
    reference_start: int
    mapping_quality: int
    cigarstring: str
    next_reference_id: int
    next_reference_name: Optional[str]
    next_reference_start: int
    query_length: int
    template_length: int
    query_sequence: Optional[str]
    query_qualities: Optional[array]
    bin: int
    is_paired: bool
    is_proper_pair: bool
    is_unmapped: bool
    mate_is_unmapped: bool
    is_reverse: bool
    mate_is_reverse: bool
    is_read1: bool
    is_read2: bool
    is_secondary: bool
    is_qcfail: bool
    is_duplicate: bool
    is_supplementary: bool
    reference_end: Optional[int]
    reference_length: Optional[int]
    query_alignment_sequence: Optional[str]
    query_alignment_qualities: Optional[array]
    query_alignment_start: int
    query_alignment_end: int
    query_alignment_length: int
    cigartuples: Optional[List[Tuple[int, int]]]

    def __init__(self, header: Optional[AlignmentHeader] = ...) -> None: ...
    def compare(self, other: AlignedSegment) -> int: ...
    def to_string(self) -> str: ...
    @classmethod
    def fromstring(cls, sam: str, header: AlignmentHeader) -> AlignedSegment: ...
    def to_dict(self) -> Any: ...
    @classmethod
    def from_dict(cls, sam_dict: Dict[str, Any], header: AlignmentHeader) -> Any: ...
    def get_reference_positions(self, full_length: bool = ...) -> List[int]: ...
    def infer_query_length(self) -> Optional[int]: ...
    def infer_read_length(self) -> Optional[int]: ...
    def get_reference_sequence(self) -> str: ...
    def get_forward_sequence(self) -> Optional[str]: ...
    def get_forward_qualities(self) -> Optional[array]: ...
    def get_aligned_pairs(self, matches_only: bool = ..., with_seq: bool = ...) -> List[Tuple[int, int]]: ...
    def get_blocks(self) -> List[Tuple[int, int]]: ...
    def get_overlap(self, start: int, end: int) -> Optional[int]: ...
    def get_cigar_stats(self) -> Tuple[array, array]: ...
    def set_tag(self,
        tag: str,
        value: Union[int, float, str, bytes, array, List, Tuple, None],
        value_type: Optional[Literal["A", "i", "f", "Z", "H", "B", "c", "C", "s", "S", "I"]] = ...,
        replace: bool = ...,
    ) -> None: ...
    def has_tag(self, tag: str) -> bool: ...
    @overload
    def get_tag(self, tag: str, with_value_type: Literal[False]) -> TagValue: ...
    @overload
    def get_tag(self, tag, with_value_type: Literal[True]) -> Tuple[TagValue, str]: ...
    @overload
    def get_tag(self, tag, with_value_type: bool = ...) -> Union[TagValue, Tuple[TagValue, str]]: ...
    @overload
    def get_tags(self, with_value_type: Literal[False]) -> List[Tuple[str, TagValue]]: ...
    @overload
    def get_tags(self, with_value_type: Literal[True]) -> List[Tuple[str, TagValue, str]]: ...
    @overload
    def get_tags(self, tag, with_value_type: bool = ...) -> Union[List[Tuple[str, TagValue, str]], List[Tuple[str, TagValue]]]: ...
    def set_tags(self, tags: Any) -> None: ...
    def __eq__(self, other): ...
    def __ge__(self, other): ...
    def __gt__(self, other): ...
    def __le__(self, other): ...
    def __lt__(self, other): ...
    def __ne__(self, other): ...
    # def __hash__(self) -> Any: ...
    # def __copy__(self) -> Any: ...
    # def __deepcopy__(self, memo) -> Any: ...
    # def __reduce__(self) -> Any: ...
    # def __setstate__(self, state) -> Any: ...


class PileupRead:
    alignment: Any = ...
    indel: Any = ...
    is_del: Any = ...
    is_head: Any = ...
    is_refskip: Any = ...
    is_tail: Any = ...
    level: Any = ...
    query_position: Any = ...
    query_position_or_next: Any = ...


class PileupColumn:
    reference_id: int
    reference_name: Optional[str]
    nsegments: int
    reference_pos: int
    pileups: List[PileupRead]

    def set_min_base_quality(self, min_base_quality: int) -> None: ...
    def __len__(self) -> int: ...
    def get_num_aligned(self) -> int: ...
    def get_query_sequences(self,
        mark_matches: bool = ...,
        mark_ends: bool = ...,
        add_indels: bool = ...,
    ) -> List[str]: ...
    def get_query_qualities(self) -> List[int]: ...
    def get_mapping_qualities(self) -> List[int]: ...
    def get_query_positions(self) -> List[int]: ...
    def get_query_names(self) -> List[str]: ...
