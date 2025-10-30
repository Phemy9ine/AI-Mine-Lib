"""
AI-Mine-Lib: The foundational toolkit for AI Mining Engineering.
"""

__version__ = "0.1.0-alpha"
__author__ = "AI Mining Engineering Community"

from aime.core.base_miner import BaseMiner
from aime.core.model_connector import ModelConnector

# Pillar imports
from aime.mine import knowledge, reasoning, latent, synthetic

__all__ = [
    "BaseMiner",
    "ModelConnector", 
    "knowledge",
    "reasoning", 
    "latent",
    "synthetic",
]
