"""Configuration loader for language translations.
Uses JSON files (built-in, no dependencies).
"""

import json
from pathlib import Path
from typing import Dict, Any, Optional
from .settings import Settings


class ConfigLoader:
    """Loads and caches language configuration files."""
    
    _cache: Dict[str, Dict[str, Any]] = {}
    
    @classmethod
    def load_language_config(cls, language: str) -> Dict[str, Any]:
        """
        Load language configuration from JSON file.
        
        Args:
            language: Language code (e.g., 'english', 'arabic')
        
        Returns:
            Dictionary containing language configuration
        
        Raises:
            FileNotFoundError: If configuration file doesn't exist
            json.JSONDecodeError: If JSON file is malformed
        """
        # Normalize language
        normalized_lang = Settings.SUPPORTED_LANGUAGES.get(
            language.lower(), 
            language.lower()
        )
        
        # Check cache
        if normalized_lang in cls._cache:
            return cls._cache[normalized_lang]
        
        # Load from file
        config_path = Settings.get_config_path(normalized_lang)
        
        if not config_path.exists():
            raise FileNotFoundError(
                f"Configuration file not found: {config_path}. "
                f"Language: {language}"
            )
        
        try:
            with open(config_path, 'r', encoding='utf-8') as f:
                config = json.load(f)
            
            if config is None:
                raise ValueError(f"Empty configuration file: {config_path}")
            
            # Cache the configuration
            cls._cache[normalized_lang] = config
            return config
        
        except json.JSONDecodeError as e:
            raise ValueError(f"Error parsing JSON file {config_path}: {e}")
    
    @classmethod
    def clear_cache(cls) -> None:
        """Clear the configuration cache."""
        cls._cache.clear()
    
    @classmethod
    def reload_language_config(cls, language: str) -> Dict[str, Any]:
        """Force reload of language configuration."""
        normalized_lang = Settings.SUPPORTED_LANGUAGES.get(
            language.lower(),
            language.lower()
        )
        if normalized_lang in cls._cache:
            del cls._cache[normalized_lang]
        return cls.load_language_config(language)

