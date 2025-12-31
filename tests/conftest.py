"""Pytest configuration and fixtures."""
from __future__ import annotations

import shutil
import tempfile
from pathlib import Path
from unittest.mock import AsyncMock, MagicMock, patch

import pytest
from homeassistant.core import HomeAssistant


def pytest_configure(config):
    """Configure pytest plugins."""
    # Disable pytest-socket blocking for asyncio event loops
    # This is needed on Windows where asyncio uses sockets for event loop creation
    import pytest_socket
    pytest_socket.disable_socket()

    # Re-enable socket for asyncio operations
    import socket
    original_socket = socket.socket
    socket.socket = original_socket


@pytest.fixture
def hass():
    """Create a Home Assistant instance for testing."""
    hass_instance = MagicMock(spec=HomeAssistant)
    hass_instance.config = MagicMock()
    hass_instance.config.path = MagicMock(return_value=str(Path(tempfile.mkdtemp()) / "config"))
    hass_instance.services.async_call = AsyncMock()
    yield hass_instance


@pytest.fixture
def temp_config_dir():
    """Create a temporary config directory for testing."""
    temp_dir = tempfile.mkdtemp()
    yield Path(temp_dir)
    shutil.rmtree(temp_dir)


@pytest.fixture
def mock_config_file(temp_config_dir):
    """Create a mock configuration.yaml file."""
    config_file = temp_config_dir / "configuration.yaml"
    config_file.write_text("# Test configuration\n")
    return config_file

