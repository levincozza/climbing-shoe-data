from dataclasses import dataclass, field
from enum import Enum

class Gender(Enum):
    MEN = "Men"
    WOMEN = "Women"
    KID = "Kid"

class Volume(Enum):
    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"

class FootWidth(Enum):
    WIDE = "Wide"                         # Men's Wide
    MEDIUM = "Medium"                     # Men's Medium or Women's Wide
    NARROW = "Narrow"                     # Men's Narrow or Women's Medium
    EXTRA_NARROW = "Extra Narrow"         # Women's Narrow
    KIDS = "Kids"

class ToeShape(Enum):
    CLASSIC = "Classic"                   # Middle toe is not the longest toe, or barely the longest toe
    MORTONS = "Morton's Toe"              # Middle toe is obviously the longest toe

class HeelWidth(Enum):
    NARROW = "Narrow"
    MEDIUM = "Medium"
    KIDS = "Kids (Adjustable)"

class Downturn(Enum):
    FLAT = "Flat"
    MEDIUM = "Medium"
    AGGRESSIVE = "Aggressive"

class Stiffness(Enum):
    EXTRA_SOFT = "Extra Soft"
    SOFT = "Soft"
    MEDIUM = "Medium"
    STIFF = "Stiff"

class AsymCurve(Enum):
    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"

class ClimbingStyle(Enum):
    GENERAL = "General"
    BOULDERING = "Bouldering"
    SINGLE_PITCH = "Single Pitch"
    MULTI_PITCH = "Multiple Pitch"
    BIG_WALL = "Big Wall"

class ClimbingGrade(Enum):
    BEGINNER = "Beginner"                # V0-V4
    INTERMEDIATE = "Intermediate"        # V4-V8
    ADVANCED = "Advanced"                # V8+

class ClosureSystem(Enum):
    LACE = "Lace"
    VELCRO = "Velcro"
    SLIPPER = "Slipper"

class UpperMaterial(Enum):
    MIXED = "Mixed"
    SYNTHETIC = "Synthetic"
    LEATHER = "Leather"

class Lining(Enum):
    UNLINED = "Unlined"
    LINED = "Lined"
    PARTIAL = "Partial"

class Source(Enum):
    MFW = "MFW"
    ROCKRUN = "Rock+Run"

@dataclass
class Shoe:
    """
    Raw Data
    """
    brand: str
    model: str
    gender: Gender
    # Size Delta is the (recommended climbing shoe size for traditional fit based on street shoe size) - (street shoe size)
    # i.e. "How much to size down from street size"
    size_delta: float
    foot_width: FootWidth
    heel_width: HeelWidth
    downturn: Downturn
    stiffness: Stiffness
    asymmetric_curve: AsymCurve
    closure_system: ClosureSystem
    rubber_type: str
    sole_thickness: float
    upper_material: UpperMaterial
    lining: Lining

    """
    Extra Data
    """
    description: str
    price: float
    small_img_urls: list[str]
    medium_img_urls: list[str]
    large_img_urls: list[str]
    affiliate_url: list[str]

    # Defaults
    id: str = field(init=False)

    climbing_style: set[ClimbingStyle] = field(default_factory=set)
    climbing_grade: set[ClimbingGrade] = field(default_factory=set)
    toe_shape: set[ToeShape] = field(default_factory=set)
    volume: set[Volume] = field(default_factory=set)
    source: set[Source] = field(default_factory=set)


    """
    Methods
    """
    def __post_init__(self):
        self.id = f"{self.brand}-{self.model}-{self.gender.value}".lower().replace(" ", "-")


if __name__ == "__main__":
    #