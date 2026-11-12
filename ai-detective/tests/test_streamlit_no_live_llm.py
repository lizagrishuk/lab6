"""Public research stand must not directly call a model or show an Ollama button."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def test_ui_is_offline_and_does_not_import_live_llm():
    ui = (ROOT / "src" / "app.py").read_text(encoding="utf-8")
    assert "from llm import" not in ui
    assert "run_model(" not in ui
    assert "generate_raw_answer" not in ui
    assert "Отправить текущий контекст в Ollama" not in ui
    assert "manual_runs.jsonl" not in ui
    assert "matched_result(" in ui
    assert "cached_intervention(" in ui

def test_mismatch_does_not_claim_live_answer():
    logic = (ROOT / "src" / "stand_logic.py").read_text(encoding="utf-8")
    assert "candidate_sha != result[\"sha256\"]" in logic
