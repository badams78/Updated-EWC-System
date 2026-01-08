"""
Data models for the restaurant recommendation system.
"""
from dataclasses import dataclass, field
from typing import Optional, List
from enum import Enum
from datetime import date


class Neighborhood(Enum):
    UPPER_EAST_SIDE = "Upper East Side"
    SOHO = "SoHo"
    LOWER_EAST_SIDE = "Lower East Side"
    WEST_VILLAGE = "West Village"
    NOHO = "NoHo"
    TRIBECA = "Tribeca"
    GREENWICH_VILLAGE = "Greenwich Village"
    MIDTOWN = "Midtown"
    MIDTOWN_EAST = "Midtown East"
    MIDTOWN_WEST = "Midtown West"
    NOMAD = "NoMad"
    FLATIRON = "Flatiron"
    GRAMERCY = "Gramercy"
    CHELSEA = "Chelsea"
    MEATPACKING = "Meatpacking District"
    HUDSON_YARDS = "Hudson Yards"
    CHINATOWN = "Chinatown"
    UPPER_WEST_SIDE = "Upper West Side"
    LINCOLN_CENTER = "Lincoln Center"
    BROOKLYN = "Brooklyn"
    OTHER = "Other"


class Cuisine(Enum):
    ITALIAN = "Italian"
    FRENCH = "French"
    JAPANESE = "Japanese"
    JAPANESE_OMAKASE = "Japanese (Omakase)"
    JAPANESE_KAISEKI = "Japanese (Kaiseki)"
    KOREAN = "Korean"
    CHINESE = "Chinese"
    AMERICAN = "American"
    AMERICAN_NEW = "New American"
    SEAFOOD = "Seafood"
    STEAKHOUSE = "Steakhouse"
    MEDITERRANEAN = "Mediterranean"
    MEXICAN = "Mexican"
    SPANISH = "Spanish"
    GREEK = "Greek"
    INDIAN = "Indian"
    THAI = "Thai"
    VIETNAMESE = "Vietnamese"
    AUSTRIAN = "Austrian"
    PIZZA = "Pizza"
    OTHER = "Other"


class BookingPlatform(Enum):
    RESY = "Resy"
    OPENTABLE = "OpenTable"
    TOCK = "Tock"
    SEVENROOMS = "SevenRooms"
    PHONE_ONLY = "Phone Only"
    WALK_IN = "Walk-in Only"
    MEMBERS_ONLY = "Members Only"


class DifficultyRating(Enum):
    EASY = "Easy"
    MODERATE = "Moderate"
    HARD = "Hard"
    LOTTERY = "Lottery"


class MichelinStatus(Enum):
    THREE_STAR = "Three Stars"
    TWO_STAR = "Two Stars"
    ONE_STAR = "One Star"
    BIB_GOURMAND = "Bib Gourmand"
    NONE = "None"


class DiningMode(Enum):
    FAMILY = "Family"
    FRIENDS = "Friends"


@dataclass
class Restaurant:
    id: str
    name: str
    neighborhood: Neighborhood
    cuisine: Cuisine
    google_rating: Optional[float] = None
    michelin_status: MichelinStatus = MichelinStatus.NONE
    infatuation_rating: Optional[float] = None
    eater_essential: bool = False
    nyt_reviewed: bool = False
    nyt_critic_pick: bool = False
    opening_date: Optional[date] = None
    is_currently_hot: bool = False
    recent_press: bool = False
    scene_score: int = 5
    food_quality_score: int = 5
    noise_level: int = 5
    booking_platform: BookingPlatform = BookingPlatform.RESY
    booking_url: Optional[str] = None
    booking_window_days: int = 30
    booking_release_time: str = "9:00 AM ET"
    difficulty: DifficultyRating = DifficultyRating.MODERATE
    pro_tip: Optional[str] = None
    price_tier: int = 3
    is_positive_example: bool = False
    is_negative_example: bool = False
    last_recommended: Optional[date] = None
    tags: List[str] = field(default_factory=list)
    
    def age_months(self):
        if not self.opening_date:
            return None
        today = date.today()
        return (today.year - self.opening_date.year) * 12 + (today.month - self.opening_date.month)
    
    def is_new(self):
        age = self.age_months()
        return age is not None and age <= 18
    
    def is_in_convenience_zone(self):
        return self.neighborhood == Neighborhood.UPPER_EAST_SIDE
    
    def is_in_scene_zone(self):
        return self.neighborhood in [
            Neighborhood.SOHO, Neighborhood.LOWER_EAST_SIDE, Neighborhood.WEST_VILLAGE,
            Neighborhood.NOHO, Neighborhood.TRIBECA, Neighborhood.GREENWICH_VILLAGE, Neighborhood.MEATPACKING,
        ]


@dataclass
class Recommendation:
    restaurant: Restaurant
    mode: DiningMode
    party_size: int
    score: float
    target_date: date
    booking_action: str
    why_recommended: str


@dataclass
class WeeklyDigest:
    generated_date: date
    target_week_start: date
    family_picks: List[Recommendation]
    friends_picks: List[Recommendation]
