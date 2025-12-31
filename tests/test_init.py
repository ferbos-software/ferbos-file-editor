"""Unit tests for __init__.py module."""
from __future__ import annotations

from unittest.mock import AsyncMock, MagicMock

import pytest
from homeassistant.core import HomeAssistant


@pytest.mark.unit
class TestAppendConfigLines:
    """Test _append_config_lines function."""

    @pytest.mark.asyncio
    async def test_append_config_lines_success(self, temp_config_dir, mock_config_file):
        """Test successful appending of lines to configuration.yaml."""
        from custom_components.ferbos_file_editor import _append_config_lines

        hass = MagicMock(spec=HomeAssistant)
        hass.config = MagicMock()
        hass.config.path = MagicMock(return_value=str(mock_config_file))
        hass.services.async_call = AsyncMock()

        payload = {
            "lines": ["# New line", "sensor:", "  - platform: template"],
            "validate": False,
            "reload_core": False,
            "backup": False,
        }

        result = await _append_config_lines(hass, payload)

        assert result["success"] is True
        assert mock_config_file.read_text().endswith("# New line\nsensor:\n  - platform: template\n")

    @pytest.mark.asyncio
    async def test_append_config_lines_invalid_input(self):
        """Test handling of invalid input."""
        from custom_components.ferbos_file_editor import _append_config_lines

        hass = MagicMock(spec=HomeAssistant)

        payload = {"lines": "not a list"}

        result = await _append_config_lines(hass, payload)

        assert result["success"] is False
        assert result["error"]["code"] == "invalid"

    @pytest.mark.asyncio
    async def test_append_config_lines_file_not_found(self):
        """Test handling when configuration.yaml doesn't exist."""
        from custom_components.ferbos_file_editor import _append_config_lines

        hass = MagicMock(spec=HomeAssistant)
        hass.config = MagicMock()
        hass.config.path = MagicMock(return_value="/nonexistent/path/configuration.yaml")

        payload = {"lines": ["test"]}

        result = await _append_config_lines(hass, payload)

        assert result["success"] is False
        assert result["error"]["code"] == "not_found"

    @pytest.mark.asyncio
    async def test_append_config_lines_with_backup(self, temp_config_dir, mock_config_file):
        """Test backup creation when backup=True."""
        from custom_components.ferbos_file_editor import _append_config_lines

        hass = MagicMock(spec=HomeAssistant)
        hass.config = MagicMock()
        hass.config.path = MagicMock(return_value=str(mock_config_file))
        hass.services.async_call = AsyncMock()

        payload = {
            "lines": ["# Test"],
            "backup": True,
            "validate": False,
            "reload_core": False,
        }

        result = await _append_config_lines(hass, payload)

        assert result["success"] is True
        # Check that backup file was created
        backup_files = list(mock_config_file.parent.glob("*.backup.*.yaml"))
        assert len(backup_files) > 0


@pytest.mark.unit
class TestHandleUIFileOperation:
    """Test _handle_ui_file_operation function."""

    @pytest.mark.asyncio
    async def test_handle_ui_file_operation_success(self, temp_config_dir):
        """Test successful file creation."""
        from custom_components.ferbos_file_editor import _handle_ui_file_operation

        hass = MagicMock(spec=HomeAssistant)
        hass.config = MagicMock()
        hass.config.path = MagicMock(return_value=str(temp_config_dir))

        args = {
            "path": "test_file.yaml",
            "template": "test: content",
            "overwrite": True,
        }

        result = await _handle_ui_file_operation(hass, args)

        assert result["success"] is True
        test_file = temp_config_dir / "test_file.yaml"
        assert test_file.exists()
        assert test_file.read_text().startswith("test: content")

    @pytest.mark.asyncio
    async def test_handle_ui_file_operation_missing_path(self):
        """Test handling of missing path."""
        from custom_components.ferbos_file_editor import _handle_ui_file_operation

        hass = MagicMock(spec=HomeAssistant)

        args = {"template": "content"}

        result = await _handle_ui_file_operation(hass, args)

        assert result["success"] is False
        assert result["error"]["code"] == "invalid"

    @pytest.mark.asyncio
    async def test_handle_ui_file_operation_directory_traversal(self):
        """Test prevention of directory traversal attacks."""
        from custom_components.ferbos_file_editor import _handle_ui_file_operation

        hass = MagicMock(spec=HomeAssistant)

        args = {
            "path": "../../etc/passwd",
            "template": "malicious",
        }

        result = await _handle_ui_file_operation(hass, args)

        assert result["success"] is False
        assert result["error"]["code"] == "invalid"

    @pytest.mark.asyncio
    async def test_handle_ui_file_operation_file_exists_no_overwrite(self, temp_config_dir):
        """Test handling when file exists and overwrite=False."""
        from custom_components.ferbos_file_editor import _handle_ui_file_operation

        hass = MagicMock(spec=HomeAssistant)
        hass.config = MagicMock()
        hass.config.path = MagicMock(return_value=str(temp_config_dir))

        # Create existing file
        existing_file = temp_config_dir / "existing.yaml"
        existing_file.write_text("existing content")

        args = {
            "path": "existing.yaml",
            "template": "new content",
            "overwrite": False,
        }

        result = await _handle_ui_file_operation(hass, args)

        assert result["success"] is False
        assert result["error"]["code"] == "file_exists"

    @pytest.mark.asyncio
    async def test_handle_ui_file_operation_with_lines(self, temp_config_dir):
        """Test file creation using lines parameter."""
        from custom_components.ferbos_file_editor import _handle_ui_file_operation

        hass = MagicMock(spec=HomeAssistant)
        hass.config = MagicMock()
        hass.config.path = MagicMock(return_value=str(temp_config_dir))

        args = {
            "path": "test_lines.yaml",
            "lines": ["line1", "line2", "line3"],
            "overwrite": True,
        }

        result = await _handle_ui_file_operation(hass, args)

        assert result["success"] is True
        test_file = temp_config_dir / "test_lines.yaml"
        assert test_file.exists()
        content = test_file.read_text()
        assert "line1" in content
        assert "line2" in content
        assert "line3" in content

