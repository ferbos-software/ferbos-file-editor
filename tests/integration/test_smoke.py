"""Smoke tests for basic integration functionality."""
from __future__ import annotations

import pytest
from unittest.mock import AsyncMock, MagicMock, patch
from pathlib import Path
import tempfile
import shutil

from homeassistant.core import HomeAssistant


@pytest.mark.integration
@pytest.mark.smoke
class TestSmokeTests:
    """Basic smoke tests to verify integration works."""

    @pytest.mark.asyncio
    async def test_websocket_commands_registered(self):
        """Smoke test: Verify WebSocket commands are registered."""
        from custom_components.ferbos_file_editor import async_setup
        
        hass = MagicMock(spec=HomeAssistant)
        hass.config.path = MagicMock(return_value=str(Path(tempfile.mkdtemp())))
        
        with patch("custom_components.ferbos_file_editor.websocket_api.async_register_command") as mock_register:
            result = await async_setup(hass, {})
            
            assert result is True
            # Verify WebSocket commands were registered
            assert mock_register.call_count >= 2

    @pytest.mark.asyncio
    async def test_config_entry_setup(self):
        """Smoke test: Verify config entry setup works."""
        from custom_components.ferbos_file_editor import async_setup_entry
        
        hass = MagicMock(spec=HomeAssistant)
        hass.config.path = MagicMock(return_value=str(Path(tempfile.mkdtemp())))
        entry = MagicMock()
        
        with patch("custom_components.ferbos_file_editor.websocket_api.async_register_command"):
            result = await async_setup_entry(hass, entry)
            
            assert result is True

    @pytest.mark.asyncio
    async def test_config_entry_unload(self):
        """Smoke test: Verify config entry unload works."""
        from custom_components.ferbos_file_editor import async_unload_entry
        
        hass = MagicMock(spec=HomeAssistant)
        entry = MagicMock()
        
        result = await async_unload_entry(hass, entry)
        
        assert result is True

