"""Application configuration via pydantic-settings.

All env var names, types, and defaults are derived from
docs/schemas/env-config.schema.json (SSOT).
"""

from functools import cached_property

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings loaded from environment variables and .env file.

    Field names are snake_case and map to UPPER_SNAKE_CASE env var names
    automatically via pydantic-settings.
    """

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    # --- AI / Inference ---
    mistral_endpoint: str = "http://localhost:11434"
    mistral_api_key: str = ""
    mistral_model: str = "mistral:7b-instruct-v0.3-q4_K_M"
    whisper_model: str = "base.en"
    whisper_base_url: str = "http://localhost:8787"
    stt_api_key: str = ""
    stt_provider: str = "whisper_local"
    stt_model: str = "base.en"
    ai_timeout_seconds: float = 30.0
    stt_timeout_seconds: float = 10.0
    ai_retry_delay_ms: int = 500
    ai_max_retries: int = 1
    ai_max_concurrent: int = 1
    ai_min_spacing_ms: int = 200

    # --- Server ---
    server_host: str = "0.0.0.0"
    server_port: int = 8000
    cors_origins: str = "http://localhost:5173"
    log_level: str = "INFO"
    environment: str = "development"

    # --- Game ---
    tick_rate: int = 20
    session_timeout_minutes: int = 30
    max_sessions: int = 1
    max_sessions_per_ip: int = 1

    # --- Audio ---
    audio_max_size_bytes: int = 10485760
    audio_min_duration_seconds: float = 0.3
    audio_max_duration_seconds: float = 10.0

    # --- Feature Flags ---
    stt_endpoint_enabled: bool = True

    # --- Debug / Determinism ---
    pythonhashseed: int = 0

    @cached_property
    def tick_interval(self) -> float:
        """Seconds per tick (1.0 / tick_rate)."""
        return 1.0 / self.tick_rate

    @property
    def is_production(self) -> bool:
        """Whether the app is running in production mode."""
        return self.environment == "production"

    @cached_property
    def cors_origin_list(self) -> list[str]:
        """Parse comma-separated CORS origins into a list, filtering empty strings."""
        return [o.strip() for o in self.cors_origins.split(",") if o.strip()]


settings = Settings()
