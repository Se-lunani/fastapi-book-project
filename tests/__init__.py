import sys
from pathlib import Path

# Add project root to Python path (critical for CI/CD)
sys.path.insert(0, str(Path(__file__).parent.parent))

# Import after path configuration (ignore E402 warning)
from fastapi.testclient import TestClient  # noqa: E402
from main import app  # noqa: E402

client = TestClient(app, base_url="http://test/api/v1")
