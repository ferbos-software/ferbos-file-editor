"""Unit tests for config_flow.py module."""
from __future__ import annotations

import pytest
from unittest.mock import MagicMock

from homeassistant.core import HomeAssistant
from homeassistant.data_entry_flow import FlowResultType

from custom_components.ferbos_file_editor.config_flow import FerbosFileEditorConfigFlow


@pytest.mark.unit
class TestFerbosFileEditorConfigFlow:
    """Test FerbosFileEditorConfigFlow."""

    @pytest.mark.asyncio
    async def test_config_flow_user_step(self):
        """Test user step in config flow."""
        flow = FerbosFileEditorConfigFlow()
        flow.hass = MagicMock(spec=HomeAssistant)
        flow._async_handle_discovery_without_unique_id = MagicMock()
        
        result = await flow.async_step_user()
        
        assert result["type"] == FlowResultType.FORM
        assert result["step_id"] == "user"

    @pytest.mark.asyncio
    async def test_config_flow_create_entry(self):
        """Test entry creation in config flow."""
        flow = FerbosFileEditorConfigFlow()
        flow.hass = MagicMock(spec=HomeAssistant)
        flow._async_handle_discovery_without_unique_id = MagicMock()
        
        user_input = {}
        result = await flow.async_step_user(user_input=user_input)
        
        assert result["type"] == FlowResultType.CREATE_ENTRY
        assert result["title"] == "Ferbos File Editor"

