"""
enums.py — Shared string enums for Humantic AI.

Using str-based enums means values serialize cleanly to JSON strings
(e.g., "completed") without any extra config.
"""

from enum import Enum


class TopicStatus(str, Enum):
    """Lifecycle states of a research topic."""
    queued      = "queued"        # Just submitted, waiting for a worker
    researching = "researching"   # Celery task is actively running
    completed   = "completed"     # All cycles finished, findings saved
    failed      = "failed"        # Pipeline errored out (partial results may exist)


class FindingCategory(str, Enum):
    """Category of a research finding."""
    deep_insight = "deep_insight"   # Substantive finding backed by multiple sources
    trend        = "trend"          # Emerging movement or shift in the field
    opportunity  = "opportunity"    # Actionable gap or possibility
    experimental = "experimental"   # Speculative early signal, worth watching


class ConfidenceLevel(str, Enum):
    """How confident the AI is in a finding."""
    high        = "high"        # Supported by multiple strong sources
    medium      = "medium"      # Reasonable evidence, some gaps
    speculative = "speculative" # Early signal, single source, or inferred


class FindingStatus(str, Enum):
    """User's review decision on a finding."""
    new       = "new"       # Not yet reviewed
    approved  = "approved"  # User accepted / found useful
    dismissed = "dismissed" # User rejected


class UserDomain(str, Enum):
    """The user's professional role, inferred during onboarding."""
    consultant = "consultant"
    analyst    = "analyst"
    pm         = "pm"
    other      = "other"


class ResearchDepth(str, Enum):
    """How detailed the user wants research output to be."""
    quick_summaries = "quick_summaries"
    deep_dives      = "deep_dives"
    balanced        = "balanced"


class ActionType(str, Enum):
    """Valid action_type values for the interaction_logs table (M7 foundation)."""
    query               = "query"
    view_finding        = "view_finding"
    approve             = "approve"
    dismiss             = "dismiss"
    pin_add             = "pin_add"
    pin_remove          = "pin_remove"
    follow_up           = "follow_up"
    onboarding_complete = "onboarding_complete"
    why_this_expand     = "why_this_expand"
