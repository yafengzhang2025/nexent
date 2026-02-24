"""
Simple test cases for Nexent backend exceptions.
"""
import pytest
from backend.consts import exceptions


def test_agent_run_exception():
    """Test AgentRunException can be raised and caught."""
    with pytest.raises(exceptions.AgentRunException):
        raise exceptions.AgentRunException("Agent execution failed")


def test_limit_exceeded_error():
    """Test LimitExceededError can be raised and caught."""
    with pytest.raises(exceptions.LimitExceededError):
        raise exceptions.LimitExceededError("Too many requests")


def test_unauthorized_error():
    """Test UnauthorizedError can be raised and caught."""
    with pytest.raises(exceptions.UnauthorizedError):
        raise exceptions.UnauthorizedError("User not authorized")


def test_signature_validation_error():
    """Test SignatureValidationError can be raised and caught."""
    with pytest.raises(exceptions.SignatureValidationError):
        raise exceptions.SignatureValidationError("Invalid signature")


def test_memory_preparation_exception():
    """Test MemoryPreparationException can be raised and caught."""
    with pytest.raises(exceptions.MemoryPreparationException):
        raise exceptions.MemoryPreparationException("Memory preparation failed")


def test_mcp_connection_error():
    """Test MCPConnectionError can be raised and caught."""
    with pytest.raises(exceptions.MCPConnectionError):
        raise exceptions.MCPConnectionError("MCP connection failed")


def test_exception_message_preservation():
    """Test that exception messages are preserved correctly."""
    msg = "Custom error message"
    exc = exceptions.AgentRunException(msg)
    assert str(exc) == msg


def test_exception_chaining():
    """Test exception chaining with cause."""
    cause = ValueError("Original cause")
    exc = exceptions.AgentRunException("Agent failed")
    exc.__cause__ = cause
    
    assert exc.__cause__ is cause
